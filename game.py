from wlengine import *

wl.ConsoleSetSize()

wl.Skip()
wl.Screen()

CommandInput = wl.Command()

if CommandInput == "1":
    ProjectInfinity.GalaxyMap("SHIP")
        
if CommandInput == "2":
    StarList = []
    if StarIs.get("StarIntel"):
        if StarIs.get("StarControled"): StarList.append("Переіменувати систему")
        
        if not StarIs.get("StarControled") and not StarIs.get("StarCivil"): StarList.append("Взяти під контроль")
    else:
        StarList.append("Вивчити зірку")
    
    if not StarIs.get("PlayerPinned"):
        StarList.append("Закріпити систему в Галактичну мапу")
    else: 
        StarList.append("Зняти систему із закріплень")
    
    if StarIs.get("StarControled") and Ships[PlayerIs['Ship']['ShipID']]['ShipClass'] == 3 and not StarIs.get("StarCivil"):
        StarList.append("Засновати власну колонію")

    if PlayerIs.get("Fleet"):
        if PlayerIs['Fleet']['Location'] == StarIs['StarID']:
            StarList.append(f"Флотоносець{Colore.Blue} ⊴{Colore.Reset}")
        
    wl.Skip()
    print(f" ▪ Зірка: {StarIs['Star']}")
    print(f" ▪ Спек. клас: {StarIs['Class']}")
    print(f" ▪ Температура: {StarIs['Temp']:,} K")
    print(f" ▪ Радіус: {StarIs['Size']:,} рад. Сонця")
    print(f" ▪ Маса: {StarIs['Mass']:,} мас Сонця")
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
                PlayerIs['Money'] -= 100_000_000
                ProjectInfinity.StarChange(StarIs['StarID'], "StarCivil", {"CivilEco": random.uniform(CivilEcoMin,CivilEcoMax), "CivilStation": {"StationName": f"{ranname()} Station", "StationType": random.randint(0,2), "StationStoreList": random.sample(range(len(ItemsDB)), 3)}})
        else:
            wl.Error("Не достатній рівень (>30)")

    if StarInput == f"Флотоносець{Colore.Blue} ⊴{Colore.Reset}":
        wl.Skip()
        print(f" ▪ Флотоносець: {PlayerIs['Fleet']['FleetName']}")
        print(f" ▪ Модель: {Fleets[PlayerIs['Fleet']['FleetID']]['FleetModel']}")
        print(f" ▪ Клас: {Fleets[PlayerIs['Fleet']['FleetID']]['FleetClass']}")
        print(f" ▪ Палива: {PlayerIs['Fleet']['Fuel']}/{Fleets[PlayerIs['Fleet']['FleetID']]['FleetMaxFuel']}")
        print(f" ▪ Макс. дальність: {Fleets[PlayerIs['Fleet']['FleetID']]['FleetMaxHyperdrive']} св. р")
        print(f" ▪ Кораблів в сховище: {len(PlayerIs['Fleet']['Ships']):,}")
        print(f" ▪ Товарів в сховище: {len(PlayerIs['Fleet']['Storage']):,}")
        print()

        FleetList = ["Галактична карта","Грузовий відсік","Ангар"]
        FleetChoice = wl.ChoiceMenu(FleetList)

        if FleetChoice == "Галактична карта":
            ProjectInfinity.GalaxyMap("FLEET")
        if FleetChoice == "Грузовий відсік":
            wl.Skip()
            StorageList = ['Переглянути вміст', "Перемістити предмети"]
            StorageChoice = wl.ChoiceMenu(StorageList)
            if StorageChoice == "Переглянути вміст":
                wl.Skip()
                for alli in range(len(PlayerIs['Fleet']['Storage'])):
                    ItemIs = PlayerIs['Fleet']['Storage'][alli]
                    print(f"{alli+1}. {ItemsDB[ItemIs['ItemID']]['ItemName']} ▪ Кількість: {ItemIs['ItemCount']:,}")
                
                ItemChoice = int(input("Вибрати: ")) - 1

                if ItemChoice+1 > len(PlayerIs['Ship']['Storage']) and ItemChoice+1 <= 0:
                    wl.Error("Недопустиме введення")
                else:
                    ItemIs = PlayerIs['Fleet']['Storage'][ItemChoice]
                    if ItemsDB[ItemIs['ItemID']]['ItemName'] == ItemsDB[0]['ItemName']:
                        if ItemsDB[ItemIs['ItemID']]['ItemType'] == "REFUEL_ITEM":
                            FuelMaxCapacity = Fleets[PlayerIs['Fleet']['FleetID']]['FleetMaxFuel']
                            PlayerIs['Fleet']['Fuel'] += 25
                            if PlayerIs['Fleet']['Fuel'] > FuelMaxCapacity: PlayerIs['Fleet']['Fuel'] = FuelMaxCapacity
                            wl.Loading("Заправлення", 3)
                            wl.InvRem(0, 1, 'Fleet')

            if StorageChoice == "Перемістити предмети":
                wl.Skip()
                MoveItemChoice = wl.ChoiceMenu(["Корабель -> Флотоносець","Флотоносець -> Корабель"])
                if MoveItemChoice == "Корабель -> Флотоносець":
                    wl.Skip()
                    for alli in range(len(PlayerIs['Ship']['Storage'])):
                        ItemIs = PlayerIs['Ship']['Storage'][alli]
                        print(f"{alli+1}. {ItemsDB[ItemIs['ItemID']]['ItemName']} ▪ Кількість: {ItemIs['ItemCount']:,}")
                    
                    ItemChoice = int(input("Вибрати: ")) - 1
                    if ItemChoice+1 > len(PlayerIs['Ship']['Storage']) and ItemChoice+1 <= 0:
                        wl.Error("Недопустиме введення")
                    else:
                        ItemIs = PlayerIs['Ship']['Storage'][ItemChoice]
                        ItemCount = int(input("Скільки перемістити: "))
                        if ItemCount > ItemIs['ItemCount']:
                            wl.Error("Перебільшена кількість")
                        else:
                            wl.Loading("Переміщення товару", 3)
                            wl.InvAdd(ItemIs['ItemID'], ItemCount, "Fleet")
                            wl.InvRem(ItemIs['ItemID'], ItemCount, "Ship")

                if MoveItemChoice == "Флотоносець -> Корабель":
                    wl.Skip()
                    for alli in range(len(PlayerIs['Fleet']['Storage'])):
                        ItemIs = PlayerIs['Fleet']['Storage'][alli]
                        print(f"{alli+1}. {ItemsDB[ItemIs['ItemID']]['ItemName']} ▪ Кількість: {ItemIs['ItemCount']:,}")
                    
                    ItemChoice = int(input("Вибрати: ")) - 1
                    if ItemChoice+1 > len(PlayerIs['Fleet']['Storage']) and ItemChoice+1 <= 0:
                        wl.Error("Недопустиме введення")
                    else:
                        ItemIs = PlayerIs['Fleet']['Storage'][ItemChoice]
                        ItemCount = int(input("Скільки перемістити: "))
                        if ItemCount > ItemIs['ItemCount']:
                            wl.Error("Перебільшена кількість")
                        else:
                            wl.Loading("Переміщення товару", 3)
                            wl.InvAdd(ItemIs['ItemID'], ItemCount, "Ship")
                            wl.InvRem(ItemIs['ItemID'], ItemCount, "Fleet")

