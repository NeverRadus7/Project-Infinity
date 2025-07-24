# Shell settings
ConsoleSizeX = 106  # Default: 130
ConsoleSizeY = 37 # Default: 30
WallSymbol = "━"
SavePath = "save/save.json"
MapPath = "save/map.json"

MaxLevel = 999 # Default: 100
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

# Map settings
MapSeed = 0x14b931fd # Default: 14b931fd | /!\ Changing this paramets will break your game
MapCivilRange = 20 # Default: 20
CivilEcoMin = 0.1 # Default: 0.1
CivilEcoMax = 1.5 # Default: 1.5
MinFulling = 1 # Default: 1
MaxFulling = 80 # Default: 90
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
