import random
import settings
import wlregister
from galaxy.mapchanges import CustomStars
from galaxy.mapchanges_lock import CustomStarsLock
from nickname_generator import generate as ranname

mapseed = settings.MapSeed

Latters = [chr(i) for i in range(65, 91)]
LowerLatters = [chr(i) for i in range(97, 123)]
Articl = ["Alpha","Beta","Gamma","Delta"]

def GenMap(seed):
    random.seed(mapseed + seed)
    def PlanetGen(x):
        Planets = []
        for gen in range(x):
            gen += 1
            planet_name = f"{solar_name}-{gen}"
            planet_class = random.randint(0, 4)
            if planet_class == 0:
                planet_temp = random.randint(0,1000)
            elif planet_class == 1:
                planet_temp = random.randint(-273,0)
            elif planet_class == 2:
                planet_temp = random.randint(-273,100)
            elif planet_class == 3:
                planet_temp = random.randint(-10,300)
            elif planet_class == 4:
                planet_temp = random.randint(-8,30)

            Planets.append(
                {
                    "PlanetName": planet_name,
                    "PlanetClass": planet_class,
                    "PlanetTemp": planet_temp
                }
            )
        return Planets
    
    solar_name = f"{random.choice(Articl)} {abs(seed)}-{abs(int(seed/20))}-{random.choice(Latters)}{random.randint(1,999)}"

    solar_class = random.choice(["O", "B", "A", "F", "G", "K", "M"])
    if solar_class == "O":
        solar_size = random.uniform(6.6,15)
        solar_mass = random.uniform(16,120)
        solar_temp = random.randint(30_000, 50_000)
    if solar_class == "B":
        solar_size = random.uniform(3.2,6.6)
        solar_mass = random.uniform(2.1,16)
        solar_temp = random.randint(10_000, 30_000)
    if solar_class == "A":
        solar_size = random.uniform(1.8,3.2)
        solar_mass = random.uniform(1.4,2.1)
        solar_temp = random.randint(7_500, 10_000)
    if solar_class == "F":
        solar_size = random.uniform(1.2,1.8)
        solar_mass = random.uniform(1.04,1.4)
        solar_temp = random.randint(6_000, 7_500)
    if solar_class == "G":
        solar_size = random.uniform(0.96,1.2)
        solar_mass = random.uniform(0.8,1.04)
        solar_temp = random.randint(5_200, 6_000)
    if solar_class == "K":
        solar_size = random.uniform(0.7,0.96)
        solar_mass = random.uniform(0.45,0.8)
        solar_temp = random.randint(3_700, 5_200)
    if solar_class == "M":
        solar_size = random.uniform(0.1,0.7)
        solar_mass = random.uniform(0.08,0.45)
        solar_temp = random.randint(2_400, 3_700)

    Starsystems = {
        "StarID": seed,
        "Star": solar_name,
        "Class": solar_class,
        "Temp": solar_temp,
        "Mass": solar_mass,
        "Size": solar_size,
        "Planets": PlanetGen(random.randint(1,8)),
        "MapPosition": random.randint(1,3780)
    }

    # Генератор колонії
    if random.randint(1,100) <= settings.MapCivilRange:
        Starsystems['Star'] = ranname()
        Starsystems['StarIntel'] = True
        Starsystems['StarCivil'] = {}
        Starsystems['StarCivil']['CivilEco'] = random.uniform(settings.CivilEcoMin,settings.CivilEcoMax)
        Starsystems['StarCivil']['CivilStation'] = {
            "StationName": f"{ranname()} Station",
            "StationType": random.randint(0,2),
            "StationStoreList": random.sample(range(len(wlregister.ItemsDB)), 5) 
        }
    
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