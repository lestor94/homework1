category = {
    "Drinks": {
        "Dairy": ["Milk", "Yoghurt", "Cotton Cheese", "Gorgonzola Cheese"],
        "Price": [10, 12, 8, 18],
        "Items": [113, 98, 50, 41]
    },
    "Fif": {
        "Fish": ["Salmon", "Mackerel", "Anchovy"],
        "Price": [32, 20, 10],
        "Items(KG)": [22, 31, 91]
    },
    3: {
        "Beverages": ["Cola", "Fanta", "Sprite", "Dr.Pepper"],
        "Price": [1, 1, 1, 1.5],
        "Items": [100, 100, 100, 120]
    },
    4: {
        "Spirits": ["Jameson", "Johnie Walker", "Tullamore", "Grant's"],
        "Price": [8, 8, 12, 14],
        "Items": [24, 32, 12, 14]
    },
    5: {
        "Sweets": ["Haribo", "Trolli", "Roshen"],
        "Price": [3, 2, 7],
        "Items": [30, 19, 45]
    }
}
print("Please, choose the grocery category: ")
print("1.Dairy, 2.Fish, 3.Beverages, 4.Spirits, 5.Sweets")

category_choose = int(input("Please, choose the category upper: "))

cs = category_choose
