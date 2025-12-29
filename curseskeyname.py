import curses

def main(stdscr):
    while True:
        key = stdscr.getkey()
        stdscr.clear()
        stdscr.addstr(0,0,key)
        if key == "q": break

curses.wrapper(main)