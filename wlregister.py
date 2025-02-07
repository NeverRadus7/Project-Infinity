PlanetClass = [
    "Кам'яна безповітряна планета",
    "Льодова безповітряна планета",
    "Кам'яно-льодова безповітряна планета",
    "Газовий гігант",
    "Землеподібна планета",
    "Скеляста планета земної групи",
]

MapFilter = ["Досліднецько-політичний", "Територія", "Спектральний"]
ShipClasses = ["Малий", "Вантажний", "Досліднецьке судно", "Військовий фрегат"]
FleetClasses = ["Великий корабель", "Флотоносець", "Конструкторний", "Космічний авантюрист"]

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
        "FleetModel": "Ra-Min H100",
        "FleetClass": 2,
        "FleetMaxFuel": 100,
        "FleetMaxHyperdrive": 1000,
        "FleetTravelingDist": 12,
        "FleetCoust": 1_500_000_000
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
    {"ItemID": 0, "ItemName": 'Паливні одиниці (Ракетне паливо)',"ItemType": 0,"ItemCategory": 0,"ItemCoust": 300},
    {"ItemID": 1, "ItemName": "Вантаж (Астероїдне золото)","ItemType": 2,"ItemCategory": 0,"ItemCoust": 5500},
    {"ItemID": 2, "ItemName": 'Вантаж (Високотехнологічні нано-трубки)',"ItemType": 3,"ItemCategory": 0,"ItemCoust": 40000},
    {"ItemID": 3, "ItemName": 'Вантаж (Екзотичні кристали)',"ItemType": 8,"ItemCategory": 0,"ItemCoust": 2000000},
    {"ItemID": 4, "ItemName": "Іонний прискорювач", "ItemType": 1, "ItemCategory": 0, "ItemCoust": 12000},
    {"ItemID": 5, "ItemName": "Сканер спектрів", "ItemType": 1, "ItemCategory": 0, "ItemCoust": 8000},
    {"ItemID": 6, "ItemName": "Вантаж (Титанова пластина)", "ItemType": 2, "ItemCategory": 0, "ItemCoust": 2500},
    {"ItemID": 7, "ItemName": "Вантаж (Алюмінієвий сплав)", "ItemType": 2, "ItemCategory": 0, "ItemCoust": 1800},
    {"ItemID": 8, "ItemName": "Вантаж (Урановий злиток)", "ItemType": 2, "ItemCategory": 0, "ItemCoust": 6700},
    {"ItemID": 9, "ItemName": "Вантаж (Кварцовий кристал)", "ItemType": 3, "ItemCategory": 0, "ItemCoust": 1400},
    {"ItemID": 10, "ItemName": "Азурит", "ItemType": 3, "ItemCategory": 0, "ItemCoust": 2200},
    {"ItemID": 11, "ItemName": "Вантаж (Емеральдова пудра)", "ItemType": 3, "ItemCategory": 0, "ItemCoust": 2900},
    {"ItemID": 12, "ItemName": "Сканер живлення", "ItemType": 4, "ItemCategory": 0, "ItemCoust": 9500},
    {"ItemID": 13, "ItemName": "Модуль гравітації", "ItemType": 4, "ItemCategory": 0, "ItemCoust": 15000},
    {"ItemID": 14, "ItemName": "Генератор щита", "ItemType": 4, "ItemCategory": 0, "ItemCoust": 13500},
    {"ItemID": 15, "ItemName": "Киснева капсула", "ItemType": 5, "ItemCategory": 0, "ItemCoust": 1200},
    {"ItemID": 16, "ItemName": "Антидот класу V", "ItemType": 5, "ItemCategory": 0, "ItemCoust": 3100},
    {"ItemID": 17, "ItemName": "Гель зцілення", "ItemType": 5, "ItemCategory": 0, "ItemCoust": 4200},
    {"ItemID": 18, "ItemName": "Аналізатор речовин", "ItemType": 6, "ItemCategory": 0, "ItemCoust": 8500},
    {"ItemID": 19, "ItemName": "Лазерний мікроскоп", "ItemType": 6, "ItemCategory": 0, "ItemCoust": 9200},
    {"ItemID": 20, "ItemName": "Кріогенний контейнер", "ItemType": 6, "ItemCategory": 0, "ItemCoust": 10800},
    {"ItemID": 21, "ItemName": "Сублімаційний білок", "ItemType": 7, "ItemCategory": 0, "ItemCoust": 2500},
    {"ItemID": 22, "ItemName": "Дегідратована їжа", "ItemType": 7, "ItemCategory": 0, "ItemCoust": 2000},
    {"ItemID": 23, "ItemName": "Енергетичний гель", "ItemType": 7, "ItemCategory": 0, "ItemCoust": 2800},
    {"ItemID": 24, "ItemName": "Ксенонова есенція", "ItemType": 8, "ItemCategory": 0, "ItemCoust": 7500},
    {"ItemID": 25, "ItemName": "Зоряний пил", "ItemType": 8, "ItemCategory": 0, "ItemCoust": 15_000},
    {"ItemID": 26, "ItemName": "Артефакт невідомого походження", "ItemType": 8, "ItemCategory": 0, "ItemCoust": 8_000_000},
    {"ItemID": 27, "ItemName": "Темна матерія", "ItemType": 8, "ItemCategory": 0, "ItemCoust": 256_000},
    {"ItemID": 28, "ItemName": "Антигравітаційний кристал", "ItemType": 8, "ItemCategory": 0, "ItemCoust": 18200},
    {"ItemID": 29, "ItemName": "Магнітний конденсатор", "ItemType": 4, "ItemCategory": 0, "ItemCoust": 11200},
    {"ItemID": 30, "ItemName": "Плазмовий генератор", "ItemType": 4, "ItemCategory": 0, "ItemCoust": 13000},
    {"ItemID": 31, "ItemName": "Синтетичний полімер", "ItemType": 5, "ItemCategory": 0, "ItemCoust": 3400},
    {"ItemID": 32, "ItemName": "Фотонний підсилювач", "ItemType": 6, "ItemCategory": 0, "ItemCoust": 8900},
    {"ItemID": 33, "ItemName": "Нано-волокна", "ItemType": 5, "ItemCategory": 0, "ItemCoust": 3700},
    {"ItemID": 34, "ItemName": "Лігірований титан", "ItemType": 2, "ItemCategory": 0, "ItemCoust": 7200}
]