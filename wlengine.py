#     ██╗    ██╗██╗     ███████╗███╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗    ██╗   ██╗ ██╗   ██████╗ ███████╗
#     ██║    ██║██║     ██╔════╝████╗  ██║██╔════╝ ██║████╗  ██║██╔════╝    ██║   ██║███║   ╚════██╗╚════██║
#     ██║ █╗ ██║██║     █████╗  ██╔██╗ ██║██║  ███╗██║██╔██╗ ██║█████╗      ██║   ██║╚██║    █████╔╝    ██╔╝
#     ██║███╗██║██║     ██╔══╝  ██║╚██╗██║██║   ██║██║██║╚██╗██║██╔══╝      ╚██╗ ██╔╝ ██║   ██╔═══╝    ██╔╝ 
#     ╚███╔███╔╝███████╗███████╗██║ ╚████║╚██████╔╝██║██║ ╚████║███████╗     ╚████╔╝  ██║▄█╗███████╗   ██║  
#      ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝      ╚═══╝   ╚═╝╚═╝╚══════╝   ╚═╝  
#                                                                                                           
#                                                                                                  
# © WhiteLight studio • 2024 • ALL RIGHTS RESERVED • https://sites.google.com/view/whitelight-studio

# -- Base import ■ ▪ ∙ •
import time, random, os, datetime, colorama, msvcrt, json

# -- Files import
from galaxy.map import GenMap
from wlregister import *
from galaxy.mapchanges import CustomStars
from settings import *
from nickname_generator import generate as ranname

# -- Save import
with open("save.json",'r', encoding="utf-8") as f:
    save = json.load(f)

# -- LICENSE
LICENSE = open("LICENSE", "r", encoding="utf-8")

PlayerIs = save
StarIs = GenMap(PlayerIs['Location']['Star'])
PlayerAtribution = PlayerIs['Atribution']

# -- Main Code
colorama.init()

VersionClient = "Dev"
EngineVersion = "2.16"

ConsoleSizeX = 135
ConsoleSizeY = 35

TimeToday = time.strftime("%d")
TimeMonth = time.strftime("%m")
TimeYear = time.strftime("%Y")

class Colore():
    Red = colorama.Fore.RED
    LightRed = colorama.Fore.LIGHTRED_EX
    Gray = colorama.Fore.LIGHTBLACK_EX
    Yellow = colorama.Fore.YELLOW
    Reset = colorama.Fore.RESET
    Green = colorama.Fore.GREEN
    Blue = colorama.Fore.BLUE

