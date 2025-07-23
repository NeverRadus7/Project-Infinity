from wlengine import *

wl.ConsoleSetSize()

wl.Skip()
wl.Screen()

CommandInput = wl.Command()

# Функція, яка відкриває мапу Галактики
if CommandInput == "1":
    pi.GalaxyMap("SHIP")

# Зоряна система
if CommandInput == "2":
    def StarInfo():
        print(
            f"{colorama.Back.BLUE} Загальна інформація {colorama.Back.RESET}\n"
            f" ▪ Зірка: {StarIs['Star']}\n"
            f" ▪ Спек. клас: {StarIs['Class']}\n"
            f" ▪ Температура: {StarIs['Temp']:,} K\n"
            f" ▪ Маса: {StarIs['Mass']:,} Ms\n"
            f" ▪ Розміри: {StarIs['Size']:,} Ss\n"
            f" ▪ Світність: {StarIs['Luminos']} Ls\n"
            f" ▪ Планет: {len(StarIs['Planets'])}\n"
        )
    
    def StarPolInfo():
        print(
            f"{colorama.Back.BLUE} Політична інформація {colorama.Back.RESET}\n"
            f" ▪ Економічний устрій: {Economics[StarIs['StarCivil']['CivilEconomicType']]}\n"
            f" ▪ Статус безпеки: {StarSecurityType[StarIs['StarCivil']['CivilSecurity']]}\n"
            f" ▪ Стабільність: {StarIs['StarCivil']['CivilStable']}%\n"
            f" ▪ Популяція: {StarIs['StarCivil']['CivilPop']:,}\n"
            f" ▪ Станція: {StarIs['StarCivil']['CivilStation']['StationName']}\n"
            f" ▪ Економічна стала: {StarIs['StarCivil']['CivilEco']}\n"
        )
        if StarIs.get("StarControled"):
            print(
                f"\033[A ▪ Колонізована: {StarIs['InfoDate']}\n"
            )
    
    def StarPlayerInfo():
        if StarIs.get("PlayerPinned") or StarIs.get("StarControled") or StarIs.get("StarIntel") or PlayerIs['Navy']['NavyLocation'] == StarIs['StarID']:
            print(f"{colorama.Back.BLUE} Користувацька інформація {colorama.Back.RESET}")
        if StarIs.get("PlayerPinned"):
            print(
                f" ▪ Прикрипліна: {colorama.Back.YELLOW} {SymbolOfStarPinned} {StarIs['PlayerPinnedDesc']} {colorama.Back.RESET}"
            )
        if StarIs.get("StarControled"): 
            print(
                f" ▪ Контроль: {StarIs['StarControled']}"
            )

        if StarIs.get("StarIntel"):
            print(
                f" ▪ Досліджена: {StarIs['StarIntel']}"
            )
        if StarIs.get("StarCivil"):
            if StarIs['StarCivil']['CivilReputation'] >= 80: print(f" ▪ Репутація в системі: {Colore.Green}{StarIs['StarCivil']['CivilReputation']}%{Colore.Reset}")
            elif StarIs['StarCivil']['CivilReputation'] <= 25: print(f" ▪ Репутація в системі: {Colore.Red}{StarIs['StarCivil']['CivilReputation']}%{Colore.Reset}")
            else: print(f" ▪ Репутація в системі: {StarIs['StarCivil']['CivilReputation']}%")

        if PlayerIs['Navy']['NavyLocation'] == StarIs['StarID']:
            print(
                " ▪ Флот: Знаходиться тут"
            )

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
        StarList.append("Заснувати власну колонію")

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

    if PlayerIs['Navy']['NavyLocation'] == StarIs['StarID']:
        StarList.append(f"Флот {Colore.Red}⟁{Colore.Reset}")

    if StarIs.get("StarCivil") and StarIs['StarCivil']['CivilStable'] <= 50:
        StarList.append("Полювання на піратів")

    if StarIs.get("StarCivil") and StarIs['StarCivil']['CivilStable'] <= 90 and not StarIs.get("StarControled"):
        StarList.append("Піратська діяльність")
            
    wl.Skip()
    if DebugInfo == True: print(f"{Colore.Gray}ID: {StarIs['StarID']}{Colore.Reset}")
    StarInfo()
    if StarIs.get("StarCivil"): StarPolInfo()
    StarPlayerInfo()
    print()

    StarInput = wl.ChoiceMenu(StarList)

    if StarInput == "Вивчити зірку":
        if not StarIs.get("StarIntel"):
            wl.Loading(f"Досліджуємо зірку {StarIs['Star']}", 5)
            TotalIntel = 0

            for planets in range(len(StarIs['Planets'])):
                PlanetIs = StarIs['Planets'][planets]

                if PlanetIs['PlanetLive'] == True: CoefficientsPlanetSpecialIs = 'Live'
                elif PlanetIs['PlanetTerraform'] == True: CoefficientsPlanetSpecialIs = 'Terraform'
                else: CoefficientsPlanetSpecialIs = 0
                
                PlanetIntel = int(random.randint(1000,2000) * (1 + (CoefficientsPlanetClasses[PlanetIs['PlanetClass']] + CoefficientsPlanetSpecial[CoefficientsPlanetSpecialIs] + pi.PlayerShipModificationAll(2))))
                TotalIntel += int(PlanetIntel)
                wl.Loading(f"Скануємо планету {PlanetIs['PlanetName']} {Colore.Blue}(+{PlanetIntel:,} ◭){Colore.Reset}", 3)

            PlayerIs['Statistic']['StarInteled'] += 1
            PlayerIs['IntelBall'] += TotalIntel
            PlayerIs['XP'] += random.randint(100,1000) * (len(StarIs['Planets']))

            pi.StarChange(StarIs['StarID'], "StarIntel", True)
    
    if StarInput == "Переіменувати систему":
        wl.Skip()
        NewNameStar = input("Нова назва: ")
        if NewNameStar == "" or NewNameStar == " ": exit()
        pi.StarChange(StarIs['StarID'], "Star", NewNameStar)
                
    if StarInput == "Закріпити систему в Галактичну мапу":
        wl.Skip()
        PinnedDesc = input("Назва тегу для закріплення: ")
        pi.StarChange(StarIs['StarID'], "PlayerPinned", True)
        pi.StarChange(StarIs['StarID'], "PlayerPinnedDesc", PinnedDesc)

    if StarInput == "Зняти систему із закріплень":
        pi.StarChange(StarIs['StarID'], "PlayerPinned", False)
    
    if StarInput == "Взяти під контроль":
        PlayerIs['Statistic']['StarControled'] += 1
        pi.StarChange(StarIs['StarID'], "StarControled", True)
    
    if StarInput == "Заснувати власну колонію":
        wl.Massage("Заснування колонії - це третій шаг встановлення влади, колонії дають можливість продавати чи покупати товари, мати постійне місце проживання та постійний прибуток. Але під постійним прибуток вважається стабільна економіка системи, яка урегулюєця трьома параметрами: кількість планет, популярність та тип головної станції системи.")
        wl.Massage("Перед тим, як заснувати, вам треба мати: Флотоносець класу Контруктор, 100,000,000 © та 30 рівень галактичної репутації")
        for i in range(len(PlayerIs['Fleet'])):
            FleetIs = PlayerIs['Fleet'][i]
            if FleetIs['Location'] == StarIs['StarID'] and Fleets[FleetIs['FleetID']]['FleetClass'] == 2:
                break
            else: pass
        if wl.Level >= 30:
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
                wl.Menu(Economics)
                
                EconomicChoice = int(input("Вибрати: ")) - 1
                
                pi.StarChange(
                    StarIs['StarID'], 
                    "StarCivil", 
                    {
                        "CivilEconomicType": EconomicChoice,
                        "CivilEco": random.uniform(CivilEcoMin,CivilEcoMax), 
                        "CivilStable": random.randint(1,100),
                        "CivilReputation": 100,
                        'CivilSecurity': 0,
                        "Navy": {
                            "NavyLevel": 1,
                            "NavyCruisers": 0,
                            "NavyShips": 1
                        },
                        "CivilStation": {
                            "StationName": f"{ranname()} Station",
                            "StationType": random.randint(0,2),
                            "StationStoreList": random.sample(range(len(ItemsDB)), int(random.randint(1,len(ItemsDB))))}, 
                        "CivilPop": random.randint(100,200)
                    }
                )
                wl.Skip()
                pi.StarChange(StarIs['StarID'], "InfoDate", wl.Date())
                pi.StarChange(StarIs['StarID'], "InfoIncome", 0)
                PlayerIs['Statistic']['StarColony'] += 1
        else:
            wl.Error("Не достатній рівень (>30)")

    if StarInput == "Керівництво системи":
        def ControlInfo():
            print(
                f"{colorama.Back.GREEN} Керівництво системи {colorama.Back.RESET}\n"
                f" ▪ Система: {StarIs['Star']}\n"
                f" ▪ Тип економіки: {Economics[StarIs['StarCivil']['CivilEconomicType']]}\n"
                f" ▪ Станція: {StarIs['StarCivil']['CivilStation']['StationName']}\n"
                f" ▪ Населення: {StarIs['StarCivil']['CivilPop']:,}\n"
                f" ▪ Прибуток: {StarIs['InfoIncome']:,} ©\n"
                f" ▪ Стабільність: {StarIs['StarCivil']['CivilStable']}%\n"
            )
        wl.Skip()
        ControlInfo()

        ControlInput = wl.ChoiceMenu(["Переіменувати станцію", "Служба безпеки системи"])

        if ControlInput == "Переіменувати станцію":
            wl.Skip()
            StarIs['StarCivil']['CivilStation']['StationName'] = input("Назва для станції: ")
            pi.StarChange(StarIs['StarID'], "StarCivil", StarIs['StarCivil'])

        if ControlInput == "Служба безпеки системи":
            wl.InfoBlock(
                titleColore={
                    'colore': colorama.Back.RED,
                    'title': "Флот системи"
                },
                text=f" ▪ Рівень флоту: {StarIs['StarCivil']['Navy']['NavyLevel']}\n" 
                     f" ▪ Крейсерів: {StarIs['StarCivil']['Navy']['NavyCruisers']:,}\n"
                     f" ▪ Кораблів: {StarIs['StarCivil']['Navy']['NavyShips']:,}"
                )
            input()

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
            pi.GalaxyMap("FLEET", FleetIsChoice)

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

    if StarInput == f"Флот {Colore.Red}⟁{Colore.Reset}":
        wl.Skip()
        def NavyInfo():
            print(
                f"{colorama.Back.RED} Інформація про флот ⟁ {colorama.Back.RESET}\n"
                f" ▪ Досвід флоту: {PlayerIs['Navy']['NavyLevel']}\n"
                f" ▪ Крейсерів: {PlayerIs['Navy']['NavyCruisers']:,}\n"
                f" ▪ Кораблів: {PlayerIs['Navy']['NavyShips']:,}\n"
                f" ▪ Бойовий рейтинг: {int(int(PlayerIs['Navy']['NavyShips'] * (PlayerIs['Navy']['NavyCruisers'])) * int(PlayerIs['Navy']['NavyLevel'])):,}\n"
            )
        
        NavyInfo()

        NavyList = ["Перемістити флот", "Виділити з флоту"]

        if StarIs.get("StarCivil") and not StarIs.get("StarControled"):
            NavyList.append(f"{Colore.Red}Завоювати систему{Colore.Reset}")

        NavyChoice = wl.ChoiceMenu(NavyList)

        if NavyChoice == "Перемістити флот":
            wl.Skip()
            print("Яку відстань флот повинен передолати?")
            TARGET = int(input("Перемістити: "))
            MAX_WARP = 10
            
            if abs(TARGET) > MAX_WARP:
                wl.Error("Максимальна дальність стрибка!")
            else:
                PlayerIs['Navy']['NavyLocation'] += TARGET
                PlayerIs['Location'] += TARGET

        if NavyChoice == f"{Colore.Red}Завоювати систему{Colore.Reset}":
            Battle = pi.Navy("Завоювання системи | Війна")
            if Battle == True:
                PlayerIs['Statistic']['StarColony'] += 1
                PlayerIs['Statistic']['StarControled'] += 1
                pi.StarChange(StarIs['StarID'], 'StarCivil', StarIs['StarCivil'])
                pi.StarChange(StarIs['StarID'], 'Planets', StarIs['Planets'])
                pi.StarChange(StarIs['StarID'], 'StarControled', True)
                pi.StarChange(StarIs['StarID'], 'InfoDate', wl.Date())

        if NavyChoice == "Виділити з флоту":
            wl.Skip()
            try:
                CruisersCount = int(input("Скільки КРЕЙСЕРІВ перемістити: "))
            except (ValueError, TypeError):
                CruisersCount = 0
            
            try:
                ShipsCount = int(input("Скільки КОРАБЛІВ перемістити:"))
            except (ValueError, TypeError):
                ShipsCount = 0

            SystemTo = input("В яку систему ([ENTER] - В поточну): ")
            if SystemTo in [" ", ""]: SystemTo = StarIs['StarID']

            Star = GenMap(int(SystemTo))

            if not Star.get("StarControled") and not Star.get("StarCivil"):
                wl.Error("Система не підкоряється вам!")
            else:
                Star['StarCivil']['Navy']['NavyCruisers'] += CruisersCount
                Star['StarCivil']['Navy']['NavyShips'] += ShipsCount
                pi.StarChange(Star['StarID'], 'StarCivil', Star['StarCivil'])

    if StarInput == "Полювання на піратів":
        BotAccuracy = rwos.randint(30,90)
        BotInterval = rwos.randint(1,7)
        PirateBattle = pi.Duel(f"Полювання на піратів - Система: {StarIs['Star']}", 
        {
            "Bot": "Пірат",
            "BotShip": rwos.choice(Ships),
            "BotModificationSlots": [],
            "BotAccuracy": BotAccuracy,
            "BotInterval": BotInterval
        })
        if PirateBattle == True:
            wl.ScreenTextLable("Ви перемогли пірата")
            PlayerIs['BattleScore'] += rwos.randint(100,1500) * wl.Level
            PlayerIs['XP'] += rwos.randint(100,200)
            StarIs['StarCivil']['CivilStable'] += rwos.randint(5,30)
            StarIs['StarCivil']['CivilReputation'] += rwos.randint(1,5)
            pi.StarChange(StarIs['StarID'], 'StarCivil', StarIs['StarCivil'])
            if rwos.randint(1,100) <= 30: wl.InvAdd(len(ItemsDB)-1,rwos.randint(1,20))

    if StarInput == "Піратська діяльність":
        BotName = rwos.choice(['Сили оборони системи','Торговий корабель','Громадянський корабель'])
        
        if StarIs['StarCivil']['CivilSecurity'] == 2:
            BotShip = rwos.choice([Ships[0],Ships[1]])
        if StarIs['StarCivil']['CivilSecurity'] == 1:
            BotShip = rwos.choice([Ships[1],Ships[2]])
        if StarIs['StarCivil']['CivilSecurity'] == 0:
            BotShip = rwos.choice([Ships[2],Ships[3]])
        
        BotAccuracy = rwos.randint(30,90)
        BotInterval = rwos.randint(1,7)

        SystemBattle = pi.Duel(f"Піратська діяльність - Система: {StarIs['Star']}",{
                                             "Bot": BotName,
                                             "BotShip": BotShip,
                                             "BotModificationSlots": [],
                                             "BotAccuracy": BotAccuracy,
                                             "BotInterval": BotInterval})
        
        if SystemBattle == True:
            wl.ScreenTextLable("Перемога")
            StarIs['StarCivil']['CivilStable'] -= rwos.randint(1,5)
            StarIs['StarCivil']['CivilReputation'] -= rwos.randint(5,10)
            pi.StarChange(StarIs['StarID'], 'StarCivil', StarIs['StarCivil'])
            if rwos.randint(1,100) <= 30: wl.InvAdd(len(ItemsDB)-1,rwos.randint(1,20))

