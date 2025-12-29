"""
Cool/specialized/interactive utilities which use
both STDIN and STDOUT utilities.
"""

# import sys
# import functools

from . import stdin
from . import stdout
from . import settings
from .utils import conversion

# def console_intermission(enable_on_call=True, clear=80*24):
#     """
#     Decorator to allow functions to exist as brief intermissions
#     in terms console echoing.  Simply put, if you normally have
#     echoing DISABLED but want one function to be an exception, wrap
#     it with this decorator.  Vice versa is also true -- just pass
#     enable_on_call=False instead.

#     Can also clear the console on entrace/exit if provided the window size.
#     """

#     def toggle(to_enable):
#         """Toggle console echoing on/off"""
#         if to_enable:
#             stdout.enable_echoing()
#         else:
#             stdout.disable_echoing()

#     def maybe_clear():
#         if clear:
#             stdout.printsl(stdout.clear(clear))

#     def _console_intermission(func):

#         @functools.wraps(func)
#         def wrapped(*args, **kwargs):

#             maybe_clear()
#             toggle(enable_on_call)
            
#             try:
#                 out = func(*args, **kwargs)
#                 toggle(not enable_on_call)
#                 maybe_clear()

#                 return out
#             except:
#                 # SOURCE: http://stackoverflow.com/questions/9005941/python-exception-decorator-how-to-preserve-stacktrace
#                 (errorobj, errortype, errtraceback) = sys.exc_info()  # error/type/traceback
#                 toggle(not enable_on_call)
#                 maybe_clear()

#                 raise errorobj, errortype, errtraceback

#         return wrapped

#     return _console_intermission

####################################

def getch_until_enter_echo(echo=True, hidden=True, can_delete=True, strip_last=True, max_chars=0):
    """
    Runs getch, accumulating chars until an 'enter' key

    Warning:    running with settings (1,0,0,-)
                (aka, echoing, non-hidden, and non-deleting)
                can cause visual problems if the delete key is pressed
                (since we're basically printing deletion characters).

    Warning:    Printing tabs and other such characters is usually a bad idea.
                Perhaps a "banned-for-print" list is sensible.
    """

    buff = []

    while True:
        char = stdin.getch()

        prev_len = len(buff)
        buff.append(char)
        clear_len = len(buff)

        if char in settings.ENTER_KEYS:
            break
        elif can_delete and char in settings.DELETE_KEYS:
            buff = buff[:-2] # delete the 'DEL' that was added, and the previous
            clear_len = prev_len
        elif can_delete and char == conversion.chars(settings.KEYS['FN-DEL']):
            buff = []
            clear_len = prev_len
        elif char == settings.CONTROL_C: # arbitrary decision.
            raise KeyboardInterrupt
        elif max_chars and len(buff) > max_chars:
            buff = buff[:-1]
            continue

        if echo:
            echo_str = "*" * len(buff) if hidden else ''.join(buff)
            stdout.printsl(stdout.back(prev_len))
            stdout.printsl(stdout.clear(clear_len))
            stdout.printsl(echo_str)

    if strip_last:
        buff = buff[:-1]

    return ''.join(buff)

def getpass():
    """Runs getch until a carriage return

    NOTE:  respects the BS/DEL keys"""

    return getch_until_enter_echo(strip_last=True) # ignore trailing carriage return

def getpass_cool():
    # stdout.disable_echoing()
    stdout.print_and_drop_cursor_formatted("Password: [{}        ]")
    out = getch_until_enter_echo(max_chars=8)
    # stdout.enable_echoing()
    return out
