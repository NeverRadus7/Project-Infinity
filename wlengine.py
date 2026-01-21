# ██╗    ██╗██╗     ███████╗███╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗    ██╗   ██╗ ██╗   ██████╗  █████╗ 
# ██║    ██║██║     ██╔════╝████╗  ██║██╔════╝ ██║████╗  ██║██╔════╝    ██║   ██║███║   ╚════██╗██╔══██╗
# ██║ █╗ ██║██║     █████╗  ██╔██╗ ██║██║  ███╗██║██╔██╗ ██║█████╗      ██║   ██║╚██║    █████╔╝╚█████╔╝
# ██║███╗██║██║     ██╔══╝  ██║╚██╗██║██║   ██║██║██║╚██╗██║██╔══╝      ╚██╗ ██╔╝ ██║   ██╔═══╝ ██╔══██╗
# ╚███╔███╔╝███████╗███████╗██║ ╚████║╚██████╔╝██║██║ ╚████║███████╗     ╚████╔╝  ██║██╗███████╗╚█████╔╝
#  ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝      ╚═══╝   ╚═╝╚═╝╚══════╝ ╚════╝ 
#                                                                                                           
# © WhiteLight studio • 2025 • ALL RIGHTS RESERVED • https://sites.google.com/view/whitelight-studio

# -- Base import ■ ▪ ∙ •
import time
import random
import os
import colorama
import json
import math
import curses
import numpy

from datetime import datetime, timedelta, date

# -- Files import
from galaxy.map import GenMap
from wlregister import *
from settings import *
from nickname_generator import generate as ranname

# -- Save import
with open(SavePath,'r', encoding="utf-8") as f:
    save = json.load(f)

with open(MapPath, 'r', encoding="utf-8") as f:
    CustomStars = json.load(f)

# -- LICENSE
LICENSE = open("LICENSE", "r", encoding="utf-8")

PlayerIs = save
StarIs = GenMap(PlayerIs['Location'])
PlayerAtribution = PlayerIs['Atribution']

# -- Main Code
colorama.init()

GameName = "Project Infinity"
VersionClient = "1.1 Beta"
EngineVersion = "2.16"

TimeToday = time.strftime("%d")
TimeMonth = time.strftime("%m")
TimeYear = time.strftime("%Y")

rwos = random.Random() # Random.WithOut.Seed

