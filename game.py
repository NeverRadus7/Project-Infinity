from wlengine import *

wl.ConsoleSetSize()

wl.Skip()
wl.Screen()

CommandInput = wl.Command()

if CommandInput == "1":
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
            
            sp = "⁝" * random.randint(10,100)
            empty_map += f"{Colore.Gray}{sp}{Colore.Reset}{SelectedFrame}{PlayerLight}{PlayerSymbol} {StarIs['Star']}{Colore.Reset}{SelectedFrameBack}{Colore.Gray}{sp}{Colore.Reset}"

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
        if com == "q" or com == "Q":
            PlayerIs['MapSettings']['Filter'] = 0
            wl.Skip()
            exit()
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
        
if CommandInput == "2":
    StarList = []
    if StarIs.get("StarIntel"):
        if StarIs.get("StarControled") == True: StarList.append("Переіменувати систему")
        
        if not StarIs.get("StarControled") and not StarIs.get("StarCivil"): StarList.append("Взяти під контроль")
    else:
        StarList.append("Вивчити зірку")
    
    if not StarIs.get("PlayerPinned"):
        StarList.append("Закріпити систему в Галактичну мапу")
    else: 
        StarList.append("Зняти систему із закріплень")
    
    if StarIs.get("StarControled") and Ships[PlayerIs['Ship']['ShipID']]['ShipClass'] == 3 and not StarIs.get("StarCivil"):
        StarList.append("Засновати власну колонію")
        
    wl.Skip()
    print(f" ▪ Зірка: {StarIs['Star']}")
    print(f" ▪ Спек. клас: {StarIs['Class']}")
    print(f" ▪ Температура: {StarIs['Temp']} K")
    print(f" ▪ Радіус: {StarIs['Size']} рад. Сонця")
    print(f" ▪ Маса: {StarIs['Mass']} мас Сонця")
    if StarIs.get("StarIntel"):
        print()
        print(" ▪ Політична інформація:")
        print("     - Дослідженна: Так")
        if StarIs.get("StarCivil"):
            print(f"     - Наявна колонія: Так") 
            print(f"     - Економічна стала: {StarIs['StarCivil']['CivilEco']}")
        if StarIs.get("StarControled"):
            print(f"     - Підкорив: {PlayerIs['Nickname']}")
        if StarIs.get("StarCivil") and not StarIs['StarCivil']['CivilStation'] == {}:
            print(f"     - Станція: {StarIs['StarCivil']['CivilStation']['StationName']}")
    print()
    print(f" ▪ Планет:")
    for abs in range(len(StarIs['Planets'])):
        PlanetIs = StarIs['Planets'][abs]
        print(f"     - {PlanetIs['PlanetName']} - Клас: {PlanetClass[PlanetIs['PlanetClass']]} - Температура: {PlanetIs['PlanetTemp']} °C")
    print()

    StarInput = wl.ChoiceMenu(StarList)

    if StarInput == "Вивчити зірку":
        if not StarIs.get("StarIntel"):
            wl.Loading(f"Досліджуємо зірку {StarIs['Star']}", 5)
            for planets in range(len(StarIs['Planets'])):
                PlanetIs = StarIs['Planets'][planets]['PlanetName']
                wl.Loading(f"Скануємо поверхню та проводимо аніліз планети {PlanetIs}", 3)
            PlayerIs['Statistic']['StarInteled'] += 1
            PlayerIs['IntelBall'] += (random.randint(100,500)) * ((len(StarIs['Planets']) * wl.Level))
            PlayerIs['XP'] += random.randint(100,1000) * (len(StarIs['Planets']))
            ProjectInfinity.StarChange(StarIs['StarID'], "StarIntel", True)
    
    if StarInput == "Переіменувати систему":
        wl.Skip()
        NewNameStar = input("Нова назва: ")
        ProjectInfinity.StarChange(StarIs['StarID'], "Star", NewNameStar)
                
    if StarInput == "Закріпити систему в Галактичну мапу":
        wl.Skip()
        PinnedDesc = input("Назва тегу для закріплення: ")
        ProjectInfinity.StarChange(StarIs['StarID'], "PlayerPinned", True)
        ProjectInfinity.StarChange(StarIs['StarID'], "PlayerPinnedDesc", PinnedDesc)

    if StarInput == "Зняти систему із закріплень":
        ProjectInfinity.StarChange(StarIs['StarID'], "PlayerPinned", False)
    
    if StarInput == "Взяти під контроль":
        PlayerIs['Statistic']['StarControled'] += 1
        ProjectInfinity.StarChange(StarIs['StarID'], "StarControled", True)
    
    if StarInput == "Засновати власну колонію":
        wl.Massage("Заснування колонії - це третій шаг встановлення влади, колонії дають можливість продавати чи покупати товари, мати постійне місце проживання та постійний прибуток. Але під постійним прибуток вважається стабільна економіка системи, яка урегулюєця трьома параметрами: кількість планет, популярність та тип головної станції системи.")
        wl.Massage("Перед тим, як заснувати, вам треба мати: 100,000,000 © та 30 рівень галактичної репутації")
        if PlayerIs['Money'] >= 100_000_000: wl.ParrametrInspect(True, "Наявність 100,000,000 ©")
        else: wl.ParrametrInspect(False, "Наявність 100,000,000 ©")
        if wl.Level >= 30: wl.ParrametrInspect(True, "Наявність 30 рівня")
        else: wl.ParrametrInspect(False, "Наявність 30 рівня")
        time.sleep(1)
        if wl.Level >= 30:
            if Ships[PlayerIs['Ship']['ShipID']]['ShipClass'] == 3:
                wl.Loading("Будування станції", 5)
                ProjectInfinity.StarChange(StarIs['StarID'], "StarCivil", {"CivilEco": random.uniform(CivilEcoMin,CivilEcoMax), "CivilStation": {"StationName": f"{ranname()} Station", "StationType": random.randint(0,2), "StationStoreList": random.sample(range(len(ItemsDB)), 3)}})
        else:
            wl.Error("Не достатній рівень (>30)")

