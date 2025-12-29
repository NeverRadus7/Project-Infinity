
# TODO:
# note to self:
# - getch thread needs to be the main thread
# - therefore, write getchwrap(func),
#   where func() is the user's main function,
#   so they can use the getch code

####################################
# getch thread
_DO_GETCH = True
_KEY = ''

def getch_thread():
    global _KEY

    while _DO_GETCH:
        _KEY = getch()

def start_getch_thread():
    thread = threading.Thread(target=getch_thread)
    thread.daemon = True
    thread.start()

def stop_getch_thread():
    global _DO_GETCH
    _DO_GETCH = False

def next_key():
    global _KEY
    return _KEY

def reset_key():
    global _KEY
    _KEY = ''

####################################
# getch context manager

class GetchManager(object):
    
    def __init__(self):
        pass

    def __enter__(self):
        stdout.disable_echoing()
        stdin.start_getch_thread()
        return self                     # <---<<<  IMPORTANT

    def __exit__(self, typ, val, tb):
        # getch thread is daemonic -- no stopping required.
        stdout.enable_echoing()

    def get(self):
        return stdin.next_key()

    def reset(self):
        stdin.reset_key()