class wl():   # Main class
    Wall = WallSymbol * (ConsoleSizeX - 1)
    DoList = "1. Галактична карта ▪ 2. Зоряна система ▪ 3. Планета ▪ 4. Станція ▪ 5. Інше".center(ConsoleSizeX)
    Player = f"{PlayerIs['Nickname']}"
    Data = f"{TimeToday}.{TimeMonth}.{TimeYear}"
    ID = f"0x{random.randint(int(1e+7),int(9e+7))}"
    Level = int(PlayerIs['XP'] / XpToLevel)
    StopGame = exit
    SquereSymbol = "▪"
    Latters = [chr(i) for i in range(65, 91)]
    LowerLatters = [chr(i) for i in range(97, 123)]

    def ConsoleSetSize():
        os.system(f"mode con cols={ConsoleSizeX} lines={ConsoleSizeY}")

    def Logo():
        C = int((ConsoleSizeX/2) - int(83/2))
        P = " " * C
        print(
            f"{P}██████  ██████   ██████       ██ ███████  ██████ ████████     ██ ███    ██ ███████ \n"
            f"{P}██   ██ ██   ██ ██    ██      ██ ██      ██         ██        ██ ████   ██ ██      \n"
            f"{P}██████  ██████  ██    ██      ██ █████   ██         ██        ██ ██ ██  ██ █████   \n"
            f"{P}██      ██   ██ ██    ██ ██   ██ ██      ██         ██        ██ ██  ██ ██ ██      \n"
            f"{P}██      ██   ██  ██████   █████  ███████  ██████    ██        ██ ██   ████ ██      \n"
        )

    def Icon():
        print(
            "                                ██╗    ██╗██╗  ██╗██╗████████╗███████╗██╗     ██╗ ██████╗ ██╗  ██╗████████╗\n",
            "                               ██║    ██║██║  ██║██║╚══██╔══╝██╔════╝██║     ██║██╔════╝ ██║  ██║╚══██╔══╝\n",
            "                               ██║ █╗ ██║███████║██║   ██║   █████╗  ██║     ██║██║  ███╗███████║   ██║   \n",
            "                               ██║███╗██║██╔══██║██║   ██║   ██╔══╝  ██║     ██║██║   ██║██╔══██║   ██║   \n",
            "                               ╚███╔███╔╝██║  ██║██║   ██║   ███████╗███████╗██║╚██████╔╝██║  ██║   ██║   \n",
            "                                ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   \n",
            "                                                                                                           \n",
            "                                            ███████╗████████╗██╗   ██╗██████╗ ██╗ ██████╗                  \n",
            "                                            ██╔════╝╚══██╔══╝██║   ██║██╔══██╗██║██╔═══██╗                 \n",
            "                                            ███████╗   ██║   ██║   ██║██║  ██║██║██║   ██║                 \n",
            "                                            ╚════██║   ██║   ██║   ██║██║  ██║██║██║   ██║                 \n",
            "                                            ███████║   ██║   ╚██████╔╝██████╔╝██║╚██████╔╝                 \n",
            "                                            ╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═╝ ╚═════╝                  \n",
            "\n",
        )

    def Error(text):
        for Skip_screen in range(31):
            print()
        print(f"{Colore.Red}/!\\{Colore.Red}".center(ConsoleSizeX+8))
        print(f"{Colore.Red}{text}{Colore.Reset}".center(ConsoleSizeX+8))
        print(f"{Colore.Gray}Нажміть ENTER щоб перезавантажити{Colore.Reset}".center(ConsoleSizeX+8))
        wl.SkipValue(int(ConsoleSizeY / 2) - 2)
        input()
        exit()

    def ScreenTextLable(text):
        wl.Skip()
        print(f"{text}".center(ConsoleSizeX))
        wl.SkipValue(int(ConsoleSizeY / 2) - 2)
        time.sleep(3)

    def CenterTextLable(text):
        wl.Skip()
        print(f"{text}".center(ConsoleSizeX))
        wl.SkipValue(int(ConsoleSizeY / 2))
    
    def CenterText(text):
        print(f"{text}".center(ConsoleSizeX))

    def CenterTextEnd(x=0):
        wl.SkipValue(int((ConsoleSizeY-x) / 2))

    def Skip():
        for Skip_screen in range(ConsoleSizeY*2):
            print()
    
    def SkipValue(value):
        for SkipScreen in range(value):
            print()
    
    def Quation(text):
        print(f"{text} (1/0): ")
        quation = wl.Command()
        if quation == "1":
            return quation
        else:
            exit()
    
    def Massage(text):
        wl.Skip()
        print(f"{Colore.Gray}{text}{Colore.Reset}")
        input()
    
    def ParrametrInspect(par, text):
        if par is True:
            print(f"{Colore.Green}◈ {text}{Colore.Reset}")
        else:
            print(f"{Colore.Red}◈ {text}{Colore.Reset}")

    def ArabicToRoman(n):
        roman_numerals = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M',
        }
        
        result = ''
        for value in sorted(roman_numerals.keys(), reverse=True):
            while n >= value:
                result += roman_numerals[value]
                n -= value
        
        return result

    def ItemName(index, name, space, item):
        spaces = str("   ") * int(space)
        print(f"{spaces}{index}. {name} | Кількість: {item}")

    def ItemDescript(text, space):
        spaces = str("   ") * int(space)
        print(f"{Colore.Gray}{spaces}{text}{Colore.Reset}")

    def ItemRerity(colore, text, space):
        spaces = str("   ") * int(space)
        print(f"{Colore.Gray}{spaces}Рідкість:{colore} {text}{Colore.Reset}")
    
    def ItemType(text, space):
        spaces = str("   ") * int(space)
        print(f"{Colore.Gray}{spaces}Тип: {text}{Colore.Reset}")

    def Background(textcolore, backcolore, text):
        B = f"{textcolore}{backcolore} {text} {colorama.Fore.RESET}{colorama.Back.RESET}"
        return B

    def NumberFormat(x):
        formatted_number = "{:,}".format(x)
        formatted_number_with_space = formatted_number.replace(",", " ")
        return formatted_number_with_space

    def NumberFormatComa(x):
        formatted_number = "{:,}".format(x)
        return formatted_number

    def Dialog(type, name, dia, descript, quat1, quat2, quat3, quat4):
        wl.Skip()
        print(wl.Wall)
        if type == "DIALOG":
            print(f" ▪ {name} {Colore.Gray}({descript}){Colore.Reset}")
        elif type == "CHOICE":
            print(f" ▪ {name}")
        print(wl.Wall)
        for a in range(5):
            print()
        print(f" ▪ {dia} ▪")
        for a in range(5):
            print()
        print(wl.Wall)
        for a in range(1):
            print()
        if not quat1 == "":
            print(f" 1. {quat1}")
            for a in range(1):
                print()
        if not quat2 == "":
            print(f" 2. {quat2}")
            for a in range(1):
                print()
        if not quat3 == "":
            print(f" 3. {quat3}")
            for a in range(1):
                print()
        if not quat4 == "":
            print(f" 4. {quat4}")
            for a in range(1):
                print()
        print(wl.Wall)

    def Status(text, value):
        print(f"{text}: {value}", end="\r")

    def Wait(second):
        time.sleep(second)

    def LegecyLoading(name, ranger):
        wl.Skip()
        for loading in range(ranger):
                print(f"  {name} ◇",end="\r")
                time.sleep(0.2)
                print(f"  {name} ◈",end="\r")
                time.sleep(0.2)
                print(f"  {name} ◇",end="\r")
                time.sleep(0.2)
                print(f"  {name} ◈",end="\r")
                time.sleep(0.2)
        print(f"  {name} ◆",end="\r")
        time.sleep(0.2)

    def Loading(name, ranger):
        for loading in range(ranger):
            wl.CenterTextLable(f" {name} ○\r")
            time.sleep(0.2)
            wl.CenterTextLable(f" {name} ●\r")
            time.sleep(0.2)
        wl.Skip()

    def SearchIndex(listing, object , name):
        for index, item in enumerate(listing):
            if item[object] == name:
                return index
        else: return -1

    def TextColorePr(text, colore):
        textt = f"{colore}{text}{Colore.Reset}"
        print(textt)

    def TextColore(text, colore):
        textt = f"{colore}{text}{Colore.Reset}"
        return textt
    
    def TextCenter(text):
        S = len(text)
        C = int((ConsoleSizeX/2) - int(S/2))
        P = " " * C
        result = f"{P}{text}"
        print(result)

    def Screen():
        n = 24

        wl.Logo()
        wl.TextCenter(f"Project Infinity ▪ {VersionClient}")
        print(wl.Wall)
        print(f" ▪ Баланс: {Colore.Yellow}{PlayerIs['Money']:,} ©{Colore.Reset} ▪ {Colore.Blue}{PlayerIs['IntelBall']:,} ◭ {Colore.Reset} ▪ {Colore.Red}{PlayerIs['BattleScore']:,} ⊙{Colore.Reset}  ▪ {Colore.Green}{PlayerIs['SocialScore']:,} ⑇{Colore.Reset} ▪ {PlayerIs['XP']:,} XP {Colore.Gray}| Level: {wl.Level} {Colore.Reset} ▪ {wl.Date()}")
        print(wl.Wall)
        print(f" ▪ Зірка: {StarIs['Star']}")
        print(f" ▪ Ім'я: {PlayerIs['Nickname']}")
        print(f" ▪ Ранг: {LevelRangIs}")
        print(f" ▪ Вивчено систем: {PlayerIs['Statistic']['StarInteled']:,}")
        print(f" ▪ Систем під контролем: {PlayerIs['Statistic']['StarControled']:,}")
        print(f" ▪ Кількість колонії: {PlayerIs['Statistic']['StarColony']:,}")
        print(f" ▪ Прибуток з колонії: {PlayerIs['Statistic']['IncomeFromColony']:,} ©")
        if DebugInfo == True: print(f"{Colore.Red}Debug-інформація: MapSeed: {MapSeed}, StarID: {StarIs['StarID']}{Colore.Reset}")
        print(wl.Wall)
        print(f" ▪ Корабель: {PlayerIs['Ship']['ShipName']}{Colore.Gray} ({Ships[PlayerIs['Ship']['ShipID']]['ShipName']}) | МВС: {TravelDistation} св. р | Паливо: {PlayerIs['Ship']['Fuel']}/{FuelMaxCapacity} тон{Colore.Reset}")
        print(wl.Wall)
        print(wl.DoList)
        wl.TextCenter(f"{Colore.Gray}© WhiteLight studio - all rights reserved{Colore.Reset}")
        for abis in range(int((ConsoleSizeY/2)-n/2)):
            print()

    def ReadList(list, a0):
        if a0 == 1:
            for i in range(len(list)):
                print(f" - {list[i]}")
        if a0 == 2:
            for i in range(len(list)):
                print(f"{list[i]}")
        if a0 == 3:
            for i in range(len(list)):
                print(f"{i+1}. {list[i]}")
        else:
            return -1

    def ReadBox(list, item):
        for i in range(0, len(list)):
            elist = list[i]
            print(f"{i+1}. {elist[item]}")

    def ReadBoxCat(list, item, elements):
        wl.Skip()
        BoxSize = len(list)
        if BoxSize > elements:
            Page = BoxSize / elements
            Page = int(Page)
            for pages in range(Page):
                print(f"{pages+1}. Сторінка {pages+1}")
            pageIs = int(input("Вибрати сторінку: "))
            pageIs = int(pageIs)
            wl.Skip()
            if pageIs == 1:
                StartList = 0
                EndList = elements
            elif pageIs == 2:
                StartList = elements
                EndList = elements * (pageIs)
            else:
                StartList = elements * (pageIs-1)
                EndList = elements * (pageIs)
            for i in range(StartList,  EndList):
                elist = list[i]
                print(f"{i+1}. {elist[item]}")

    def InfoBlock(titleColore={'colore': colorama.Back.BLUE, 'title': "Test"}, text=""):
        wl.Skip()
        print(f"{titleColore['colore']} {titleColore['title']} {colorama.Back.RESET}")
        print(text)
    
    def InfoText(colore=colorama.Back.BLUE, title="Test"):
        print(f"{colore} {title} {colorama.Back.RESET}")

    def ReadList(list, puncktuation):
        if puncktuation == True:
            for i in range(len(list)):
                print(f" - {list[i]}")
        else:
            for i in range(len(list)):
                print(f"{list[i]}")

    def ReadJSON(file):
        with open(file, 'r', encoding="utf-8") as f:
            jsonfileread = json.load(f)
        return jsonfileread

    def SaveJSON(file, element):
        with open(file, 'w', encoding="utf-8") as f:
            json.dump(element, f, ensure_ascii=False, indent=4)

    def GetObjectID(list, name):
        for index, item in enumerate(list):
            if item["ID"] == name:
                return index
            else:
                return -1

    def Menu(list):
        for i, elements in enumerate(list):
            print(f"{i+1}. {elements}")

    def ChoiceMenu(list):
        for i, elements in enumerate(list):
            print(f"{i+1}. {elements}")
        try:
            Command = wl.Command()
            Choice = int(Command)
            if Choice <= 0 or Choice > len(list):
                exit()
            return list[Choice-1]
        except (ValueError, TypeError):
            pass

    def LMenu(menu_list):
        elementsVal = len(menu_list) 
        menu_line = ""
        for elements in range(elementsVal):
            NameElement = menu_list[elements]
            menu_line += f" {elements+1}. {NameElement}{Colore.Reset} {wl.SquereSymbol} "

            print(menu_line, end="\r")

    def ChoiceLMenu(list):
        elementsVal = len(list)
        menu_line = ""
        for elements in range(elementsVal):
            NameElement = list[elements]
            menu_line += f" {elements+1}. {NameElement}{Colore.Reset} {wl.SquereSymbol} "
            print(menu_line, end="\r")

        Command = wl.Command()
        Choice = list[int(Command) - 1]
        return Choice

    def Date():
        start_date = datetime(3000, 1, 1)
        start_date += timedelta(days=PlayerIs["WorldDay"])
        prdate = f"{start_date.strftime("%d.%m.%Y")}"
        return prdate

    def DateString(x):
        start_date = datetime(3000, 1, 1)
        start_date += timedelta(days=x)
        prdate = f"{start_date.strftime("%d.%m.%Y")}"
        return prdate
    
    def InvAdd(itemID, count):
        if itemID > len(ItemsDB):
            wl.Error(f"Предмет із номером #{itemID} не існує")
        else:
            if len(PlayerIs["Ship"]['Storage']) == 0:
                if count <= PlayerMaxItems:
                    PlayerIs["Ship"]['Storage'].append(
                        {
                            "ItemID": itemID,
                            "ItemCount": count
                        }
                    )
                else:
                    wl.Error("Перевищений максимум!")
            else:
                FleetID = None
                for alli in range(len(PlayerIs["Ship"]['Storage'])):
                    ItemIs = PlayerIs["Ship"]['Storage'][alli]
                    if ItemIs['ItemID'] == itemID:
                        break
                if ItemIs['ItemID'] == itemID:
                    SecureCount = ItemIs['ItemCount'] + count
                    if SecureCount <= PlayerMaxItems:
                        ItemIs['ItemCount'] += count
                    else:
                        wl.Error("Перевищений максимум!")
                else:
                    if count <= PlayerMaxItems:
                        PlayerIs["Ship"]['Storage'].append(
                            {
                                "ItemID": itemID,
                                "ItemCount": count
                            }
                        )

    def InvRem(itemID, count):
        if itemID > len(ItemsDB):
            wl.Error(f"Предмет із номером #{itemID} не існує")
        else:
            if len(PlayerIs["Ship"]['Storage']) == 0:
                wl.Error("В сховище порожньо")
            else:
                for alli in range(len(PlayerIs["Ship"]['Storage'])):
                    ItemIs = PlayerIs["Ship"]['Storage'][alli]
                    if ItemIs['ItemID'] == itemID:
                        ItemIsID = alli
                        break
                if ItemIs['ItemID'] == itemID:
                    if ItemIs['ItemCount'] <= count:
                        PlayerIs["Ship"]['Storage'].pop(ItemIsID)
                    else:
                        ItemIs['ItemCount'] -= count

    def InvCheak(itemID, count=1):
        flag = None
        for i, item in enumerate(PlayerIs['Ship']['Storage']):
            if item['ItemID'] == itemID and item['ItemCount'] >= count:
                flag = i
        return flag

    def FleetInvAdd(itemID, count, FleetID=None):
        if itemID > len(ItemsDB):
            wl.Error(f"Предмет із номером #{itemID} не існує")
        else:
            if len(PlayerIs["Fleet"][FleetID]['Storage']) == 0:
                PlayerIs["Fleet"][FleetID]['Storage'].append(
                    {
                        "ItemID": itemID,
                        "ItemCount": count
                    }
                )
            else:
                for alli in range(len(PlayerIs["Fleet"][FleetID]['Storage'])):
                    ItemIs = PlayerIs["Fleet"][FleetID]['Storage'][alli]
                    if ItemIs['ItemID'] == itemID:
                        break
                if ItemIs['ItemID'] == itemID:
                    ItemIs['ItemCount'] += count
                else:
                    PlayerIs["Fleet"][FleetID]['Storage'].append(
                        {
                            "ItemID": itemID,
                            "ItemCount": count
                        }
                    )

    def FleetInvRem(itemID, count, FleetID):
        if itemID > len(ItemsDB):
            wl.Error(f"Предмет із номером #{itemID} не існує")
        else:
            if len(PlayerIs["Fleet"][FleetID]['Storage']) == 0:
                wl.Error("В сховище порожньо")
            else:
                for alli in range(len(PlayerIs["Fleet"][FleetID]['Storage'])):
                    ItemIs = PlayerIs["Fleet"][FleetID]['Storage'][alli]
                    if ItemIs['ItemID'] == itemID:
                        ItemIsID = alli
                        break
                if ItemIs['ItemID'] == itemID:
                    if ItemIs['ItemCount'] <= count:
                        PlayerIs["Fleet"][FleetID]['Storage'].pop(ItemIsID)
                    else:
                        ItemIs['ItemCount'] -= count