class wl(): # Main class
    Wall = "─" * (ConsoleSizeX - 1)
    DoList = "1. Галактична карта ▪ 2. Зоряна система ▪ 3. Планета ▪ 4. Станція ▪ 5. Інше".center(ConsoleSizeX)
    Player = f"{PlayerIs['Nickname']}"
    Data = f"{TimeToday}.{TimeMonth}.{TimeYear}"
    ID = f"0x{random.randint(int(1e+7),int(9e+7))}"
    Level = int(int(PlayerIs['XP']) / XpToLevel) + 1
    StopGame = exit
    SquereSymbol = "▪"
    Latters = [chr(i) for i in range(65, 91)]
    LowerLatters = [chr(i) for i in range(97, 123)]

    def Command():
        key = msvcrt.getch()
        key = key.decode("utf-8")
        return key

    def ConsoleSetSize():
        os.system(f"mode con cols={ConsoleSizeX} lines={ConsoleSizeY}")

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
        wl.SkipValue(int(ConsoleSizeY / 2) - 2)
    
    def Skip():
        for Skip_screen in range(ConsoleSizeY):
            print()
    
    def SkipValue(value):
        for SkipScreen in range(value):
            print()
    
    def Quation(text):
        quation = input(f"{text} (1/0): ")
        if quation == "1":
            return quation
        else:
            exit()
    
    def Massage(text):
        wl.Skip()
        print(f"{Colore.Gray}{text}{Colore.Reset}")
        input()
    
    def ParrametrInspect(par, text):
        if par == True:
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

    def Loading(name, ranger):
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

    def SearchIndex(listing, object , name):
        for index, item in enumerate(listing):
            if item[object] == name:
                return index
        else: return -1
    
    def TextColore(text, colore):
        textt = f"{colore}{text}{Colore.Reset}"
        print(textt)

    def Screen():
        print(f"Project Infinity ▪ {VersionClient}".center(ConsoleSizeX))
        print(f"© WhiteLight studio - all rights reserved")
        print(wl.Wall)
        print(f" ▪ Зірка: {StarIs['Star']}")
        print(wl.Wall)
        print(f" ▪ Ім'я: {PlayerIs['Nickname']}")
        print(f" ▪ Кредити: {Colore.Yellow}{PlayerIs['Money']:,} ©{Colore.Reset}")
        print(f" ▪ Досл. бали: {Colore.Blue}{PlayerIs['IntelBall']:,} ◭{Colore.Reset}")
        print(f" ▪ XP: {PlayerIs['XP']:,} XP {Colore.Gray}| Level: {wl.Level} {Colore.Reset}")
        print(f" ▪ Корабель: {PlayerIs['Ship']['ShipName']}{Colore.Gray} ({Ships[PlayerIs['Ship']['ShipID']]['ShipName']}) | МВС: {TravelDistation} св. р | Паливо: {PlayerIs['Ship']['Fuel']}/{Ships[PlayerIs['Ship']['ShipID']]['ShipMaxFuel']} тон{Colore.Reset}")
        if DebugInfo == True: print(f"{Colore.Red}Debug-інформація: MapSeed: {MapSeed}, StarID: {StarIs['StarID']}{Colore.Reset}")
        print(wl.Wall)
        print(wl.DoList)
        print(wl.Wall)
        for abis in range(9):
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
        else: return -1

    def Menu(list):
        for elements in range(len(list)):
            NameElement = list[elements]
            print(f"{elements+1}. {NameElement}")
    
    def ChoiceMenu(list):
        for elements in range(len(list)):
            NameElement = list[elements]
            print(f"{elements+1}. {NameElement}")
        Command = wl.Command()
        Choice = list[int(Command) - 1]
        return Choice
            
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

    def DateDay(d):
        today = time.strftime("%d")

        if today in str(d):
            event = True
        else:
            event = False
        return event
    
    def DateMonth(m):
        tomonth = time.strftime("%m")

        if m == tomonth:
            event = True
        else:
            event = False
        return event
    
    def DateYear(y):
        toyear = time.strftime("%Y")

        if y == toyear:
            event = True
        else:
            event = False
        return event
    
    def getDate():
        a = datetime.date.today()
        return a
    
    def InvAdd(itemID, count, inStorage):
        if itemID > len(ItemsDB):
            wl.Error(f"Предмет із номером #{itemID} не існує")
        else:
            if len(PlayerIs[inStorage]['Storage']) == 0:
                PlayerIs[inStorage]['Storage'].append(
                    {
                        "ItemID": itemID,
                        "ItemCount": count
                    }
                )
            else:
                for alli in range(len(PlayerIs[inStorage]['Storage'])):
                    ItemIs = PlayerIs[inStorage]['Storage'][alli]
                    if ItemIs['ItemID'] == itemID:
                        break
                if ItemIs['ItemID'] == itemID:
                    ItemIs['ItemCount'] += count
                else:
                    PlayerIs[inStorage]['Storage'].append(
                        {
                            "ItemID": itemID,
                            "ItemCount": count
                        }
                    )
        
    def InvRem(itemID, count, inStorage):
        if itemID > len(ItemsDB):
            wl.Error(f"Предмет із номером #{itemID} не існує")
        else:
            if len(PlayerIs[inStorage]['Storage']) == 0:
                wl.Error("В сховище порожньо")
            else:
                for alli in range(len(PlayerIs[inStorage]['Storage'])):
                    ItemIs = PlayerIs[inStorage]['Storage'][alli]
                    if ItemIs['ItemID'] == itemID:
                        ItemIsID = alli
                        break
                if ItemIs['ItemID'] == itemID:
                    if ItemIs['ItemCount'] <= count:
                        PlayerIs[inStorage]['Storage'].pop(ItemIsID)
                    else:
                        ItemIs['ItemCount'] -= count

    
