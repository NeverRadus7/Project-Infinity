import json
import settings

if input("Do you want reset all progress? ") == "y":
    with open(settings.MapPath, "w", encoding="utf-8") as f:
        f.write("[]")

    print(f"Map in path: [{settings.MapPath}] was cleared!")
    input()