class pi():
    def reitingPrint(x, max_x):
        return f"{(ModLevelSym*x)[:max_x]}{ModLevelEmptySym*(max_x-x)}"

    def menuscreen(stdscr, title, menu):
        curses.start_color()
        curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.curs_set(0)
        sel = 0
        while True:
            size_y, size_x = stdscr.getmaxyx()
            other_win = curses.newwin(len(menu)+2,40,int((size_y-(len(menu)+2))/2), int((size_x-40)/2))
            other_win.clear()
            ot_y, ot_x = other_win.getmaxyx()
            other_win.box()
            other_win.addstr(0,int((ot_x-len(title))/2), title)
            for i in range(len(menu)):
                if sel == i:
                    color = curses.color_pair(1)
                else:
                    color = curses.color_pair(0)
                other_win.addstr(i+1,1,f"{menu[i]}"+str(" " * (ot_x-len(f"{menu[i]}")-2)),color)
            other_win.refresh()
            keyname = other_win.getkey()

            if keyname == "q":
                return "QUIT"
            if keyname == "A":
                if sel > 0:
                    sel -= 1
            if keyname == "B":
                if sel < len(menu)-1:
                    sel += 1
            if keyname == "\n":
                return menu[sel]
    
    def message(stdscr,s_y=5,s_x=30,title="Simple", message="..."):
        size_y, size_x = stdscr.getmaxyx()
        mes = curses.newwin(s_y,s_x,int((size_y-s_y)/2), int((size_x-s_x)/2))
        mes.addstr(1,int((s_x-len(title))/2), title)
        mes.addstr(2,int((s_x-len(message))/2),message)
        mes.box()
        mes.getch()

    def selectscr(stdscr):
        while True:
            try:
                curses.echo(True)
                size_y, size_x = stdscr.getmaxyx()
                curses.curs_set(1)
                sel = curses.newwin(3,45,int((size_y-3)/2), int((size_x-45)/2))
                sel.box()
                sel.addstr(1,1,"Input: ")
                str = sel.getstr(1,8)
                curses.curs_set(0)
                return str
            except:
                break

    def StarChange(StarID, ElementTag, ElementValue):
        if len(CustomStars) == 0:
            CustomStars.append(
                {
                    'StarID': StarID,
                    str(ElementTag): ElementValue
                }
            )
        else:
            for i in range(len(CustomStars)):
                CustomStarIs = CustomStars[i]
                if CustomStarIs['StarID'] == StarID:
                    break
            if CustomStarIs['StarID'] == StarID:
                CustomStarIs[ElementTag] = ElementValue
            else:
                CustomStars.append(
                    {
                        'StarID': StarID,
                        str(ElementTag): ElementValue
                    }
                )
        # file = open("galaxy/mapchanges.py", "w", encoding="utf-8")
        # file.write(f"CustomStars = {CustomStars}")
        wl.SaveJSON(MapPath, CustomStars)

    def LocalSave():
        if len(CustomStars) == 0:
            CustomStars.append(StarIs)
        else:
            for i in range(len(CustomStars)):
                CustomStarIs = CustomStars[i]
                if CustomStarIs['StarID'] == StarIs['StarID']:
                    break
            if CustomStarIs['StarID'] == StarIs['StarID']:
                CustomStarIs = StarIs
            else:
                CustomStars.append(StarIs)
        
        wl.SaveJSON(MapPath, CustomStars)
    
    def loading(stdscr, t=5, title="Simple"):
        y, x = stdscr.getmaxyx()
        loading = curses.newwin(3,30,int((y-3)/2),int((x-30)/2))
        loading_y, loading_x = loading.getmaxyx()
        loading.box()
        loading.addstr(1,int((30-len(title))/2),title)
        loading.move(loading_y-1,loading_x-1)
        loading.refresh()
        curses.curs_set(0)
        curses.napms(t*1000)

    def error_stdscr(stdscr,text,text2):
            sz_y, sz_x = stdscr.getmaxyx()
            error = curses.newwin(4,40,int((sz_y-4)/2),int((sz_x-40)/2))
            er_y,er_x = error.getmaxyx()
            error.attron(curses.color_pair(100))
            error.box()
            error.addstr(0,int((er_x-len("/!\\"))/2), "/!\\", curses.color_pair(100))
            error.addstr(1,int((er_x-len(text))/2), text)
            error.addstr(2,int((er_x-len(text2))/2), text2)
            error.attrset(curses.color_pair(0))
            error.move(er_y-1,er_x-1)
            error.getch()
            return 0
    
    def NewGalaxyMap(star, stdscr):
        StartLoc = PlayerIs['Location']
        stdscr.clear()
        curses.start_color()
        curses.curs_set(0)
        y,x = stdscr.getmaxyx()
        
        def borderEX(x):
            for i in range(x):
                wall = " " * x
            return wall
        
        def loading(t):
            loading = curses.newwin(3,30,int((y-3)/2),int((x-30)/2))
            loading_y, loading_x = loading.getmaxyx()
            loading.box()
            loading.addstr(1,int((30-len("Traveling..."))/2),"Traveling...")
            loading.move(loading_y-1,loading_x-1)
            loading.refresh()
            curses.napms(t*1000)

        def error(text,text2):
            error = curses.newwin(4,40,int((y-4)/2),int((x-40)/2))
            er_y,er_x = error.getmaxyx()
            error.attron(curses.color_pair(100))
            error.box()
            error.addstr(0,int((er_x-len("/!\\"))/2), "/!\\", curses.color_pair(100))
            error.addstr(1,int((er_x-len(text))/2), text)
            error.addstr(2,int((er_x-len(text2))/2), text2)
            error.attrset(curses.color_pair(0))
            error.move(er_y-1,er_x-1)
            error.getch()
            return 0

        max_colors = curses.COLORS
        if max_colors > 8:
            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
            curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
            curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_YELLOW)
            curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_GREEN)
            curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_RED)
            curses.init_pair(100, curses.COLOR_RED, curses.COLOR_BLACK) # RED
            curses.init_pair(101, curses.COLOR_GREEN, curses.COLOR_BLACK) # GREEN
            curses.init_pair(102, curses.COLOR_BLUE, curses.COLOR_BLACK) # BLUE
            curses.init_pair(103, curses.COLOR_YELLOW, curses.COLOR_BLACK) # YELLOW

            #Spectrum for stars
            curses.init_pair(10, 81, curses.COLOR_BLACK) # O
            curses.init_pair(11, 45, curses.COLOR_BLACK) # B
            curses.init_pair(12, 123, curses.COLOR_BLACK) # A
            curses.init_pair(13, 15, curses.COLOR_BLACK) # F
            curses.init_pair(14, 184, curses.COLOR_BLACK) # G
            curses.init_pair(15, 166, curses.COLOR_BLACK) # K
            curses.init_pair(16, 202, curses.COLOR_BLACK) # M, T, L
        else:
            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
            curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_GREEN)
            curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_YELLOW)
            curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_GREEN)
            curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_RED)

        filt = PlayerIs['MapFilter']
        selected = star
        location = selected / BorderMap
        location = int(location) * BorderMap
        selecLock = location
        border = BorderMap

        while True:
            y, x = stdscr.getmaxyx()

            filter_str = f" Selected filter: {MapFilter[filt]} "
            selected_str = f" Selected: {selected} "
            vision_str = f" Vision: {selecLock} "

            map = ""
            for i in range(x*y):
                map += MapSymbol

            loxes = ((x-1)*(y-1)) - 1
            stdscr.addstr(1,0,map[:loxes], curses.color_pair(0) | curses.A_DIM)

            for i in range(selecLock-border, selecLock+border):
                staris = GenMap(i)

                Distation = abs(selected - StartLoc)
                if Distation > TravelDistation:
                    stdscr.addstr(1,x-len(" /!\\ Too far ") - 2, " /!\\ Too far ", curses.color_pair(5))
                
                starran = random.Random()
                starran.seed(MapSeed + staris["StarID"])

                size_y, size_x  = stdscr.getmaxyx()
                staris["x"] = starran.randint(1,size_x-len(staris['Star']))
                staris["y"] = starran.randint(2, size_y-2)

                if staris.get("PlayerPinned") and staris['PlayerPinned'] == True:
                    symbol = SymbolOfStarPinned
                else:
                    symbol = SymbolOfStar

                dim = 0
                color = 0
                if filt == 0: #Досл-пол
                    if staris.get("StarCivil") and staris["StarCivil"] != []:
                        color = 101
                    elif staris.get("StarIntel") and staris["StarIntel"] == True:
                        color = 102
                    else:
                        color = 0
                        dim = curses.A_DIM
                elif filt == 1:
                    if staris.get("StarControled") and staris["StarControled"] == True:
                        color = 100
                    else:
                        color = 0
                        dim = curses.A_DIM
                elif filt == 2:
                    if staris['Class'] == "O":
                        color = 10
                    elif staris['Class'] == "B":
                        color = 11
                    elif staris["Class"] == "A":
                        color = 12
                    elif staris['Class'] == "F":
                        color = 13
                    elif staris['Class'] == "G":
                        color = 14
                    elif staris['Class'] == "K":
                        color = 15
                    elif staris['Class'] in ["M", "T", "L"]:
                        color = 16
                    else:
                        color = 0
                        dim = curses.A_DIM
                elif filt == 3:
                    if staris.get('StarCivil'):
                        if staris['StarCivil']['CivilEco'] >= EcoFilter[0]:
                            symbol = "▲+ "
                            color = 102
                        elif staris['StarCivil']['CivilEco'] >= EcoFilter[1]:
                            symbol = "▲ "
                            color = 101
                        elif staris['StarCivil']['CivilEco'] >= EcoFilter[2]:
                            symbol = "= "
                            color = 103
                        else:
                            symbol = "▼ "
                            color = 100
                    else:
                        color = 0
                        dim = curses.A_DIM
                else:
                    color = 0

                if selected == staris["StarID"]:
                    selected_frame1 = "["
                    selected_frame2 = "]"
                    color = 103
                    dim = 0
                else:
                    selected_frame1 = " "
                    selected_frame2 = " "
                
                symbolselected = ""
                if StartLoc == staris['StarID']:
                    symbolselected = "➤ "
                
                sec_sym = ""
                if staris.get("StarCivil") and staris['StarCivil'] != []:
                    civil_id = f" ({staris['StarID']})"
                    if staris['StarCivil']['CivilStation']['StationHangar'] != []:
                        sec_sym = " ⛛"
                else:
                    civil_id = ""
            
                stdscr.addstr(int(staris['y']),int(staris['x']),str(selected_frame1+symbolselected+symbol+staris['Star']+civil_id+sec_sym+selected_frame2), curses.color_pair(color) | dim)
                
            staris = GenMap(selected)

            stdscr.addstr(0,0,borderEX(x),curses.color_pair(2))
            stdscr.addstr(1,1,filter_str, curses.color_pair(1))
            stdscr.addstr(1,len(filter_str)+2, selected_str, curses.color_pair(1))
            stdscr.addstr(1,len(filter_str)+2+len(selected_str)+1, vision_str, curses.color_pair(1))
            stdscr.addstr(y-1,0,borderEX(x-1),curses.color_pair(2))
            stdscr.addstr(1,len(vision_str)+1+len(filter_str)+2+len(selected_str)+1, f" Distance: {Distation:,} ", curses.color_pair(4))
            stdscr.box()
            stdscr.addstr(0,int((x-len("GalaxyMap"))/2), "GalaxyMap")
            menu = "| [ENTER]-Trav | [←↑↓→]-Navigation | [f]-Filter | [s]-Select | [c]-Vision | [i]-Info |"
            stdscr.addstr(y-1,int((x-len(menu))/2), menu)
            stdscr.move(y-1,x-1)
            stdscr.refresh()

            keyname = stdscr.getkey()

            if keyname == "f":
                menu = MapFilter

                choice = pi.menuscreen(stdscr, "Filters", menu)

                for i,k in enumerate(MapFilter):
                    if choice == k:
                        filt = i
            
            PlayerIs['MapFilter'] = filt
            
            if keyname == "q":
                break
            
            if keyname == "s":
                curses.echo(True)
                win = curses.newwin(3,40,y-4,1)
                win.box()
                win.addstr(1,1,"Select: ")
                try:
                    selected = int(win.getstr(1,9).decode())
                except:
                    selected = selected

            if keyname == "c":
                curses.echo(True)
                win = curses.newwin(3,40,y-4,1)
                win.box()
                win.addstr(1,1,"Vision: ")
                try:
                    selecLock = int(win.getstr(1,9).decode())
                except:
                    selecLock = selecLock

            if keyname == "i":
                if DebugInfo == True or (staris.get("StarIntel") and staris['StarIntel'] == True):
                    infostar = curses.newwin(25,40,int((y-25)/2),(x-40)-1)
                    infostar.box()
                    infostar.addstr(1,int((40-len("Star system information"))/2),"Star system information")
                    infostar.addstr(3,1,f"StarID: {staris['StarID']}", curses.color_pair(100))
                    infostar.addstr(4,1,f"Star: {staris['Star']}")
                    infostar.addstr(5,1,f"Physical statistic:")
                    infostar.addstr(6,1,f"    - StCl: {staris['Class']}")
                    infostar.addstr(7,1,f"    - Temp: {staris['Temp']:,} K")
                    infostar.addstr(8,1,f"    - Mass: {staris['Mass']:,} ☉")
                    infostar.addstr(9,1,f"    - Size: {staris['Size']:,} ☉")
                    infostar.addstr(10,1,f"    - Lum: {staris['Luminos']:,} ☉")
                    infostar.addstr(11,1,f"Planets: {len(staris['Planets']):,}")
                    infostar.addstr(12,1,f"Asteroids: {len(staris['Asteroids'])}")
                    infostar.addstr(13,1,f"Inteled: {str(staris.get("StarIntel"))}")
                    if staris.get("StarCivil") and staris["StarCivil"] != []:
                        infostar.addstr(14,1,f"Civilization:", curses.color_pair(101))
                        infostar.addstr(15,1,f"    - Station: {staris['StarCivil']['CivilStation']['StationName']}", curses.color_pair(101))
                        infostar.addstr(16,1,f"    - Population: {staris['StarCivil']['CivilPop']:,}", curses.color_pair(101))
                        infostar.addstr(17,1,f"    - Stable: {staris['StarCivil']['CivilStable']}%", curses.color_pair(101))
                        infostar.addstr(18,1,f"    - Economic: {Economics[staris['StarCivil']['CivilEconomicType']]}", curses.color_pair(101))
                        infostar.addstr(19,1,f"    - ECO: {staris['StarCivil']['CivilEco']}", curses.color_pair(101))
                        infostar.addstr(20,1,f"    - Secure: {StarSecurityType[staris['StarCivil']['CivilSecurity']]}", curses.color_pair(101))
                    if staris.get("PlayerPinned") and staris["PlayerPinned"] == True:
                        infostar.addstr(21,1,f"Favorite: {staris['PlayerPinnedDesc']}", curses.color_pair(103))
                    infostar.getch()
                else:
                    pi.error_stdscr(stdscr, "Error", "Do not find information.")
            
            if keyname == "\n":
                if selected == StartLoc: break
                if Distation > TravelDistation:
                    if error("Too far to flight!", "Upgrade your ship's engine!") == 0:
                        break
                if PlayerIs['Ship']['Fuel'] >= FuelRequire:
                    loading(3)
                    PlayerIs['Location'] = selected
                    PlayerIs['Ship']['Fuel'] -= FuelRequire
                    break
                else:
                    if error("Out of fuel!","Refuel at the nearest station") == 0:
                        break

            if keyname == "KEY_RIGHT":
                selected += 1
            if keyname == "KEY_LEFT":
                selected += -1
            if keyname == "KEY_UP":
                selecLock += border*2
            if keyname == "KEY_DOWN":
                selecLock += -border*2
            stdscr.clear()

    def ship_cargo(stdscr):
        select = 0
        while True:
            if PlayerIs['Ship']['Storage'] != []:
                curses.start_color()
                curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE)
                stdscr.clear()
                size_y, size_x = stdscr.getmaxyx()
                stdscr.box()
                stdscr.addstr(0,int((size_x-len("Cargo"))/2), "Cargo")
                stdscr.addstr(1,8, "Item")
                stdscr.addstr(1,(size_x-len("Count"))-2, "Count")

                for i, item in enumerate(PlayerIs['Ship']['Storage']):
                    if select == i:
                        color = curses.color_pair(1)
                        stdscr.addstr(size_y-2, int((size_x-len(f"Selected: {ItemsDB[item['ItemID']]['ItemName']}"))-1), f"Selected: {ItemsDB[item['ItemID']]['ItemName']}")
                    else:
                        color = curses.color_pair(0)
                    stdscr.addstr(i+2, 1, f" {ItemsDB[item['ItemID']]['ItemName']}", color)
                    stdscr.addstr(i+2, (size_x-len("Count"))-2, f"{item['ItemCount']:,}")

                stdscr.addstr(size_y-2, 1, f"Total: {ShipTotalItems}/{PlayerMaxItems} | Types: {i+1}")
                key = stdscr.getkey()

                if key == "\n":
                    return PlayerIs['Ship']['Storage'][select]['ItemID']
                if key == "KEY_DOWN":
                    if select < i:
                        select += 1
                if key == "KEY_UP":
                    if select > 0:
                        select -= 1
                if key == "q":
                    break
            else:
                pi.error_stdscr(stdscr, "Cargo is empty", "Buy anything in station store.")
                break

    def Logic():
        PlayerIs["WorldDay"] += 1
        PlayerIs['Statistic']['IncomeFromColony'] = 0
        for i in range(len(CustomStars)):
            StarIs = CustomStars[i] 
            # Player colony money income
            if StarIs.get("StarControled") and StarIs['StarControled'] == True:
                if StarIs.get("StarCivil"):
                    Star = GenMap(StarIs['StarID'])
                    PlanetLiveCount = 0
                    for ii in range(len(Star['Planets'])):
                        if Star['Planets'][ii]['PlanetClass'] == 4:
                            if Star['Planets'][ii]['PlanetLive'] == True:
                                PlanetLiveCount += 1
                    PlayerIs['Statistic']['IncomeFromColony'] += int((int(StarIs['StarCivil']['CivilPop'] * 3) * (4 * PlanetLiveCount+1)) * StarIs['StarCivil']['CivilEco'])
                    pi.StarChange(StarIs['StarID'], 'InfoIncome', int((int(StarIs['StarCivil']['CivilPop']* 3) * (4 * PlanetLiveCount+1)) * StarIs['StarCivil']['CivilEco']))
                    PlayerIs['Money'] += int((int(StarIs['StarCivil']['CivilPop'] * 3) * (4 * PlanetLiveCount+1)) * StarIs['StarCivil']['CivilEco'])
                    
            # Civil Eco changes
            if StarIs.get("StarCivil"):
                if rwos.randint(1,2) == 1:
                    StarIs['StarCivil']['CivilEco'] -= rwos.uniform(sett_eco_include[0], sett_eco_include[1])
                else:
                    StarIs['StarCivil']['CivilEco'] += rwos.uniform(sett_eco_include[0], sett_eco_include[1])
                if StarIs['StarCivil']['CivilEco'] < CivilEcoMin:
                    StarIs['StarCivil']['CivilEco'] = CivilEcoMin
                else:
                    if StarIs['StarCivil']['CivilEco'] > CivilEcoMax:
                        StarIs['StarCivil']['CivilEco'] = CivilEcoMax

                if rwos.randint(1,4) == 1:
                    StarIs['StarCivil']['CivilStable'] += rwos.randint(-1,1)

                if StarIs['StarCivil']['CivilStable'] > 100: StarIs['StarCivil']['CivilStable'] = 100
                if StarIs['StarCivil']['CivilStable'] < 0: StarIs['StarCivil']['CivilStable'] = 0
                pi.StarChange(StarIs['StarID'],'StarCivil',StarIs['StarCivil'])

            if StarIs.get("StarCivil") and StarIs.get('StarControled'):
                if StarIs.get("Planets"):
                    for i in range(len(StarIs['Planets'])):
                        PlanetIs = StarIs['Planets'][i]
                        if PlanetIs.get("PlanetColony"):
                            if PlanetIs['PlanetColony']['ColonyBuild']['Enabled'] == True:
                                if wlengine.DateCheck(wlengine.DateRead(PlanetIs['PlanetColony']['ColonyBuild']['EndBuild'])):
                                    PlanetIs['PlanetColony']['ColonyBuild']['Enabled'] = False

                        if PlanetIs.get("PlanetColony"):
                            if PlanetIs['PlanetColony']['ColonyBuild']['Enabled'] == False:
                                PlanetIs['PlanetColony']['ColonyPop'] += rwos.randint(sett_pop_include[0],sett_pop_include[1]) * (1 + (PlanetIs['PlanetColony']['ColonyLevel']**2))
                        pi.StarChange(StarIs['StarID'], 'Planets', StarIs['Planets'])

            # Pop include
            if StarIs.get("StarCivil"):
                ColonyAllPops = 0
                if StarIs.get("Planets"):
                    for i in range(len(StarIs['Planets'])):
                        PlanetIs = StarIs['Planets'][i]
                        if PlanetIs.get('PlanetColony'):
                            if PlanetIs['PlanetColony']['ColonyBuild']['Enabled'] == False:
                                ColonyAllPops += PlanetIs['PlanetColony']['ColonyPop']
    
                StarIs['StarCivil']['CivilPop'] = ColonyAllPops
                pi.StarChange(StarIs['StarID'],'StarCivil',StarIs['StarCivil'])
            
            if StarIs.get("StarCivil") and StarIs['StarCivil']['CivilPop'] >= 10_000 and StarIs['StarCivil']['CivilStable'] >= 50:
                PlayerIs['SocialScore'] += rwos.randint(1,10) * wl.Level

    def Duel(Title="Test", Target={"Bot": "TestBot", "BotShip": rwos.choice(Ships), "BotModificationSlots": [], "BotAccuracy": 50, "BotInterval": 3}):
        def BattleScreen(stdscr):
            stdscr.box()
            sz_y, sz_x = stdscr.getmaxyx()
            stdscr.addstr(0,int((sz_x-len("Battle"))/2), "Battle")
            player = stdscr.derwin(20,30,1,1)
            player.box()
            curses.napms(2000)
            # wl.Skip()
            # print(wl.Wall)
            # print(Title)
            # print(wl.Wall)
            # print(f" ▪ {PlayerPrefix} Гравець: {LevelRangIs} {wl.Player} - HP: {PlayerHP:,} - DM: {PlayerDMG:,} | {PlayerMessage}")
            # print(f"     {Colore.Gray} ▪ Корабель: {PlayerIs['Ship']['ShipName']}{Colore.Reset}")
            # print(wl.Wall)
            # print(f" ▪ {BotPrefix} Опонент: {str(Target['Bot'])} - HP: {BotHP:,} - DM: {BotDMG:,} | {BotMessage}")
            # print(f"     {Colore.Gray} ▪ Корабель: {BotShip['ShipName']}{Colore.Reset}")
            # print(wl.Wall)
            # time.sleep(BattleCooldown)

        BotModificationSlots = []
        BotShip = Target['BotShip']

        if Target['BotModificationSlots'] == []:
            for i in range(BotShip['ShipMaxModification']):
                BotModificationSlots.append({"ModificationID": None, "ModificationLevel": rwos.randint(1,ModMaxLevel)})

            ModTypeArmor = []
            for i, mod in enumerate(ShipModifications):
                if mod['ModType'] == 1: ModTypeArmor.append(mod['ModID'])

            ModTypeWeapons = []
            for i, mod in enumerate(ShipModifications):
                if mod['ModType'] == 3: ModTypeWeapons.append(mod['ModID'])

            for i, mod in enumerate(BotModificationSlots):
                if i in [0,1]: mod['ModificationID'] = rwos.choice(ModTypeArmor)
                else: mod['ModificationID'] = rwos.choice(ModTypeWeapons)
        
        PlayerHP = PlayerShipHP
        
        BotHP = BotShip['ShipHealth']
        for i, mod in enumerate(BotModificationSlots):
            if ShipModifications[mod['ModificationID']]['ModType'] == 1:
                BotHP += ShipModifications[mod['ModificationID']]['ModValue'] * (mod['ModificationLevel'] * ModLevelCoeff)

        PlayerDMG = PlayerShipDMG
        PlayerInterval = PlayerShipInterval

        BotDMG = 0
        BotInterval = 0
        for i, mod in enumerate(BotModificationSlots):
            if ShipModifications[mod['ModificationID']]['ModType'] == 3:
                BotDMG += ShipModifications[mod['ModificationID']]['ModValue']['damage'] * (mod['ModificationLevel'] * ModLevelCoeff)
                BotInterval += ShipModifications[mod['ModificationID']]['ModValue']['interval']

        PlayerAccuracy = 40
        BotAccuracy = Target['BotAccuracy']

        BattleToggle = True

        PlayerMessage = ""
        BotMessage = ""

        while BattleToggle == True:
            PlayerDM = int(PlayerDMG * rwos.uniform(BattleCoefMin, BattleCoefMax))
            BotDM = int(BotDMG * rwos.uniform(BattleCoefMin, BattleCoefMax))
            
            for p_i in range(PlayerInterval):
                BotPrefix = f"{Colore.Blue}⛊{Colore.Reset}"
                PlayerPrefix = f"({p_i+1}) {Colore.Red}▶{Colore.Reset}"
                if rwos.randint(1,2) == 1:
                    PlayerMessage = "Залп"
                    if rwos.randint(1,100) <= PlayerAccuracy:
                        BotHP -= PlayerDM
                        BotMessage = f"Ненесена шкода ({PlayerDM})"
                    else:
                        BotHP -= 0
                        PlayerMessage = "Залп: Промах"
                if BotHP <= 0:
                    BotHP = 0
                    return True
                
            PlayerMessage = ""

            for b_i in range(BotInterval):
                PlayerPrefix = f"{Colore.Blue}⛊{Colore.Reset}"
                BotPrefix = f"({b_i+1}) {Colore.Red}▶{Colore.Reset}"
                if rwos.randint(1,2) == 1:
                    BotMessage = "Залп"
                    if rwos.randint(1,100) <= BotAccuracy:
                        PlayerHP -= BotDM
                        PlayerMessage = f"Ненесена шкода ({BotDM})"
                    else:
                        PlayerHP -= 0
                        BotMessage = "Залп: Промах"
                if PlayerHP <= 0:
                    PlayerHP = 0
                    return False
            
            BotMessage = ""
            curses.wrapper(BattleScreen)
            curses.napms(2000)

    def Navy(Title="Test"):
        PlayerNavy = PlayerIs['Navy']
        BotNavy = StarIs['StarCivil']['Navy']

        def BattleScreen():
            wl.Skip()
            print(
                f"{wl.Wall}\n"
                f"{Title}\n"
                f"{wl.Wall}\n"
                f"Флот {LevelRangIs} {wl.Player}\n"
                f"   ▪ Крейсерів: {PlayerNavy['NavyCruisers']:,}\n"
                f"   ▪ Кораблів: {PlayerNavy['NavyShips']:,}\n"
                f"   ▪ Рівень кораблів: {PlayerNavy['NavyLevel']}\n"
                f"   ▪ Бойовий ранг: {int(PlayerNavy['NavyCruisers'] * PlayerNavy['NavyShips'] * PlayerNavy['NavyLevel']):,}\n"
                f"{PlayerShipHealth:.2f} - {PlayerCruiserHealth:.2f}\n"
                f"{wl.Wall}\n"
                f"Флот {StarIs['Star']}\n"
                f"   ▪ Крейсерів: {BotNavy['NavyCruisers']:,}\n"
                f"   ▪ Кораблів: {BotNavy['NavyShips']:,}\n"
                f"   ▪ Рівень кораблів: {BotNavy['NavyLevel']}\n"
                f"   ▪ Бойовий ранг: {int(BotNavy['NavyCruisers'] * BotNavy['NavyShips'] * BotNavy['NavyLevel']):,}\n"
                f"{BotShipHealth:.2f} - {BotCruiserHealth:.2f}\n"
                f"{wl.Wall}\n"
            )
        
        x = 0
        PlayerShipHealth = 200 * PlayerNavy['NavyLevel']
        PlayerCruiserHealth = 500 * PlayerNavy['NavyLevel']
        BotShipHealth = 200 * BotNavy['NavyLevel']
        BotCruiserHealth = 500 * BotNavy['NavyLevel']

        while True:
            x += 1
            
            for i in range(int((ConsoleSizeY/2) - (15/2))):
                print()

            PlayerShipHealth -= ((0.6 * BotNavy['NavyLevel'] * BotNavy['NavyShips'] * (1 + (0.133 * BotNavy['NavyCruisers']))))
            BotShipHealth -= ((0.6 * PlayerNavy['NavyLevel'] * PlayerNavy['NavyShips'] * (1 + (0.133 * PlayerNavy['NavyCruisers']))))
            PlayerCruiserHealth -= ((0.3 * BotNavy['NavyLevel'] * BotNavy['NavyShips'] * (1 + (0.133 * BotNavy['NavyCruisers']))))
            BotCruiserHealth -= ((0.3 * PlayerNavy['NavyLevel'] * PlayerNavy['NavyShips'] * (1 + (0.133 * PlayerNavy['NavyCruisers']))))

            if PlayerShipHealth <= 0:
                PlayerNavy['NavyShips'] -= 1
                PlayerShipHealth = 200 * PlayerNavy['NavyLevel']

            if BotShipHealth <= 0:
                BotNavy['NavyShips'] -= 1
                BotShipHealth = 200 * BotNavy['NavyLevel']

            if PlayerCruiserHealth <= 0:
                PlayerNavy['NavyCruisers'] -= 1
                PlayerCruiserHealth = 500 * PlayerNavy['NavyLevel']

            if BotCruiserHealth <= 0:
                BotNavy['NavyCruisers'] -= 1
                BotCruiserHealth = 500 * BotNavy['NavyLevel']

            if PlayerNavy['NavyShips'] <= 0: PlayerNavy['NavyShips'] = 0
            if BotNavy['NavyShips'] <= 0: BotNavy['NavyShips'] = 0
            if PlayerNavy['NavyCruisers'] <= 0: PlayerNavy['NavyCruisers'] = 0
            if BotNavy['NavyCruisers'] <= 0: BotNavy['NavyCruisers'] = 0
            if PlayerNavy['NavyShips'] <= 0 and PlayerNavy['NavyCruisers'] <= 0: return False
            if BotNavy['NavyShips'] <= 0 and BotNavy['NavyCruisers'] <= 0: return True

            BattleScreen()
            for i in range(int((ConsoleSizeY/2) - (15/2))): print()
            time.sleep(0.3)

    def NavyBattle(Title="Test", Navy = {"NavyCruisers": rwos.randint(1,100), "NavyShips": rwos.randint(1,500), "NavyLevel": rwos.randint(1,100)}):
        PlayerNavy = PlayerIs['Navy']
        BotNavy = Navy

        def BattleScreen():
            wl.Skip()
            print(
                f"{wl.Wall}\n"
                f"{Title}\n"
                f"{wl.Wall}\n"
                f"Флот {LevelRangIs} {wl.Player}\n"
                f"   ▪ Крейсерів: {PlayerNavy['NavyCruisers']:,}\n"
                f"   ▪ Кораблів: {PlayerNavy['NavyShips']:,}\n"
                f"   ▪ Рівень кораблів: {PlayerNavy['NavyLevel']}\n"
                f"   ▪ Бойовий ранг: {int(PlayerNavy['NavyCruisers'] * PlayerNavy['NavyShips'] * PlayerNavy['NavyLevel']):,}\n"
                f"{PlayerShipHealth:.2f} - {PlayerCruiserHealth:.2f}\n"
                f"{wl.Wall}\n"
                f"Флот {StarIs['Star']}\n"
                f"   ▪ Крейсерів: {BotNavy['NavyCruisers']:,}\n"
                f"   ▪ Кораблів: {BotNavy['NavyShips']:,}\n"
                f"   ▪ Рівень кораблів: {BotNavy['NavyLevel']}\n"
                f"   ▪ Бойовий ранг: {int(BotNavy['NavyCruisers'] * BotNavy['NavyShips'] * BotNavy['NavyLevel']):,}\n"
                f"{BotShipHealth:.2f} - {BotCruiserHealth:.2f}\n"
                f"{wl.Wall}\n"
            )
        
        x = 0
        PlayerShipHealth = 200 * PlayerNavy['NavyLevel']
        PlayerCruiserHealth = 500 * PlayerNavy['NavyLevel']
        BotShipHealth = 200 * BotNavy['NavyLevel']
        BotCruiserHealth = 500 * BotNavy['NavyLevel']

        while True:
            x += 1
            
            for i in range(int((ConsoleSizeY/2) - (15/2))):
                print()

            PlayerShipHealth -= ((0.6 * BotNavy['NavyLevel'] * BotNavy['NavyShips'] * (1 + (0.133 * BotNavy['NavyCruisers']))))
            BotShipHealth -= ((0.6 * PlayerNavy['NavyLevel'] * PlayerNavy['NavyShips'] * (1 + (0.133 * PlayerNavy['NavyCruisers']))))
            PlayerCruiserHealth -= ((0.3 * BotNavy['NavyLevel'] * BotNavy['NavyShips'] * (1 + (0.133 * BotNavy['NavyCruisers']))))
            BotCruiserHealth -= ((0.3 * PlayerNavy['NavyLevel'] * PlayerNavy['NavyShips'] * (1 + (0.133 * PlayerNavy['NavyCruisers']))))

            if PlayerShipHealth <= 0:
                PlayerNavy['NavyShips'] -= 1
                PlayerShipHealth = 200 * PlayerNavy['NavyLevel']

            if BotShipHealth <= 0:
                BotNavy['NavyShips'] -= 1
                BotShipHealth = 200 * BotNavy['NavyLevel']

            if PlayerCruiserHealth <= 0:
                PlayerNavy['NavyCruisers'] -= 1
                PlayerCruiserHealth = 500 * PlayerNavy['NavyLevel']

            if BotCruiserHealth <= 0:
                BotNavy['NavyCruisers'] -= 1
                BotCruiserHealth = 500 * BotNavy['NavyLevel']

            if PlayerNavy['NavyShips'] <= 0: PlayerNavy['NavyShips'] = 0
            if BotNavy['NavyShips'] <= 0: BotNavy['NavyShips'] = 0
            if PlayerNavy['NavyCruisers'] <= 0: PlayerNavy['NavyCruisers'] = 0
            if BotNavy['NavyCruisers'] <= 0: BotNavy['NavyCruisers'] = 0
            if PlayerNavy['NavyShips'] <= 0 and PlayerNavy['NavyCruisers'] <= 0: return False
            if BotNavy['NavyShips'] <= 0 and BotNavy['NavyCruisers'] <= 0: return True

            BattleScreen()
            for i in range(int((ConsoleSizeY/2) - (15/2))): print()
            time.sleep(0.3)

    def PlayerShipModificationAll(ModType):
        Value = 0
        for i in range(len(PlayerIs['Ship']['ShipModification'])):
            ModPlayerIs = PlayerIs['Ship']['ShipModification'][i]
            if ModPlayerIs['ModificationID'] != None:
                ModIs = ShipModifications[ModPlayerIs['ModificationID']]
                if ModIs['ModType'] == ModType:
                    Value += (ModIs['ModValue'] * (ModPlayerIs['ModificationLevel'] * ModLevelCoeff))
        return int(Value)

    def Battle(title="Test", sub=["Simple text.", "Target: Sol (3170)"], Enemy={"Enemy": "Test", "BotShip": 1, "ShipMods": 5, "Level": 1}):
        BotMods = []
        ModsWeapon = []
        for i, k in enumerate(ShipModifications):
            if k['ModType'] == 3:
                ModsWeapon.append(k['ModID'])

        for i in range(Enemy['ShipMods']):
            if i == 0:
                BotMods.append(
                    {
                        "ModificationID": rwos.choice(ModsWeapon),
                        "ModificationLevel": rwos.randint(0,ModMaxLevel)
                    }
                )
            else:
                BotMods.append(
                    {
                        "ModificationID": rwos.randint(0, len(ShipModifications)-1),
                        "ModificationLevel": rwos.randint(0,ModMaxLevel)
                    }
                )
        
        EnemyHP = Ships[Enemy['BotShip']]['ShipHealth']
        EnemyDM = 0
        for i,k in enumerate(BotMods):
            if ShipModifications[k['ModificationID']]['ModType'] == 1:
                EnemyHP += int(ShipModifications[k['ModificationID']]['ModValue'] * k['ModificationLevel'])
            if ShipModifications[k['ModificationID']]['ModType'] == 3:
                EnemyDM += int(ShipModifications[k['ModificationID']]['ModValue']['damage'] * k['ModificationLevel'])
        def screen(stdscr, EnemyHP, EnemyDM, PlayerHP, PlayerDM):
            sz_y, sz_x = stdscr.getmaxyx()
            zone = stdscr.derwin(sz_y-11-len(sub),sz_x-5, len(sub)+1,int((sz_x-(sz_x-5))/2))
            z_y, z_x = zone.getmaxyx()
            
            player_pos = rwos.randint(1,z_y-2)
            bot_pos = rwos.randint(1,z_y-2)
            while True:
                stdscr.clear()
                stdscr.box()

                stdscr.addstr(0,int((sz_x-len(title))/2), title)
                
                for i,k in enumerate(sub):
                    stdscr.addstr(1+i, 1, k)

                player = stdscr.derwin(9,40,int((sz_y-10)), 1)
                bot = stdscr.derwin(9,40,int((sz_y-10)), int(sz_x-41))

                player.box()
                bot.box()

                player.addstr(1,1,f"You: {PlayerIs['Nickname']}")
                player.addstr(2,1,f"Ship: {Ships[PlayerIs['Ship']['ShipID']]['ShipName']}")
                player.addstr(3,1,f"HP: {PlayerHP:,} HP")
                player.addstr(4,1,f"DM: {PlayerDM:,} DM")
                player.addstr(5,1,f"INT: {PlayerShipInterval:,}")
                player.addstr(6,1,f"RET: ({pi.reitingPrint(int(PlayerHP/100), 5)})")

                bot.addstr(1,1,f"Enemy: {Enemy['Enemy']}")
                bot.addstr(2,1,f"Ship: {Ships[Enemy['BotShip']]['ShipName']}")
                bot.addstr(3,1,f"HP: {EnemyHP:,} HP")
                bot.addstr(4,1,f"DM: {EnemyDM:,} DM")
                bot.addstr(5,1,f"INT: 2")
                bot.addstr(6,1,f"LVL: {Enemy['Level']} ({pi.reitingPrint(int(Enemy['Level']/33),5)})")

                zone.clear()
                zone.box()

                player_pos += rwos.randint(-5,5)
                if player_pos <= 2:
                    player_pos = 2
                if player_pos >= z_y-2:
                    player_pos = z_y-2
                
                bot_pos += rwos.randint(-5,5)
                if bot_pos <= 2:
                    bot_pos = 2
                if bot_pos >= z_y-2:
                    bot_pos = z_y-2

                if rwos.randint(1,100) <= 10:
                    bot_pos = player_pos

                zone.addstr(player_pos,2,">")
                zone.addstr(bot_pos,z_x-3, "<")

                zone.addstr(player_pos-1,1,"YOU")
                zone.addstr(bot_pos-1,z_x-4, "ENE")

                if rwos.randint(1,100) <= 75 and player_pos == bot_pos:
                    for i in range(z_x-5):
                        zone.addstr(player_pos, 3, f"{" "*i}-")
                        zone.refresh()
                        curses.napms(30)
                    zone.addstr(bot_pos, z_x-3, "✷")
                    zone.refresh()
                    curses.napms(300)
                    EnemyHP -= PlayerDM

                if EnemyHP <= 0:
                    pi.message(stdscr, title="Win", message="You win.")
                    return 1

                if rwos.randint(1,100) <= 75 and bot_pos == player_pos:
                    for i in range(z_x-5):
                        zone.addstr(player_pos, z_x-4-i, f"-{" "*i}")
                        zone.refresh()
                        curses.napms(30)
                    zone.addstr(player_pos, 2, "✷")
                    zone.refresh()
                    curses.napms(300)
                    PlayerHP -= EnemyDM
                
                if PlayerHP <= 0:
                    pi.message(stdscr, title="Lose", message="You lose.")
                    return 0

                zone.refresh()
                stdscr.refresh()
                curses.napms(500)


        curses.wrapper(lambda stdscr: screen(stdscr, EnemyHP, EnemyDM, PlayerShipHP, PlayerShipDMG))

