"""
Platform-hopefully-independent utility for "getch"ing a
single character of STDIN input from the terminal.

This code was taken from
    http://code.activestate.com/recipes/134892/
All other sources found online, such as
    http://pleac.sourceforge.net/pleac_python/userinterfaces.html
point to the first link as being the ultimate source of this code.

(c) 2015 Matthew Cotton
"""


class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""

    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()


class _GetchUnix:
    """Gets a single character from standard input.  Does not echo to the screen."""

    def __init__(self):
        import sys, tty, termios

    def __call__(self):
        import sys, tty, termios
        file_desc = sys.stdin.fileno()
        old_settings = termios.tcgetattr(file_desc)

        try:
            tty.setraw(sys.stdin.fileno())
            char = sys.stdin.read(1)
        finally:
            termios.tcsetattr(file_desc, termios.TCSADRAIN, old_settings)

        return char


class _GetchWindows:
    """Gets a single character from standard input.  Does not echo to the screen."""

    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()
