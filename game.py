from wlengine import *

wl.ConsoleSetSize()

wl.Skip()
wl.Screen()

CommandInput = wl.Command()

# Функція, яка відкриває мапу Галактики
if CommandInput == "1":
    ProjectInfinity.GalaxyMap("SHIP")
        
# Зоряна система
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
    
    if StarIs.get("StarControled") and not StarIs.get("StarCivil"):
        StarList.append("Засновати власну колонію")

    if PlayerIs.get("Fleet") and len(PlayerIs['Fleet']) > 0:
        for i in range(len(PlayerIs['Fleet'])):
            if PlayerIs['Fleet'][i]['Location'] == StarIs['StarID']:
                StarList.append(f"Космоносці{Colore.Blue} ⊴{Colore.Reset}")
                break
    
    if StarIs.get("StarIntel"):
        if StarIs.get("StarCivil"):
            StarSymbol = f"{Colore.Red if StarIs.get("StarControled") else Colore.Green}⚑{Colore.Reset}"
        elif StarIs.get("StarControled"):
            StarSymbol = f"{Colore.Red}⛊{Colore.Reset}"
        else:
            StarSymbol = f"{Colore.Blue}⌬{Colore.Reset}"     
    else:
        StarSymbol = ""

    if StarIs.get("StarCivil") and StarIs.get("StarControled"):
        StarList.append("Керівництво системи")
            
    wl.Skip()
    print(f"{Colore.Gray}ID: {StarIs['StarID']}{Colore.Reset}")
    Cont = Text()
    Cont.append(f"Зірка: {StarIs['Star']} {StarSymbol}\n")
    Cont.append(f"Спек. клас: {StarIs['Class']}\n")
    Cont.append(f"Температура: {StarIs['Temp']:,} K\n")
    Cont.append(f"Радіус: {StarIs['Size']:,.2f} рад. Сонця\n")
    Cont.append(f"Маса: {StarIs['Mass']:,.2f} мас Сонця\n")
    Cont.append(f"Світність: {StarIs['Luminos']:.2f} світ. Сонця")

    Rconsole.print(Panel(Cont,border_style="white",title="[yellow]Зоряна система"))
    #if StarIs.get("StarIntel"):
    #    print()
    #    print(" ▪ Політична інформація:")
    #    print("     - Дослідженна: Так")
    #    if StarIs.get("StarCivil"):
    #        print(f"     - Наявна колонія: Так") 
    #    if StarIs.get("StarControled"):
    #        print(f"     - Підкорив: {PlayerIs['Nickname']}")
    #    if StarIs.get("StarCivil") and not StarIs['StarCivil']['CivilStation'] == {}:
    #        print(f"     - Системні володарі: {StarIs['StarCivil']['CivilFraction']['FractionName']}")
    #        print(f"     - Населення: {StarIs['StarCivil']['CivilFraction']['FractionPop']:,}")
    #        print(f"     - Станція: {StarIs['StarCivil']['CivilStation']['StationName']}")
    #    print()

    if StarIs.get("StarIntel"):
        if StarIs.get("StarCivil"):
            Cont1 = Text()
            Cont1.append(f"Тип економіки: {Economics[StarIs['StarCivil']['CivilEconomicType']]}\n")
            if StarIs.get("StarControled"):
                Cont1.append(f"Економічна стала: {StarIs['StarCivil']['CivilEco']:.2f}\n")
            if StarIs.get("InfoIncome"): 
                Cont1.append(f"Прибуток: {StarIs['InfoIncome']:,} ©\n")

            Cont2 = Text()
            Cont2.append("Досліджена: Так\n")
            if StarIs.get("StarCivil"):
                Cont2.append("Заселенна: Так\n")
            if StarIs.get("StarCivil") and not StarIs['StarCivil']['CivilStation'] == {}:
                Cont2.append(f"Системні володарі: {StarIs['StarCivil']['CivilFraction']['FractionName']}\n")
                Cont2.append(f"Населення: {StarIs['StarCivil']['CivilFraction']['FractionPop']:,}\n")
                Cont2.append(f"Станція: {StarIs['StarCivil']['CivilStation']['StationName']}\n")

            Rconsole.print(Panel(Cont1,border_style="white",title="Економіка"))
    
            Rconsole.print(Panel(Cont2, title="[blue]Політична інформація", border_style="white"))

    PlanetContent = Text()
    for abs in range(len(StarIs['Planets'])):
        PlanetIs = StarIs['Planets'][abs]

        TerraformSymbol = ""
        if PlanetIs['PlanetTerraform'] == True and PlanetIs['PlanetLive'] == False:
            TerraformSymbol = f"{colorama.Fore.GREEN} 𖤖{colorama.Fore.RESET}"

        PlanetContent.append(f"{PlanetIs['PlanetName']}{TerraformSymbol} - Клас: {PlanetClass[PlanetIs['PlanetClass']]} - Температура: {PlanetIs['PlanetTemp']:.2f} °C - Велика піввісь: {PlanetIs['PlanetDistance']:.2f} а. о.\n")
    
    Rconsole.print(Panel(PlanetContent,border_style="white",title="[green]Планети"))
    print()

    StarInput = wl.ChoiceMenu(StarList)

    if StarInput == "Вивчити зірку":
        if not StarIs.get("StarIntel"):
            wl.Loading(f"Досліджуємо зірку {StarIs['Star']}", 5)
            for planets in range(len(StarIs['Planets'])):
                PlanetIs = StarIs['Planets'][planets]['PlanetName']
                wl.Loading(f"Скануємо планету {PlanetIs}", 3)
            PlayerIs['Statistic']['StarInteled'] += 1
            PlayerIs['IntelBall'] += (random.randint(100,500)) * ((len(StarIs['Planets']) * wl.Level))
            PlayerIs['XP'] += random.randint(100,1000) * (len(StarIs['Planets']))
            ProjectInfinity.StarChange(StarIs['StarID'], "StarIntel", True)
    
    if StarInput == "Переіменувати систему":
        wl.Skip()
        NewNameStar = input("Нова назва: ")
        if NewNameStar == "" or NewNameStar == " ": exit()
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
        wl.Massage("Перед тим, як заснувати, вам треба мати: Флотоносець класу Контруктор, 100,000,000 © та 30 рівень галактичної репутації")
        for i in range(len(PlayerIs['Fleet'])):
            FleetIs = PlayerIs['Fleet'][i]
            if FleetIs['Location'] == StarIs['StarID']:
                break
            else: pass
        if wl.Level >= 30:
            if Fleets[FleetIs['FleetID']]['FleetClass'] == 2:
                if FleetIs['Location'] == StarIs['StarID']:
                    ItemSearcher = 0
                    for i in range(len(PlayerIs['Ship']['Storage'])):
                        ItemIs = PlayerIs['Ship']['Storage'][i]
                        if ItemIs["ItemID"] == 1:
                            ItemSearcher = 1
                            wl.InvRem(1, 1)
                            break
                        else:
                            ItemSearcher += 0
                    if ItemSearcher == 0:
                        wl.Error("Немає будівельних матеріалів в трюмі")
                    wl.Loading("Будування станції", 5)
                    ProjectInfinity.StarChange(
                        StarIs['StarID'], 
                        "StarCivil", 
                        {
                            "CivilEconomicType": random.randint(0, len(Economics)),
                            "CivilEco": random.uniform(CivilEcoMin,CivilEcoMax), 
                            "CivilBank": 0,
                            "CivilStation": {
                                "StationName": f"{ranname()} Station", 
                                "StationType": random.randint(0,2), 
                                "StationStoreList": random.sample(range(len(ItemsDB)), 1)}, 
                            "CivilFraction": {
                                "FractionName": f"{PlayerIs['Nickname']}",
                                "FractionPop": random.randint(100,1000),
                                "FractionEcoType": 0,
                                "FractionRep": 100,
                                "FractionPolType": 0
                            }
                        }
                    )
                    ProjectInfinity.StarChange(StarIs['StarID'], "InfoDate", wl.Date())
                    ProjectInfinity.StarChange(StarIs['StarID'], "InfoIncome", 0)
                    PlayerIs['Statistic']['StarColony'] += 1
        else:
            wl.Error("Не достатній рівень (>30)")

    if StarInput == "Керівництво системи":
        wl.Skip()
        Cont = Text()
        Cont.append(f"Система: {StarIs['Star']}\n")
        Cont.append(f"Тип економіки: {Economics[StarIs['StarCivil']['CivilEconomicType']]}\n")
        Cont.append(f"Станція: {StarIs['StarCivil']['CivilStation']['StationName']}\n")
        Cont.append(f"Населення: {StarIs['StarCivil']['CivilFraction']['FractionPop']:,}\n")
        Cont.append(f"Прибуток: {StarIs['InfoIncome']:,} ©")
        Rconsole.print(Panel(Cont,border_style="white", title="Інформація о системі"))
        
        ControlInput = wl.ChoiceMenu(["Переіменувати станцію", "Змінити економіку"])

        if ControlInput == "Переіменувати станцію":
            wl.Skip()
            StarIs['StarCivil']['CivilStation']['StationName'] = input("Назва для станції: ")
            ProjectInfinity.StarChange(StarIs['StarID'], "StarCivil", StarIs['StarCivil'])

        if ControlInput == "Змінити економіку":
            wl.Skip()
            wl.Menu(Economics)
            EconomicChoice = int(input("Вибрати: ")) - 1
            StarIs['StarCivil']['CivilEconomicType'] = EconomicChoice
            ProjectInfinity.StarChange(StarIs['StarID'], "StarCivil", StarIs['StarCivil'])

    if StarInput == f"Космоносці{Colore.Blue} ⊴{Colore.Reset}":
        wl.Skip()
        for i in range(len(PlayerIs['Fleet'])):
            FleetIs = PlayerIs['Fleet'][i]
            if FleetIs['Location'] == StarIs['StarID']:
                print(f"{i+1}. {FleetIs['FleetName']} ▪ Модель: {Fleets[FleetIs['FleetID']]['FleetModel']} ▪ Клас: {FleetClasses[Fleets[FleetIs['FleetID']]['FleetClass']]} ▪ Палива: {FleetIs['Fuel']}")

        FleetIsChoice = int(input("Вибрати: "))-1
        FleetIs = PlayerIs['Fleet'][FleetIsChoice]

        if FleetIs['Location'] != StarIs['StarID']:
            wl.Error("Космоносця не знайдено")

        wl.Skip()
        print(f" ▪ Космоносець: {FleetIs['FleetName']}")
        print(f" ▪ Модель: {Fleets[FleetIs['FleetID']]['FleetModel']}")
        print(f" ▪ Клас: {FleetClasses[Fleets[FleetIs['FleetID']]['FleetClass']]}")
        print(f" ▪ Палива: {FleetIs['Fuel']}/{Fleets[FleetIs['FleetID']]['FleetMaxFuel']}")
        print(f" ▪ Макс. дальність: {Fleets[FleetIs['FleetID']]['FleetMaxHyperdrive']} св. р")
        print(f" ▪ Кораблів в сховище: {len(FleetIs['Ships']):,}")
        print(f" ▪ Товарів в сховище: {len(FleetIs['Storage']):,}")
        print()

        FleetList = ["Галактична карта","Грузовий відсік","Ангар","Переіменувати космоносець"]
        FleetChoice = wl.ChoiceMenu(FleetList)

        if FleetChoice == "Галактична карта":
            ProjectInfinity.GalaxyMap("FLEET", FleetIsChoice)
        if FleetChoice == "Грузовий відсік":
            wl.Skip()
            StorageList = ['Переглянути вміст', "Перемістити предмети"]
            StorageChoice = wl.ChoiceMenu(StorageList)
            if StorageChoice == "Переглянути вміст":
                wl.Skip()
                for alli in range(len(FleetIs['Storage'])):
                    ItemIs = FleetIs['Storage'][alli]
                    print(f"{alli+1}. {ItemsDB[ItemIs['ItemID']]['ItemName']} ▪ Кількість: {ItemIs['ItemCount']:,}")
                
                ItemChoice = int(input("Вибрати: ")) - 1

                if ItemChoice+1 > len(PlayerIs['Ship']['Storage']) and ItemChoice+1 <= 0:
                    wl.Error("Недопустиме введення")
                else:
                    ItemIs = FleetIs['Storage'][ItemChoice]
                    if ItemsDB[ItemIs['ItemID']]['ItemName'] == ItemsDB[0]['ItemName']:
                        if ItemsDB[ItemIs['ItemID']]['ItemType'] == 0:
                            FuelMaxCapacity = Fleets[FleetIs['FleetID']]['FleetMaxFuel']
                            FleetIs['Fuel'] += 25
                            if FleetIs['Fuel'] > FuelMaxCapacity: FleetIs['Fuel'] = FuelMaxCapacity
                            wl.Loading("Заправлення", 3)
                            wl.FleetInvRem(0, 1, FleetIsChoice)

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
                            wl.FleetInvAdd(ItemIs['ItemID'], ItemCount, FleetIsChoice)
                            wl.InvRem(ItemIs['ItemID'], ItemCount)

                if MoveItemChoice == "Флотоносець -> Корабель":
                    wl.Skip()
                    for alli in range(len(FleetIs['Storage'])):
                        ItemIs = FleetIs['Storage'][alli]
                        print(f"{alli+1}. {ItemsDB[ItemIs['ItemID']]['ItemName']} ▪ Кількість: {ItemIs['ItemCount']:,}")
                    
                    ItemChoice = int(input("Вибрати: ")) - 1
                    if ItemChoice+1 > len(FleetIs['Storage']) and ItemChoice+1 <= 0:
                        wl.Error("Недопустиме введення")
                    else:
                        ItemIs = FleetIs['Storage'][ItemChoice]
                        ItemCount = int(input("Скільки перемістити: "))
                        if ItemCount > ItemIs['ItemCount']:
                            wl.Error("Перебільшена кількість")
                        else:
                            wl.Loading("Переміщення товару", 3)
                            wl.InvAdd(ItemIs['ItemID'], ItemCount)
                            wl.FleetInvRem(ItemIs['ItemID'], ItemCount, FleetIsChoice)
                
        if FleetChoice == "Переіменувати космоносець":
            wl.Skip()
            NewFleetName = input("Нова назва: ")
            if NewFleetName == "": exit()
            FleetIs['FleetName'] = NewFleetName
        
        if FleetChoice == "Ангар":
            wl.Skip()
            AngarList = ["Подивитися вміст","Використати корабель"]
            AngarChoice = wl.ChoiceMenu(AngarList)

            if AngarChoice == "Подивитися вміст":
                wl.Skip()
                for i in range(len(FleetIs['Ships'])):
                    ShipIs = FleetIs['Ships'][i]
                    InShipsIs = Ships[ShipIs['ShipID']]
                    print(f"{i+1}. {ShipIs['ShipName']} ▪ Модель корабля: {InShipsIs['ShipName']}")
                input()

            if AngarChoice == "Використати корабель":
                wl.Skip()
                for i in range(len(FleetIs['Ships'])):
                    ShipIs = FleetIs['Ships'][i]
                    InShipsIs = Ships[ShipIs['ShipID']]
                    print(f"{i+1}. {ShipIs['ShipName']} ▪ Модель корабля: {InShipsIs['ShipName']}")
                
                ShipIs = int(input("Вибрати: ")) - 1
                if ShipIs > len(FleetIs['Ships']) or ShipIs < 0:
                    wl.Error("Невірне введення")
                else:
                    wl.Loading("Сідаємо до іншого корабля", 3)
                    FleetIs['Ships'].append(PlayerIs['Ship'])
                    PlayerIs['Ship'] = FleetIs['Ships'][ShipIs]
                    FleetIs['Ships'].pop(ShipIs)

