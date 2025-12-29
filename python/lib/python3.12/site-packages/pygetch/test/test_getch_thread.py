
import time

from PyGetch.pygetch import stdout, special
stdout.printsl('\r\n') # newline isn't enough anymore

with special.GetchManager() as keyman:
    for i in xrange(10):
        stdout.printsl("Working...\r\n")
        time.sleep(0.3)
        stdout.printsl(repr(keyman.get()) + '\r\n')
        keyman.reset()
