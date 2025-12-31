import random
import settings
import wlregister
import math
import json
#from galaxy.mapchanges import CustomStars
from galaxy.mapchanges_lock import CustomStarsLock
from nickname_generator import generate as ranname

with open(settings.MapPath, 'r', encoding="utf-8") as t:
    CustomStars = json.load(t)

mapseed = settings.MapSeed

Latters = [chr(i) for i in range(65, 91)]
LowerLatters = [chr(i) for i in range(97, 123)]
Articl = ["Alpha", "Beta", "Gamma", "Delta"]

def GenMap(seed):
    random.seed(mapseed + seed)
    
    def PlanetGen(x):
        Planets = []

        for gen in range(x):
            gen += 1
            planet_number = gen
            planet_name = f"{solar_name}-{planet_number}"
            planet_range = random.randint(1,100)

            planet_atmo_albedo = random.uniform(0,1)
            planet_atmo_greenhouse = random.uniform(0,1)

            #planet_distance = random.uniform(1e+11*planet_number, 2e+11*planet_number) * planet_number
            planet_distance = random.uniform(1e+11*(planet_number * 0.4), 2e+11*(planet_number * 0.4)) * planet_number
            planet_ao = planet_distance / (1.496e+11)
            planet_effective_temp = ((solar_luminos * 1e+5)/ (16 * math.pi * 5.67e-8 * (planet_ao**2))) ** (1/4)
            planet_kelvin_temp = planet_effective_temp * ((1 + (planet_atmo_greenhouse + planet_atmo_albedo)) ** (1/4))
            planet_temp = planet_kelvin_temp - 273.15

            planet_mass = random.uniform(0.1,44)
            planet_size = random.choice(
                [
                    random.uniform(0.1,0.5), 
                    random.uniform(0.5,1),
                    random.uniform(1,5),
                    random.uniform(5,10),
                    random.uniform(10,50)
                ]
            )
            planet_colore = random.randint(0,7)
            planet_living_coef = random.randint(1,100)

            # Default classification
            planet_class_live = 2
            planet_class_unique = 0
            
            # Classification of temperature
            if planet_temp >= -273.15:
                planet_class_temp = 6
            if planet_temp >= -100:
                planet_class_temp = 5
            if planet_temp >= -50:
                planet_class_temp = 4
            if planet_temp >= -10:
                planet_class_temp = 3
            if planet_temp >= 30:
                planet_class_temp = 2
            if planet_temp >= 100:
                planet_class_temp = 1
            if planet_temp >= 300:
                planet_class_temp = 0

            # Classification of type
            planet_class_type = random.randint(0, 4)
            
            if planet_size >= 11:
                planet_class_type = 5

            planet_live = False
            if random.randint(1,100) <= 5:
                if planet_class_type in [0,1,2,3,4]:
                    if planet_temp >= -20 and planet_temp <= 40:
                        planet_live = True
                        planet_class_live = 0
                        planet_class_unique = 1
                    else:
                        planet_live = False
                else:
                    planet_class_live = 2
                    planet_class_unique = 0
                
            planet_terraform_confirm = False
            if random.randint(1,100) <= 20:
                if planet_class_type in [0,1,2,3,4]:
                    if planet_living_coef >= 50 and planet_live == False:
                        planet_terraform_confirm = True
                        planet_class_live = 1

            planet_rings = False
            if random.randint(1,6) == 1:
                planet_rings = True
    
            planet_class = {
                    "TypeClass": planet_class_type,
                    "TempClass": planet_class_temp,
                    "LiveClass": planet_class_live,
                    "UniqueClass": planet_class_unique
                }

            Planets.append(
                {
                    "PlanetID": gen,
                    "PlanetName": planet_name,
                    "PlanetClass": planet_class,
                    "PlanetEffectiveTemp": planet_effective_temp,
                    "PlanetKelvinTemp": planet_kelvin_temp,
                    "PlanetSize": planet_size,
                    "PlanetColore": planet_colore,
                    "PlanetTemp": planet_temp,
                    "PlanetMass": planet_mass,
                    "PlanetAtmoAlbedo": planet_atmo_albedo,
                    "PlanetAtmoGreenhouse": planet_atmo_greenhouse,
                    "PlanetDistance": planet_ao,
                    "PlanetTerraform": planet_terraform_confirm,
                    "PlanetRings": planet_rings,
                    "PlanetLive": planet_live,
                    "PlanetViewSeed": int(random.random())
                }
            )
        return Planets
    
    solar_name = f"{random.choice(Articl)} {abs(seed)}-{abs(int(seed/20))}-{random.choice(Latters)}{random.randint(1,999)}"

    standart_solar_class = ["O", "B", "A", "F", "G", "K", "M", "L", "T"]
    exotic_solar_class = ["NS","BH"]

    if random.randint(1,20) == 1:
        solar_class = random.choice(exotic_solar_class)
    else:
        solar_class = random.choice(standart_solar_class)

    if solar_class == "O":
        solar_size = random.uniform(6.6,15)
        solar_mass = random.uniform(16,120)
        solar_temp = random.randint(30_000, 50_000)
        solar_luminos = random.uniform(100,10e+6)
    if solar_class == "B":
        solar_size = random.uniform(3.2,6.6)
        solar_mass = random.uniform(2.1,16)
        solar_temp = random.randint(10_000, 30_000)
        solar_luminos = random.uniform(10,1000)
    if solar_class == "A":
        solar_size = random.uniform(1.8,3.2)
        solar_mass = random.uniform(1.4,2.1)
        solar_temp = random.randint(7_500, 10_000)
        solar_luminos = random.uniform(1,100)
    if solar_class == "F":
        solar_size = random.uniform(1.2,1.8)
        solar_mass = random.uniform(1.04,1.4)
        solar_temp = random.randint(6_000, 7_500)
        solar_luminos = random.uniform(0.1,10)
    if solar_class == "G":
        solar_size = random.uniform(0.96,1.2)
        solar_mass = random.uniform(0.8,1.04)
        solar_temp = random.randint(5_200, 6_000)
        solar_luminos = random.uniform(0.05, 5)
    if solar_class == "K":
        solar_size = random.uniform(0.7,0.96)
        solar_mass = random.uniform(0.45,0.8)
        solar_temp = random.randint(3_700, 5_200)
        solar_luminos = random.uniform(0.01, 2)
    if solar_class == "M":
        solar_size = random.uniform(0.1,0.7)
        solar_mass = random.uniform(0.08,0.45)
        solar_temp = random.randint(2_400, 3_700)
        solar_luminos = random.uniform(1e-3, 0.1)
    if solar_class == "L":
        solar_size = random.uniform(0.05,0.1)
        solar_mass = random.uniform(0.01,0.08)
        solar_temp = random.randint(1_000, 2_400)
        solar_luminos = random.uniform(1e-4, 1e-2)
    if solar_class == "T":
        solar_size = random.uniform(0.01,0.05)
        solar_mass = random.uniform(0.001,0.01)
        solar_temp = random.randint(500,1_000)
        solar_luminos = random.uniform(1e-5, 1e-3)
    if solar_class == "NS":
        solar_size = random.uniform(0.001,0.05)
        solar_mass = random.uniform(10, 25)
        solar_temp = random.randint(1_000_000,10_000_000)
        solar_luminos = random.uniform(0.001, 0.1)
    if solar_class == "BH":
        solar_size = random.uniform(20,500)
        solar_mass = random.uniform(1_000,500_000)
        solar_temp = random.randint(0,0)
        solar_luminos = 1e-36
    
    if solar_luminos > 1000:
        planet_count = 0
    else:
        planet_count = random.randint(1,15)

    asteroid = []
    if random.randint(1,100) <= 20:
        for i in range(random.randint(1,8)):
            asteroid_name = f"{solar_name} Ast.Belt {ranname()}"
            asteroid_type = random.randint(0,len(wlregister.AsteroidsType))
            asteroid_rate = float(random.uniform(0.01,1))
            asteroid_mass = random.randint(5000,20000) * asteroid_rate 

            asteroid_table = {
                "AsteroidName": asteroid_name,
                "AsteroidType": asteroid_type,
                "AsteroidRate": asteroid_rate,
                "AsteroidMass": asteroid_mass
            }

            asteroid.append(asteroid_table)

    Starsystems = {
        "StarID": seed,
        "Star": solar_name,
        "Class": solar_class,
        "Temp": solar_temp,
        "Mass": solar_mass,
        "Size": solar_size,
        "Luminos": solar_luminos,
        "Planets": PlanetGen(planet_count),
        "Asteroids": asteroid
    }

    # Генератор колонії
    if random.randint(1,100) <= settings.MapCivilRange and Starsystems.get('Planets'):
        Economic = random.choice(wlregister.Economics)
        
        # Генерація списка товарів
        StationStoreList = []
        if Economic == wlregister.Economics[1]:
            StationStoreList = [item for item in wlregister.ItemsDB if item['ItemEconomicType'] == 1]
        else:
            StationStoreList = wlregister.ItemsDB

        Starsystems['StarIntel'] = True
        Starsystems['StarCivil'] = {}

        for i, planet in enumerate(Starsystems['Planets']):
            if random.randint(1,100) <= settings.PlanetColonyRange:
                planet['PlanetColony'] = {}
                planet['PlanetColony']['ColonyName'] = ranname() + " Colony"
                planet['PlanetColony']['ColonyLevel'] = random.randint(1,100)
                planet['PlanetColony']['ColonyPop'] = random.choice(
                                    [random.randint(100,1000), random.randint(1000,100000),
                                     random.randint(100000,1000000), random.randint(1000000,100000000)])
                planet['PlanetColony']['ColonyBuildings'] = [1]
                planet['PlanetColony']['ColonyBuild'] = {"Enabled": False, "EndBuild": 0}
                planet['PlanetColony']['ColonyMaxBuildings'] = random.randint(1,settings.MaxColonyBuildings)
                planet['PlanetColony']['ColonyMaxPops'] = 50000

        Pops = 0
        for i, planet in enumerate(Starsystems['Planets']):
            if planet.get("PlanetColony"):
                Pops += planet['PlanetColony']['ColonyPop']
        Starsystems['StarCivil']['CivilPop'] = Pops

        if Pops >= 0:
            CivilSecurity = 0
            CivilStable = random.randint(0,40)

        if Pops >= 100_000_000:
            CivilSecurity = 1
            CivilStable = random.randint(40,90)

        if Pops >= 1_000_000_000:
            CivilSecurity = 2
            CivilStable = random.randint(90,100)

        CivilUpgrade = []
        for i in range(3):
            elementChoice = random.choice(["","Workshop", "Fleet_Shipyard", "Cruiser_Shipyard"])
            CivilUpgrade.append(elementChoice)
        
        Starsystems['StarCivil']['CivilEconomicType'] = random.randint(0, len(wlregister.Economics)-1)
        Starsystems['StarCivil']['CivilEco'] = random.uniform(settings.CivilEcoMin,settings.CivilEcoMax)
        Starsystems['StarCivil']['CivilReputation'] = 50
        Starsystems['StarCivil']['CivilSecurity'] = CivilSecurity
        Starsystems['StarCivil']['CivilStable'] = CivilStable
        Starsystems['StarCivil']['CivilUpgrade'] = CivilUpgrade
        Starsystems['StarCivil']['CivilStation'] = {
            "StationName": f"{ranname()} Station",
            "StationType": random.randint(0,2),
            "StationStoreList": random.sample(range(len(StationStoreList)), int(random.randint(1,len(StationStoreList)))),
            "StationHangar": []
        }

        # Перевіряємо, чи є в цій системі населення?
        if Pops == 0:
            Starsystems.pop('StarCivil')
            Starsystems.pop('StarIntel')
        else:
            Starsystems['Star'] = ranname()

    # Імпорт всіх змін, тепер з заблокованного mapchanges_lock.py
    for abis in range(len(CustomStarsLock)):
        CustomStarsIs = CustomStarsLock[abis]
        if Starsystems['StarID'] == CustomStarsIs['StarID']:
            Starsystems.update(CustomStarsIs)
    
    # Імпорт всіх змін із mapchanges.py
    for abis in range(len(CustomStars)):
        CustomStarsIs = CustomStars[abis]
        if Starsystems['StarID'] == CustomStarsIs['StarID']:
            Starsystems.update(CustomStarsIs)

    return Starsystems