# Планети поточної зоряної системи
if CommandInput == "3":
    wl.Skip()
    for abs in range(len(StarIs['Planets'])):
        PlanetIs = StarIs['Planets'][abs]

        TerraformSymbol = ""
        if PlanetIs['PlanetTerraform'] == True:
            TerraformSymbol = f"{colorama.Fore.GREEN} 𖤖{colorama.Fore.RESET}"

        print(f"{abs+1}. {PlanetIs['PlanetName']}{TerraformSymbol} - Клас: {PlanetClass[PlanetIs['PlanetClass']]} - Температура: {PlanetIs['PlanetTemp']} °C")

    PlanetChoice = int(input("Відправитися: "))-1
    
    if PlanetChoice > len(StarIs['Planets']) or PlanetChoice < 0:
        wl.Error("Невірне введення")
    else:
        PlanetIs = StarIs['Planets'][PlanetChoice]
        if PlanetIs['PlanetClass'] == 3:
            wl.Error("На газових гігантів посадка неможлива")
        else:
            wl.Skip()

            PlanetList = []
            if "PLAYER_MINERTOOL" in PlayerIs['Atribution']:
                PlanetList.append("Видобуток корисних копалин")

            if not StarIs.get('StarCivil'):
                PlanetList.append("Зробити поверхневий аналіз")

            if StarIs.get('StarControled') and StarIs['StarControled'] == True:
                PlanetList.append("Переіменувати планету")

            if "PLAYER_TERRAFORMER_DEVICE" in PlayerIs['Atribution']:
                if PlanetIs['PlanetTerraform'] == True and PlanetIs['PlanetLive'] == False:
                    PlanetList.append(f"Почати тераформінг {Colore.Green}𖤖{Colore.Reset}")

            print(f" ▪ Планета: {PlanetIs['PlanetName']}")
            print(f" ▪ Клас: {PlanetClass[PlanetIs['PlanetClass']]}")
            print(f" ▪ Температура: {PlanetIs['PlanetTemp']} °C\n")
            PlanetChoice = wl.ChoiceMenu(PlanetList)

            if PlanetChoice == "Переіменувати планету":
                wl.Skip()
                NewPlanetName = input("Нова назва: ")
                if NewPlanetName == "":
                    exit()
                PlanetIs['PlanetName'] = NewPlanetName
                ProjectInfinity.StarChange(StarIs['StarID'], "Planets", StarIs['Planets'])
                wl.Loading("Застосовуємо зміни", 1)

            if PlanetChoice == f"Почати тераформінг {Colore.Green}𖤖{Colore.Reset}":
                PlanetIs['PlanetClass'] = 4
                for abs in range(len(PlayerIs['Ship']['Storage'])):
                    ItemIs = PlayerIs['Ship']['Storage'][abs]
                    ItemSec = 0
                    if ItemIs['ItemID'] == 36:
                        ItemSec += 1
                    else: ItemSec += 0
                if ItemSec > 0:
                    wl.InvRem(36, 1)
                else:
                    wl.Error(f"В трюмі відсутній: {ItemsDB[36]['ItemName']}")

