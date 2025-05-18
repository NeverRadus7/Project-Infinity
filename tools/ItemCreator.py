while True:
    ItemID = int(input("ItemID: "))
    ItemName = input("ItemName: ")
    ItemType = int(input("ItemType: "))
    ItemEconomicType = int(input("ItemEconomicType: "))
    ItemCoust = int(input("ItemCoust: "))

    list = []
    list.append({
        "ItemID": ItemID,
        "ItemName": ItemName,
        "ItemType": ItemType,
        "ItemEconomicType": ItemEconomicType,
        "ItemCoust": ItemCoust
    })

    print(list)