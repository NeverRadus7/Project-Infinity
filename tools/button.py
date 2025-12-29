import getch

def Command():
        key = getch.getch()
        return key

while True:
    print(Command())