# Планети поточної зоряної системи
if CommandInput == "3":
    wl.Skip()
    if not StarIs.get("StarIntel"): wl.Error("Система не досліджена")
    print(f"{colorama.Back.BLUE} Планети {StarIs['Star']} {colorama.Back.RESET}")
    for abs in range(len(StarIs['Planets'])):
        PlanetIs = StarIs['Planets'][abs]

        TerraformSymbol = ""
        if PlanetIs['PlanetTerraform'] == True:
            TerraformSymbol = f"{colorama.Fore.GREEN} 𖤖{colorama.Fore.RESET}"

        ColonySymbol = ""
        if PlanetIs.get("PlanetColony") and PlanetIs['PlanetColony']['ColonyBuild']['Enabled'] == True:
            ColonySymbol = f"{Colore.Yellow} ⚐⏲{Colore.Reset}"
        elif PlanetIs.get("PlanetColony") and PlanetIs['PlanetColony']['ColonyBuild']['Enabled'] == False:
            ColonySymbol = f"{Colore.Green} ⚑{Colore.Reset}"

        print(f"{abs+1}. {PlanetIs['PlanetName']}{TerraformSymbol}{ColonySymbol} - Клас: {PlanetClass[PlanetIs['PlanetClass']]} - Температура: {PlanetIs['PlanetTemp']} °C")
    
    print()
    
    try:
        PlanetChoice = int(input("Відправитися: "))-1
    except (TypeError, ValueError):
        exit()
    
    if PlanetChoice > len(StarIs['Planets']) or PlanetChoice < 0:
        wl.Error("Невірне введення")
    else:
        PlanetIs = StarIs['Planets'][PlanetChoice]
        def PlanetInfo():
            print(
                f"{colorama.Back.BLUE}Інформація планети{colorama.Back.RESET}\n"
                f" ▪ Планета: {PlanetIs['PlanetName']}\n"
                f" ▪ Клас: {PlanetClass[PlanetIs['PlanetClass']]}\n"
                f" ▪ Температура: {PlanetIs['PlanetTemp']} °C\n"
            )

        def ColonyInfo():
            print(
                f"{colorama.Back.BLUE}Колоніальна інформація{colorama.Back.RESET}\n"
                f" ▪ Колонія: {PlanetIs['PlanetColony']['ColonyName']}\n"
                f" ▪ Популяція: {PlanetIs['PlanetColony']['ColonyPop']:,}\n"
                f" ▪ Рівень: {PlanetIs['PlanetColony']['ColonyLevel']}\n"
            )

            if PlanetIs['PlanetColony']['ColonyBuild']['Enabled'] == True:
                print(
                    f"\033[A ▪ На будівництві до {wl.DateString(PlanetIs['PlanetColony']['ColonyBuild']['EndBuild'])}\n"
                )

        wl.Skip()

        PlanetList = []
        if "PLAYER_MINERTOOL" in PlayerIs['Atribution']:
            PlanetList.append("Видобуток корисних копалин")

        if not StarIs.get('StarCivil'):
            PlanetList.append("Зробити поверхневий аналіз")

        if StarIs.get('StarControled') and StarIs['StarControled'] == True:
            PlanetList.append("Переіменувати планету")

        if "PLAYER_TERRAFORMER_DEVICE" in PlayerIs['Atribution']:
            if PlanetIs['PlanetTerraform'] == True:
                if PlanetIs['PlanetLive'] == False:
                    PlanetList.append(f"Почати тераформінг {Colore.Green}𖤖{Colore.Reset}")

        if len(PlayerIs['Fleet']) != 0:
            for i in range(len(PlayerIs['Fleet'])):
                if PlayerIs['Fleet'][i]['Location'] == StarIs['StarID'] and StarIs.get("StarControled") and StarIs.get("StarCivil"):
                    if Fleets[PlayerIs['Fleet'][i]['FleetID']]['FleetClass'] == 2:
                        if not PlanetIs.get("PlanetColony"): 
                            PlanetList.append(f"Побудувати колонію")
                            break
        
        print(f"{colorama.Back.BLUE} Вигляд планети {colorama.Back.RESET}")
        pi.PlanetView(PlanetIs['PlanetViewSeed'], PlanetIs['PlanetSize'], PlanetIs['PlanetColore'])
        print()

        PlanetInfo()
        if PlanetIs.get("PlanetColony"): ColonyInfo()
        PlanetChoice = wl.ChoiceMenu(PlanetList)

        if PlanetChoice == "Переіменувати планету":
            wl.Skip()
            NewPlanetName = input("Нова назва: ")
            if NewPlanetName == "":
                exit()
            PlanetIs['PlanetName'] = NewPlanetName
            pi.StarChange(StarIs['StarID'], "Planets", StarIs['Planets'])
            wl.Loading("Застосовуємо зміни", 1)

        if PlanetChoice == "Видобуток корисних копалин":
            wl.Skip()
            try:
                MINE_CYCLE = int(input("Скільки разів: "))
            except (ValueError): 
                MINE_CYCLE = 1
            for i in range(MINE_CYCLE):
                MINE_AMOUNT = rwos.randint(1,10)
                MINE_THIS = rwos.choice(range(5,9))
                if rwos.randint(1,100) <= 10:
                    wl.InvAdd(9,MINE_AMOUNT)
                else:
                    wl.InvAdd(MINE_THIS, MINE_AMOUNT)
                wl.Loading(f"Видобуваємо {ItemsDB[MINE_THIS]['ItemName']} {Colore.Yellow}(+{MINE_AMOUNT}){Colore.Reset}",3)

        if PlanetChoice == f"Почати тераформінг {Colore.Green}𖤖{Colore.Reset}":
            PlanetIs['PlanetClass'] = 4
            PlanetIs['PlanetLive'] = True
            PlanetIs['PlanetTemp'] = rwos.uniform(-10,30)
            ItemSec = 0
            for abs in range(len(PlayerIs['Ship']['Storage'])):
                ItemIs = PlayerIs['Ship']['Storage'][abs]
                if ItemIs['ItemID'] == 4:
                    ItemSec += 1
                else: ItemSec += 0
            if ItemSec > 0:
                wl.InvRem(4, 1)
                pi.StarChange(StarIs['StarID'], "Planets", StarIs['Planets'])
                wl.Loading("Тераформуємо планету (Це може заняти кілька тижднів)", 5)
                game.world.mature(rwos.randint(7,28))
            else:
                wl.Error(f"В трюмі відсутній: {ItemsDB[4]['ItemName']}")

        if PlanetChoice == "Побудувати колонію":
            wl.Skip()
            for i in range(len(PlayerIs['Ship']['Storage'])):
                ItemIs = PlayerIs['Ship']['Storage'][i]
                if ItemIs['ItemID'] == 1 and ItemIs['ItemCount'] >= 1:
                    wl.InvRem(1,1)

                    PlanetIs['PlanetColony'] = {}
                    PlanetIs['PlanetColony']['ColonyName'] = "Test"
                    PlanetIs['PlanetColony']['ColonyLevel'] = 1
                    PlanetIs['PlanetColony']['ColonyPop'] = 0
                    PlanetIs['PlanetColony']['ColonyBuild'] = {"Enabled": True, "EndBuild": PlayerIs['WorldDay'] + 31}

                    pi.StarChange(StarIs['StarID'], 'Planets', StarIs["Planets"])
                    break

