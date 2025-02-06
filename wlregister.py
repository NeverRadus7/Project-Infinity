PlanetClass = [
    "Кам'яна безповітряна планета",
    "Льодова безповітряна планета",
    "Кам'яно-льодова безповітряна планета",
    "Газовий гігант",
    "Землеподібна планета",
    "Скеляста планета земної групи",
]

MapFilter = ["Досліднецько-політичний", "Територія", "Спектральний"]
ShipClasses = ["Малий", "Вантажний", "Досліднецьке судно", "Великий корабель"]

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
        "ShipName": "BigFleet Explorer-36",
        "ShipClass": 3,
        "ShipTravelingDist": 10,
        "ShipMaxFuel": 15,
        "ShipCoust": 3_750_000
    }
]

Fleets = [
    {
        "FleetID": 0,
        "FleetModel": "Ra Min H100",
        "FleetClass": 0,
        "FleetMaxFuel": 100,
        "FleetMaxHyperdrive": 1000,
        "FleetTravelingDist": 12,
    }
]

ItemsType = [
    "Паливні",
    "Функціональні предмети",
    "Метали",
    "Мінерали",
    "Техніка",
    "Хімічні препарати",
    "Лабораторні обладнення",
    "Харчові продукти",
    "Екзотичні"
]

ItemsDB = [
    {
        "ItemName": 'Паливні одиниці (Астробак)',
        "ItemType": 0,
        "ItemCategory": 0,
        "ItemCoust": 300
    },
    {
        "ItemName": "Вантаж (Астероїдне золото)",
        "ItemType": 2,
        "ItemCategory": 0,
        "ItemCoust": 5500
    },
    {
        "ItemName": 'Вантаж (Високотехнологічні нано-трубки)',
        "ItemType": 3,
        "ItemCategory": 0,
        "ItemCoust": 40000
    },
    {
        "ItemName": 'Вантаж (Екзотичні кристали)',
        "ItemType": 8,
        "ItemCategory": 0,
        "ItemCoust": 2000000
    }
]