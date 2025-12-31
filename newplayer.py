from wlengine import wlengine
from datetime import timedelta
import settings
import json
import random

Date = wlengine.Date() + timedelta(days=1)
writeDate = wlengine.DateSave(Date)

Player = {
    "Nickname": "Player",
    "Location": random.randint(-500,500),
    "Ship": {
        "ShipID": 0,
        "ShipName": "Rookie",
        "ShipModification": [
            {
                "ModificationID": None,
                "ModificationLevel": 0
            },
            {
                "ModificationID": None,
                "ModificationLevel": 0
            },
        ],
        "ShipFlags": ["STARTED_SHIP"],
        "Storage": [],
        "Fuel": 20,
        "ItemsCount": 0
    },
    "Exo": {
        "ExoClass": 0,
        "ExoLevel": 1,
        "ExoMod": []
    },
    "Money": 0,
    "IntelBall": 0,
    "BattleScore": 0,
    "SocialScore": 0,
    "XP": 0,
    "Reputation": 0,
    "WorldDay": 0,
    "Atribution": [],
    "Statistic": {
        "StarInteled": 0,
        "StarControled": 0,
        "StarColony": 0,
        "CreditsFromSelled": 0,
        "CreditsFromScience": 0,
        "IncomeFromColony": 0
    },
    "MapSettings": {
        "Filter": 0
    },
    "NextDate": writeDate,
    "GameUpdate": 4
}

file = open(settings.SavePath, "w", encoding="utf-8")
json.dump(Player, file, ensure_ascii=False, indent=4)
file.close()

file = open(settings.MapPath, "w", encoding="utf-8")
file.write("[]")
file.close()