# Станція
if CommandInput == "4":
    if StarIs.get("StarCivil"):
            wl.Skip()
            print(f" ▪ Станція: {StarIs['StarCivil']['CivilStation']['StationName']}")
            print(f" ▪ Економічна стала: {StarIs['StarCivil']['CivilEco']}")
            print()

            StationList = ["Здати досліди", "Заправитися", "Верф", "Ринок"]

            if StarIs['StarCivil']['CivilStation']['StationType'] == 2:
                StationList.append("Верф флотоносців")

            if StarIs['StarCivil']['CivilEconomicType'] in [1,3,4]:
                StationList.append("Майстерня")

            StationCom = wl.ChoiceMenu(StationList)

            if StationCom == "Здати досліди":
                if PlayerIs['IntelBall'] > 0:
                    wl.Loading("Здавання дослідження",3)
                    PlayerIs['Money'] += (PlayerIs['IntelBall'] * 3)
                    PlayerIs['IntelBall'] = 0
            
            if StationCom == "Заправитися":
                NewFuel = 0
                for i in range(len(PlayerIs['Ship']['ShipModification'])):
                    if PlayerIs['Ship']['ShipModification'][i]['ModificationID'] == 0:
                        NewFuel += 50

                FuelNow = PlayerIs['Ship']['Fuel']
                FuelMaxCapacity = Ships[PlayerIs['Ship']['ShipID']]['ShipMaxFuel'] + NewFuel
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
                    print(f"{ship+1}. {ShipIs['ShipName']} | Клас: {ShipClasses[ShipIs['ShipClass']]} | Ціна: {int(ShipIs['ShipCoust'] * StarIs['StarCivil']['CivilEco']):,} ©")
                ShipChoice = input("Вибрати: ")
                ShipChoised = Ships[int(ShipChoice)-1]

                if PlayerIs['Money'] >= int(ShipChoised['ShipCoust'] * StarIs['StarCivil']['CivilEco']):
                    def ShipBuyScript():
                        wl.Loading("Купівля", 3)
                        PlayerIs['Ship']['ShipID'] = ShipChoised['ShipID']
                        PlayerIs['Ship']['Fuel'] = ShipChoised['ShipMaxFuel']
                        PlayerIs['Ship']['ShipName'] = ShipChoised['ShipName']
                        PlayerIs['Ship']['Storage'] = []
                        PlayerIs['Money'] -= int(ShipChoised['ShipCoust'] * StarIs['StarCivil']['CivilEco'])
                        PlayerIs['XP'] += int(int(ShipChoised['ShipCoust'] * StarIs['StarCivil']['CivilEco']) / 5)
                    def ShipBuyToFleetScript():
                        for i in range(len(PlayerIs['Fleet'])):
                            FleetIs = PlayerIs['Fleet'][i]
                            if FleetIs['Location'] == StarIs['StarID']:
                                break
                            else: pass
                        FleetIs['Ships'].append(
                            {
                                "ShipID": ShipChoised['ShipID'],
                                "ShipName": ShipChoised['ShipName'],
                                "Storage": [],
                                "Fuel": ShipChoised['ShipMaxFuel']
                            }
                        )
                        PlayerIs['Money'] -= int(ShipChoised['ShipCoust'] * StarIs['StarCivil']['CivilEco'])
                        PlayerIs['XP'] += int(int(ShipChoised['ShipCoust'] * StarIs['StarCivil']['CivilEco']) / 5)
                    
                    if PlayerIs.get("Fleet"):
                        for i in range(len(PlayerIs['Fleet'])):
                            if PlayerIs['Fleet'][i]['Location'] == StarIs['StarID']:
                                FleetIs = PlayerIs['Fleet'][i]
                                break
                        if FleetIs['Location'] == StarIs['StarID']:
                            wl.Skip()
                            TypeBuy = wl.ChoiceMenu(["Купити та замінити свій корабель", "Купити та перемістити до флотоносця"])
                            if TypeBuy == "Купити та перемістити до флотоносця":
                                wl.Loading("Купівля", 3)
                                ShipBuyToFleetScript()
                            else:
                                ShipBuyScript()
                        else:
                                ShipBuyScript()
                    else:
                        ShipBuyScript()

            if StationCom == "Ринок":
                wl.Skip()
                StationStoreChoice = wl.ChoiceMenu(["Купити", "Продати"])
                if StationStoreChoice == "Купити":
                    wl.Skip()
                    for alli in range(len(StarIs['StarCivil']['CivilStation']['StationStoreList'])):
                        ItemIs = StarIs['StarCivil']['CivilStation']['StationStoreList'][alli]
                        ItemCoust = int(int(ItemsDB[ItemIs]['ItemCoust']) * StarIs['StarCivil']['CivilEco'])
                        print(f"{alli+1}. {ItemsDB[ItemIs]['ItemName']} ▪ Ціна: {ItemCoust:,} © ▪ Тип: {ItemsType[ItemsDB[ItemIs]['ItemType']]}")
                    ChoiceItem = int(input("Купити: ")) - 1

                    if ChoiceItem < len(StarIs['StarCivil']['CivilStation']['StationStoreList']) and ChoiceItem >= 0:
                        wl.Skip()
                        Count = int(input("Скільки: "))
                        ItemIs = StarIs['StarCivil']['CivilStation']['StationStoreList'][ChoiceItem]
                        ItemCoust = int(int(ItemsDB[ItemIs]['ItemCoust']) * StarIs['StarCivil']['CivilEco']) * Count
                        if PlayerIs['Money'] <= ItemCoust:
                            wl.Error("Не достатньо грошей")
                        else:
                            StarIs['StarCivil']['CivilEco'] += StarIs['StarCivil']['CivilEco'] + 0.01 * math.log10((int(ItemCoust) * int(Count)))
                            if StarIs['StarCivil']['CivilEco'] < CivilEcoMin:
                                StarIs['StarCivil']['CivilEco'] = CivilEcoMin
                            else:
                                if StarIs['StarCivil']['CivilEco'] > CivilEcoMax:
                                    StarIs['StarCivil']['CivilEco'] = CivilEcoMax
                            ProjectInfinity.StarChange(StarIs['StarID'], 'StarCivil', StarIs['StarCivil'])
                            PlayerIs['Money'] -= ItemCoust
                            wl.InvAdd(ItemIs, Count)

                if StationStoreChoice == "Продати":
                    wl.Skip()
                    for alli in range(len(PlayerIs['Ship']['Storage'])):
                        ItemIs = PlayerIs['Ship']['Storage'][alli]
                        ItemCoust = int(int(ItemsDB[ItemIs['ItemID']]['ItemCoust']) * StarIs['StarCivil']['CivilEco'])
                        print(f"{alli+1}. {ItemsDB[ItemIs['ItemID']]['ItemName']} ▪ Ціна: {ItemCoust:,} © ▪ Тип: {ItemsType[ItemsDB[alli]['ItemType']]} ▪ Ціна разом: {int(ItemCoust*ItemIs['ItemCount']):,} © ▪ Кількість в сховище: {ItemIs['ItemCount']:,}")
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
                            StarIs['StarCivil']['CivilEco'] -= StarIs['StarCivil']['CivilEco'] + 0.01 * math.log10((int(ItemCoust) * int(SellLot)))
                            if StarIs['StarCivil']['CivilEco'] < CivilEcoMin:
                                StarIs['StarCivil']['CivilEco'] = CivilEcoMin
                            else:
                                if StarIs['StarCivil']['CivilEco'] > CivilEcoMax:
                                    StarIs['StarCivil']['CivilEco'] = CivilEcoMax
                            ProjectInfinity.StarChange(StarIs['StarID'], 'StarCivil', StarIs['StarCivil'])
                            wl.InvRem(ItemIs['ItemID'], int(SellLot))

            if StationCom == "Верф флотоносців":
                wl.Skip()
                for i in range(len(Fleets)):
                    FleetIs = Fleets[i]
                    FleetCoust = int(FleetIs['FleetCoust'] * StarIs['StarCivil']['CivilEco'])
                    print(f"{i+1}. {FleetIs['FleetModel']} ▪ {FleetIs['FleetCoust']:,} ©")

                FleetChoice = int(input("Купити: ")) - 1

                if FleetChoice > len(Fleets) or FleetChoice < 0:
                    wl.Error("Невірне введення")
                else:
                    FleetIs = Fleets[FleetChoice]
                    if PlayerIs['Money'] > FleetIs['FleetCoust']:
                        PlayerIs['Fleet'].append(
                            {
                                "FleetID": FleetIs['FleetID'],
                                "FleetName": FleetIs['FleetModel'],
                                "Ships": [],
                                "Storage": [],
                                "Location": StarIs['StarID'],
                                "Modules": {},
                                "Fuel": FleetIs['FleetMaxFuel']
                            }
                        )
                        PlayerIs['Money'] -= FleetCoust

            if StationCom == "Майстерня":
                def ChoiceModificationSlot():
                    wl.Skip()
                    for abs in range(len(PlayerIs['Ship']['ShipModification'])):
                        SlotIs = PlayerIs['Ship']['ShipModification'][abs]
                        if SlotIs['ModificationID'] != None:
                            ModIs = ShipModifications[SlotIs['ModificationID']]
                            ModLabel = f"{Colore.Yellow}{ModIs['ModName']}{Colore.Reset}"
                        else:
                            ModLabel = f"{Colore.Gray}Відсутній{Colore.Reset}"
                        print(f"{abs+1}. {abs+1} слот: [{ModLabel}]")
                    inp = int(wl.Command()) - 1
                    return inp
                
                wl.Skip()
                Categories = ["Придбати та встановити модифікацію", "Продати модифікацію"]
                IsCategories = wl.ChoiceMenu(Categories)
                
                if IsCategories == "Придбати та встановити модифікацію":
                    wl.Skip()
                    Modifications = ShipModifications
                    for abs in range(len(Modifications)):
                        ModificationIs = Modifications[abs]
                        ModificationDynamicCoust = int(ModificationIs['ModCoust'] * StarIs['StarCivil']['CivilEco'])
                        print(f"{abs+1}. {ModificationIs['ModName']} ▪ Ціна: {ModificationDynamicCoust:,} ©")
                    ModificationBuy = int(input("Вибрати: ")) - 1
                    ModificationIs = Modifications[ModificationBuy]
                    Slot = ChoiceModificationSlot()
                    if PlayerIs['Money'] >= ModificationIs['ModCoust']:
                        if PlayerIs['Ship']['ShipModification'][Slot]['ModificationID'] == None:
                            PlayerIs['Ship']['ShipModification'][Slot]['ModificationID'] = ModificationBuy
                            PlayerIs['Money'] -= ModificationIs['ModCoust']
                            wl.Loading("Встановлюємо модифікацію", 3)
                        else:
                            wl.Error("У вашему кораблі вже встановлена модифікація!")
                    else: wl.Error("Не достатньо грошей!")
                    