if CommandInput == "4":
    if StarIs.get("StarCivil"):
            wl.Skip()
            print(f" ▪ Станція: {StarIs['StarCivil']['CivilStation']['StationName']}")
            print(f" ▪ Економічна стала: {StarIs['StarCivil']['CivilEco']}")
            print()

            StationList = ["Здати досліди", "Заправитися", "Верф", "Ринок"]

            if StarIs['StarCivil']['CivilStation']['StationType'] == 2:
                StationList.append("Верф флотоносців")

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
                            wl.InvAdd(ItemIs, Count, 'Ship')

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
                            PlayerIs['Statistic']['CreditsFromSelled'] += ItemCoust
                            wl.InvRem(ItemIs['ItemID'], int(SellLot), 'Ship')

if CommandInput == "5":
    wl.Skip()
    OtherList = ["Статистика", "Сховище корабля", "Закріпленні"]
    OtherCom = wl.ChoiceMenu(OtherList)
    if OtherCom == "Статистика":
        wl.Skip()
        print("Статистика систем")
        print(f" ▪ Вивчено систем: {PlayerIs['Statistic']['StarInteled']:,}")
        print(f" ▪ Систем під контролем: {PlayerIs['Statistic']['StarControled']:,}")
        print()
        print(f" ▪ Усього кредитів отримана з торгівлі: {PlayerIs['Statistic']['CreditsFromSelled']:,} ©")
        if PlayerIs.get("Fleet"): print(f" ▪ Місце розташування флотоносця: {GenMap(PlayerIs['Fleet']['Location'])['Star']} ({GenMap(PlayerIs['Fleet']['Location'])['StarID']})")
        input()

    if OtherCom == "Сховище корабля":
        wl.Skip()
        for alli in range(len(PlayerIs['Ship']['Storage'])):
            ItemIs = PlayerIs['Ship']['Storage'][alli]
            print(f"{alli+1}. {ItemsDB[ItemIs['ItemID']]['ItemName']} ▪ Кількість: {ItemIs['ItemCount']:,}")
        
        ItemChoice = int(input("Вибрати: ")) - 1
        
        if ItemChoice+1 > len(PlayerIs['Ship']['Storage']) and ItemChoice+1 <= 0:
            wl.Error("Недопустиме введення")
        else:
            ItemIs = PlayerIs['Ship']['Storage'][ItemChoice]
            if ItemsDB[ItemIs['ItemID']]['ItemName'] == ItemsDB[0]['ItemName']:
                if ItemsDB[ItemIs['ItemID']]['ItemType'] == "REFUEL_ITEM":
                    FuelMaxCapacity = Ships[PlayerIs['Ship']['ShipID']]['ShipMaxFuel']
                    PlayerIs['Ship']['Fuel'] += 5
                    if PlayerIs['Ship']['Fuel'] > FuelMaxCapacity: PlayerIs['Ship']['Fuel'] = FuelMaxCapacity
                    wl.Loading("Заправлення", 3)
                    wl.InvRem(0, 1, 'Ship')

    if OtherCom == "Закріпленні":
        wl.Skip()
        for absi in range(len(CustomStars)):
            CustomStarsIs = CustomStars[absi]
            StarIs = GenMap(int(CustomStarsIs['StarID']))
            if CustomStarsIs['PlayerPinned'] == True:
                print(f"{Colore.Yellow} ▪ {StarIs['Star']} ({StarIs['StarID']}) ▪ Опис: {CustomStarsIs['PlayerPinnedDesc']}")
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