class game():
    class player():
        def refuel():
            PlayerIs['Ship']['Fuel'] = Ships[PlayerIs['Ship']['ShipID']]['ShipMaxFuel']
        def loc(x):
            PlayerIs['Location'] = x
    
    class world():
        def mature(cycle):
            for i in range(cycle):
                pi.Logic()

    class docs():
        def stars(x,y):
            file = open("file.txt","w")
            file.write()
            file.close()

            file = open("file.txt","a")
            file.write()

class wlengine():
    def level_upgrade(
            x,
            maxlevel=100,
            parametrs={
                'coust': False,
                'coust_par': 1000,
                'coust_type': 'money' # [money] [intelball] [battlescore]
            }
        ):

        wl.Skip()

        CurrentLevel = x
        while True:
            wl.Skip()

            NewLevel = int(x) + 1
            NewLevelLable = NewLevel
            Level = int(x)

            if NewLevel == maxlevel:
                NewLevelLable = "MAX"

            if NewLevel <= maxlevel:
                wl.Skip()
                
                wl.CenterText("Покращення рівня")
                wl.CenterText(f"                       {Colore.Green}{Level}{Colore.Gray} ━━━━━━━━━━━━━━━━━━━━━━► {Colore.Yellow}{NewLevelLable}{Colore.Reset}")
                wl.CenterTextEnd(1)
                if parametrs['coust'] == True:
                    coust = parametrs['coust_par'] * NewLevel
                    if parametrs['coust_type'] == 'money':
                        print(f"Це буде коштувати: {wl.TextColore(f"{coust:,} ©", Colore.Yellow)}")
                    if parametrs['coust_type'] == 'intelball':
                        print(f"Це буде коштувати: {wl.TextColore(f"{coust:,} ◭", Colore.Blue)}")
                    if parametrs['coust_type'] == 'battlescore':
                        print(f"Це буде коштувати: {wl.TextColore(f"{coust:,} ⊙", Colore.Red)}")
                wl.TextColorePr("[SPACE] для підтвердження", Colore.Gray)

                Command = wl.Command()

                if Command in ["d", "D"] and x < MaxNavyLevel-1:
                    x += 1
                if Command in ["a", "A"] and x > 1 and x > CurrentLevel:
                    x -= 1
                if Command in ['e', ' ']:
                    if x == CurrentLevel:
                        exit()
                    else:
                        if parametrs['coust'] == False:
                            return x
                        else:
                            return x, coust
                if Command in ['q']:
                    exit()
    
    def Date():
        if CustomToday:
            dat = date(SetDate[2], SetDate[1], SetDate[0])
            return dat
        else:
            return date.today()

    def DateCheck(other_date):
        today = wlengine.Date()
        if today >= other_date:
            return True
        else:
            return False

    def DiffDate(other_date):
        return abs((wlengine.Date() - other_date).days)

    def DateStr():
        dat = wlengine.Date()
        return f"{dat.strftime("%d.%m.%Y")}"
    
    def DateOtherStr(other_date):
        dat = other_date
        return f"{dat.strftime("%d.%m.%Y")}"
    
    def DateSave(other_date):
        return [other_date.day, other_date.month, other_date.year]
    
    def DateRead(table):
        return date(day=table[0], month=table[1], year=table[2])
    
    PlayerDate = DateRead(PlayerIs['NextDate'])

