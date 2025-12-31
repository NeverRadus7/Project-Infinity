from wlengine import *
#wl.Screen()
wl.Skip()

def infoscreen(stdscr, StarIs):
    curses.use_default_colors()
    curses.curs_set(0)
    max_colors = curses.COLORS
    if max_colors > 8:
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(10, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(100, curses.COLOR_RED, curses.COLOR_BLACK) # RED
        curses.init_pair(101, curses.COLOR_GREEN, curses.COLOR_BLACK) # GREEN
        curses.init_pair(102, curses.COLOR_BLUE, curses.COLOR_BLACK) # BLUE
        curses.init_pair(103, curses.COLOR_YELLOW, curses.COLOR_BLACK) # YELLOW

    curses.curs_set(0)

    while True:
        size_y, size_x = stdscr.getmaxyx()
        stdscr.clear()

        stdscr.box()
        stdscr.refresh()
        stdscr.addstr(0,int((size_x-len(GameName))/2), GameName)

        balance = stdscr.derwin(7,40,1,((size_x-40)-2))
        bal_y, bal_x = balance.getmaxyx()
        balance.box()
        balance.addstr(0,int((bal_x-len("Balance"))/2), "Balance")
        bal_money = f"CRD: {PlayerIs['Money']:,} ©"
        bal_intelball = f"InB: {PlayerIs['IntelBall']:,} ◭"
        bal_battleball = f"BatB: {PlayerIs['BattleScore']:,} ✪"
        bal_socialball = f"SocB: {PlayerIs['SocialScore']:,} ⑇"
        bal_xp = f"XP: {PlayerIs['XP']:,} XP"
        balance.addstr(1,1,bal_money, curses.color_pair(103))
        balance.addstr(2,1,bal_intelball, curses.color_pair(102))
        balance.addstr(3,1,bal_battleball, curses.color_pair(100))
        balance.addstr(4,1,bal_socialball, curses.color_pair(101))
        balance.addstr(5,1,bal_xp)
        balance.refresh()

        ship = stdscr.derwin(10,40,8,((size_x-40)-2))
        ship_y, ship_x = ship.getmaxyx()
        ship.box()
        ship.addstr(0,int((ship_x-len("Ship"))/2), "Ship")
        ship.addstr(1,1,f"Ship: {PlayerIs['Ship']['ShipName']}")
        ship.addstr(2,1,f"  - Class: {ShipClasses[Ships[PlayerIs['Ship']['ShipID']]['ShipClass']]}")
        ship.addstr(3,1,f"  - HP: {PlayerShipHP:,} ♥︎")
        ship.addstr(4,1,f"  - DM: {PlayerShipDMG:,} ⚔︎")
        ship.addstr(5,1,f"  - DIST: {TravelDistation:,} y.l")
        ship.addstr(6,1,f"  - Max. Cap: {PlayerMaxItems:,} (+{PlayerMaxItems-Ships[PlayerIs['Ship']['ShipID']]['ShipMaxItems']})")
        ship.addstr(7,1,f"  - Fuel: {PlayerIs['Ship']['Fuel']:,}/{FuelMaxCapacity:,} ({int((PlayerIs['Ship']['Fuel']/FuelMaxCapacity)*100)}%)", curses.color_pair(103))
        ship.refresh()

        statistic = stdscr.derwin(((size_y-18)-2),40,18,((size_x-40)-2))
        stat_y, stat_x = statistic.getmaxyx()
        statistic.box()
        statistic.addstr(0, int((ship_x-len("Statistic"))/2), "Statistic")
        statistic.addstr(1, 1, f"Data: {wlengine.DateStr()}")
        statistic.addstr(2,1,f"Next update: {wlengine.DateOtherStr(wlengine.DateRead(PlayerIs['NextDate']))}")
        for i,k in enumerate(PlayerIs['Statistic']):
            statistic.addstr(int(i+3),1, f"{k}: {PlayerIs['Statistic'][k]:,}")
        statistic.refresh()

        player = stdscr.derwin(17,((size_x-40))-4,1, 2)
        pl_y, pl_x = player.getmaxyx()
        player.box()
        player.addstr(0,int((pl_x-len("Player"))/2),"Player")
        player.addstr(1,1,f"In: {StarIs['Star']} ({StarIs['StarID']})")
        player.addstr(2,1,f"Nickname: {PlayerIs['Nickname']}")
        player.addstr(3,1,f"Rang: {LevelRangIs}")
        player.addstr(4,1,f"Level: {wl.Level}")
        player.addstr(5,1,f"Reputation: {PlayerIs['Reputation']} % | WIP")
        player.addstr(7,1,f"Exosuit:")
        player.addstr(8,1,f"    - Class: {PlayerIs['Exo']['ExoClass']}")
        player.addstr(9,1,f"    - Level: {PlayerIs['Exo']['ExoLevel']}")
        player.refresh()

        n = 0
        colonies = stdscr.derwin((size_y-18)-2,((size_x-40))-4,18,2)
        col_y, col_x = colonies.getmaxyx()
        colonies.scrollok(True)
        colonies.box()
        colonies.addstr(0,int((col_x-len("Colonies"))/2), "Colonies")

        for i,k in enumerate(CustomStars):
            StarIs = CustomStars[i]
            if StarIs.get("StarCivil") and StarIs["StarCivil"] != []:
                if StarIs['StarCivil']['CivilEco'] >= 1.4:
                    color = curses.color_pair(101)
                elif StarIs['StarCivil']['CivilEco'] >= 0.8 and StarIs['StarCivil']['CivilEco'] <= 1.1:
                    color = curses.color_pair(103)
                elif StarIs['StarCivil']['CivilEco'] < 0.8:
                    color = curses.color_pair(100)
                else:
                    color = curses.color_pair(0) 

                if StarIs.get("StarControled") and StarIs['StarControled'] == True:
                    n += 1
                    if n >= 0 and n <= col_y-2:
                        colonies.addstr(int(n),1,f"{n}. {StarIs['Star']}({StarIs['StarID']}) - Pops: {StarIs['StarCivil']['CivilPop']:,} - ECO: {StarIs['StarCivil']['CivilEco']} - Station: {StarIs['StarCivil']['CivilStation']['StationName']}"[:col_x-2], color)
        colonies.refresh()

        stdscr.addstr(size_y-2,size_x-len("© Kaluhin's studio - 2025")-2, "© Kaluhin's studio - 2025", curses.color_pair(0) | curses.A_DIM)
        stdscr.addstr(size_y-2,3,f"Version {VersionClient}", curses.color_pair(0) | curses.A_DIM)
        menu = "| [1]-Galaxy | [2]-Star | [3]-Planets | [4]-Station | [5]-Other |"
        stdscr.addstr(size_y-1, int((size_x-len(menu))/2), menu)
        stdscr.move(size_y-1, size_x-1)

        key = stdscr.getch()
        keyname = curses.keyname(key).decode()

        if keyname == "^J":
            pass

        return keyname

CommandInput = curses.wrapper(lambda stdscr: infoscreen(stdscr, StarIs))

# Функція, яка відкриває мапу Галактики
if CommandInput == "1":
    curses.wrapper(lambda stdscr: pi.NewGalaxyMap(PlayerIs["Location"], stdscr))

if CommandInput == "2":
    def starinfoscr(pattern):
        curses.init_pair(100, curses.COLOR_RED, curses.COLOR_BLACK)
        while True:
            pattern.clear()
            size_y, size_x = pattern.getmaxyx()
            pattern.box()
            pattern.addstr(0,int((size_x-len("Star system"))/2), "Star system")

            maininfo = pattern.derwin(14,40,1,2)
            m_y, m_x = maininfo.getmaxyx()
            maininfo.box()
            maininfo.addstr(0,int((m_x-len("System"))/2), "System")
            maininfo.addstr(1,1,f"StarID: {StarIs['StarID']}")
            maininfo.addstr(2,1,f"Star: {StarIs['Star']}")
            maininfo.addstr(3,1,f"Planets: {len(StarIs['Planets'])}")
            maininfo.addstr(4,1,f"Physical information: ")
            maininfo.addstr(5,1,f"  - Stellar Classification: {StarIs['Class']}")
            maininfo.addstr(6,1,f"  - Mass: {StarIs['Mass']}")
            maininfo.addstr(7,1,f"  - Size: {StarIs['Size']}")
            maininfo.addstr(8,1,f"  - Luminos: {StarIs['Luminos']}")
            if StarIs.get("StarIntel") and StarIs['StarIntel'] == True:
                maininfo.addstr(9,1,f"Inteled: Yes")
            if StarIs.get("StarControled") and StarIs['StarControled'] == True:
                maininfo.addstr(10,1,f"Controled: Yes")

            if StarIs.get("PlayerPinned") and StarIs['PlayerPinned'] == True:
                favoscr = maininfo.derwin(3,int(len(StarIs['PlayerPinnedDesc']))+8,((m_y-3)-1),((m_x-int(len(StarIs['PlayerPinnedDesc'])))-9))
                max_colors = curses.COLORS
                if max_colors > 8:
                    curses.init_pair(50, 11, curses.COLOR_BLACK)
                f_y, f_x = favoscr.getmaxyx()
                favoscr.attrset(curses.color_pair(50))
                favoscr.box()
                favoscr.addstr(0,int((f_x-len("Favorite"))/2), "Favorite")
                favoscr.addstr(1,int((f_x-len(StarIs['PlayerPinnedDesc']))/2),f"{StarIs['PlayerPinnedDesc']}")
                favoscr.attrset(curses.color_pair(0))
                favoscr.refresh()

            maininfo.refresh()

            civil = pattern.derwin(((size_y-16)), 40, 15, 2)
            civ_y, civ_x = civil.getmaxyx()
            civil.box()
            civil.addstr(0,int((m_x-len("Civil"))/2), "Civil")
            if StarIs.get("StarCivil") and StarIs['StarCivil'] != []:
                stationscr = civil.derwin(5, 35, civ_y-6, int((civ_x-35)/2))
                st_y, st_x = stationscr.getmaxyx()
                stationscr.box()
                stationscr.addstr(0,int((st_x-len("Station"))/2), "Station")
                stationscr.addstr(1,1, f"Station: {StarIs['StarCivil']['CivilStation']['StationName']}")
                stationscr.addstr(2,1, f"Type: {StationType[StarIs['StarCivil']['CivilStation']['StationType']]}")
                if StarIs.get("InfoDate"):
                    stationscr.addstr(3,1, f"Date: {StarIs['InfoDate']}")
                stationscr.refresh()

                civil.addstr(1,1,f"Economic: {Economics[StarIs['StarCivil']['CivilEconomicType']]}")
                civil.addstr(2,1,f"ECO: {StarIs['StarCivil']['CivilEco']:.4f}")
                civil.addstr(3,1,f"Security: {StarSecurityType[StarIs['StarCivil']['CivilSecurity']]}")
                civil.addstr(4,1,f"Stable: {StarIs['StarCivil']['CivilStable']}%")
                civil.addstr(5,1,f"Loc. Reputation: {StarIs['StarCivil']['CivilReputation']}%")
                civil.addstr(6,1,f"Population: {StarIs['StarCivil']['CivilPop']:,}")
            else:
                civil.addstr(int((civ_y-1)/2), int((civ_x-len("No information"))/2), "No information")
            civil.refresh()

            planetinfo = pattern.derwin(((size_y-2)), ((size_x-44)), 1, 42)
            p_y, p_x = planetinfo.getmaxyx()
            planetinfo.box()
            planetinfo.addstr(0,int((p_x-len("Architectory"))/2), "Architectory")
            
            if StarIs.get("StarIntel") and StarIs['StarIntel'] == True:
                if StarIs['Planets'] != []:
                    planetinfo.addstr(1,1,"Planets:")
                    for i,k in enumerate(StarIs['Planets']):
                        if i >= 0 and i < p_y-2:
                            planetinfo.addstr(i+2, 1, f" - {k['PlanetName']} - {PlanetClass["TypeClass"][k['PlanetClass']['TypeClass']]}"[:p_x-2])
                else:
                    planetinfo.addstr(1,1,"/!\\ There are no planets in this system.", curses.color_pair(100))
                if StarIs['Asteroids'] != []:
                    planetinfo.addstr(3+len(StarIs['Planets']), 1, f"Asteroid belts:")
                    for i, astr in enumerate(StarIs['Asteroids']):
                        planetinfo.addstr(4+i+len(StarIs['Planets']), 1, f" - Asteroid: {astr['AsteroidName']}")
                else:
                    planetinfo.addstr(3+len(StarIs['Planets']), 1, "/!\\ There are no asteroids in this system.", curses.color_pair(100))
            else:
                planetinfo.addstr(int((p_y-1)/2), int((p_x-len("Not inteled"))/2), "Not inteled")
            planetinfo.refresh()

            menu = "| [m]-Menu | [q]-Quit |"
            pattern.addstr(size_y-1, int((size_x-len(menu))/2), menu)
            pattern.refresh()
            key = pattern.getkey()

            if key in ["m", "\n"]:
                menu = []

                if not StarIs.get("PlayerPinned") or StarIs['PlayerPinned'] == False:
                    menu.append("Make favorite")
                else:
                    menu.append("Disable favorite")

                if StarIs['Asteroids'] != [] and Ships[PlayerIs['Ship']['ShipID']]['ShipClass'] == 4:
                    menu.append("Mining in asteroid belt")

                if StarIs.get("StarIntel") and StarIs['StarIntel'] == True:
                    if StarIs.get("StarControled") and StarIs['StarControled'] == True:
                        menu.append("Rename system")
                        if StarIs.get("StarCivil") and StarIs['StarCivil'] != []:
                            menu.append("System control menu")
                        else:
                            menu.append("Built the station")
                    else:
                        if not StarIs.get("StarCivil"):
                            menu.append("Take control")
                else:
                    menu.append("Research this the system")

                choice = pi.menuscreen(pattern, "Star menu", menu)
                return str(choice)

            if key == "q":
                break
    
    choice = curses.wrapper(lambda stdscr: starinfoscr(stdscr))
    
    if choice == "Research this the system":
        def intel_lo(stdscr):
            stdscr.clear()
            stdscr.box()
            sz_y, sz_x = stdscr.getmaxyx()
            stdscr.addstr(0,int((sz_x-len("Researched"))/2), "Researched")
            planets = len(StarIs['Planets'])
            intel_balls = 0
            stdscr.addstr(1,1,f"Star for research: {StarIs['Star']}")
            stdscr.addstr(1,sz_x-len(f"Total planets: {planets}")-2, f"Total planets: {planets}")
            for i in range(planets):
                PlanetIs = StarIs['Planets'][i]
                intel_ball = int(rwos.randint(MinIntel,MaxIntel) * (1 + CoefficientsPlanetClasses[PlanetIs['PlanetClass']['TypeClass']]))
                intel_balls += intel_ball
                stdscr.addstr(i+2,1,f"  - Planet inteled: {PlanetIs['PlanetName']} (+{intel_ball:,} ◭)")
                stdscr.addstr(sz_y-2, 1, f"Total: {intel_balls:,} ◭")
                stdscr.refresh()
                curses.napms(rwos.randint(500,3000))

            PlayerIs['IntelBall'] += intel_balls
            PlayerIs['Statistic']['StarInteled'] += 1
            PlayerIs['XP'] += rwos.randint(IncCoefXP[0],IncCoefXP[1]) * (1 + int((intel_balls)/100))
        
        curses.wrapper(intel_lo)
        pi.StarChange(StarIs['StarID'], "StarIntel", True)

    if choice == "Take control":
        pi.StarChange(StarIs['StarID'], "StarControled", True)
    
    if choice == "Built the station":
        def station_build(stdscr):
            size_y, size_x = stdscr.getmaxyx()
            stat = curses.newwin(5,60,int((size_y-5)/2), int((size_x-60)/2))
            stat_y, stat_x = stat.getmaxyx()
            stat.box()
            stat.addstr(0,int((stat_x-len("Quation"))/2),"Quation")
            stat.addstr(1,1,"The construction of the station will cost 200,000,000 credits, after transactions, the station will be ready instantly.")
            menu = "| [y]-Yes | [n]-No |"
            stat.addstr(stat_y-1, int((stat_x-len(menu))/2), menu)
            key = stat.getkey()
            if key == "y":
                return 1
            
        if PlayerIs['Money'] >= 250_000_000:
            lox = curses.wrapper(station_build)
            if lox == 1:
                PlayerIs['Money'] -= 250_000_000
                PlayerIs['XP'] += random.randint(IncCoefXP[0], IncCoefXP[1]) * 100
                StationStoreList = ItemsDB
                StarCivil = {
                    "CivilPop": 0,
                    "CivilEconomicType": rwos.randint(0, len(Economics)-1),
                    "CivilEco": 1,
                    "CivilReputation": 100,
                    "CivilSecurity": 0,
                    "CivilStable": 5,
                    "CivilUpgrade": [],
                    "CivilStation": {
                        "StationName": "You're station",
                        "StationType": 0,
                        "StationStoreList": random.sample(range(len(StationStoreList)), int(random.randint(1,len(StationStoreList)))),
                        "StationHangar": []
                    }
                }
                pi.StarChange(StarIs['StarID'], 'Star', StarIs['Star'])
                pi.StarChange(StarIs['StarID'], "StarCivil", StarCivil)
                curses.wrapper(lambda stdscr: pi.loading(stdscr, 5, "Building..."))
        else:
            curses.wrapper(lambda stdscr: pi.error_stdscr(stdscr, "Not enough credits!", "Become rich"))

    if choice == "Rename system":
        inp = curses.wrapper(pi.selectscr).decode()
        if inp == "":
            pass
        else:
            pi.StarChange(StarIs['StarID'], 'Star', inp)
    
    if choice == "Make favorite":
        fav = curses.wrapper(pi.selectscr)
        if fav == "":
            pass
        else:
            pi.StarChange(StarIs['StarID'], 'PlayerPinned', True)
            pi.StarChange(StarIs['StarID'], 'PlayerPinnedDesc', fav.decode())
    
    if choice == "Disable favorite":
        pi.StarChange(StarIs['StarID'], 'PlayerPinned', False)

    if choice == "System control menu":
        menu = ["Rename station", "Economic", "Security", "Population"]
        choice = curses.wrapper(lambda stdscr: pi.menuscreen(stdscr, "SCM", menu))

        if choice == "Rename station":
            name = curses.wrapper(pi.selectscr)
            StarIs['StarCivil']['CivilStation']['StationName'] = name.decode()
            pi.StarChange(StarIs['StarID'], 'StarCivil', StarIs['StarCivil'])

if CommandInput == "3":
    def planet(stdscr):
        page = 1
        select = 0
        while True:
            stdscr.clear()
            stdscr.box()
            size_y, size_x = stdscr.getmaxyx()
            curses.start_color()
            max_colors = curses.COLORS
            if max_colors > 8:
                curses.init_pair(103, curses.COLOR_YELLOW, curses.COLOR_BLACK)
            per_page = int((size_y)/(7))
            len_pl = len(StarIs['Planets'])
            pages = int(len_pl / per_page) +1

            start = (page - 1) * per_page + 1
            end = page * per_page

            menu = "| [SP]-Select | [↑]-Up | [↓]-Down | [q]-Quit |"
            stdscr.addstr(0,int((size_x-len("Planets"))/2), "Planets")
            stdscr.addstr(size_y-1, (size_x-len(f"{page}/{pages}")-3), f"{page}/{pages}")
            stdscr.addstr(size_y-1, int((size_x -len(menu))/2), menu)
            for idx, i in enumerate(range(start, end + 1), start=1):
                if i <= len_pl:
                    k = StarIs['Planets'][i-1]
                    if per_page > idx-1:
                        planet = stdscr.derwin(6,((size_x-2)),((idx-1)*6)+1,1)
                        p_y, p_x = planet.getmaxyx()
                        if select == i-1:
                            color = 103
                            planet.attrset(curses.color_pair(color))
                            planet.addstr(0,p_x-50, "SELECTED")
                        else:
                            color = 0
                            planet.attrset(curses.color_pair(color))
                        
                        planet.box()
                        planet.addstr(1,1,f"{k['PlanetName']}:")
                        planet.addstr(2,1,f"    - Class: {PlanetClass['TypeClass'][k['PlanetClass']['TypeClass']]}")
                        planet.addstr(3,1,f"    - Temp: {k['PlanetTemp']:,} °C")
                        planet.addstr(4,1,f"    - Size: {k['PlanetSize']} Earth")
                        planet.attrset(curses.color_pair(color))
                        if k.get("PlanetColony") and k['PlanetColony'] != []:
                            if k['PlanetColony']['ColonyBuild']['Enabled'] == False:
                                planet.addstr(1,p_x-3,"⚑")
                            else:
                                planet.addstr(1,p_x-4,"⚑⏱")
                        planet.refresh()
            
            stdscr.refresh()
            key = stdscr.getkey()

            if key == "q":
                break
            if key == "KEY_UP":
                if select > 0:
                    select -= 1
                if (select) == (i-idx)-1:
                    page -= 1
            if key == "KEY_DOWN":
                if select < len(StarIs['Planets'])-1:
                    select += 1
                if (select) >= (idx*page):
                    page += 1
            if key == "\n":
                PlanetIs = StarIs['Planets'][select]
                #### COLORS ICONS
                max_colors = curses.COLORS
                if max_colors > 8:
                    if PlanetIs['PlanetClass']['TypeClass'] == 0:
                        curses.init_pair(2,curses.COLOR_WHITE, curses.COLOR_GREEN)
                    elif PlanetIs['PlanetClass']['TypeClass'] == 1:
                        curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_YELLOW)
                    elif PlanetIs['PlanetClass']['TypeClass'] == 2:
                        curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_BLUE)
                    elif PlanetIs['PlanetClass']['TypeClass'] == 3:
                        curses.init_pair(2,curses.COLOR_WHITE, curses.COLOR_CYAN)
                    elif PlanetIs['PlanetClass']['TypeClass'] == 4:
                        curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_RED)
                    elif PlanetIs['PlanetClass']['TypeClass'] == 5:
                        curses.init_pair(2,curses.COLOR_WHITE, 101)
                    else:
                        curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_WHITE)
                ####
                planet_is = curses.newwin(30,65, int((size_y-30)/2), int((size_x-65)/2))
                planet_is.box()
                p_y, p_x = planet_is.getmaxyx()
                planet_is.addstr(0, int((p_x-len("Planet"))/2), "Planet")
                planet_is_logo = planet_is.derwin(6,11,1,2)
                planet_is_logo.addstr(1,3, "     ", curses.color_pair(2))
                planet_is_logo.addstr(2,2, "       ", curses.color_pair(2))
                planet_is_logo.addstr(3,2, "       ", curses.color_pair(2))
                planet_is_logo.addstr(4,3, "     ", curses.color_pair(2))
                planet_is_logo.box()
                planet_is.addstr(2,14,f"Planet: {PlanetIs['PlanetName']}")
                planet_is.addstr(3,14,f"Class: {PlanetClass['LiveClass'][PlanetIs['PlanetClass']['LiveClass']]} {PlanetClass['TempClass'][PlanetIs['PlanetClass']['TempClass']]} {PlanetClass['TypeClass'][PlanetIs['PlanetClass']['TypeClass']]}")
                planet_is.addstr(4,14,f"Mass: {PlanetIs['PlanetMass']:,} M🜨")
                planet_is.addstr(5,14,f"Size: {PlanetIs['PlanetSize']} 🜨")
                planet_is.addstr(6,14,f"Temp: {PlanetIs['PlanetTemp']} °C")
                planet_is.addstr(7,2,f"Effective temp: {PlanetIs['PlanetEffectiveTemp']} K")
                planet_is.addstr(8,2,f"Albedo: {(PlanetIs['PlanetAtmoAlbedo']*100):.2f}%")
                planet_is.addstr(9,2,f"Greehouse: {(PlanetIs['PlanetAtmoGreenhouse']*100):.2f}%")
                planet_is.addstr(10,2,f"Distance to star: {PlanetIs['PlanetDistance']:.2f} a.u")
                menu = "| [m]-Menu | [q]-Quit |"
                planet_is.addstr(p_y-1,int((p_x-len(menu))/2), menu)
                if PlanetIs.get("PlanetColony") and PlanetIs['PlanetColony'] != []:
                    colony_is = planet_is.derwin(10,p_x-2,p_y-11,1)
                    colony_is.box()
                    c_y,c_x = colony_is.getmaxyx()
                    colony_is.addstr(0,int((c_x-len("Colony"))/2), "Colony")
                    colony_is.addstr(1,1,f"Colony: {PlanetIs['PlanetColony']['ColonyName']}")
                    colony_is.addstr(2,1,f"Population: {PlanetIs['PlanetColony']['ColonyPop']:,}")
                    colony_is.addstr(3,1,f"Level: {PlanetIs['PlanetColony']['ColonyLevel']}")
                    colony_is.addstr(4,1,f"Buildings: {len(PlanetIs['PlanetColony']['ColonyBuildings'])}")
                    colony_is.addstr(5,1,f"Information: ")
                    colony_is.addstr(6,1,f"     - Max buildings: {PlanetIs['PlanetColony']['ColonyMaxBuildings']}")
                    colony_is.addstr(7,1,f"     - Max popul.: {PlanetIs['PlanetColony']['ColonyMaxPops']:,}")
                    if PlanetIs['PlanetColony']['ColonyBuild']['Enabled'] == True:
                        colony_is.addstr(8,1,f"End building: {wlengine.DateOtherStr(wlengine.DateRead(PlanetIs['PlanetColony']['ColonyBuild']['EndBuild']))}")
                    colony_is.refresh()

                planet_is.refresh()
                keyname = planet_is.getkey()
                if keyname in ["m", "\n"]:
                    if not PlanetIs['PlanetClass']['TypeClass'] == 5:
                        menu = ["Land to surface"]
                    else:
                        menu = ["Collect of gases"]

                    if StarIs.get('StarCivil') and StarIs['StarCivil'] != []:
                        if StarIs.get("StarControled") and StarIs['StarControled'] == True:
                            if not PlanetIs.get("PlanetColony"):
                                menu.append("Build surface colony")
                    
                    choice = pi.menuscreen(stdscr, "Planet menu", menu)

                    if choice == "Build surface colony":
                        pi.message(stdscr, 4,40, "Require", "10 Buildings resources")
                        
                        # Check in inventory player

                        if wl.InvCheak(1,10) != None:
                            DateEnd = wlengine.Date() + timedelta(days=rwos.randint(1,7))
                            PlanetColony = {
                                "ColonyName": "You're colony",
                                "ColonyLevel": 1,
                                "ColonyPop": 100,
                                "ColonyBuildings": [1],
                                "ColonyBuild": {
                                    "Enabled": True,
                                    "EndBuild": wlengine.DateSave(DateEnd)
                                },
                                "ColonyMaxBuildings": 4,
                                "ColonyMaxPops": 50_000
                            }

                            wl.InvRem(1, 10)

                            PlayerIs['XP'] += random.randint(IncCoefXP[0], IncCoefXP[1]) * 3
                            PlanetIs['PlanetColony'] = PlanetColony
                            pi.StarChange(StarIs['StarID'], 'Planets', StarIs['Planets'])
                            break
                        else:
                            pi.error_stdscr(stdscr, "Not find item!", "Check your cargo in ship.")

    if StarIs.get("StarIntel") and StarIs['StarIntel'] == True:
        curses.wrapper(planet)
    else:
        curses.wrapper(lambda stdscr: pi.error_stdscr(stdscr, "System not inteled!", "Research system."))