class ProjectInfinity():
    def StarChange(StarID, ElementTag, ElementValue):
        if len(CustomStars) == 0:
            CustomStars.append(
                {
                    f'StarID': StarID,
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
                        f'StarID': StarID,
                        str(ElementTag): ElementValue
                    }
                )
        file = open("galaxy/mapchanges.py", "w", encoding="utf-8")
        file.write(f"CustomStars = {CustomStars}")
    
    def GalaxyMap(type):
        StartLoc = PlayerIs['Location']['Star']
        while True:
            wl.Skip()
            empty_map = ""

            for star in range(StartLoc-TravelDistation, StartLoc+(TravelDistation + 1)):
                StarIs = GenMap(star)
                SymbolFrame = ""
                SymbolFrameBack = ""
                if StarIs.get("PlayerPinned"):
                    PlayerSymbol = SymbolOfStarPinned
                else:
                    PlayerSymbol = SymbolOfStar

                if PlayerIs.get("Fleet"):
                    if PlayerIs['Fleet']['Location'] == StarIs['StarID']:
                        FleetSymbol = f"{Colore.Blue} ⊴{Colore.Reset}"
                    else:
                        FleetSymbol = ""
                else:
                    FleetSymbol = ""

                if PlayerIs['MapSettings']['Filter'] == 2:
                    if StarIs['Class'] == "O":
                        PlayerLight = colorama.Fore.BLUE
                    elif StarIs['Class'] == "B":
                        PlayerLight = colorama.Fore.LIGHTBLUE_EX
                    elif StarIs['Class'] == "A":
                        PlayerLight = colorama.Fore.WHITE
                    elif StarIs['Class'] == "F":
                        PlayerLight = colorama.Fore.LIGHTYELLOW_EX
                    elif StarIs['Class'] == "G":
                        PlayerLight = colorama.Fore.YELLOW
                    elif StarIs['Class'] == "K":
                        PlayerLight = colorama.Fore.LIGHTRED_EX
                    elif StarIs['Class'] == "M":
                        PlayerLight = colorama.Fore.RED

                if PlayerIs['MapSettings']['Filter'] == 1:
                    if StarIs.get("StarControled") and StarIs['StarControled'] == True:
                        PlayerLight = Colore.Red
                    else:
                        PlayerLight = Colore.Gray

                if PlayerIs['MapSettings']['Filter'] == 0:
                    if StarIs.get("StarCivil"):
                        PlayerLight = colorama.Fore.GREEN
                    elif StarIs.get("StarIntel"):
                        PlayerLight = colorama.Fore.LIGHTBLUE_EX
                    elif StarIs.get("PlayerPinned"):
                        PlayerLight = colorama.Fore.YELLOW
                    else: 
                        PlayerLight = Colore.Gray

                if PlayerIs['Location']['Star'] == StarIs["StarID"]:
                    SelectedFrame = "["
                    SelectedFrameBack = "]"
                else:
                    SelectedFrame = " "
                    SelectedFrameBack = " "
                
                sp = "⁝" * random.randint(MinFulling,MaxFulling)
                empty_map += f"{Colore.Gray}{sp}{Colore.Reset}{SelectedFrame}{PlayerLight}{PlayerSymbol} {StarIs['Star']}{Colore.Reset}{FleetSymbol}{SelectedFrameBack}{Colore.Gray}{sp}{Colore.Reset}"

            text = "Galaxy Map"
            print(f"{"─" * (int(ConsoleSizeX / 2) - len(text))} {text} {"─" * (int(ConsoleSizeX / 2)-1)}")
            MapFilterPrint = f"{colorama.Back.WHITE}{colorama.Fore.BLACK}█ Фільтр мапи: {MapFilter[PlayerIs['MapSettings']['Filter']]} █{colorama.Back.RESET}{colorama.Fore.RESET}"
            print(MapFilterPrint)
            print(f"{"─" * ConsoleSizeX}")
            StarIs = GenMap(PlayerIs['Location']['Star'])
            Distation = abs(PlayerIs['Location']['Star'] - StartLoc)
            print(empty_map)

            if StarIs.get("PlayerPinned") and StarIs['PlayerPinned'] == True:
                SelectedStar = f"{colorama.Back.YELLOW}{colorama.Fore.BLACK}█ Вибрано: {StarIs['Star']} █{colorama.Back.RESET}{colorama.Fore.RESET}"
                PinnedDescPrint = f"{colorama.Back.YELLOW}{colorama.Fore.BLACK}█ ★⚲ {StarIs['PlayerPinnedDesc']} █{colorama.Back.RESET}{colorama.Fore.RESET}"
            else:
                SelectedStar = f"{colorama.Back.WHITE}{colorama.Fore.BLACK}█ Вибрано: {StarIs['Star']} █{colorama.Back.RESET}{colorama.Fore.RESET}"
                PinnedDescPrint = ""
            if Distation > TravelDistation:
                SelectedDist = f"{colorama.Back.RED}{colorama.Fore.BLACK}█ Дистанція: /!\\ █{colorama.Back.RESET}{colorama.Fore.RESET}"
            else:
                SelectedDist = f"{colorama.Back.GREEN}{colorama.Fore.BLACK}█ Дистанція: {Distation} св. р █{colorama.Back.RESET}{colorama.Fore.RESET}"
            print(f"{"─" * ConsoleSizeX}")
            print(f"{SelectedStar}{PinnedDescPrint}{SelectedDist}")
            print(f"{"─" * ConsoleSizeX}")
            com = wl.Command()

            if com == "w" or com == "W":
                PlayerIs['Location']['Star'] -= 1
            if com == "s" or com == "S":
                PlayerIs['Location']['Star'] += 1
            if com == " ":
                if StartLoc == PlayerIs['Location']['Star']:
                    wl.Skip()
                    break
                else:
                    if type == "SHIP":
                        if Distation > TravelDistation:
                            wl.Error("Занадто далеко!")
                        if PlayerIs['Ship']['Fuel'] >= FuelRequire:
                            PlayerIs['Location']['Star']
                            PlayerIs['Ship']['Fuel'] -= FuelRequire
                            PlayerIs['MapSettings']['Filter'] = 0
                            wl.Loading(f"Подорож до {GenMap(PlayerIs['Location']['Star'])['Star']}", 5)
                            wl.SaveJSON("save.json", save)
                            wl.Skip()
                            break
                        else:
                            wl.Skip()
                            wl.Error("Невисточає пального")
                    if type == "FLEET":
                        if Distation > TravelDistation:
                            wl.Error("Занадто далеко!")
                        if PlayerIs['Ship']['Fuel'] >= FuelRequire:
                            PlayerIs['Location']['Star']
                            PlayerIs['Fleet']['Location'] = PlayerIs['Location']['Star']
                            PlayerIs['Fleet']['Fuel'] -= FuelRequire
                            PlayerIs['MapSettings']['Filter'] = 0
                            wl.Loading(f"Подорож до {GenMap(PlayerIs['Location']['Star'])['Star']}", 5)
                            wl.SaveJSON("save.json", save)
                            wl.Skip()
                            break
                        else:
                            wl.Skip()
                            wl.Error("Невисточає пального")
            if com == "q" or com == "Q":
                PlayerIs['MapSettings']['Filter'] = 0
                wl.Skip()
                exit()
            if type == "FLEET":
                if com == "e":
                    wl.Massage("Ви перейшли до Гіперстрибку флотоносця - в цьому режимі, Ви можете відправитися куда-завгодно, але це вимагає багато палива!")
                    wl.Skip()
                    StarChoiceFleet = int(input("Пункт призначення: "))
                    HyperDistant = abs(StartLoc - StarChoiceFleet)
                    if HyperDistant > FleetMaxDistant:
                        wl.Error("Занадто далеко")
                    if PlayerIs['Fleet']['Fuel'] <= 50:
                        wl.Error("Не достатньо пального!")
                    else:
                        PlayerIs['Location']['Star'] = StarChoiceFleet
                        PlayerIs['Fleet']['Location'] = StarChoiceFleet
                        PlayerIs['Fleet']['Fuel'] -= 50
                        StartLoc = StarChoiceFleet
                        wl.Loading(f"Перебуваємо в гіперстрибку до {GenMap(StarChoiceFleet)['Star']}", 10)
                        break
            if com == "f":
                if PlayerIs['MapSettings']['Filter'] == 0: PlayerIs['MapSettings']['Filter'] = 1
                elif PlayerIs['MapSettings']['Filter'] == 1: PlayerIs['MapSettings']['Filter'] = 2
                elif PlayerIs['MapSettings']['Filter'] == 2: PlayerIs['MapSettings']['Filter'] = 0
            if com == "m":
                wl.Skip()
                m1 = int(input("Від: "))
                m2 = int(input("До: "))
                wl.Skip()
                for absi in range(m1, m2):
                    StarIs = GenMap(absi)
                    if StarIs.get("StarCivil"): StarColor = colorama.Fore.GREEN
                    else: StarColor = colorama.Fore.RED
                    print(f"{StarColor}StarID: {StarIs['StarID']} - Система: {StarIs['Star']} - Планет: {len(StarIs['Planets'])}{colorama.Fore.RESET}")
                input()

class Debug():
    def Refuel():
        PlayerIs['Ship']['Fuel'] = Ships[PlayerIs['Ship']['ShipID']]['ShipMaxFuel']

TravelDistation += Ships[PlayerIs['Ship']['ShipID']]['ShipTravelingDist']