class Colore():
    Red = colorama.Fore.RED
    LightRed = colorama.Fore.LIGHTRED_EX
    Gray = colorama.Fore.LIGHTBLACK_EX
    Yellow = colorama.Fore.YELLOW
    Reset = colorama.Fore.RESET
    Green = colorama.Fore.GREEN
    Blue = colorama.Fore.BLUE
    Cyan = colorama.Fore.CYAN
    LightYellow = colorama.Fore.LIGHTYELLOW_EX
    White = colorama.Fore.WHITE

def ChoiceModificationSlot():
    wl.Skip()
    for abs in range(MaxShipModification):
        SlotIs = PlayerIs['Ship']['ShipModification'][abs]
        if SlotIs['ModificationID'] != None:
            ModIs = ShipModifications[SlotIs['ModificationID']]
            if ModIs['ModType'] == 0: ColoreMod = Colore.Yellow
            if ModIs['ModType'] == 1: ColoreMod = Colore.Red
            if ModIs['ModType'] == 2: ColoreMod = Colore.Blue
            if ModIs['ModType'] == 3: ColoreMod = Colore.LightRed
            if ModIs['ModType'] == 4: ColoreMod = colorama.Fore.LIGHTYELLOW_EX
            if ModIs['ModType'] == 5: ColoreMod = colorama.Fore.GREEN
            ModLabel = f"{ColoreMod}{ModIs['ModName']}{Colore.Reset}"
        else:
            ModLabel = f"{Colore.Gray}Відсутній{Colore.Reset}"
        ModLevel = SlotIs['ModificationLevel']
        ModLevelEmpty = f"{Colore.Gray}{ModLevelEmptySym}{Colore.Reset}"
        ModLevelSymbol = f"{Colore.Yellow}{ModLevelSym}{Colore.Reset}"
        ModLevelA = ModLevelSymbol * (ModLevel)
        ModLevelB = ModLevelEmpty * (ModMaxLevel-ModLevel)
        ModLevelIs = ModLevelA + ModLevelB
        print(f"{abs+1}. {abs+1} слот: [{ModLabel}] ({ModLevelIs})")
    inp = int(input("Вибрати слот: ")) - 1
    return inp