if CommandInput == "4":
    def station(stdscr):
        while True:
            stdscr.clear()
            stdscr.box()
            sz_y, sz_x = stdscr.getmaxyx()
            stdscr.addstr(0,int((sz_x-len("Station"))/2), "Station")
            menu = "| [m]-Menu | [q]-Quit |"
            stdscr.addstr(sz_y-1, int((sz_x-len(menu))/2), menu)

            part1 = stdscr.derwin((sz_y-2),int((sz_x/3)-1),1,1)
            part1.box()
            part1.addstr(1,1,f"Station: {StarIs['StarCivil']['CivilStation']['StationName']}")
            part1.addstr(2,1,f" - Eco: {StarIs['StarCivil']['CivilEco']}")
            part1.addstr(3,1,f" - Economic: {Economics[StarIs['StarCivil']['CivilEconomicType']]}")
            part1.addstr(4,1,f" - Loc. Reputation: {StarIs['StarCivil']['CivilReputation']}%")

            part2 = stdscr.derwin((sz_y-2),int((sz_x/3)),1,int((sz_x/3)))
            part2.box()
            part2.addstr(1,1,f"Star: {StarIs['Star']}")
            part2.addstr(2,1,f"Population: {StarIs['StarCivil']['CivilPop']:,}")
            part2.addstr(3,1,f"Addition:")
            for i,it in enumerate(StarIs['StarCivil']['CivilUpgrade']):
                part2.addstr(i+4,1,f" - {it}")

            part3 = stdscr.derwin((sz_y-2),int((sz_x/3)-1),1,int((sz_x/3)*2))
            p3_y, p3_x = part3.getmaxyx()
            part3.box()
            part3.addstr(0,int((p3_x-len("Market"))/2), "Market")
            for alli in range(len(StarIs['StarCivil']['CivilStation']['StationStoreList'])):
                ItemIs = StarIs['StarCivil']['CivilStation']['StationStoreList'][alli]
                ItemCoust = int(int(ItemsDB[ItemIs]['ItemCoust']) * StarIs['StarCivil']['CivilEco'])
                part3.addstr(alli+1, 1,f"{ItemsDB[ItemIs]['ItemName'][:int(p3_x/2)]}... - {ItemCoust:,} ©")

            keyname = stdscr.getkey()

            if keyname in ["m", "\n"]:
                menu = [ 
                    "Refuel own ship",
                    "Market",
                    "Hangar",
                    "Shipyard",
                ]

                if "Workshop" in StarIs['StarCivil']['CivilUpgrade']:
                    menu.append("Ship workshop")

                if PlayerIs['IntelBall'] > 0:
                    menu.append("Pass the research")
                
                choice = pi.menuscreen(stdscr, "Station", menu)

                if choice == "Pass the research":
                    pi.message(stdscr, 5,30,"Success", "Intel has passed")
                    PlayerIs['Money'] += (PlayerIs['IntelBall'] * IntelToCredits)
                    PlayerIs['Statistic']['CreditsFromScience'] += (PlayerIs['IntelBall'] * IntelToCredits)
                    PlayerIs['IntelBall'] = 0
                    break

                if choice == "Refuel own ship":
                    FuelNow = PlayerIs['Ship']['Fuel']
                    FuelMaxCapacity = Ships[PlayerIs['Ship']['ShipID']]['ShipMaxFuel'] + NewFuel
                    FuelCoust = (FuelMaxCapacity - FuelNow) * 12
                    if PlayerIs['Ship']['Fuel'] != FuelMaxCapacity:
                        if PlayerIs['Money'] >= FuelCoust:
                            PlayerIs['Ship']['Fuel'] += FuelMaxCapacity - FuelNow
                            PlayerIs['Money'] -= FuelCoust
                            pi.message(stdscr, title="Success", message="Ship refueled")
                    break

                if choice == "Hangar":
                    def main(stdscr):
                        select = 0
                        max_colors = curses.COLORS
                        if max_colors > 8:
                            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
                        while True:
                            stdscr.clear()
                            stdscr.border()
                            sz_y, sz_x = stdscr.getmaxyx()
                            stdscr.addstr(0,int((sz_x-len("Hangar"))/2), "Hangar")
                            stdscr.addstr(1,1, "Ship")
                            stdscr.addstr(1,int(sz_x/4), "Class")
                            stdscr.addstr(1,int(sz_x/2), "Modification")
                            stdscr.addstr(1,int(sz_x-len("Storage"))-2, "Storage")
                            stdscr.hline(2,1, curses.ACS_HLINE, sz_x-2)
                            stdscr.hline(sz_y-3,1, curses.ACS_HLINE, sz_x-2)
                            stdscr.addstr(sz_y-2,1,f"Total: {len(StarIs['StarCivil']['CivilStation']['StationHangar'])}/10")
                            if StarIs['StarCivil']['CivilStation']['StationHangar'] != []:
                                for i, sh in enumerate(StarIs['StarCivil']['CivilStation']['StationHangar']):
                                    shipdb = Ships[sh['ShipID']]
                                    if select == i:
                                        color = 1
                                    else:
                                        color = 0
                                    stdscr.addstr(i+3,1,f"{sh['ShipName'][:int(sz_x/4)-1]}", curses.color_pair(color))
                                    stdscr.addstr(i+3,int(sz_x/4),f"{ShipClasses[shipdb['ShipClass']][:int((sz_x/2)-sz_x/4)]}")
                                    stdscr.addstr(i+3,int(sz_x/2),f"{len(sh['ShipModification'])}")
                                    stdscr.addstr(i+3,int(sz_x-len("Storage")-2), f"{len(sh['Storage'])}")
                            menu = "| [m]-Menu | [q]-Quit |"
                            stdscr.addstr(sz_y-1,int((sz_x-len(menu))/2), menu)
                            keyname = stdscr.getkey()
                            if keyname == "KEY_UP":
                                if select > 0:
                                    select -= 1
                            if keyname == "KEY_DOWN":
                                if select < len(StarIs['StarCivil']['CivilStation']['StationHangar'])-1:
                                    select += 1
                            if keyname in ["m", "\n"]:
                                menu = ["Store ship", "Bring back", "Sell ship"]
                                choice = pi.menuscreen(stdscr, "Hangar", menu)
                                if choice == "Store ship":
                                    if "STARTED_SHIP" in PlayerIs['Ship']['ShipFlags']:
                                        pi.error_stdscr(stdscr, "Error", "Cannot store started ship")
                                        break
                                    else:
                                        StarIs['StarCivil']['CivilStation']['StationHangar'].append(PlayerIs['Ship'])
                                        pi.StarChange(StarIs['StarID'], "StarCivil", StarIs['StarCivil'])
                                        PlayerIs['Ship'] = {
                                            "ShipID": 0,
                                            "ShipName": "Started ship",
                                            "ShipModification": [],
                                            "ShipFlags": ["STARTED_SHIP"],
                                            "Storage": [],
                                            "Fuel": MaxFulling,
                                            "ItemsCount": 0
                                        }
                                        pi.message(stdscr, title="Success", message="Success stored ship.")
                                        break
                                if choice == "Bring back":
                                    if "STARTED_SHIP" in PlayerIs['Ship']['ShipFlags']:
                                        PlayerIs['Ship'] = StarIs['StarCivil']['CivilStation']['StationHangar'][select]
                                        StarIs['StarCivil']['CivilStation']['StationHangar'].pop(select)
                                    else:
                                        temp = PlayerIs['Ship']
                                        PlayerIs['Ship'] = StarIs['StarCivil']['CivilStation']['StationHangar'][select]
                                        StarIs['StarCivil']['CivilStation']['StationHangar'].pop(select)
                                        StarIs['StarCivil']['CivilStation']['StationHangar'].append(temp)
                                    pi.StarChange(StarIs['StarID'], "StarCivil", StarIs['StarCivil'])
                                    pi.message(stdscr, title="Success", message="Success bring back.")
                                    break
                            if keyname == "q":
                                break
                    
                    main(stdscr)
                    break
                
                if choice == "Market":
                    menu = ["Buy", "Sell"]
                    choice = pi.menuscreen(stdscr, "Market", menu)

                    def buy(stdscr):
                        max_colors = curses.COLORS
                        if max_colors > 8:
                            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
                            curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
                        select = 0
                        while True:
                            stdscr.clear()
                            stdscr.box()
                            sz_y, sz_x = stdscr.getmaxyx()
                            stdscr.addstr(0,int((sz_x-len("Market"))/2), "Market")
                            stdscr.addstr(1,2,"Product")
                            stdscr.addstr(1,int(sz_x-len("Buy")-20), "Buy")
                            stdscr.hline(2,1,curses.ACS_HLINE,sz_x-2)
                            balance_str = f"Balance: {PlayerIs['Money']:,} ©"
                            stdscr.addstr(sz_y-2,(sz_x-len(balance_str))-2, balance_str, curses.color_pair(2))
                            menu = "| [ENTER]-Buy | [q]-Quit |"
                            stdscr.addstr(sz_y-1, int((sz_x-len(menu))/2), menu)
                            for i, it in enumerate(StarIs['StarCivil']['CivilStation']['StationStoreList']):
                                item = ItemsDB[it]
                                ItemCoust = int(int(ItemsDB[it]['ItemCoust']) * StarIs['StarCivil']['CivilEco'])
                                if select == i:
                                    color = 1
                                else:
                                    color = 0
                                stdscr.addstr(i+3, 2, item['ItemName'], curses.color_pair(color))
                                stdscr.addstr(i+3, int(sz_x-len("Buy")-20), f"{ItemCoust:,} ©", curses.color_pair(2))

                            keyname = stdscr.getkey()

                            if keyname == "\n":
                                ItemIs = StarIs['StarCivil']['CivilStation']['StationStoreList'][select]
                                count = 1
                                while True:
                                    ItemCoust = (int(int(ItemsDB[ItemIs]['ItemCoust']) * StarIs['StarCivil']['CivilEco'])) * count
                                    buyscr = curses.newwin(8,45, int((sz_y-8)/2), int((sz_x-45)/2))
                                    buyscr.box()
                                    b_y, b_x = buyscr.getmaxyx()
                                    buyscr.addstr(0,int((b_x-len("Buy product"))/2), "Buy product")
                                    buyscr.addstr(1,1,f"Selected: {ItemsDB[ItemIs]['ItemName'][:20]}...")
                                    buyscr.addstr(1,int(b_x-3),"↑")
                                    buyscr.addstr(2,int((b_x-len(str(count)))-2),str(count))
                                    buyscr.addstr(2,1,f"Coust: {ItemCoust:,} ©")
                                    buyscr.addstr(3,1,f"Storage: {ShipTotalItems:,}/{PlayerMaxItems}")
                                    buyscr.addstr(3,int(b_x-3),"↓")

                                    keyname2 = buyscr.getkey()
                                    if keyname2 == "\n":
                                        if PlayerIs['Money'] >= ItemCoust:
                                            pi.loading(stdscr, title="Uploading to storage...")
                                            wl.InvAdd(ItemIs, count)
                                            PlayerIs['Money'] -= ItemCoust
                                            ItemCoustClear = int(ItemsDB[ItemIs]['ItemCoust'])
                                            pi.message(stdscr,title="Success",message="You succesfully buyed.")
                                            StarIs['StarCivil']['CivilEco'] += (1 - (ItemCoustClear/(ItemCoust)))/10
                                            if StarIs['StarCivil']['CivilEco'] < CivilEcoMin:
                                                StarIs['StarCivil']['CivilEco'] = CivilEcoMin
                                            else:
                                                if StarIs['StarCivil']['CivilEco'] > CivilEcoMax:
                                                    StarIs['StarCivil']['CivilEco'] = CivilEcoMax
                                            pi.StarChange(StarIs['StarID'], 'Star', StarIs['Star'])
                                            pi.StarChange(StarIs['StarID'], 'StarCivil', StarIs['StarCivil'])
                                            pi.StarChange(StarIs['StarID'], 'Planets', StarIs['Planets'])
                                            break
                                        else:
                                            pi.error_stdscr(stdscr,"Error", "Not enough money!")
                                    if keyname2 == "A":
                                        if count < PlayerMaxItems-ShipTotalItems:
                                            count += 1
                                    if keyname2 == "B":
                                        if count > 1:
                                            count -= 1
                                    if keyname2 == "e":
                                        try:
                                            count = int(pi.selectscr(stdscr))
                                        except: pass
                                    if keyname2 == "q":
                                        break
                            if keyname == "q":
                                break
                            if keyname == "KEY_UP":
                                if select > 0: select -= 1
                            if keyname == "KEY_DOWN":
                                if select < len(StarIs['StarCivil']['CivilStation']['StationStoreList']) -1: select += 1
                    
                    def sell(stdscr):
                        max_colors = curses.COLORS
                        if max_colors > 8:
                            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
                            curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
                        select = 0
                        while True:
                            stdscr.clear()
                            stdscr.box()
                            sz_y, sz_x = stdscr.getmaxyx()
                            stdscr.addstr(0,int((sz_x-len("Market"))/2), "Market")
                            stdscr.addstr(1,1,"Product")
                            stdscr.addstr(1,int(sz_x-len("Sell")-15), "Sell")
                            stdscr.hline(2,1,curses.ACS_HLINE,sz_x-2)
                            balance_str = f"Balance: {PlayerIs['Money']:,} ©"
                            stdscr.addstr(sz_y-2,(sz_x-len(balance_str))-2, balance_str, curses.color_pair(2))
                            menu = "| [ENTER]-Sell | [q]-Quit |"
                            stdscr.addstr(sz_y-1, int((sz_x-len(menu))/2), menu)
                            for i, it in enumerate(PlayerIs['Ship']['Storage']):
                                item = ItemsDB[it['ItemID']]
                                ItemCoust = int(int(ItemsDB[it['ItemID']]['ItemCoust']) * StarIs['StarCivil']['CivilEco'] * 0.95)
                                if select == i:
                                    color = 1
                                else:
                                    color = 0
                                stdscr.addstr(i+3, 1, item['ItemName'], curses.color_pair(color))
                                stdscr.addstr(i+3, int(sz_x-len("Sell")-15), f"{ItemCoust:,} ©", curses.color_pair(2))

                            keyname = stdscr.getkey()

                            if keyname == "\n":
                                ItemIs = PlayerIs['Ship']['Storage'][select]
                                count = 1
                                while True:
                                    ItemCoust = int(((int(int(ItemsDB[ItemIs['ItemID']]['ItemCoust']) * StarIs['StarCivil']['CivilEco'])) * 0.95) * count)
                                    ItemCoustClear = int(ItemsDB[ItemIs['ItemID']]['ItemCoust'])
                                    buyscr = curses.newwin(8,45, int((sz_y-8)/2), int((sz_x-45)/2))
                                    buyscr.box()
                                    b_y, b_x = buyscr.getmaxyx()
                                    buyscr.addstr(0,int((b_x-len("Sell product"))/2), "Sell product")
                                    buyscr.addstr(1,1,f"Selected: {ItemsDB[ItemIs['ItemID']]['ItemName'][:20]}...")
                                    buyscr.addstr(1,int(b_x-3),"↑")
                                    buyscr.addstr(2,int((b_x-len(str(count)))-2),str(count))
                                    buyscr.addstr(2,1,f"Coust: {ItemCoust:,} ©")
                                    buyscr.addstr(3,1,f"Storage: {ItemIs['ItemCount']:,}")
                                    buyscr.addstr(3,int(b_x-3),"↓")

                                    keyname2 = buyscr.getkey()

                                    if keyname2 == "\n":
                                        try:
                                            wl.InvRem(ItemIs['ItemID'], count)
                                            PlayerIs['Money'] += ItemCoust
                                            PlayerIs['Statistic']['CreditsFromSelled'] += ItemCoust
                                            StarIs['StarCivil']['CivilEco'] -= (1 - (ItemCoustClear/(ItemCoust)))/10
                                            if StarIs['StarCivil']['CivilEco'] < CivilEcoMin:
                                                StarIs['StarCivil']['CivilEco'] = CivilEcoMin
                                            else:
                                                if StarIs['StarCivil']['CivilEco'] > CivilEcoMax:
                                                    StarIs['StarCivil']['CivilEco'] = CivilEcoMax
                                            pi.StarChange(StarIs['StarID'], 'Star', StarIs['Star'])
                                            pi.StarChange(StarIs['StarID'], 'StarCivil', StarIs['StarCivil'])
                                            pi.StarChange(StarIs['StarID'], 'Planets', StarIs['Planets'])
                                            pi.message(stdscr, title="Success", message="You succesfully selled.")
                                            break
                                        except:
                                            pi.error_stdscr(stdscr, "Error", "Not pass this trans.")
                                            break
                                    if keyname2 == "A":
                                        if count < ItemIs['ItemCount']:
                                            count += 1
                                    if keyname2 == "B":
                                        if count > 1:
                                            count -= 1
                                    if keyname2 == "c":
                                        try:
                                            count = int(pi.selectscr(stdscr))
                                        except: pass
                                    if keyname2 == "q":
                                        break
                            if keyname == "q":
                                break
                            if keyname == "KEY_UP":
                                if select > 0: select -= 1
                            if keyname == "KEY_DOWN":
                                if select < len(PlayerIs['Ship']['Storage']) -1: select += 1
                    
                    if choice == "Buy":
                        buy(stdscr)

                    if choice == "Sell":
                        sell(stdscr)
                    break

                if choice == "Shipyard":
                    def main(stdscr):
                        max_colors = curses.COLORS
                        if max_colors > 8:
                            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
                        select = 0
                        while True:
                            stdscr.clear()
                            stdscr.box()
                            sz_y, sz_x = stdscr.getmaxyx()
                            stdscr.addstr(0,int((sz_x-len("Shipyard"))/2), "Shipyard")
                            menu = "| [q]-Quit |"
                            stdscr.addstr(sz_y-1,int((sz_x-len(menu))/2), menu)

                            stdscr.addstr(1,1,"Ship")
                            stdscr.addstr(1,30, "Class")
                            stdscr.addstr(1,50, "Modifi.")
                            stdscr.addstr(1,70, "TD.")
                            stdscr.addstr(1,int((sz_x-len("Coust"))-15), "Coust")

                            stdscr.hline(2,1,curses.ACS_HLINE, sz_x-2)

                            for i, sh in enumerate(Ships):
                                if select == i:
                                    color = 1
                                else:
                                    color = 0
                                
                                stdscr.addstr(i+3, 1, sh['ShipName'], curses.color_pair(color))

                            keyname = stdscr.getkey()

                            if keyname == "\n":
                                ShipIs = Ships[select]
                                Price = int(ShipIs['ShipCoust'] * StarIs['StarCivil']['CivilEco'])
                                sec = curses.newwin(10,40,int((sz_y-10)/2), int((sz_x-40)/2))
                                sec.box()
                                s_y, s_x = sec.getmaxyx()
                                sec.addstr(1,1,f"Selected: {ShipIs['ShipName']}")
                                sec.addstr(2,1,f" - Class: {ShipClasses[ShipIs['ShipClass']]}")
                                sec.addstr(3,1,f" - Travel dist.: {ShipIs['ShipTravelingDist']:,} l.y")
                                sec.addstr(4,1,f" - Max modification: {ShipIs['ShipMaxModification']}")
                                sec.addstr(5,1,f" - Max fuel: {ShipIs['ShipMaxFuel']}")
                                sec.addstr(6,1,f" - Max storage: {ShipIs['ShipMaxItems']}")
                                sec.addstr(8,1,f"Price: {Price:,} ©")
                                sec.addstr(7,1,f"Balance: {PlayerIs['Money']:,} ©")
                                menu = "| [y]-Yes | [n]-No |"
                                sec.addstr(s_y-1,int((s_x-len(menu))/2), menu)
                                if sec.getkey() == "y":
                                    if PlayerIs['Money'] >= Price:
                                        StarIs['StarCivil']['CivilStation']['StationHangar'].append({
                                            "ShipID": ShipIs['ShipID'],
                                            "ShipName": ShipIs['ShipName'],
                                            "ShipModification": [],
                                            "ShipFlags": [],
                                            "Storage": [],
                                            "Fuel": ShipIs['ShipMaxFuel'],
                                            "ItemsCount": 0
                                        })
                                        pi.StarChange(StarIs['StarID'], "StarCivil", StarIs['StarCivil'])
                                        PlayerIs['Money'] -= Price
                                        pi.message(stdscr, title="Success", message="Success buying new ship :D")
                                        break
                                    else:
                                        pi.error_stdscr(stdscr, "Error", "Not enough money!")
                                        break
                            if keyname == "KEY_UP":
                                if select > 0:
                                    select -= 1
                            if keyname == "KEY_DOWN":
                                if select < len(Ships)-1:
                                    select += 1
                            if keyname in ["q", "n"]:
                                break
                    
                    main(stdscr)
                    break
                
                if choice == "Ship workshop":
                    def sec(stdscr):
                        max_colors = curses.COLORS
                        if max_colors > 8:
                            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
                        select = 0
                        while True:
                            stdscr.clear()
                            stdscr.box()
                            sz_y, sz_x = stdscr.getmaxyx()
                            stdscr.addstr(0,int((sz_x-len("Workshop"))/2), "Workshop")
                            stdscr.hline(2,1,curses.ACS_HLINE,sz_x-2)
                            stdscr.addstr(1,5,"Modification")
                            stdscr.addstr(1,40,"Level")
                            for i,cell in enumerate(PlayerIs['Ship']['ShipModification']):
                                LevelStar = ModLevelSym * cell['ModificationLevel']
                                LevelStarEmpty = ModLevelEmptySym * (ModMaxLevel - cell['ModificationLevel'])
                                LevelStars = LevelStar + LevelStarEmpty
                                if select == i:
                                    color = 1
                                else:
                                    color = 0
                                if cell['ModificationID'] == None:
                                    stdscr.addstr(i+3,1,"Empty", curses.color_pair(color))
                                else:
                                    stdscr.addstr(i+3,1,f"{ShipModifications[cell['ModificationID']]['ModName']}", curses.color_pair(color))
                                    stdscr.addstr(i+3,40,LevelStars)

                            keyname = stdscr.getkey()

                            if keyname == "\n":
                                do_menu = ["Replace/Place modification", "Upgrade cell"]
                                do = pi.menuscreen(stdscr, "Mods", do_menu)

                                if do == "Replace/Place modification":
                                    menu_cat = []
                                    for i, sh in enumerate(ModificationType):
                                        menu_cat.append(sh)
                                    choice = pi.menuscreen(stdscr, "Mods", menu_cat)

                                    menu = []
                                    for i, mod in enumerate(ShipModifications):
                                        if ModificationType[mod['ModType']] == choice:
                                            menu.append(mod['ModName'])
                                    choice2 = pi.menuscreen(stdscr, "Mods", menu)

                                    ModIndex = None
                                    for i, mod in enumerate(ShipModifications):
                                        if choice2 == ShipModifications[i]['ModName']:
                                            ModIndex = i
                                            break

                                    ModIs = ShipModifications[ModIndex]
                                    selected = curses.newwin(10,50,int((sz_y-10)/2), int((sz_x-50)/2))
                                    selected.box()
                                    sel_y, sel_x = selected.getmaxyx()
                                    selected.addstr(0,int((sel_x-len("Modification"))/2), "Modification")
                                    selected.addstr(1,1,f"Selected: {ModIs['ModName']}")
                                    Price = int((ModIs['ModCoust']) * StarIs['StarCivil']['CivilEco'])
                                    selected.addstr(2,1,f"Type: {ModificationType[ModIs['ModType']]}")
                                    selected.addstr(3,1,f"Value: {ModIs['ModValue']}")
                                    selected.addstr(7,1,f"Balance: {PlayerIs['Money']:,} ©")
                                    selected.addstr(8,1,f"Price: {Price:,} ©")
                                    menu = "| [y]-Yes | [n]-No |"
                                    selected.addstr(sel_y-1, int((sel_x-len(menu))/2), menu)

                                    choice3 = selected.getkey()
                                    
                                    if choice3 == "y":
                                        if PlayerIs['Money'] >= Price:
                                            PlayerIs['Ship']['ShipModification'][select]['ModificationID'] = ModIs['ModID']
                                            PlayerIs['Ship']['ShipModification'][select]['ModificationLevel'] = 0
                                            pi.loading(stdscr, title="Installation...")
                                            pi.message(stdscr,title="Success",message="Done.")
                                        else:
                                            pi.error_stdscr(stdscr, "Error", "Not enough money!")

                                if do == "Upgrade cell":
                                    CellIs = PlayerIs['Ship']['ShipModification'][select]                
                                    CellLevelTemp = CellIs['ModificationLevel']
                                    select2 = CellLevelTemp
                                    if CellIs['ModificationID'] == None:
                                        pi.error_stdscr(stdscr, "Error", "Cell not found!")
                                    else:
                                        while True:
                                            CellLevel = select2
                                            Price = int(ShipModifications[CellIs['ModificationID']]['ModCoust'] * (ModLevelCoeff * select2 * (1 + StarIs['StarCivil']['CivilEco'])))
                                            upgr = curses.newwin(10,45,int((sz_y-10)/2), int((sz_x-45)/2))
                                            upgr.box()
                                            u_y, u_x = upgr.getmaxyx()
                                            upgr.addstr(0,int((u_x-len("Upgrade"))/2), "Upgrade")
                                            upgr.addstr(1,int((u_x-len(ShipModifications[CellIs['ModificationID']]['ModName']))/2),f"{ShipModifications[CellIs['ModificationID']]['ModName']}")
                                            upgr.addstr(2,int((u_x-len(f"Price: {Price:,} ©"))/2), f"Price: {Price:,} ©")
                                            upgr.addstr(4,int((u_x-1)/2), "↑")
                                            upgr.addstr(5,int((u_x-1)/2), str(CellLevel))
                                            upgr.addstr(6,int((u_x-1)/2), "↓")
                                            upgr.addstr(8,int((u_x-len(f"Balance: {PlayerIs['Money']:,} ©"))/2),f"Balance: {PlayerIs['Money']:,} ©")
                                            keyname2 = upgr.getkey()
                                            if keyname2 == "\n":
                                                if select2 == CellLevelTemp:
                                                    break
                                                if PlayerIs['Money'] >= Price:
                                                    PlayerIs['Ship']['ShipModification'][select]['ModificationLevel'] = CellLevel
                                                    PlayerIs['Money'] -= Price
                                                    pi.loading(stdscr, title="Upgrading...")
                                                    pi.message(stdscr, title="Success", message="Modif. has been updated!")
                                                    break
                                                else:
                                                    pi.error_stdscr(stdscr, "Error", "Not enough money!")
                                                    break
                                            if keyname2 == "A":
                                                if select2 < ModMaxLevel:
                                                    select2 += 1
                                            if keyname2 == "B":
                                                if select2 > CellLevelTemp:
                                                    select2 -= 1
                                            if keyname2 == "q":
                                                break

                            if keyname == "q":
                                break
                            if keyname == "KEY_UP":
                                if select > 0:
                                    select -= 1
                            if keyname == "KEY_DOWN":
                                if select < len(PlayerIs['Ship']['ShipModification'])-1:
                                    select += 1
                    
                    sec(stdscr)
                    break

            if keyname == "q":
                break
    
    if StarIs.get("StarCivil") and StarIs['StarCivil'] != []:
        curses.wrapper(station)
    else:
        curses.wrapper(lambda stdscr: pi.error_stdscr(stdscr, "Invalid civilisation!", "In star system not find civ."))

