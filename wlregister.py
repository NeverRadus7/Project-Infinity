PlanetClass = {
    "LiveClass": ["Придатний", "Напівпридатний", "Непридатний", "Мертвий"],
    
    "TypeClass": ["Землеподібний світ", "Пустельний світ", "Океанічний світ",
                   "Льодовий світ", "Вулканічний світ", "Газовий гігант",],

    "TempClass": ["Розпечений", "Гарячий", "Теплий", 
                  "Помірний", 
                  "Прохолодний", "Холодний", "Крижаний"],

    "UniqueClass": ["", "з життям", "з цивілізацією", 
                    "з колоніями", "з унікальним сигналом"]
}

MapFilter = ["Досліднецько-політичний", "Територія", "Спектральний", "Економічний"]
ShipClasses = ["Малий", "Вантажний", "Досліднецьке судно", "Військовий фрегат"]
FleetClasses = ["Великий корабель", "Флотоносець", "Конструкторний", "Космічний авантюрист"]

LevelRang = {
    0: "Пілот-новачок",
    1: "Пілот-новачок І",
    2: "Пілот-новачок ІІ",
    3: "Пілот-новачок ІІІ",
    4: "Пілот-новачок ІV",
    5: "Пілот-новачок -=V=-",
    6: "Продвинутий пілот",
    7: "Продвинутий пілот І",
    8: "Продвинутий пілот ІІ",
    9: "Продвинутий пілот ІІІ",
    10: "Продвинутий пілот IV",
    11: "Продвинутий пілот -=V=-",
    12: "Експерт",
    13: "Експерт І",
    14: "Експерт ІІ",
    15: "Експерт ІІІ",
    16: "Експерт ІV",
    17: "Експерт -=V=-",
    18: "Досвідчений пілот",
    19: "Досвідчений пілот І",
    20: "Досвідчений пілот ІІ",
    21: "Досвідчений пілот ІІІ",
    22: "Досвідчений пілот IV",
    23: "Досвідчений пілот -=V=-", 
    999: "Галактичний імператор [MAX]"
}

# Economics = [
#     "Відсутнє", # 0
#     "Змішене", # 1
#     "Сільське господарство", # 2
#     "Технології", # 3
#     "Важка промисловість", # 4
#     "Хімічна промисловість", # 5
#     "Переробна", # 6
#     "Видобувна", # 7
#     "Військове", # 8
#     "Фінанси" # 9
# ]

Economics = [
    "Відсутнє",
    "Аграрна",
    "Мінеральна",
    "Енергетична",
    "Біосировинна",
    "Індустріальна",
    "Технократична",
    "Військова",
    "Торгівельний порт",
    "Фінансовий центр",
    "Туристична"
    "Наукова",
    "Піратська",
    "Релігійна",
    "Постапокаліптична",
    "Мегакорпоративна",
    "Залежна колонія"
]

Buildings = [
    "Житловий блок"
]