def ModificationSlots(x):
    for abs in range(MaxShipModification):
        SlotIs = PlayerIs['Ship']['ShipModification'][abs]
        if SlotIs['ModificationID'] != None:
            ModIs = ShipModifications[SlotIs['ModificationID']]
            if ModIs['ModType'] == 0: ColoreMod = Colore.Yellow
            if ModIs['ModType'] == 1: ColoreMod = Colore.Red
            if ModIs['ModType'] == 2: ColoreMod = Colore.Blue
            if ModIs['ModType'] == 3: ColoreMod = Colore.LightRed
            if ModIs['ModType'] == 4: ColoreMod = colorama.Fore.LIGHTYELLOW_EX
            if ModIs['ModType'] == 5: ColoreMod = colorama.Fore.GREEN
            ModLabel = f"{ColoreMod}{ModIs['ModName']}{Colore.Reset}"
        else:
            ModLabel = f"{Colore.Gray}Відсутній{Colore.Reset}"
        sr = "  " * x
        ModLevel = SlotIs['ModificationLevel']
        ModLevelEmpty = f"{Colore.Gray}{ModLevelEmptySym}{Colore.Reset}"
        ModLevelSymbol = f"{Colore.Yellow}{ModLevelSym}{Colore.Reset}"
        ModLevelA = ModLevelSymbol * (ModLevel)
        ModLevelB = ModLevelEmpty * (ModMaxLevel-ModLevel)
        ModLevelIs = ModLevelA + ModLevelB
        print(f"{sr} ▪ {abs+1} слот: [{ModLabel}] ({ModLevelIs})")