if CommandInput == "5":
    menu = ["My ship", "Favorite system"]

    other = curses.wrapper(lambda stdscr: pi.menuscreen(stdscr, "Other", menu))
    
    if other == "My ship":
        def ship_stdscr(stdscr):
            size_y, size_x = stdscr.getmaxyx()
            ship = curses.newwin(30,70,int((size_y-30)/2),int((size_x-70)/2))
            ship.box()
            sh_y, sh_x = ship.getmaxyx()
            ship.addstr(0,int((sh_x-len("Ship"))/2), "Ship")
            s_icon = ship.derwin(7,14,1,2)
            s_icon.addstr(1,4, "█    █")
            s_icon.addstr(2,3, "██    ██")
            s_icon.addstr(3,3, "███  ███")
            s_icon.addstr(4,3, "████████")
            s_icon.addstr(5,4, "██████  ")
            s_icon.box()
            ship.addstr(2,17, f"Ship: {PlayerIs['Ship']['ShipName']} | [{Ships[PlayerIs['Ship']['ShipID']]['ShipName']}]")
            ship.addstr(3,17, f"Class: {ShipClasses[Ships[PlayerIs['Ship']['ShipID']]['ShipClass']]}")
            ship.addstr(4,17, f"Health: {PlayerShipHP:,} HP")
            ship.addstr(5,17, f"Damage: {PlayerShipDMG:,} DM")
            ship.addstr(6,17, f"IIB: {PlayerShipInterval:,}")
            ship.addstr(7,17, f"Cargo cap.: {PlayerMaxItems:,} (+{PlayerMaxItems-Ships[PlayerIs['Ship']['ShipID']]['ShipMaxItems']})")
            ship.addstr(8,2, f"Max warp distance: {Ships[PlayerIs['Ship']['ShipID']]['ShipTravelingDist']} (+{TravelDistation-Ships[PlayerIs['Ship']['ShipID']]['ShipTravelingDist']})")
            ship.addstr(9,2, f"Max fuel: {Ships[PlayerIs['Ship']['ShipID']]['ShipMaxFuel']} (+{FuelMaxCapacity-Ships[PlayerIs['Ship']['ShipID']]['ShipMaxFuel']})")
            modif_sh = ship.derwin(sh_y-11,sh_x-2, 10, 1)
            modif_sh.box()
            modif_sh_y, modif_sh_x = modif_sh.getmaxyx()
            modif_sh.addstr(0, int((modif_sh_x-len("Modifications"))/2), "Modifications")
            for abs in range(MaxShipModification):
                SlotIs = PlayerIs['Ship']['ShipModification'][abs]
                if SlotIs['ModificationID'] != None:
                    ModIs = ShipModifications[SlotIs['ModificationID']]
                    LevelStar = ModLevelSym * SlotIs['ModificationLevel']
                    LevelStarEmpty = ModLevelEmptySym * (ModMaxLevel - SlotIs['ModificationLevel'])
                    LevelStars = LevelStar + LevelStarEmpty
                    modif_sh.addstr(abs+1,1,f" - Module: {ModIs['ModName']} | Level: [{LevelStars}]")
                else:
                    modif_sh.addstr(abs+1,1," - Empty")
            total = 0
            for i,mod in enumerate(PlayerIs['Ship']['ShipModification']):
                if mod['ModificationID'] != None:
                    total += 1
            total_str = f"{total}/{MaxShipModification}"
            modif_sh.addstr(1,int((modif_sh_x-len(total_str))-1), total_str)
            menu = "| [m]-Menu |"
            ship.addstr(sh_y-1, int((sh_x-len(menu))/2), menu)
            ship.refresh()
            keyname = modif_sh.getkey()

            if keyname in ["m", "\n"]:
                menu = ["Cargo", "Rename ship"]
                choice = pi.menuscreen(stdscr, "Ship Menu", menu)

                if choice == "Rename ship":
                    name = pi.selectscr(stdscr).decode()
                    PlayerIs['Ship']['ShipName'] = name
                
                if choice == "Cargo":
                    choice = pi.ship_cargo(stdscr)
                    if choice == 0:
                        pi.loading(stdscr, title="Refueling...", t=5)
                        PlayerIs['Ship']['Fuel'] = FuelMaxCapacity
                        wl.InvRem(0, 1)
        
        curses.wrapper(ship_stdscr)

        # wl.Skip()
        # wl.InfoText(title="Корабель")
        # print(f"Ваш корабель: {PlayerIs['Ship']['ShipName']}")
        # print(f"    ▪ Клас: {ShipClasses[Ships[PlayerIs['Ship']['ShipID']]['ShipClass']]}")
        # print(f"    ▪ Міцність: {PlayerShipHP:,} HP")
        # print(f"    ▪ Урон: {PlayerShipDMG:,} DM")
        # print(f"    ▪ Інтервалів: {PlayerShipInterval:,}")
        # print(f"    ▪ Макс. місткість: {PlayerMaxItems:,} (+{PlayerMaxItems-Ships[PlayerIs['Ship']['ShipID']]['ShipMaxItems']})")
        # print(f"    ▪ Макс. дистанція стрибка: {Ships[PlayerIs['Ship']['ShipID']]['ShipTravelingDist']} (+{TravelDistation-Ships[PlayerIs['Ship']['ShipID']]['ShipTravelingDist']})")
        # print(f"    ▪ Макс. палива: {Ships[PlayerIs['Ship']['ShipID']]['ShipMaxFuel']} (+{FuelMaxCapacity-Ships[PlayerIs['Ship']['ShipID']]['ShipMaxFuel']})")
        # print(f"    ▪ Модифікації:")
        # ModificationSlots(3)
        # print()
        # ShipList = ["Переіменувати корабель", "Сховище корабля",]

        # ShipCom = wl.ChoiceMenu(ShipList)

        # if ShipCom == "Сховище корабля":
        #     wl.Skip()
        #     wl.InfoText(title="Сховище корабля")
        #     print(wl.Wall)
        #     for alli in range(len(PlayerIs['Ship']['Storage'])):
        #         ItemIs = PlayerIs['Ship']['Storage'][alli]
        #         print(f"{alli+1}. {ItemsDB[ItemIs['ItemID']]['ItemName']} ▪ Тип: {ItemsType[ItemsDB[ItemIs['ItemID']]['ItemType']]} ▪ Кількість: {ItemIs['ItemCount']:,}")
        #     if len(PlayerIs['Ship']['Storage']) == 0:
        #         wl.TextColore("Сховище порожнє", Colore.Gray)
        #     print(wl.Wall)
        #     for i in range( int((ConsoleSizeY/2) - ((3+len(PlayerIs['Ship']['Storage']))/2)) ):
        #         print()

        #     try:
        #         ItemChoice = int(input("Вибрати: ")) - 1
        #     except (TypeError, ValueError):
        #         exit()

        #     if ItemChoice+1 > len(PlayerIs['Ship']['Storage']) and ItemChoice+1 <= 0:
        #         wl.Error("Недопустиме введення")
        #     else:
        #         ItemIs = PlayerIs['Ship']['Storage'][ItemChoice]
        #         if ItemsDB[ItemIs['ItemID']]['ItemName'] == ItemsDB[0]['ItemName']:
        #                 if ItemsDB[ItemIs['ItemID']]['ItemType'] == 0:
        #                     PlayerIs['Ship']['Fuel'] += 5
        #                     if PlayerIs['Ship']['Fuel'] > FuelMaxCapacity: 
        #                         PlayerIs['Ship']['Fuel'] = FuelMaxCapacity
        #                     wl.Loading("Заправлення", 3)
        #                     wl.InvRem(0, 1)
        #                     # ID OF FUEL: 0

        # if ShipCom == "Переіменувати корабель":
        #     wl.Skip()
        #     NewName = input("Введіть нову назву кораблю: ")
        #     if NewName == "" or NewName == " ": exit()
        #     PlayerIs['Ship']['ShipName'] = NewName
        #     wl.Loading("Застосовуємо зміни", 1)

# Перезавантажує гру, не зберігає процеси
if CommandInput == "*":
    exit()

# Командна строка для ведення кодів чи команд
if DebugInfo == True and CommandInput == "/":
    wl.Skip()
    debug = exec(input("/"))
    if debug == "":
        exit()
    input("Нажміть ENTER щоб продовжити")

if wlengine.DateCheck(wlengine.PlayerDate):
    NewPlayerDate = wlengine.Date() + timedelta(days=1)
    days = wlengine.DiffDate(wlengine.PlayerDate)
    PlayerIs['NextDate'] = wlengine.DateSave(NewPlayerDate)
    for i in range(days):
        pi.Logic()

# Збереження прогресу через функцію SaveJSON із WhiteEngine
wl.SaveJSON(SavePath, save)