# Станція
if CommandInput == "4":
    if StarIs.get("StarCivil"):
        if StarIs['StarCivil']['CivilReputation'] <= 25: wl.Error("До станції доступ заборонений (<25% Репутація)")
        wl.Skip()
        print(f"{colorama.Back.BLUE} Станція {colorama.Back.RESET}")
        print(f" ▪ Станція: {StarIs['StarCivil']['CivilStation']['StationName']}")
        print(f" ▪ Економічна стала: {StarIs['StarCivil']['CivilEco']}")
        print()

        StationList = ["Здати досліди", "Заправитися", "Верф", "Ринок"]

        if StarIs['StarCivil']['CivilEconomicType'] == 8:
            StationList.append("Верф флоту")

        if StarIs['StarCivil']['CivilStation']['StationType'] == 2:
            StationList.append("Верф крейсерів")

        if StarIs['StarCivil']['CivilEconomicType'] in [1,3,4]:
            StationList.append("Майстерня")

        StationCom = wl.ChoiceMenu(StationList)

        if StationCom == "Здати досліди":
            if PlayerIs['IntelBall'] > 0:
                wl.Loading("Здавання дослідження",3)
                PlayerIs['Money'] += (PlayerIs['IntelBall'] * IntelToCredits)
                PlayerIs['Statistic']['CreditsFromScience'] += (PlayerIs['IntelBall'] * IntelToCredits)
                PlayerIs['IntelBall'] = 0
        
        if StationCom == "Заправитися":
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
                    PlayerIs['Ship']['ShipModification'] = []
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
                            "ShipModification": [],
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
                    ItemCoustClear = int(int(ItemsDB[ItemIs]['ItemCoust']) * StarIs['StarCivil']['CivilEco']) 
                    ItemCoust = int(int(ItemsDB[ItemIs]['ItemCoust']) * StarIs['StarCivil']['CivilEco']) * Count
                    if PlayerIs['Money'] <= ItemCoust:
                        wl.Error("Не достатньо грошей")
                    else:
                        StarIs['StarCivil']['CivilEco'] += (1 - (ItemCoustClear/(ItemCoust)))/10
                        if StarIs['StarCivil']['CivilEco'] < CivilEcoMin:
                            StarIs['StarCivil']['CivilEco'] = CivilEcoMin
                        else:
                            if StarIs['StarCivil']['CivilEco'] > CivilEcoMax:
                                StarIs['StarCivil']['CivilEco'] = CivilEcoMax
                        pi.StarChange(StarIs['StarID'], 'StarCivil', StarIs['StarCivil'])
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
                    ItemCoustClear = int(int(ItemsDB[ItemIs['ItemID']]['ItemCoust']) * StarIs['StarCivil']['CivilEco'])
                    ItemCoust = int(int(ItemsDB[ItemIs['ItemID']]['ItemCoust']) * StarIs['StarCivil']['CivilEco']) * int(SellLot)
                    if int(SellLot) > ItemIs['ItemCount']: wl.Error("Не висточає товару для продажу")
                    else:
                        PlayerIs['Money'] += ItemCoust
                        PlayerIs['XP'] += int((int(SellLot)) * 5)
                        PlayerIs['Statistic']['CreditsFromSelled'] += ItemCoust
                        StarIs['StarCivil']['CivilEco'] -= (1 - (ItemCoustClear/(ItemCoust)))/10
                        if StarIs['StarCivil']['CivilEco'] < CivilEcoMin:
                            StarIs['StarCivil']['CivilEco'] = CivilEcoMin
                        else:
                            if StarIs['StarCivil']['CivilEco'] > CivilEcoMax:
                                StarIs['StarCivil']['CivilEco'] = CivilEcoMax
                        pi.StarChange(StarIs['StarID'], 'StarCivil', StarIs['StarCivil'])
                        wl.InvRem(ItemIs['ItemID'], int(SellLot))

        if StationCom == "Верф крейсерів":
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
            wl.Skip()
            Categories = ["Придбати та встановити модифікацію", "Продати модифікацію", "Покращити модифікацію"]
            IsCategories = wl.ChoiceMenu(Categories)
            
            if IsCategories == "Придбати та встановити модифікацію":
                wl.Skip()
                Modifications = ShipModifications
                wl.Menu(ModificationType)
                ModType = int(input("Вибрати: "))-1
                if ModType > len(ModificationType) or ModType < 0:
                    wl.Error("Невірне введення")
                wl.Skip()
                for abs in range(len(Modifications)):
                    ModificationIs = Modifications[abs]
                    if ModificationIs['ModType'] == ModType:
                        ModificationDynamicCoust = int(ModificationIs['ModCoust'] * StarIs['StarCivil']['CivilEco'])
                        print(f"{abs+1}. {ModificationIs['ModName']} ▪ Ціна: {ModificationDynamicCoust:,} ©")

                ModificationBuy = int(input("Вибрати: ")) - 1
                ModificationIs = Modifications[ModificationBuy]

                Slot = ChoiceModificationSlot()

                if PlayerIs['Money'] >= ModificationIs['ModCoust']:
                    if PlayerIs['Ship']['ShipModification'][Slot]['ModificationID'] == None:
                        PlayerIs['Ship']['ShipModification'][Slot]['ModificationID'] = ModificationBuy
                        PlayerIs['Ship']['ShipModification'][Slot]['ModificationLevel'] = 0
                        PlayerIs['Money'] -= ModificationIs['ModCoust']
                        wl.Loading("Встановлюємо модифікацію", 3)
                    else:
                        wl.Error("У вашему кораблі вже встановлена модифікація!")
                else: wl.Error("Не достатньо грошей!")
            
            if IsCategories == "Продати модифікацію":
                wl.Skip()
                Slot = ChoiceModificationSlot()
                ModIs = PlayerIs['Ship']['ShipModification'][Slot]
                ModRegisterIs = ShipModifications[ModIs['ModificationID']]
                
                wl.Skip()
                wl.Quation("Ви точно хочете продати існуючу модифікацію?")

                NewCoust = int((ModRegisterIs['ModCoust'] * 0.95) * (1 + ModIs['ModificationLevel']))
                ModIs['ModificationID'] = None
                ModIs['ModificationLevel'] = 0
                PlayerIs['Money'] += NewCoust
                wl.Loading("Демонтаж модифікації", 3)

            if IsCategories == "Покращити модифікацію":
                wl.Skip()
                Slot = ChoiceModificationSlot()
                ModIs = PlayerIs['Ship']['ShipModification'][Slot]
                
                if ModIs['ModificationLevel'] >= ModMaxLevel:
                    wl.Error("Вже максимальний рівень модифікації")
                else:
                    LevelIs = int(input(f"Від 1 до {ModMaxLevel-ModIs['ModificationLevel']}: "))
                    if LevelIs <= (ModMaxLevel-ModIs['ModificationLevel']) and LevelIs <= ModMaxLevel:
                        CoustUp = int(ShipModifications[ModIs['ModificationID']]['ModCoust'] * (StarIs['StarCivil']['CivilEco']) * (1 + ModIs['ModificationLevel']) * (LevelIs * 5) * ModLevelCoeff)
                        wl.Skip()
                        wl.Quation(f"Ви точно хочете покращити модифікацію ({CoustUp:,} ©)")
                        if PlayerIs['Money'] >= CoustUp:
                            PlayerIs['Money'] -= CoustUp
                            ModIs['ModificationLevel'] += LevelIs
                            wl.Loading("Покращуємо модифікацію",3)
                    else:
                        wl.Error("Перевишений максимум рівня")

        if StationCom == "Верф флоту":
            wl.Skip()
            NavyList = ["Придбати більше кораблів"]

            NavyChoice = wl.ChoiceMenu(NavyList)
            if NavyChoice == "Придбати більше кораблів":
                wl.Skip()
                ShipsCount = int(input("Скільки кораблів: "))

                ShipsCoust = (ShipsCount * 1_250_000)

                if PlayerIs['Money'] >= ShipsCoust:
                    PlayerIs['Navy']['NavyShips'] += ShipsCount
                else:
                    wl.Error("Не висточає грошей!")

