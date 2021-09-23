Dairy = {
        "Milk": {"Price: ": 1, "Quantity: ": 113},
        "Yoghurt": {"Price: ": 2, "Quantity: ": 98},
        "Cottage Cheese": {"Price: ": 4, "Quantity: ": 50},
        "Gorgonzola Cheese": {"Price: ": 7, "Quantity: ": 41},
        },
Fish = {
        "Salmon": {"Price: ": 20, "Quantity: ": 22},
        "Mackerel": {"Price: ": 14, "Quantity: ": 31},
        "Anchovy": {"Price: ": 10, "Quantity: ": 91},
        },
Beverages = {
        "Cola": {"Price: ": 1, "Quantity: ": 100},
        "Fanta": {"Price: ": 1, "Quantity: ": 100},
        "Sprite": {"Price: ": 1, "Quantity: ": 100},
        "Dr.Pepper": {"Price: ": 1.5, "Quantity: ": 120},
        },
Spirits = {
        "Jameson": {"Price: ": 8, "Quantity: ": 24},
        "Johnie Walker": {"Price: ": 8, "Quantity: ": 32},
        "Tullamore Dew": {"Price: ": 12, "Quantity: ": 12},
        "Grant's": {"Price: ": 14, "Quantity: ": 14},
    },
Sweets = {
        "Haribo": {"Price: ": 1, "Quantity: ": 22},
        "Trolli": {"Price: ": 1, "Quantity: ": 31},
        "Roshen": {"Price: ": 1.5, "Quantity: ": 91},
        },

while True:

    print("Please, choose the grocery category: ")
    print("1.Dairy, 2.Fish, 3.Beverages, 4.Spirits, 5.Sweets")

    category_choice = int(input("Please, choose the category upper: "))
    cs = category_choice

    if cs == 1:
        print(Dairy)
        break
    if cs == 2:
        print(Fish)
        break
    if cs == 3:
        print(Beverages)
        break
    if cs == 4:
        print(Spirits)
        break
    if cs == 5:
        print(Sweets)
        break

else:
    print("Invalid Input")
