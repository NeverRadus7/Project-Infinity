PlanetClass = {
    "LiveClass": ["Liveable", "Semi-Liveable", "Unliveable", "Dead"],

    "TypeClass": ["Terrestrial", "Desert", "Ocean",
                 "Ice", "Volcanic", "Gas Giant",],

    "TempClass": ["Hot", "Hot", "Warm",
                  "Moderate",
                  "Cool", "Cold", "Icy"],

    "UniqueClass": ["", "with life", "with civilization",
                    "with colonies", "with unique signal"]

}

MapFilter = ["Research-Political", "Territory", "Spectral", "Economic"]
ShipClasses = ["Small", "Cargo", "Explorer", "Military", "Miner"]
FleetClasses = ["Large Ship", "Fleet Carrier", "Construction", "Space Adventurer"]
StationType = ["Linear Station", "Modular Station", "Wheel Station", "Ring Station"]

LevelRang = {
    0: "Novice Pilot",
    1: "Novice Pilot I",
    2: "Novice Pilot II",
    3: "Novice Pilot III",
    4: "Novice Pilot IV",
    5: "Novice Pilot -=V=-",
    6: "Advanced Pilot",
    7: "Advanced Pilot I",
    8: "Advanced Pilot II",
    9: "Advanced Pilot III",
    10: "Advanced Pilot IV",
    11: "Advanced Pilot -=V=-",
    12: "Expert",
    13: "Expert I",
    14: "Expert II",
    15: "Expert III",
    16: "Expert IV",
    17: "Expert -=V=-",
    18: "Experienced pilot",
    19: "Experienced Pilot I",
    20: "Experienced Pilot II",
    21: "Experienced Pilot III",
    22: "Experienced Pilot IV",
    23: "Experienced Pilot -=V=-",
    999: "⏴MAXIMA⏵"
}

Economics = [
    "Anarchy",
    "Agricultural",
    "Mineral",
    "Energy",
    "Bio-resources",
    "Industrial",
    "Technological",
    "Military",
    "Trade",
    "Financial",
    "Tourist",
    "Scientific",
    "Pirate",
    "Religious",
    "Post-apocalyptic",
    "Mega-corporate",
    "Dependent colony"
]

EconomicsDesc = [
    ""
]

#Buildings = [
#    "Житловий блок"
#]

Buildings = {
    0: {
            "BuildingName": "Residential block",
            "BuildingType": 0,
            "BuildingValue": 150_000,
            "BuildingCoust": 800_000_000
        },
    1: {
            "BuildingName": "Storages",
            "BuildingType": 1,
            "BuildingValue": 30_000,
            "BuildingCoust": 200_000_000
       }
}

# Типифікація будівель може впливати на збільшення 
# вмісткості жителів, наприклад [1] збільшує вмісткість 
# населення, а [2] збільшує слоти зберігання сировини 
# та інших припасів.