AddTravelDistation = 0
for i in range(len(PlayerIs['Ship']['ShipModification'])):
    ModIs = PlayerIs['Ship']['ShipModification'][i]
    if not ModIs['ModificationID'] == None: 
        Mod = ShipModifications[ModIs['ModificationID']]
        if Mod['ModType'] == 5:
            AddTravelDistation += (Mod['ModValue'] * (1 + ModIs['ModificationLevel']))
TravelDistation = Ships[PlayerIs['Ship']['ShipID']]['ShipTravelingDist'] + AddTravelDistation + SetTravelDistation

if wl.Level >= MaxLevel:
    wl.Level = MaxLevel

MaxShipModification = (Ships[PlayerIs['Ship']['ShipID']]['ShipMaxModification'] + AddShipModification)
if len(PlayerIs['Ship']['ShipModification']) < MaxShipModification:
    for abs in range(MaxShipModification - len(PlayerIs['Ship']['ShipModification'])):
        PlayerIs['Ship']['ShipModification'].append(
            {
                "ModificationID": None,
                "ModificationLevel": 0
            }
        )
elif len(PlayerIs['Ship']['ShipModification']) > MaxShipModification:
    for abs in range(len(PlayerIs['Ship']['ShipModification']) - MaxShipModification):
        PlayerIs['Ship']['ShipModification'].pop()

