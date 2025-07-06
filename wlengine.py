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
import time, random, os, colorama, json, math, getch
from datetime import datetime, timedelta, date
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

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
StarIs = GenMap(PlayerIs['Location'])
PlayerAtribution = PlayerIs['Atribution']

# -- Main Code
colorama.init()

VersionClient = "Dev"
EngineVersion = "2.16"

ConsoleSizeX = 120
ConsoleSizeY = 35
Rconsole = Console()

TimeToday = time.strftime("%d")
TimeMonth = time.strftime("%m")
TimeYear = time.strftime("%Y")

rwos = random.Random()

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
    Level = int(PlayerIs['XP'] / XpToLevel)
    StopGame = exit
    SquereSymbol = "▪"
    Latters = [chr(i) for i in range(65, 91)]
    LowerLatters = [chr(i) for i in range(97, 123)]

    def Command():
        key = getch.getch()
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
        print(f" ▪ Зірка: {StarIs['Star']}" + wl.Date().center(int(ConsoleSizeX - 25 - len(f" ▪ Зірка: {StarIs['Star']}"))))
        print(wl.Wall)
        print(f" ▪ Ім'я: {PlayerIs['Nickname']}")
        print(f" ▪ Кредити: {Colore.Yellow}{PlayerIs['Money']:,} ©{Colore.Reset}")
        print(f" ▪ Досл. бали: {Colore.Blue}{PlayerIs['IntelBall']:,} ◭{Colore.Reset}")
        print(f" ▪ XP: {PlayerIs['XP']:,} XP {Colore.Gray}| Level: {wl.Level} {Colore.Reset}")
        print(f" ▪ Корабель: {PlayerIs['Ship']['ShipName']}{Colore.Gray} ({Ships[PlayerIs['Ship']['ShipID']]['ShipName']}) | МВС: {TravelDistation} св. р | Паливо: {PlayerIs['Ship']['Fuel']}/{FuelMaxCapacity} тон{Colore.Reset}")
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

    def Date():
        start_date = datetime(3000,1,1)
        start_date += timedelta(days=PlayerIs["WorldDay"])
        date = f"{start_date.strftime("%d.%m.%Y")}"
        return date
    
    def InvAdd(itemID, count):
        if itemID > len(ItemsDB):
            wl.Error(f"Предмет із номером #{itemID} не існує")
        else:
            if len(PlayerIs["Ship"]['Storage']) == 0:
                PlayerIs["Ship"]['Storage'].append(
                    {
                        "ItemID": itemID,
                        "ItemCount": count
                    }
                )
            else:
                FleetID = None
                for alli in range(len(PlayerIs["Ship"]['Storage'])):
                    ItemIs = PlayerIs["Ship"]['Storage'][alli]
                    if ItemIs['ItemID'] == itemID:
                        break
                if ItemIs['ItemID'] == itemID:
                    ItemIs['ItemCount'] += count
                else:
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

    def FleetInvAdd(itemID, count, FleetID):
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
                FleetID = None
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
    
    def GalaxyMap(type, FleetID=None):
        StartLoc = PlayerIs['Location']
        StartMapLoc = PlayerIs['Location']
        while True:
            wl.Skip()
            empty_map = ""

            for star in range(StartMapLoc-15, StartMapLoc+16):
                StarIs = GenMap(star)
                SymbolFrame = ""
                SymbolFrameBack = ""

                if StarIs.get("PlayerPinned"):
                    PlayerSymbol = SymbolOfStarPinned
                else:
                    if StarIs['StarSister'] != []:
                        PlayerSymbol = SymbolOfStar + SymbolOfStar
                    else:
                        if StarIs['Class'] == "BH":
                            PlayerSymbol = "⚬ "
                        else:
                            PlayerSymbol = SymbolOfStar

                if PlayerIs.get("Fleet"):
                    for i in range(len(PlayerIs['Fleet'])):
                        if PlayerIs['Fleet'][i]['Location'] == StarIs['StarID']:
                            FleetSymbol = f"{Colore.Blue} ⊴{Colore.Reset}"
                            break
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
                    elif StarIs['Class'] == "L":
                        PlayerLight = colorama.Fore.RED
                    elif StarIs['Class'] == "T":
                        PlayerLight = colorama.Fore.RED
                    else:
                        PlayerLight = colorama.Fore.LIGHTBLACK_EX

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

                if PlayerIs['Location'] == StarIs["StarID"]:
                    SelectedFrame = "["
                    SelectedFrameBack = "]"
                else:
                    SelectedFrame = " "
                    SelectedFrameBack = " "
                starview = f"{SelectedFrame}{PlayerLight}{PlayerSymbol}{StarIs['Star']}{Colore.Reset}{FleetSymbol}{SelectedFrameBack}"
                sp = "⋮" * random.randint(MinFulling, MaxFulling)
                empty_map += f"{sp}{starview}{sp}"

            text = "Galaxy Map"
            print(f"{"─" * (int(ConsoleSizeX / 2) - len(text))} {text} {"─" * (int(ConsoleSizeX / 2)-1)}")
            MapFilterPrint = f"{colorama.Back.WHITE}{colorama.Fore.BLACK}█ Фільтр мапи: {MapFilter[PlayerIs['MapSettings']['Filter']]} █{colorama.Back.RESET}{colorama.Fore.RESET}"
            ShiftMap = f"{colorama.Back.WHITE}{colorama.Fore.BLACK} Центр: {StartMapLoc} █{colorama.Fore.RESET}{colorama.Back.RESET}"
            print(MapFilterPrint,ShiftMap)
            print(f"{"─" * ConsoleSizeX}")

            StarIs = GenMap(PlayerIs['Location'])
            Distation = abs(PlayerIs['Location'] - StartLoc)
            
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
            if PlayerIs['MapSettings']['Filter'] == 2:
                SpecularClassBar = f"{colorama.Back.WHITE}{colorama.Fore.BLACK}█ Спек. клас: {StarIs['Class']} █{colorama.Fore.RESET}{colorama.Back.RESET}"
                if StarIs.get("StarIntel") and StarIs["StarIntel"] == True:
                    PlanetCountBar = f"{colorama.Back.WHITE}{colorama.Fore.BLACK}█ Кількість планет: {len(StarIs['Planets'])} █{colorama.Fore.RESET}{colorama.Back.RESET}"
                else:
                    PlanetCountBar = ""
            else:
                SpecularClassBar = ""
                PlanetCountBar = ""
                
            print(f"{"─" * ConsoleSizeX}")
            print(f"{SelectedStar}{PinnedDescPrint}{SelectedDist}{SpecularClassBar}{PlanetCountBar}")
            print(f"{"─" * ConsoleSizeX}")
            com = wl.Command()

            if com == "a" or com == "A":
                PlayerIs['Location'] -= 1
            if com == "d" or com == "D":
                PlayerIs['Location'] += 1
            if com == "s" or com == "S":
                StartMapLoc += 1
            if com == "w" or com == "W":
                StartMapLoc -= 1
            if com == "c" or com == "C":
                StartMapLoc = int(input("Назначити центр: "))
            if com == " ":
                if StartLoc == PlayerIs['Location']:
                    wl.Skip()
                    break
                else:
                    if type == "SHIP":
                        FleetID = None
                        if Distation > TravelDistation:
                            wl.Error("Занадто далеко!")
                        if PlayerIs['Ship']['Fuel'] >= FuelRequire:
                            PlayerIs['Location']
                            PlayerIs['Ship']['Fuel'] -= FuelRequire
                            wl.Loading(f"Подорож до {GenMap(PlayerIs['Location'])['Star']}", 5)
                            wl.SaveJSON("save.json", save)
                            wl.Skip()
                            break
                        else:
                            wl.Skip()
                            wl.Error("Невисточає пального")
                    if type == "FLEET":
                        if Distation > TravelDistation:
                            wl.Error("Занадто далеко!")
                        if PlayerIs['Fleet'][FleetID]['Fuel'] >= FuelRequire:
                            PlayerIs['Location']
                            PlayerIs['Fleet'][FleetID]['Location'] = PlayerIs['Location']
                            PlayerIs['Fleet'][FleetID]['Fuel'] -= FuelRequire
                            wl.Loading(f"Подорож до {GenMap(PlayerIs['Location'])['Star']}", 5)
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
                    StarChoiceFleet = int(input("Пункт призначення: "))
                    HyperDistant = abs(StartLoc - StarChoiceFleet)
                    if HyperDistant > Fleets[PlayerIs['Fleet'][FleetID]['FleetID']]['FleetMaxHyperdrive']:
                        wl.Error("Занадто далеко")
                    if PlayerIs['Fleet'][FleetID]['Fuel'] < 50:
                        wl.Error("Не достатньо пального!")
                    else:
                        PlayerIs['Location'] = StarChoiceFleet
                        PlayerIs['Fleet'][FleetID]['Location'] = StarChoiceFleet
                        PlayerIs['Fleet'][FleetID]['Fuel'] -= 50
                        StartLoc = StarChoiceFleet
                        wl.Loading(f"Перебуваємо в гіперстрибку до {GenMap(StarChoiceFleet)['Star']}", 10)
                        break
            if com == "f" or com == "F":
                if PlayerIs['MapSettings']['Filter'] == 0: PlayerIs['MapSettings']['Filter'] = 1
                elif PlayerIs['MapSettings']['Filter'] == 1: PlayerIs['MapSettings']['Filter'] = 2
                elif PlayerIs['MapSettings']['Filter'] == 2: PlayerIs['MapSettings']['Filter'] = 0
            if com == "m" or com == "M":
                wl.Skip()
                m1 = int(input("Від: "))
                m2 = int(input("До: "))
                wl.Skip()
                for absi in range(m1, m2):
                    StarIs = GenMap(absi)
                    PlanetLive = 0
                    for i in range(len(StarIs['Planets'])):
                        if StarIs['Planets'][i]['PlanetClass'] == 4:
                            PlanetLive += 1
                        else:
                            PlanetLive += 0
                    if StarIs.get("StarCivil"):
                        StarColor = colorama.Fore.GREEN
                        print(f"{StarColor}StarID: {StarIs['StarID']} - Система: {StarIs['Star']} - Планет: {len(StarIs['Planets'])}: з життям: {PlanetLive} - Цивілізація: Станція: {StarIs['StarCivil']['CivilStation']['StationName']} - Фракція: {StarIs['StarCivil']['CivilFraction']['FractionName']} - Населення: {StarIs['StarCivil']['CivilFraction']['FractionPop']:,}{colorama.Fore.RESET}")
                    else: 
                        StarColor = colorama.Fore.RED
                        print(f"{StarColor}StarID: {StarIs['StarID']} - Система: {StarIs['Star']} - Планет: {len(StarIs['Planets'])}: з життям: {PlanetLive}{colorama.Fore.RESET}")
                input()
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
                            PlanetLiveCount += 1
                    PlayerIs['Statistic']['IncomeFromColony'] += int((int(StarIs['StarCivil']['CivilFraction']['FractionPop'] * 2) * (4 * PlanetLiveCount+1)) * StarIs['StarCivil']['CivilEco'])
                    ProjectInfinity.StarChange(StarIs['StarID'], 'InfoIncome', int((int(StarIs['StarCivil']['CivilFraction']['FractionPop'] * 2) * (4 * PlanetLiveCount+1)) * StarIs['StarCivil']['CivilEco']))
                    PlayerIs['Money'] += int((int(StarIs['StarCivil']['CivilFraction']['FractionPop'] * 2) * (4 * PlanetLiveCount+1)) * StarIs['StarCivil']['CivilEco'])
                    PlayerIs['XP'] += int(StarIs['StarCivil']['CivilFraction']['FractionPop'] / 12) * (3 * PlanetLiveCount)
            # Pop include
            if StarIs.get("StarCivil"):
                StarIs['StarCivil']['CivilFraction']['FractionPop'] += int(rwos.randint(-2,4) * (math.sqrt(StarIs['StarCivil']['CivilFraction']['FractionPop'])) + 1)
                if StarIs['StarCivil']['CivilFraction']['FractionPop'] < 1:
                    StarIs['StarCivil']['CivilFraction']['FractionPop'] = 0
                ProjectInfinity.StarChange(StarIs['StarID'],'StarCivil',StarIs['StarCivil'])
            # Civil Eco changes
            if StarIs.get("StarCivil"):
                StarIs['StarCivil']['CivilEco'] += random.uniform(-0.00001, 0.01)
                if StarIs['StarCivil']['CivilEco'] < CivilEcoMin:
                    StarIs['StarCivil']['CivilEco'] = CivilEcoMin
                else:
                    if StarIs['StarCivil']['CivilEco'] > CivilEcoMax:
                        StarIs['StarCivil']['CivilEco'] = CivilEcoMax
                ProjectInfinity.StarChange(StarIs['StarID'],'StarCivil',StarIs['StarCivil'])

class game():
    class player():
        def refuel():
            PlayerIs['Ship']['Fuel'] = Ships[PlayerIs['Ship']['ShipID']]['ShipMaxFuel']
        def loc(x):
            PlayerIs['Location'] = x
    
    class world():
        def mature(cycle):
            for i in range(cycle):
                ProjectInfinity.Logic()

TravelDistation += Ships[PlayerIs['Ship']['ShipID']]['ShipTravelingDist']

if wl.Level >= MaxLevel:
    wl.Level = MaxLevel

NewFuel = 0
for i in range(len(PlayerIs['Ship']['ShipModification'])):
    if PlayerIs['Ship']['ShipModification'][i]['ModificationID'] == 0:
        NewFuel += 50

FuelNow = PlayerIs['Ship']['Fuel']
FuelMaxCapacity = Ships[PlayerIs['Ship']['ShipID']]['ShipMaxFuel'] + NewFuel