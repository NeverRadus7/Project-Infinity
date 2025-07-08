import random
import settings
import wlregister
import math
from galaxy.mapchanges import CustomStars
from galaxy.mapchanges_lock import CustomStarsLock
from nickname_generator import generate as ranname

mapseed = settings.MapSeed

Latters = [chr(i) for i in range(65, 91)]
LowerLatters = [chr(i) for i in range(97, 123)]
Articl = ["Alpha","Beta","Gamma","Delta"]

FractionSuffix = ["Liga", "Party", "Organisation", "Company", "Empire", "Clan", "Group", "Brotherhood"]

def GenMap(seed):
    random.seed(mapseed + seed)
    def FractionGen():
        FractionName = f"{ranname()} {random.choice(FractionSuffix)}"
        FractionRep = 0
        FractionEcoType = 0
        FractionPolType = 0
        FractionPop = 0
        procentrange = random.randint(0,100)
        if procentrange <= 100:
            FractionPop = random.randint(100,1000)
        if procentrange <= 75:
            FractionPop = random.randint(1000,10000)
        if procentrange <= 30:
            FractionPop = random.randint(10000,100000)
        if procentrange <= 15:
            FractionPop = random.randint(100000,1000000)
        if procentrange <= 5:
            FractionPop = random.randint(1_000_000, 10_000_000_000_000)
        FractionIs = {
            "FractionName": FractionName,
            "FractionRep": FractionRep,
            "FractionEcoType": FractionEcoType,
            "FractionPolType": FractionPolType,
            "FractionPop": FractionPop,
            "FractionPopHap": 50
        }
        return FractionIs
    
    def PlanetGen(x):
        Planets = []
        for gen in range(x):
            gen += 1
            planet_number = gen
            planet_name = f"{solar_name}-{planet_number}"
            planet_range = random.randint(1,100)

            if planet_range <= 100:
                planet_class = random.choice([0,1,2,5])
            if planet_range <= 30:
                planet_class = 3
            if planet_range <= 5:
                planet_class = 4

            if planet_class == 0:
                planet_mass = random.uniform(0.6,5)
            elif planet_class == 1:
                planet_mass = random.uniform(0.6,5)
            elif planet_class == 2:
                planet_mass = random.uniform(0.5,4)
            elif planet_class == 3:
                planet_mass = random.uniform(9,18)
            elif planet_class == 4:
                planet_mass = random.uniform(0.8,1.5)
            elif planet_class == 5:
                planet_mass = random.uniform(0.8,1.5)
            elif planet_class == 6:
                planet_mass = random.uniform(0.6,2)
            elif planet_class == 7:
                planet_mass = random.uniform(0.6,5)

            planet_atmo_albedo = random.uniform(0,1)
            planet_atmo_greenhouse = random.uniform(0,1)

            planet_distance = random.uniform(1e+11*planet_number, 2e+11*planet_number) * planet_number
            planet_ao = planet_distance / (1.496e+11)
            planet_effective_temp = ((solar_luminos * 1e+4)/ (16 * math.pi * 5.67e-8 * (planet_ao**2))) ** (1/4)
            planet_kelvin_temp = planet_effective_temp * ((1 + (planet_atmo_greenhouse + planet_atmo_albedo)) ** (1/4))
            planet_temp = planet_kelvin_temp - 273.15

            planet_live = False
            if random.randint(1,4) == 1:
                if planet_temp >= -8 and planet_temp <= 25:
                    planet_live = True
                else:
                    pass
                
            planet_terraform_confirm = False
            if planet_class == 4 and planet_live == False:
                if planet_temp >= -30 and planet_temp <= 50:
                    planet_terraform_confirm = True
                else:
                    pass
    
            Planets.append(
                {
                    "PlanetID": gen,
                    "PlanetName": planet_name,
                    "PlanetClass": planet_class,
                    "PlanetEffectiveTemp": planet_effective_temp,
                    "PlanetKelvinTemp": planet_kelvin_temp,
                    "PlanetTemp": planet_temp,
                    "PlanetMass": planet_mass,
                    "PlanetAtmoAlbedo": planet_atmo_albedo,
                    "PlanetAtmoGreenhouse": planet_atmo_greenhouse,
                    "PlanetDistance": planet_ao,
                    "PlanetTerraform": planet_terraform_confirm,
                    "PlanetLive": planet_live
                }
            )
        return Planets
    
    solar_name = f"{random.choice(Articl)} {abs(seed)}-{abs(int(seed/20))}-{random.choice(Latters)}{random.randint(1,999)}"

    standart_solar_class = ["O", "B", "A", "F", "G", "K", "M", "L", "T", "NS", "BH"]
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
    solar_sisters = []
    if random.randint(1,8) == 1:
        solar_sisters = []
        other_random = random.Random()
        for i in range(random.randint(1,3)):
            other_random.seed(0x0BA7643 + seed + i)
            solar_class_sis = other_random.choice(["O", "B", "A", "F", "G", "K", "M", "L", "T", "NS", "BH"])
            solar_sisters.append({
                "Star": solar_name + " " + Latters[i+1],
                "Class": solar_class_sis,
                "Temp": solar_temp,
                "Mass": solar_mass,
                "Size": solar_size,
                "Luminos": solar_luminos
            })
        solar_name = f"{solar_name} A"
    
    if solar_luminos > 1000:
        planet_count = 0
    else: planet_count = random.randint(1,15)

    Starsystems = {
        "StarID": seed,
        "Star": solar_name,
        "StarSister": solar_sisters,
        "Class": solar_class,
        "Temp": solar_temp,
        "Mass": solar_mass,
        "Size": solar_size,
        "Luminos": solar_luminos,
        "Planets": PlanetGen(planet_count),
        "MapPosition": random.randint(1,3780)
    }

    # Генератор колонії
    if random.randint(1,100) <= settings.MapCivilRange:
        Economic = random.choice(wlregister.Economics)
        
        # Генерація списка товарів
        StationStoreList = []
        if Economic == wlregister.Economics[1]:
            StationStoreList = [item for item in wlregister.ItemsDB if item['ItemEconomicType'] == 1]
        else:
            StationStoreList = wlregister.ItemsDB

        for i in range(len(Starsystems['Planets'])):
            PlanetIs = Starsystems['Planets'][i]
            if PlanetIs['PlanetLive'] == True:
                Starsystems['Star'] = ranname()
                break
                
            
        Starsystems['StarIntel'] = True
        Starsystems['StarCivil'] = {}
        Starsystems['StarCivil']['CivilEconomicType'] = random.randint(0, len(wlregister.Economics))
        Starsystems['StarCivil']['CivilEco'] = random.uniform(settings.CivilEcoMin,settings.CivilEcoMax)
        Starsystems['StarCivil']['CivilStation'] = {
            "StationName": f"{ranname()} Station",
            "StationType": random.randint(0,2),
            "StationStoreList": random.sample(range(len(StationStoreList)), random.randint(1,1)) 
        }
        Starsystems['StarCivil']['CivilFraction'] = FractionGen()
    
    # Імпорт всіх змін із mapchanges.py
    for abis in range(len(CustomStars)):
        CustomStarsIs = CustomStars[abis]
        if Starsystems['StarID'] == CustomStarsIs['StarID']:
            Starsystems.update(CustomStarsIs)

    # Імпорт всіх змін, тепер з заблокованного mapchanges_lock.py
    for abis in range(len(CustomStarsLock)):
        CustomStarsIs = CustomStarsLock[abis]
        if Starsystems['StarID'] == CustomStarsIs['StarID']:
            Starsystems.update(CustomStarsIs)

    return Starsystems