PlanetClass = [
    "Кам'яна планета",
    "Льодова планета",
    "Кам'яно-льодова планета",
    "Газовий гігант",
    "Землеподібна планета",
]

MapFilter = ["Досліднецько-політичний", "Територія", "Спектральний"]
ShipClass = ["Малий", "Вантажний", "Досліднецьке судно", "Великий корабель"]

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
    },
    {
        "ShipID": 3,
        "ShipName": "ASI Contstructor",
        "ShipClass": 4,
        "ShipTravelingDist": 8,
        "ShipMaxFuel": 30,
        "ShipCoust": 200_000_000
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

ItemsDB = [
    {
        "ItemName": 'Астробак',
        "ItemType": "REFUEL_ITEM",
        "ItemCategory": 0,
        "ItemCoust": 300
    },
    {
        "ItemName": 'Вантаж (Золотом)',
        "ItemCoust": 5500
    },
    {
        "ItemName": 'Вантаж (Високотехнологічні нано-трубки)',
        "ItemCoust": 40000
    },
    {
        "ItemName": 'Вантаж (Екзотичні кристали)',
        "ItemCoust": 2000000
    }
]