ShipModifications = [
    {
        "ModID": 0,
        "ModType": 0,
        "ModName": "Addtional fuel tanks",
        "ModCoust": 200_000,
        "ModValue": 3 # + Fuel maximum capacity
    },
    {
        "ModID": 1,
        "ModType": 1,
        "ModName": "Light surface alloy",
        "ModCoust": 180_000,
        "ModValue": 10 # + Health ship
    },
    {
        "ModID": 2,
        "ModType": 2,
        "ModName": "Improved research sensors",
        "ModCoust": 500_000,
        "ModValue": 2 # + Coefficient intel
    },
    {
        "ModID": 3,
        "ModType": 1,
        "ModName": "Reactive surface",
        "ModCoust": 2_000_000,
        "ModValue": 30 # + Health ship
    },
    {
        "ModID": 4,
        "ModType": 5,
        "ModName": "Mass reducer",
        "ModCoust": 15_000_000,
        "ModValue": 5 # + Warp distance
    },
    {
        "ModID": 5,
        "ModType": 3,
        "ModName": "Laser small cannon",
        "ModCoust": 35_000,
        "ModValue": {'damage': 3, 'interval': 1}
    },
    {
        "ModID": 6,
        "ModType": 3,
        "ModName": "Automatic guns",
        "ModCoust": 60_000,
        "ModValue": {'damage': 1, 'interval': 4}
    },
    {
        "ModID": 7,
        "ModType": 3,
        "ModName": "Artillery establishment",
        "ModCoust": 4_000_000,
        "ModValue": {'damage': 5, 'interval': 4}
    },
    {
        "ModID": 8,
        "ModType": 3,
        "ModName": "Plasma gun",
        "ModCoust": 200_000_000,
        "ModValue": {'damage': 160, 'interval': 1}
    },
    {
        "ModID": 9,
        "ModType": 1,
        "ModName": "High-strength alloy",
        "ModCoust": 10_000_000,
        "ModValue": 50
    },
    {
        "ModID": 10,
        "ModType": 3,
        "ModName": "Automatic machine guns",
        "ModCoust": 160_000,
        "ModValue": {'damage': 10, 'interval': 8}
    },
    {
        "ModID": 11,
        "ModType": 3,
        "ModName": "AMG-100 [MILLYTECH]",
        "ModCoust": 800_000,
        "ModValue": {'damage': 30, 'interval': 8}
    },
    {
        "ModID": 12,
        "ModType": 5,
        "ModName": "Megaspace engine",
        "ModCoust": 60_000_000,
        "ModValue": 5
    },
    {
        "ModID": 13,
        "ModType": 5,
        "ModName": "Superspace engine",
        "ModCoust": 250_000_000,
        "ModValue": 10
    },
    {
        "ModID": 14,
        "ModType": 5,
        "ModName": "Hyperspace engine",
        "ModCoust": 700_000_000,
        "ModValue": 20
    },
    {
        "ModID": 15,
        "ModType": 4,
        "ModName": "Astrosensory [ASTRA INC.]",
        "ModCoust": 150_000_000,
        "ModValue": 10
    },
    {
        "ModID": 16,
        "ModType": 3,
        "ModName": "Small railgun",
        "ModCoust": 30_000_000,
        "ModValue": {'damage': 26, 'interval': 1}
    },
    {
        "ModID": 17,
        "ModType": 3,
        "ModName": "Railgun",
        "ModCoust": 70_000_000,
        "ModValue": {'damage': 40, 'interval': 1}
    },
    {
        "ModID": 18,
        "ModType": 3,
        "ModName": "Double-barreled railgun",
        "ModCoust": 40_000_000,
        "ModValue": {'damage': 20, 'interval': 2}
    },
    {
        "ModID": 19,
        "ModType": 6,
        "ModName": "Storage cell 50+",
        "ModCoust": 100_000,
        "ModValue": 50
    },
    {
        "ModID": 20,
        "ModType": 7,
        "ModName": "Asteroid-level bur",
        "ModCoust": 30_000,
        "ModValue": 1
    }
]

ModificationType = [
    "Fuel tanks", 
    "Armorplates",
    "Intel technologi", 
    "Military technologi", 
    "Precision instruments", 
    "Engines", 
    "Storage",
    "Mining technologi",
]

Ships = [
    {
        "ShipID": 0,
        "ShipName": "Rookie ORT-100",
        "ShipHealth": 100,
        "ShipClass": 0,
        "ShipTravelingDist": 5,
        "ShipMaxFuel": 20,
        "ShipMaxModification": 2,
        "ShipMaxItems": 50,
        "ShipCoust": 10_000
    },
    {
        "ShipID": 1,
        "ShipName": "Excalibur EXP-10",
        "ShipHealth": 80,
        "ShipClass": 2,
        "ShipTravelingDist": 8,
        "ShipMaxFuel": 25,
        "ShipMaxModification": 3,
        "ShipMaxItems": 50,
        "ShipCoust": 250_000
    },
    {
        "ShipID": 2,
        "ShipName": "LSPM Enrue",
        "ShipHealth": 120,
        "ShipClass": 4,
        "ShipTravelingDist": 3,
        "ShipMaxFuel": 25,
        "ShipMaxModification": 4,
        "ShipMaxItems": 75,
        "ShipCoust": 1_000_000
    },
    {
        "ShipID": 3,
        "ShipName": "MILLYTECH QR-I",
        "ShipHealth": 600,
        "ShipClass": 3,
        "ShipTravelingDist": 3,
        "ShipMaxFuel": 30,
        "ShipMaxModification": 4,
        "ShipMaxItems": 20,
        "ShipCoust": 3_750_000
    },
    {
        "ShipID": 4,
        "ShipName": "Anabelus co. EXP-LUPA",
        "ShipHealth": 100,
        "ShipClass": 2,
        "ShipTravelingDist": 15,
        "ShipMaxFuel": 20,
        "ShipMaxModification": 6,
        "ShipMaxItems": 60,
        "ShipCoust": 15_000_000
    }
]

