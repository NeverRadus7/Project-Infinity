PlanetClass = [
    "Силікатна планета", #0
    "Крижана планета", #1
    "Пустельна планета", #2
    "Газовий гігант", #3
    "Землеподібна планета", #4
    "Залізна планета", #5
    "Водна планета", #6
    "Карбонові планети", #7
]

MapFilter = ["Досліднецько-політичний", "Територія", "Спектральний"]
ShipClasses = ["Малий", "Вантажний", "Досліднецьке судно", "Військовий фрегат", "Тераформер"]
FleetClasses = ["Великий корабель", "Флотоносець", "Конструкторний", "Космічний авантюрист"]

Economics = [
    "Відсутнє", # 0
    "Змішене", # 1
    "Сільське господарство", # 2
    "Високі технології", # 3
    "Важка промисловість", # 4
    "Хімічна промисловість", # 5
    "Переробна", # 6
    "Видобувна", # 7
    "Військове", # 8
    "Фінанси"
]

ShipModifications = [
    {
        "ModID": 0,
        "ModType": 0,
        "ModName": "Паливний бак 50т",
        "ModCoust": 7000000,
        "ModValue": 50
    }
]

Ships = [
    {
        "ShipID": 0,
        "ShipName": "R-145",
        "ShipClass": 0,
        "ShipTravelingDist": 5,
        "ShipMaxFuel": 20,
        "ShipCoust": 10_000
    },
    {
        "ShipID": 1,
        "ShipName": "NR-516",
        "ShipClass": 2,
        "ShipTravelingDist": 8,
        "ShipMaxFuel": 25,
        "ShipCoust": 250_000
    },
    {
        "ShipID": 2,
        "ShipName": "Emu Exp-36",
        "ShipClass": 3,
        "ShipTravelingDist": 10,
        "ShipMaxFuel": 15,
        "ShipCoust": 3_750_000
    },
    {
        "ShipID": 3,
        "ShipName": "Emu Exp-50",
        "ShipClass": 3,
        "ShipTravelingDist": 15,
        "ShipMaxFuel": 20,
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

ItemsType = [
    "Паливні", # 0
    "Метали", # 1
    "Мінерали", # 2
    "Техніка", # 3
    "Хімічні препарати", # 4
    "Наукові зразки", # 5
    "Харчові продукти", # 6
    "Екзотичні" # 7
]

ItemsDB = [
    {"ItemID": 0, "ItemName": 'Ракетне паливо', "ItemType": 0,"ItemEconomicType": 1,"ItemCoust": 300},
    {"ItemID": 1, "ItemName": 'Будівельний матеріал', "ItemType": 4,"ItemEconomicType": 3,"ItemCoust": 300},
    {"ItemID": 2, "ItemName": "Золото", "ItemType": 1, "ItemEconomicType": 1, "ItemCoust": 15000},
    {'ItemID': 3, 'ItemName': 'Реактивна сталь', 'ItemType': 1, 'ItemEconomicType': 3, 'ItemCoust': 1250000}
]