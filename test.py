import curses
import shutil
import random

filters = ["POL", "ECO", "SPE"]

def wall(x):
    for i in range(x):
        wall = "-" * x
    return wall

mapseed = 0xB16B00B2

def stargen(seed,size_x,size_y):
    starran = random.Random()
    starran.seed(mapseed + seed)
    starname = f"E-{starran.randint(1000,9999)}-{seed}"

    Star = {
        "StarID": seed,
        "Star": starname,
        "StarCivil": starran.choice([True,False]),
        "StarEco": starran.randint(0,100),
        "x": starran.randint(1,size_x-len(starname)),
        "y": starran.randint(6, size_y-4)
    }

    return Star

def GalaxyMap(stdscr):
    stdscr.clear()
    curses.start_color()

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(100, 160, curses.COLOR_BLACK) # RED
    curses.init_pair(101, curses.COLOR_GREEN, curses.COLOR_BLACK) # GREEN
    curses.init_pair(102, 27, curses.COLOR_BLACK) # BLUE
    curses.init_pair(103, curses.COLOR_YELLOW, curses.COLOR_BLACK) # YELLOW

    filt = 0
    selected = 0
    selecLock = selected
    border = 6

    while True:
        x, y = shutil.get_terminal_size()
        stdscr.addstr(1,int((x-len("GalaxyMap"))/2),"GalaxyMap")
        filter_str = f" Selected filter: {filters[filt]} "
        selected_str = f" Selected: {selected} "
        vision_str = f" Vision: {selecLock} "

        map = ""
        for i in range(x*y):
            map += ":"

        loxes = ((x-1)*(y-7)) - 1
        stdscr.addstr(5,0,map[:loxes], curses.color_pair(0) | curses.A_DIM)

        for i in range(selecLock-border, selecLock+border):
            staris = stargen(i,x,y)

            if filt == 0:
                if staris["StarCivil"] == True:
                    color = curses.color_pair(102)
                else:
                    color = curses.color_pair(100)
            elif filt == 1:
                if staris["StarEco"] >= 50:
                    color = curses.color_pair(101)
                elif staris["StarEco"] <= 50 and staris["StarEco"] >= 25:
                    color = curses.color_pair(103)
                else:
                    color = curses.color_pair(100)
            else:
                color = curses.color_pair(0)

            if selected == staris["StarID"]:
                selected_frame1 = "["
                selected_frame2 = "]"
                color = curses.color_pair(103)
            else:
                selected_frame1 = " "
                selected_frame2 = " "
            
            stdscr.addstr(int(staris['y']),int(staris['x']),str(selected_frame1+staris['Star']+selected_frame2), color)

        stdscr.addstr(3,0,filter_str, curses.color_pair(1))
        stdscr.addstr(2,0,wall(x-1))
        stdscr.addstr(3,len(filter_str)+2, selected_str, curses.color_pair(1))
        stdscr.addstr(3,len(filter_str)+2+len(selected_str)+2, vision_str, curses.color_pair(1))
        stdscr.addstr(4,0,wall(x-1))
        stdscr.addstr(y-3,0,wall(x-1))

        stdscr.refresh()

        key = stdscr.getch()
        keyname = curses.keyname(key).decode()
        stdscr.clear()
        if keyname == "f":
            if filt == len(filters) - 1:
                filt = 0
            else:
                filt += 1

        if keyname == "KEY_RIGHT":
            selected += 1
        if keyname == "KEY_LEFT":
            selected += -1
        if keyname == "KEY_UP":
            selecLock += -border*2
        if keyname == "KEY_DOWN":
            selecLock += border*2

for i in range(1000):
    print()

print("1. GalaxyMap")
menu = input("Choice: ")
if menu == "1":
    curses.wrapper(GalaxyMap)