# Різне
if CommandInput == "5":
    wl.Skip()
    OtherList = ["Статистика", "Переіменувати корабель", "Сховище корабля", "Закріпленні"]

    if wl.Level >= 30:
        OtherList.append("Ваші колонії")

    OtherCom = wl.ChoiceMenu(OtherList)
    if OtherCom == "Статистика":
        wl.Skip()
        print("Статистика систем")
        print(f" ▪ Вивчено систем: {PlayerIs['Statistic']['StarInteled']:,}")
        print(f" ▪ Систем під контролем: {PlayerIs['Statistic']['StarControled']:,}")
        print(f" ▪ Колоній: {PlayerIs['Statistic']['StarColony']:,}")
        print()
        print(f" ▪ Усього кредитів отримана з торгівлі: {PlayerIs['Statistic']['CreditsFromSelled']:,} ©")
        print(f" ▪ Усього кредитів отримана з досліджень: {PlayerIs['Statistic']['CreditsFromScience']:,} ©")
        if PlayerIs['Statistic']['IncomeFromColony'] > 0:
            print()
            print(f" ▪ Прибуток з колонії: {PlayerIs['Statistic']['IncomeFromColony']:,} ©")
        input()

    if OtherCom == "Сховище корабля":
        wl.Skip()
        for alli in range(len(PlayerIs['Ship']['Storage'])):
            ItemIs = PlayerIs['Ship']['Storage'][alli]
            print(f"{alli+1}. {ItemsDB[ItemIs['ItemID']]['ItemName']} ▪ Тип: {ItemsType[ItemsDB[ItemIs['ItemID']]['ItemType']]} ▪ Кількість: {ItemIs['ItemCount']:,}")
        
        ItemChoice = int(input("Вибрати: ")) - 1
        
        if ItemChoice+1 > len(PlayerIs['Ship']['Storage']) and ItemChoice+1 <= 0:
            wl.Error("Недопустиме введення")
        else:
            ItemIs = PlayerIs['Ship']['Storage'][ItemChoice]
            if ItemsDB[ItemIs['ItemID']]['ItemName'] == ItemsDB[0]['ItemName']:
                    if ItemsDB[ItemIs['ItemID']]['ItemType'] == 0:
                        NewFuel = 0
                    for i in range(len(PlayerIs['Ship']['ShipModification'])):
                        if PlayerIs['Ship']['ShipModification'][i]['ModificationID'] == 0:
                            NewFuel += 50
                    FuelMaxCapacity = Ships[PlayerIs['Ship']['ShipID']]['ShipMaxFuel'] + NewFuel
                    PlayerIs['Ship']['Fuel'] += 5
                    if PlayerIs['Ship']['Fuel'] > FuelMaxCapacity: PlayerIs['Ship']['Fuel'] = FuelMaxCapacity
                    wl.Loading("Заправлення", 3)
                    wl.InvRem(0, 1)

    if OtherCom == "Закріпленні":
        wl.Skip()
        for absi in range(len(CustomStars)):
            CustomStarsIs = CustomStars[absi]
            StarIs = GenMap(int(CustomStarsIs['StarID']))
            if CustomStarsIs.get("PlayerPinned"):
                if CustomStarsIs['PlayerPinned'] == True:
                    print(f"{Colore.Yellow} ▪ {StarIs['Star']} ({StarIs['StarID']}) ▪ Опис: {CustomStarsIs['PlayerPinnedDesc']}")
        input()

    if OtherCom == "Переіменувати корабель":
        wl.Skip()
        NewName = input("Введіть нову назву кораблю: ")
        if NewName == "" or NewName == " ": exit()
        PlayerIs['Ship']['ShipName'] = NewName
        wl.Loading("Застосовуємо зміни", 1)
    
    if OtherCom == "Ваші колонії":
        wl.Skip()
        print("Колонії:")
        for i in range(len(CustomStars)):
            StarIs = CustomStars[i]
            Star = GenMap(StarIs['StarID'])
            if StarIs.get("StarCivil") and StarIs.get("StarControled"):
                print(f" - {Star['Star']} ({StarIs['StarID']}) ▪ Населення: {Star['StarCivil']['CivilFraction']['FractionPop']:,} ▪ Прибуток: {Star['InfoIncome']:,} © ▪ Дата колонізації: {StarIs['InfoDate']}")
        input()

# Перезавантажує гру, не зберігає процеси
if CommandInput == "*":
    exit()

# Командна строка для ведення кодів чи команд
if CommandInput == "/":
    wl.Skip()
    debug = exec(input("/"))
    if debug == "":
        exit()
    input("Нажміть ENTER щоб продовжити")

#region Logic
PlayerIs['GameUpdate'] += 1
if PlayerIs['GameUpdate'] == 5:
    PlayerIs['GameUpdate'] = 0
    ProjectInfinity.Logic()
#endregion

# Збереження прогресу через функцію SaveJSON із WhiteEngine
wl.SaveJSON("save.json", save)