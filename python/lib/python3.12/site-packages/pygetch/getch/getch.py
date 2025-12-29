"""
"""

import signal

from .ancient_getch import _Getch
from ..settings import settings
from ..utils import conversion
from ..utils import dec_buffered_output

####################################
# ANSI helpers

def is_valid_ANSI(cs):
    """Return whether the given chars are a valid ANSI sequence"""
    return (len(cs) > 1) and (cs[0] == settings.ESC) # <--- is being dynamic wrong?  should this be 27 instead?

def is_ANSI_we_recognize(cs):
    """Return whether the given chars are a recognized ANSI sequence"""
    return conversion.ords(cs) in settings.ANSI

####################################
# UTF-8 stuff
def remaining_bytes(char):
    """
    Calculate the remaining bytes of a UTF-8 sequence
    if given the first character.

    UTF-8 ONLY!
    """

    num = ord(char)
    remaining = -1
    while num > 127:
        remaining += 1
        num = (num << 1) % 256

    if (remaining == 0) or (remaining > 3):
        raise RuntimeError("Not valid UTF-8 leading byte: {}".format(bin(ord(char))))

    # aka...
    assert remaining in (-1, 1, 2, 3)  # -1 meaning single-byte input

    return remaining

####################################
# timeout utilities
class TimesUpException(Exception):
    """Thrown when timer ends"""
    pass

def _handle_timeout(signum, frame):
    """Run on timeout"""
    raise TimesUpException()

####################################
# getch

# notice:
# A few modifications make this work for the mac with Carbon,
# too: a modification to the _Getch to try one more import, a
# modification to the Unix init, and the inclusion of the instructions
# for the MacOS with Carbon support.

GETCHAR = _Getch()

@dec_buffered_output.buffer_output
def master_getch(timeout=0.005):

    global GETCHAR

    internal_timeout = 0.005
    # ^ 1/200th of a second -- DO NOT OVERRIDE
    # ^ UNRELATED TO <timeout>
    # ^ any faster, and ANSI codes and multibyte UTF-8 get split
    # ^ any slower, and the user can mimic ANSI codes -- ex: ESC-[-A
    signal.signal(signal.SIGALRM, _handle_timeout)
    out_buffer = tuple()

    if not timeout:
        # no timeout -- wait indefinitely
        cs = GETCHAR() # initialize to some value
        assert cs
    else:
        # yes timeout -- set a timer
        cs = ''

        try:
            signal.setitimer(signal.ITIMER_REAL, timeout) # used timer instead of alarm
            c = GETCHAR()   # <<< this is the critical part
            cs += c         # <<< here we are accumulating a multi-byte UTF-8 char
        except TimesUpException:
            pass # there were no more bytes -- meaning probably the end of the ANSI code (or ESC)
        finally:
            signal.alarm(0) # disable alarm

        if not cs:
            return out_buffer # no input

    ####################################
    # we only get here if there was input

    if cs != chr(27):
        # no ESC, so...
        # regular UTF-8 code

        for _ in xrange(remaining_bytes(cs)):  # <3 I read the UTF-8 documentation!
            cs += GETCHAR()
        out_buffer += (cs,)

    else:
        # got ESC, so...
        # arbitrary ANSI code (or the ESC key... or both in rapid succession...)

        while True:

            c = None

            try:
                signal.setitimer(signal.ITIMER_REAL, internal_timeout) # used timer instead of alarm
                c = GETCHAR()   # <<< this is the critical part
                cs += c         # <<< here we are accumulating a multi-byte UTF-8 char
            except TimesUpException:
                pass # there were no more bytes -- meaning probably the end of the ANSI code (or ESC)
            finally:
                signal.alarm(0) # disable alarm

            if not c:
                # no more input -- again, probably the end of the ANSI code
                break

            # THIS IS TO REMOVE THE "BAD ANSI CODE" error !
            # (to confirm that this is necessary,
            #  try hitting ESC and some arrow keys
            #  at the same time while getch-ing...
            #  ... this is why we need to buffer our output.)
            if cs == chr(27)*2: # ESC ESC, means first ESC was actually the ESC key
                out_buffer += (cs[0],) # the first ESC was valid
                cs = c      # second ESC could be anything...
                continue    # keep reading.

            if is_ANSI_we_recognize(cs):
                break

        out_buffer += (cs,)
        
    # print out_buffer
    return out_buffer