NewFuel = 0
for i in range(len(PlayerIs['Ship']['ShipModification'])):
    if not PlayerIs['Ship']['ShipModification'][i]['ModificationID'] == None:
        if ShipModifications[PlayerIs['Ship']['ShipModification'][i]['ModificationID']]['ModType'] == 0:
            NewFuel += (ShipModifications[PlayerIs['Ship']['ShipModification'][i]['ModificationID']]['ModValue'] * (1 + int(PlayerIs['Ship']['ShipModification'][i]['ModificationLevel'] * ModLevelCoeff)))

FuelNow = PlayerIs['Ship']['Fuel']
FuelMaxCapacity = Ships[PlayerIs['Ship']['ShipID']]['ShipMaxFuel'] + NewFuel
if FuelNow > FuelMaxCapacity: 
    PlayerIs['Ship']['Fuel'] = FuelMaxCapacity

PlayerShipDMG = 0
PlayerShipInterval = 0
for i in range(len(PlayerIs['Ship']['ShipModification'])):
    ModPlayer = PlayerIs['Ship']['ShipModification'][i]
    if ModPlayer['ModificationID'] != None:
        ModIs = ShipModifications[ModPlayer['ModificationID']]
        if ModIs['ModType'] == 3:
            PlayerShipDMG += (ModIs['ModValue']['damage'] * (1 +ModPlayer['ModificationLevel'] * ModLevelCoeff))
            PlayerShipInterval += ModIs['ModValue']['interval']

PlayerShipHP = Ships[PlayerIs['Ship']['ShipID']]['ShipHealth']
for i in range(len(PlayerIs['Ship']['ShipModification'])):
    ModPlayerIs = PlayerIs['Ship']['ShipModification'][i]['ModificationID']
    ModPlayer = PlayerIs['Ship']['ShipModification'][i]
    if ModPlayerIs != None:
        ModIs = ShipModifications[ModPlayerIs]
        if ModIs['ModType'] == 1:
            PlayerShipHP += (ModIs['ModValue'] * (1 + ModPlayer['ModificationLevel'] * ModLevelCoeff))

PlayerMaxItems = Ships[PlayerIs['Ship']['ShipID']]['ShipMaxItems']
for i in range(len(PlayerIs['Ship']['ShipModification'])):
    ModPlayerIs = PlayerIs['Ship']['ShipModification'][i]['ModificationID']
    ModPlayer = PlayerIs['Ship']['ShipModification'][i]
    if ModPlayerIs != None:
        ModIs = ShipModifications[ModPlayerIs]
        if ModIs['ModType'] == 6:
            PlayerMaxItems += ModIs['ModValue'] + (5 * ModPlayer['ModificationLevel'])

if StarIs.get("StarCivil"):
    if StarIs['StarCivil']['CivilReputation'] > 100:
        StarIs['StarCivil']['CivilReputation'] = 100

    if StarIs['StarCivil']['CivilReputation'] < 0:
        StarIs['StarCivil']['CivilReputation'] = 0

try:
    LevelRangIs = LevelRang[wl.Level]
except (KeyError):
    LevelRangIs = LevelRang[0]

for i, item in enumerate(PlayerIs['Ship']['Storage']):
    if item['ItemCount'] >= PlayerMaxItems:
        itemget = item['ItemCount'] - PlayerMaxItems
        wl.InvRem(item['ItemID'], itemget)

ShipTotalItems = 0
for i, k in enumerate(PlayerIs['Ship']['Storage']):
    ShipTotalItems += k['ItemCount']
PlayerIs['Ship']['ItemsCount'] = ShipTotalItems

MiningRate = 0
for i, mod in enumerate(PlayerIs['Ship']['ShipModification']):
    if mod['ModificationID'] != None:
        ModIs = ShipModifications[mod['ModificationID']]
        if ModIs['ModType'] == 7:
            MiningRate += ModIs['ModValue'] * (1 + mod['ModificationLevel'])