Fleets = [
    {
        "FleetID": 0,
        "FleetModel": "ISC G-160 Booldog",
        "FleetClass": 0,
        "FleetMaxFuel": 200,
        "FleetMaxHyperdrive": 300,
        "FleetTravelingDist": 15,
        "FleetCoust": 700_000_000
    },
    {
        "FleetID": 1,
        "FleetModel": "Ra-Min H100",
        "FleetClass": 2,
        "FleetMaxFuel": 100,
        "FleetMaxHyperdrive": 1000,
        "FleetTravelingDist": 12,
        "FleetCoust": 1_500_000_000
    },
    {
        "FleetID": 2,
        "FleetModel": "ISC G-200 Excalibur",
        "FleetClass": 3,
        "FleetMaxFuel": 50,
        "FleetMaxHyperdrive": 5000,
        "FleetTravelingDist": 15,
        "FleetCoust": 2_100_000_000
    }
]

StarSecurityType = ["Small patrols", "Frequent patrols", "Complete security"]

ItemsType = [
    "Fuel", # 0
    "Metals", # 1
    "Technology", # 2
    "Chemicals", # 3
    "Scientific samples", # 4
    "Food", # 5
    "Exotic" # 6
]

ItemsDB = [
    {"ItemID": 0, "ItemName": 'Rocket Fuel', "ItemType": 0,"ItemEconomicType": 1,"ItemCoust": 200},
    {"ItemID": 1, "ItemName": 'Building Materials', "ItemType": 3,"ItemEconomicType": 3,"ItemCoust": 30_000},
    {"ItemID": 2, "ItemName": "Refined Metal: Gold", "ItemType": 1, "ItemEconomicType": 1, "ItemCoust": 1_000},
    {'ItemID': 3, 'ItemName': 'Reactive Steel', 'ItemType': 1, 'ItemEconomicType': 3, 'ItemCoust': 100_000},
    {'ItemID': 4, 'ItemName': 'Terraforming Bacteria and Chemistry', 'ItemType': 3, 'ItemEconomicType': 4, 'ItemCoust': 500_000},
    {'ItemID': 5, 'ItemName': 'Mineral: Iron Ore ☆☆☆☆☆', 'ItemType': 1, 'ItemEconomicType': 7, 'ItemCoust': 50},
    {'ItemID': 6, 'ItemName': 'Mineral: Aluminum Ore ☆☆☆☆☆', 'ItemType': 1, 'ItemEconomicType': 7, 'ItemCoust': 30},
    {'ItemID': 7, 'ItemName': 'Mineral: Osmium Ore ★☆☆☆☆', 'ItemType': 1, 'ItemEconomicType': 7, 'ItemCoust': 60},
    {'ItemID': 8, 'ItemName': 'Mineral: Rich Osmium Ore ★★☆☆☆', 'ItemType': 1, 'ItemEconomicType': 7, 'ItemCoust': 150},
    {'ItemID': 9, 'ItemName': 'Mineral: Copper Ore ★☆☆☆☆', 'ItemType': 1, 'ItemEconomicType': 7, 'ItemCoust': 40},
    {'ItemID': 10, 'ItemName': 'Mineral: Gold Ore ★★★☆☆', 'ItemType': 1, 'ItemEconomicType': 7, 'ItemCoust': 250},
    {'ItemID': 11, 'ItemName': 'High-tension diamonds ★★★★★', 'ItemType': 1, 'ItemEconomicType': 7, 'ItemCoust': 50_000},
    {'ItemID': 12, 'ItemName': 'Vibrocrystals', 'ItemType': 1, 'ItemEconomicType': 7, 'ItemCoust': 200_000}
]

AsteroidsType = ["Rocky", "Ice", "Ice-Rocky", "Diamonds", "Crystals", "Rocky+"]