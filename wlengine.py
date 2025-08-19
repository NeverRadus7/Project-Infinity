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
from datetime import datetime, timedelta

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

VersionClient = "Dev"
EngineVersion = "2.16"

TimeToday = time.strftime("%d")
TimeMonth = time.strftime("%m")
TimeYear = time.strftime("%Y")

rwos = random.Random() # Random.WithOut.Seed

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

    def Command():
        key = getch.getch()
        return key

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
        print(f" ▪ Баланс: {Colore.Yellow}{PlayerIs['Money']:,} ©{Colore.Reset} ▪ {Colore.Blue}{PlayerIs['IntelBall']:,} ◭ {Colore.Reset} ▪ {Colore.Red}{PlayerIs['BattleScore']:,} ⊙{Colore.Reset}  ▪ {PlayerIs['XP']:,} XP {Colore.Gray}| Level: {wl.Level} {Colore.Reset} ▪ {wl.Date()}")
        print(wl.Wall)
        print(f" ▪ Зірка: {StarIs['Star']}")
        print(f" ▪ Ім'я: {PlayerIs['Nickname']}")
        print(f" ▪ Ранг: {LevelRangIs}")
        print(f" ▪ Вивчено систем: {PlayerIs['Statistic']['StarInteled']:,}")
        print(f" ▪ Систем під контролем: {PlayerIs['Statistic']['StarControled']:,}")
        print(f" ▪ Кількість колонії: {PlayerIs['Statistic']['StarColony']:,}")
        print(f" ▪ Прибуток з колонії: {PlayerIs['Statistic']['IncomeFromColony']:,} ©")
        print(f" ▪ Кількість крейсерів: {len(PlayerIs['Fleet'])}")
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
        wl.SaveJSON('save/map.json', CustomStars)

    def GalaxyMap(type, FleetID=None):
        StartLoc = PlayerIs['Location']
        StartMapLoc = PlayerIs['Location']
        while True:
            wl.Skip()
            empty_map = ""

            for star in range(StartMapLoc-15, StartMapLoc+16):
                StarIs = GenMap(star)
                #SymbolFrame = ""
                #SymbolFrameBack = ""

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
                
                if PlayerIs['Navy']['NavyDisable'] == False:
                    if PlayerIs['Navy']['NavyLocation'] == StarIs['StarID']:
                        NavySymbol = f"{Colore.Red} ⟁{Colore.Reset}"
                    else:
                        NavySymbol = ""
                else:
                        NavySymbol = ""
                
                ecosymbol = ""
                if PlayerIs['MapSettings']['Filter'] == 3:       
                    if StarIs.get("StarCivil"):
                        if StarIs['StarCivil']['CivilEco'] > 1.4:
                            ecosymbol = wl.TextColore(" ▴▴▴", Colore.Red)
                            PlayerLight = Colore.Red
                        if StarIs['StarCivil']['CivilEco'] > 1.1:
                            ecosymbol = wl.TextColore(" ▴", Colore.Red)
                            PlayerLight = Colore.Red
                        if StarIs['StarCivil']['CivilEco'] >= 0.8 and StarIs['StarCivil']['CivilEco'] <= 1.1:
                            ecosymbol = wl.TextColore(" ▸", Colore.Yellow)
                            PlayerLight = Colore.Yellow
                        if StarIs['StarCivil']['CivilEco'] < 0.8:
                            ecosymbol = wl.TextColore(" ▾", Colore.Green)
                            PlayerLight = Colore.Green
                        if StarIs['StarCivil']['CivilEco'] < 0.2:
                            ecosymbol = wl.TextColore(" ▾▾▾", Colore.Green)
                            PlayerLight = Colore.Green
                    else:
                        PlayerLight = Colore.Gray

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
                    if StarIs.get("StarCivil") and StarIs.get("StarControled"):
                        PlayerLight = Colore.Red
                    elif StarIs.get("StarControled") and StarIs['StarControled'] == True:
                        PlayerLight = colorama.Fore.LIGHTRED_EX
                    else:
                        PlayerLight = Colore.Gray

                if PlayerIs['MapSettings']['Filter'] == 0:
                    if StarIs.get("StarCivil"):
                        if StarIs['StarCivil']['CivilReputation'] <= 25: 
                            PlayerLight = colorama.Fore.RED
                            PlayerSymbol = "🕱 "
                        else:  
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
                starview = f"{SelectedFrame}{PlayerLight}{PlayerSymbol}{StarIs['Star']}{Colore.Reset}{ecosymbol}{FleetSymbol}{NavySymbol}{SelectedFrameBack}"
                sp = (Colore.Gray + SymbolFulling + Colore.Reset) * random.randint(MinFulling, MaxFulling)
                empty_map += f"{sp}{starview}{sp}"

            text = "Galaxy Map"
            print(f"{"─" * (int(ConsoleSizeX / 2) - len(text)-1)} {text} {"─" * (int(ConsoleSizeX / 2)-1)}")
            MapFilterPrint = f"{colorama.Back.WHITE}{colorama.Fore.BLACK}█ Фільтр мапи: {MapFilter[PlayerIs['MapSettings']['Filter']]} █{colorama.Back.RESET}{colorama.Fore.RESET}"
            ShiftMap = f"{colorama.Back.WHITE}{colorama.Fore.BLACK} Центр: {StartMapLoc} █{colorama.Fore.RESET}{colorama.Back.RESET}"
            print(MapFilterPrint, ShiftMap)
            print(f"{"─" * ConsoleSizeX}")

            StarIs = GenMap(PlayerIs['Location'])
            Distation = abs(PlayerIs['Location'] - StartLoc)
            
            print(empty_map)

            if StarIs.get("PlayerPinned") and StarIs['PlayerPinned'] is True:
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
                if StarIs.get("StarIntel") and StarIs["StarIntel"] is True:
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
                StartMapLoc = int(input("Перемістити фокус: "))
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
                            wl.Loading(f" Подорож до {GenMap(PlayerIs['Location'])['Star']}", 5)
                            wl.SaveJSON(SavePath, save)
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
                            wl.Loading(f" Подорож до {GenMap(PlayerIs['Location'])['Star']}", 5)
                            wl.SaveJSON(SavePath, save)
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
                elif PlayerIs['MapSettings']['Filter'] == 2: PlayerIs['MapSettings']['Filter'] = 3
                elif PlayerIs['MapSettings']['Filter'] == 3: PlayerIs['MapSettings']['Filter'] = 0
            
            if com == "m" or com == "M":
                wl.Skip()
                m1 = int(input("Від: "))
                m2 = int(input("До: "))
                wl.Skip()
                for absi in range(m1, m2):
                    StarIs = GenMap(absi)
                    PlanetLive = 0
                    for i in range(len(StarIs['Planets'])):
                        if StarIs['Planets'][i]['PlanetLive'] == True:
                            PlanetLive += 1
                        else:
                            PlanetLive += 0

                    if StarIs.get("StarCivil"):
                        StarColor = colorama.Fore.GREEN
                    else:
                        StarColor = colorama.Fore.LIGHTBLACK_EX

                    if PlayerIs['Location'] == StarIs['StarID']:
                        StarColor = Colore.White

                    for i in range(len(StarIs['Planets'])):
                        if StarIs['Planets'][i]['PlanetTerraform'] == True and StarIs['Planets'][i]['PlanetLive'] == False:
                            TerraformSymbol = f"{Colore.Red}⌬{StarColor}"
                            break
                        elif StarIs['Planets'][i]['PlanetLive'] == True:
                            TerraformSymbol = f"{Colore.Green}⌬{StarColor}"
                            break
                        else:
                            TerraformSymbol = ""

                    if StarIs.get("StarCivil"):
                        print()
                        print(
                            f"{StarColor}StarID: {StarIs['StarID']} {TerraformSymbol}\n"
                            f"- Система: {StarIs['Star']}\n"
                            f"- Планет: {len(StarIs['Planets'])} з них з життям: {PlanetLive}\n"
                            f"- Цивілізація:\n"
                            f"     - Станція: {StarIs['StarCivil']['CivilStation']['StationName']}\n"
                            f"     - Економіка: {Economics[StarIs['StarCivil']['CivilEconomicType']]}\n"
                            f"     - Населення: {StarIs['StarCivil']['CivilPop']:,}{colorama.Fore.RESET}")
                    else:
                        print()
                        print(f"{StarColor}StarID: {StarIs['StarID']} {TerraformSymbol} - Система: {StarIs['Star']} - Планет: {len(StarIs['Planets'])}: з життям: {PlanetLive}{colorama.Fore.RESET}")
                input()
            if com in ["h","H"]:
                wl.InfoBlock(
                    titleColore={
                        'colore': colorama.Back.GREEN, 
                        'title': "Допомога в командах"
                    },

                    text=
                        "[SPACE] - Відправитися до вибраної зірки\n"
                        "[WASD] - Вибрати та переміщувати центр\n"
                        "[F] - Змінити фільтр відображення\n"
                        "[C] - Перемістити фокус\n"
                        "[E] - Гіперпросторовий стрибок (Доступно тільки на крейсерів)\n"
                        "[Q] - Вийти з мапи без змін")
                
                wl.Command()

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
                    PlayerIs['Statistic']['IncomeFromColony'] += int((int(StarIs['StarCivil']['CivilPop'] * 2) * (4 * PlanetLiveCount+1)) * StarIs['StarCivil']['CivilEco'])
                    pi.StarChange(StarIs['StarID'], 'InfoIncome', int((int(StarIs['StarCivil']['CivilPop']* 2) * (4 * PlanetLiveCount+1)) * StarIs['StarCivil']['CivilEco']))
                    PlayerIs['Money'] += int((int(StarIs['StarCivil']['CivilPop'] * 2) * (4 * PlanetLiveCount+1)) * StarIs['StarCivil']['CivilEco'])
                    PlayerIs['XP'] += int(StarIs['StarCivil']['CivilPop'] / 12) * (3 * PlanetLiveCount)
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
                                if PlanetIs['PlanetColony']['ColonyBuild']['EndBuild'] <= PlayerIs['WorldDay']:
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

            # Security secure
            if StarIs.get("StarCivil"):
                if StarIs['StarCivil']['Navy']['NavyShips'] < 5: StarIs['StarCivil']['CivilSecurity'] = 0
                if StarIs['StarCivil']['Navy']['NavyCruisers'] >= 1 or StarIs['StarCivil']['Navy']['NavyShips'] >= 5: StarIs['StarCivil']['CivilSecurity'] = 1
                if StarIs['StarCivil']['Navy']['NavyCruisers'] >= 5 or StarIs['StarCivil']['Navy']['NavyShips'] >= 10: StarIs['StarCivil']['CivilSecurity'] = 2
                pi.StarChange(StarIs['StarID'], 'StarCivil', StarIs['StarCivil'])
            
                  
            if StarIs.get("StarCivil") and StarIs['StarCivil']['CivilStable'] <= 10 and StarIs.get('StarControled') and StarIs['StarControled'] == True:
                if PlayerIs['Location'] == StarIs['StarID'] and PlayerIs['Navy']['NavyDisable'] == False and PlayerIs['Navy']['NavyLocation'] == StarIs['StarID'] and StarIs['StarCivil']['Navy']['NavyShips'] > 0 and StarIs['StarCivil']['Navy']['NavyCruisers'] >= 0:
                    if rwos.randint(1,100) <= 10:
                        battle = pi.NavyBattle(f"Битва за {StarIs['Star']} | Ви захищаєтесь")
                        if battle == True:
                            StarIs['StarCivil']['CivilStable'] += 80
                            pi.StarChange(StarIs['StarID'], 'StarCivil', StarIs['StarCivil'])
                            PlayerIs['BattleScore'] += rwos.randint(1000,5000) * wl.Level
                        else:
                            pi.StarChange(StarIs['StarID'], 'StarControled', False)
                else:
                    EnemyCruisers = rwos.randint(0,50)
                    EnemyShips = rwos.randint(1,200)
                    EnemyNavyLevel = rwos.randint(1,100)

                    EnemyBattle = EnemyCruisers * EnemyShips * EnemyNavyLevel
                    
                    if PlayerIs['Navy']['NavyDisable'] == False and PlayerIs['Navy']['NavyLocation'] == StarIs['StarID'] and StarIs['StarCivil']['Navy']['NavyShips'] > 0 and StarIs['StarCivil']['Navy']['NavyCruisers'] >= 0:
                        PlayerBattle = PlayerIs['Navy']['NavyCruisers'] * PlayerIs['Navy']['NavyShips'] * PlayerIs['Navy']['NavyLevel']
                    else:
                        PlayerBattle = StarIs['StarCivil']['Navy']['NavyCruisers'] * StarIs['StarCivil']['Navy']['NavyShips'] * StarIs['StarCivil']['Navy']['NavyLevel']

                    if EnemyBattle > PlayerBattle:
                        StarIs['StarCivil']['CivilStable'] = rwos.randint(1,20)
                        StarIs['StarCivil']['Navy']['NavyCruisers'] = EnemyCruisers
                        StarIs['StarCivil']['Navy']['NavyShips'] = EnemyShips
                        StarIs['StarCivil']['Navy']['NavyLevel'] = EnemyNavyLevel
                        pi.StarChange(StarIs['StarID'], 'StarControled', False)
                        pi.StarChange(StarIs['StarID'], 'StarCivil', StarIs['StarCivil'])
                        wl.ScreenTextLable(f"Ви втратали {StarIs['Star']}")
                    else:
                        PlayerIs['BattleScore'] += rwos.randint(100,500) * wl.Level
                        StarIs['StarCivil']['CivilStable'] += 80
                        pi.StarChange(StarIs['StarID'], 'StarCivil', StarIs['StarCivil'])

    def Duel(Title="Test", Target={"Bot": "TestBot", "BotShip": rwos.choice(Ships), "BotModificationSlots": [], "BotAccuracy": 50, "BotInterval": 3}):
        wl.Skip()
        wl.Quation(f"{Title}: Ви точно хочете взяти участь в битві?")
        def BattleScreen():
            wl.Skip()
            print(wl.Wall)
            print(Title)
            print(wl.Wall)
            print(f" ▪ {PlayerPrefix} Гравець: {LevelRangIs} {wl.Player} - HP: {PlayerHP:,} - DM: {PlayerDMG:,} | {PlayerMessage}")
            print(f"     {Colore.Gray} ▪ Корабель: {PlayerIs['Ship']['ShipName']}{Colore.Reset}")
            print(wl.Wall)
            print(f" ▪ {BotPrefix} Опонент: {str(Target['Bot'])} - HP: {BotHP:,} - DM: {BotDMG:,} | {BotMessage}")
            print(f"     {Colore.Gray} ▪ Корабель: {BotShip['ShipName']}{Colore.Reset}")
            print(wl.Wall)
            time.sleep(BattleCooldown)

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
                BattleScreen()
                if BotHP <= 0:
                    BotHP = 0
                    BattleScreen()
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
                BattleScreen()
                if PlayerHP <= 0:
                    PlayerHP = 0
                    BattleScreen()
                    return False
            
            BotMessage = ""

            BattleScreen()

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
    LevelRangIs = LevelRang[max(LevelRang)]

for i, item in enumerate(PlayerIs['Ship']['Storage']):
    if item['ItemCount'] >= PlayerMaxItems:
        itemget = item['ItemCount'] - PlayerMaxItems
        wl.InvRem(item['ItemID'], itemget)