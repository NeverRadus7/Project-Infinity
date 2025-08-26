# Shell settings
ConsoleSizeX = 130  # Default: 130
ConsoleSizeY = 33 # Default: 30
WallSymbol = "━"
SavePath = "save/save.json"
MapPath = "save/map.json"

# Gameplay settings
MaxLevel = 999 # Default: 100
MaxNavyLevel = 100 # Default: 100
XpToLevel = 10000 # Default: 10000
FuelRequire = 1 # Default: 1
DebugInfo = False # Default: False
SetTravelDistation = 0 # Default: 0
AddShipModification = 0 # Default: 0

SymbolOfStar = "★ "
SymbolOfStarPinned = "★⚐ "

# Economic settings
IntelToCredits = 3 # Default: 3
BattleGrantToCredits = 7 # Default: 7

# Map settings /!\ Changing this paramets will break your game
MapSeed = 0x2976579765 # Default: 0x2976579765| 
MapCivilRange = 20 # Default: 20
PlanetColonyRange = 75 # Default: 75
CivilEcoMin = 0.1 # Default: 0.1
CivilEcoMax = 1.5 # Default: 1.5
MinFulling = 1 # Default: 1
MaxFulling = 80 # Default: 60
StarViewMaxPlanets = 8
SymbolFulling = "≡"

# Battle settings
BattleCooldown = 0.5 # Default: 0.5
BattleCoefMin = 0.1 # Default: 0.1
BattleCoefMax = 1.2 # Default: 1.2

# Coefficient intel planet class
CoefficientsPlanetClasses = {
    0: 0, # Default: 0
    1: 0, # Default: 0
    2: 0.0, # Default: 0.125
    3: 0.125, # Default: 0.2
    4: 0.5, # Default: 0.5
    5: 0.0, # Default: 0.125
    6: 0.125, # Default: 04
    7: 0.0, # Default: 0.125
    8: 0.125 # Default: 0.125
}

CoefficientsPlanetSpecial = {
    0: 0, # Default: 0
    'Live': 2.5, # Default: 2.5
    'Terraform': 1.33 # Default: 1.33
}

# Modification settings
ModLevelEmptySym = "☆"
ModLevelSym = "★"
ModMaxLevel = 5 # Default: 5
ModLevelCoeff = 4 # Default: 4

# Colony/Civil settings
sett_pop_include = [0,3] # Default: [1,5]
sett_eco_include = [0.0001,0.001] # Default: [0.0001,0.001]