# Різне
if CommandInput == "5":
    wl.Skip()
    OtherList = ["Статистика", "Мій корабель", "Закріпленні"]

    if wl.Level >= 30:
        OtherList.append("Ваші колонії")
    
    if wl.Level >= 50:
        OtherList.append("Флот")

    OtherCom = wl.ChoiceMenu(OtherList)
    if OtherCom == "Статистика":
        wl.Skip()
        print(f"{colorama.Back.BLUE} Статистика систем {colorama.Back.RESET}")
        print(f" ▪ Вивчено систем: {PlayerIs['Statistic']['StarInteled']:,}")
        print(f" ▪ Систем під контролем: {PlayerIs['Statistic']['StarControled']:,}")
        print(f" ▪ Колоній: {PlayerIs['Statistic']['StarColony']:,}")
        print()
        print(f" ▪ Усього кредитів отримана з торгівлі: {PlayerIs['Statistic']['CreditsFromSelled']:,} ©")
        print(f" ▪ Усього кредитів отримана з досліджень: {PlayerIs['Statistic']['CreditsFromScience']:,} ©")
        if PlayerIs['Statistic']['IncomeFromColony'] > 0:
            print()
            print(f" ▪ Прибуток з колонії: {PlayerIs['Statistic']['IncomeFromColony']:,} ©")
        
        print()
        StatisticList = ["Скинути всі дані статистики"]
        StatisticChoice = wl.ChoiceMenu(StatisticList)

        if StatisticChoice == "Скинути всі дані статистики":
            wl.Quation("Ви точно бажаєте видалити всі дані про Вашу статистику? Всі дані будуть видаленні!")
            for i, k in enumerate(PlayerIs['Statistic']):
                PlayerIs['Statistic'][k] = 0

    if OtherCom == "Мій корабель":
        wl.Skip()
        print(f"Ваш корабель: {PlayerIs['Ship']['ShipName']}")
        print(f"    ▪ Клас: {ShipClasses[Ships[PlayerIs['Ship']['ShipID']]['ShipClass']]}")
        print(f"    ▪ Міцність: {PlayerShipHP:,} HP")
        print(f"    ▪ Урон: {PlayerShipDMG:,} DM")
        print(f"    ▪ Інтервалів: {PlayerShipInterval:,}")
        print(f"    ▪ Макс. дистанція стрибка: {Ships[PlayerIs['Ship']['ShipID']]['ShipTravelingDist']} (+{TravelDistation-Ships[PlayerIs['Ship']['ShipID']]['ShipTravelingDist']})")
        print(f"    ▪ Макс. палива: {Ships[PlayerIs['Ship']['ShipID']]['ShipMaxFuel']} (+{FuelMaxCapacity-Ships[PlayerIs['Ship']['ShipID']]['ShipMaxFuel']})")
        print(f"    ▪ Модифікації:")
        ModificationSlots(3)
        print()
        ShipList = ["Переіменувати корабель", "Сховище корабля",]

        ShipCom = wl.ChoiceMenu(ShipList)

        if ShipCom == "Сховище корабля":
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
                            PlayerIs['Ship']['Fuel'] += 5
                            if PlayerIs['Ship']['Fuel'] > FuelMaxCapacity: 
                                PlayerIs['Ship']['Fuel'] = FuelMaxCapacity
                            wl.Loading("Заправлення", 3)
                            wl.InvRem(0, 1)
                            # ID OF FUEL: 0

        if ShipCom == "Переіменувати корабель":
            wl.Skip()
            NewName = input("Введіть нову назву кораблю: ")
            if NewName == "" or NewName == " ": exit()
            PlayerIs['Ship']['ShipName'] = NewName
            wl.Loading("Застосовуємо зміни", 1)

    if OtherCom == "Закріпленні":
        wl.Skip()
        print(f"{colorama.Back.YELLOW} Закріпленні {colorama.Back.RESET}")
        for absi in range(len(CustomStars)):
            CustomStarsIs = CustomStars[absi]
            StarIs = GenMap(int(CustomStarsIs['StarID']))
            if CustomStarsIs.get("PlayerPinned"):
                if CustomStarsIs['PlayerPinned'] == True:
                    print(f" ▪ {StarIs['Star']} ({StarIs['StarID']}) ▪ Опис: {CustomStarsIs['PlayerPinnedDesc']}")
        input()
    
    if OtherCom == "Ваші колонії":
        wl.Skip()
        print(f"{colorama.Back.GREEN} Колонії {colorama.Back.RESET}")
        for i in range(len(CustomStars)):
            StarIs = CustomStars[i]
            Star = GenMap(StarIs['StarID'])
            if StarIs.get("StarCivil") and StarIs.get("StarControled"):
                print(f" - {Star['Star']} ({StarIs['StarID']}) ▪ Населення: {Star['StarCivil']['CivilPop']:,} ▪ Прибуток: {Star['InfoIncome']:,} © ▪ Дата колонізації: {StarIs['InfoDate']}")
        input()

    if OtherCom == "Флот":
        wl.Skip()
        print("Флот:")
        print(f" ▪ Досвід флоту: {PlayerIs['Navy']['NavyLevel']}")
        print(f" ▪ Кораблів: {PlayerIs['Navy']['NavyShips']}")
        print(f" ▪ Бойовий рейтинг: {int(int(PlayerIs['Navy']['NavyShips']) * int(PlayerIs['Navy']['NavyLevel']) * (int(PlayerIs['Navy']['NavyLeader']['LeaderLevel'])/5)):,}")
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
    pi.Logic()
#endregion

# Збереження прогресу через функцію SaveJSON із WhiteEngine
wl.SaveJSON("save.json", save)