NewBuildings = {
    "1": {
            "BuildingName": "Житловий блок",
            "BuildingType": 0,
            "BuildingValue": 150_000,
            "BuildingCoust": 800_000_000
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
        "ModName": "Додаткові паливні баки",
        "ModCoust": 200_000,
        "ModValue": 3 # + Fuel maximum capacity
    },
    {
        "ModID": 1,
        "ModType": 1,
        "ModName": "Легкоповерхневий сплав",
        "ModCoust": 180_000,
        "ModValue": 10 # + Health ship
    },
    {
        "ModID": 2,
        "ModType": 2,
        "ModName": "Покращені досліднецьки сенсори",
        "ModCoust": 500_000,
        "ModValue": 2 # + Coefficient intel
    },
    {
        "ModID": 3,
        "ModType": 1,
        "ModName": "Реактивна поверхня",
        "ModCoust": 2_000_000,
        "ModValue": 30 # + Health ship
    },
    {
        "ModID": 4,
        "ModType": 5,
        "ModName": "Зменшувач мас",
        "ModCoust": 15_000_000,
        "ModValue": 5 # + Warp distance
    },
    {
        "ModID": 5,
        "ModType": 3,
        "ModName": "Лазерна мала гармата",
        "ModCoust": 35_000,
        "ModValue": {'damage': 3, 'interval': 1}
    },
    {
        "ModID": 6,
        "ModType": 3,
        "ModName": "Автоматичні гармати",
        "ModCoust": 60_000,
        "ModValue": {'damage': 1, 'interval': 4}
    },
    {
        "ModID": 7,
        "ModType": 3,
        "ModName": "Артилерійна установа",
        "ModCoust": 4_000_000,
        "ModValue": {'damage': 5, 'interval': 4}
    },
    {
        "ModID": 8,
        "ModType": 3,
        "ModName": "Плазмогармата",
        "ModCoust": 200_000_000,
        "ModValue": {'damage': 160, 'interval': 1}
    },
    {
        "ModID": 9,
        "ModType": 1,
        "ModName": "Надміцний сплав",
        "ModCoust": 10_000_000,
        "ModValue": 50
    },
    {
        "ModID": 10,
        "ModType": 3,
        "ModName": "Автоматичні кулемети",
        "ModCoust": 160_000,
        "ModValue": {'damage': 10, 'interval': 8}
    },
    {
        "ModID": 11,
        "ModType": 3,
        "ModName": "Автоматичні кулемети MILLYTECH",
        "ModCoust": 800_000,
        "ModValue": {'damage': 30, 'interval': 8}
    },
    {
        "ModID": 12,
        "ModType": 5,
        "ModName": "Мегапросторовий двигун",
        "ModCoust": 60_000_000,
        "ModValue": 5
    },
    {
        "ModID": 13,
        "ModType": 5,
        "ModName": "Суперпросторовий двигун",
        "ModCoust": 250_000_000,
        "ModValue": 10
    },
    {
        "ModID": 14,
        "ModType": 5,
        "ModName": "Гіперпросторовий двигун",
        "ModCoust": 700_000_000,
        "ModValue": 20
    },
    {
        "ModID": 15,
        "ModType": 4,
        "ModName": "Астросенсори [ASTRA INC.]",
        "ModCoust": 150_000_000,
        "ModValue": 10
    },
    {
        "ModID": 16,
        "ModType": 3,
        "ModName": "Малий рельсотрон",
        "ModCoust": 30_000_000,
        "ModValue": {'damage': 26, 'interval': 1}
    },
    {
        "ModID": 17,
        "ModType": 3,
        "ModName": "Рельсотрон",
        "ModCoust": 70_000_000,
        "ModValue": {'damage': 40, 'interval': 1}
    },
    {
        "ModID": 18,
        "ModType": 3,
        "ModName": "Двох-дуловий рельсотрон",
        "ModCoust": 40_000_000,
        "ModValue": {'damage': 20, 'interval': 2}
    },
    {
        "ModID": 19,
        "ModType": 6,
        "ModName": "Контейнер на +50 предметів",
        "ModCoust": 100_000,
        "ModValue": 50
    }
]
#                         0            1                2                3                      4                                        5                                     6
ModificationType = ["Паливні баки", "Броня", "Досліднецькі прибори", "Гармати", "Прибори точності та наведення", "Двигуни, варп-двигуни, гіперпросторові двигуни", "Хранилище та контейнери"]

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
        "ShipID": 3,
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

StarSecurityType = ["Дрібні патрулі", "Часті патрулі", "Повна безпека"]

ItemsType = [
    "Паливні", # 0
    "Метали", # 1
    "Техніка", # 2
    "Хімічні препарати", # 3
    "Наукові зразки", # 4
    "Харчові продукти", # 5
    "Екзотичні" # 6
]

ItemsDB = [
    {"ItemID": 0, "ItemName": 'Ракетне паливо', "ItemType": 0,"ItemEconomicType": 1,"ItemCoust": 200},
    {"ItemID": 1, "ItemName": 'Будівельні матеріали', "ItemType": 3,"ItemEconomicType": 3,"ItemCoust": 30_000},
    {"ItemID": 2, "ItemName": "Очишений метал: Золото", "ItemType": 1, "ItemEconomicType": 1, "ItemCoust": 1_000},
    {'ItemID': 3, 'ItemName': 'Реактивна сталь', 'ItemType': 1, 'ItemEconomicType': 3, 'ItemCoust': 100_000},
    {'ItemID': 4, 'ItemName': 'Тераформічні бактерії та хімія', 'ItemType': 3, 'ItemEconomicType': 4, 'ItemCoust': 500_000},
    {'ItemID': 5, 'ItemName': 'Копалина: Залізна руда ☆☆☆☆☆', 'ItemType': 1, 'ItemEconomicType': 7, 'ItemCoust': 50},
    {'ItemID': 6, 'ItemName': 'Копалина: Алюмінюєва руда ☆☆☆☆☆', 'ItemType': 1, 'ItemEconomicType': 7, 'ItemCoust': 30},
    {'ItemID': 7, 'ItemName': 'Копалина: Осмієва руда ★☆☆☆☆', 'ItemType': 1, 'ItemEconomicType': 7, 'ItemCoust': 60},
    {'ItemID': 8, 'ItemName': 'Копалина: Багата осмієва руда ★★☆☆☆', 'ItemType': 1, 'ItemEconomicType': 7, 'ItemCoust': 150},
    {'ItemID': 9, 'ItemName': 'Копалина: Мідна руда ★☆☆☆☆', 'ItemType': 1, 'ItemEconomicType': 7, 'ItemCoust': 40},
    {'ItemID': 10, 'ItemName': 'Копалина: Золота руда ★★★☆☆', 'ItemType': 1, 'ItemEconomicType': 7, 'ItemCoust': 250}
]