if CommandInput == "4":
    if StarIs.get("StarCivil"):
            wl.Skip()
            print(f" ▪ Станція: {StarIs['StarCivil']['CivilStation']['StationName']}")
            print(f" ▪ Економічна стала: {StarIs['StarCivil']['CivilEco']}")
            print()

            StationList = ["Здати досліди", "Заправитися", "Верф", "Ринок"]
            StationCom = wl.ChoiceMenu(StationList)

            if StationCom == "Здати досліди":
                if PlayerIs['IntelBall'] > 0:
                    wl.Loading("Здавання дослідження",3)
                    PlayerIs['Money'] += (PlayerIs['IntelBall'] * 3)
                    PlayerIs['IntelBall'] = 0
            
            if StationCom == "Заправитися":
                FuelNow = PlayerIs['Ship']['Fuel']
                FuelMaxCapacity = Ships[PlayerIs['Ship']['ShipID']]['ShipMaxFuel']
                FuelCoust = (FuelMaxCapacity - FuelNow) * 12
                if PlayerIs['Ship']['Fuel'] != FuelMaxCapacity:
                    if PlayerIs['Money'] >= FuelCoust:
                        wl.Loading("Заправлення", 3)
                        PlayerIs['Ship']['Fuel'] += FuelMaxCapacity - FuelNow
                        PlayerIs['Money'] -= FuelCoust
                    else:
                        wl.Error("Не достатньо грошей")
                else:
                    wl.Error(f"{PlayerIs['Ship']['ShipName']} вже заправленний")
            
            if StationCom == "Верф":
                wl.Skip()
                for ship in range(len(Ships)):
                    ShipIs = Ships[ship]
                    print(f"{ship+1}. {ShipIs['ShipName']} | Клас: {ShipClass[ShipIs['ShipClass']]} | Ціна: {int(ShipIs['ShipCoust'] * StarIs['StarCivil']['CivilEco']):,} ©")
                ShipChoice = input("Вибрати: ")
                ShipChoised = Ships[int(ShipChoice)-1]

                if PlayerIs['Money'] >= int(ShipChoised['ShipCoust'] * StarIs['StarCivil']['CivilEco']):
                    wl.Loading("Підготовка нового корабля", 3)
                    PlayerIs['Ship']['ShipID'] = ShipChoised['ShipID']
                    PlayerIs['Ship']['Fuel'] = ShipChoised['ShipMaxFuel']
                    PlayerIs['Ship']['ShipName'] = ShipChoised['ShipName']
                    PlayerIs['Money'] -= int(ShipChoised['ShipCoust'] * StarIs['StarCivil']['CivilEco'])
                    PlayerIs['XP'] += int(int(ShipChoised['ShipCoust'] * StarIs['StarCivil']['CivilEco']) / 5)

            if StationCom == "Ринок":
                wl.Skip()
                StationStoreChoice = wl.ChoiceMenu(["Купити", "Продати"])
                if StationStoreChoice == "Купити":
                    wl.Skip()
                    for alli in range(len(StarIs['StarCivil']['CivilStation']['StationStoreList'])):
                        ItemIs = StarIs['StarCivil']['CivilStation']['StationStoreList'][alli]
                        ItemCoust = int(int(ItemsDB[ItemIs]['ItemCoust']) * StarIs['StarCivil']['CivilEco'])
                        print(f"{alli+1}. {ItemsDB[ItemIs]['ItemName']} ▪ Ціна: {ItemCoust:,} ©")
                    ChoiceItem = int(input("Купити: ")) - 1

                    if ChoiceItem < len(StarIs['StarCivil']['CivilStation']['StationStoreList']) and ChoiceItem >= 0:
                        wl.Skip()
                        Count = int(input("Скільки: "))
                        ItemIs = StarIs['StarCivil']['CivilStation']['StationStoreList'][ChoiceItem]
                        ItemCoust = int(int(ItemsDB[ItemIs]['ItemCoust']) * StarIs['StarCivil']['CivilEco']) * Count
                        if PlayerIs['Money'] <= ItemCoust:
                            wl.Error("Не достатньо грошей")
                        else:
                            PlayerIs['Money'] -= ItemCoust
                            wl.InvAdd(ItemIs, Count)

                if StationStoreChoice == "Продати":
                    wl.Skip()
                    for alli in range(len(PlayerIs['Ship']['Storage'])):
                        ItemIs = PlayerIs['Ship']['Storage'][alli]
                        ItemCoust = int(int(ItemsDB[ItemIs['ItemID']]['ItemCoust']) * StarIs['StarCivil']['CivilEco'])
                        print(f"{alli+1}. {ItemsDB[ItemIs['ItemID']]['ItemName']} ▪ Ціна: {ItemCoust:,} © ▪ Ціна разом: {int(ItemCoust*ItemIs['ItemCount']):,} © ▪ Кількість в сховище: {ItemIs['ItemCount']:,}")
                    ChoiceItem = int(input("Продати: ")) - 1
                    
                    if ChoiceItem > len(PlayerIs['Ship']['Storage'])+1 or ChoiceItem < 0:
                        wl.Error("Недоступне введення")
                    else:
                        wl.Skip()
                        SellLot = input("Скільки продати: ")
                        ItemIs = PlayerIs['Ship']['Storage'][ChoiceItem]
                        ItemCoust = int(int(ItemsDB[ItemIs['ItemID']]['ItemCoust']) * StarIs['StarCivil']['CivilEco']) * int(SellLot)
                        if int(SellLot) > ItemIs['ItemCount']: wl.Error("Не висточає товару для продажу")
                        else:
                            PlayerIs['Money'] += ItemCoust
                            PlayerIs['XP'] += int((int(SellLot)) * 5)
                            wl.InvRem(ItemIs['ItemID'], int(SellLot))

if CommandInput == "5":
    wl.Skip()
    OtherList = ["Статистика", "Сховище корабля"]
    OtherCom = wl.ChoiceMenu(OtherList)
    if OtherCom == "Статистика":
        wl.Skip()
        print(f"Вивчено систем: {PlayerIs['Statistic']['StarInteled']:,}")
        print(f"Систем під контролем: {PlayerIs['Statistic']['StarControled']:,}")
        input()

    if OtherCom == "Сховище корабля":
        wl.Skip()
        for alli in range(len(PlayerIs['Ship']['Storage'])):
            ItemIs = PlayerIs['Ship']['Storage'][alli]
            print(f"{alli+1}. {ItemsDB[ItemIs['ItemID']]['ItemName']} ▪ Кількість: {ItemIs['ItemCount']:,}")
        input()

if CommandInput == "*":
    exit()

if CommandInput == "/":
    wl.Skip()
    debug = exec(input("/"))
    if debug == "":
        exit()
    input("Нажміть ENTER щоб продовжити")

wl.SaveJSON("save.json", save)