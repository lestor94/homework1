dairy = {1: {"Price": 21, "Quantity": 113},
        2: {"Price": 39, "Quantity": 98}}

fish = {1: {"Price": 90, "Quantity": 22},
        2: {"Price": 86, "Quantity": 31}}

bever = {1: {"Price": 15, "Quantity": 100},
            2: {"Price": 15, "Quantity": 100}}

spirits = {1: {"Price": 319, "Quantity": 24},
           2: {"Price": 550, "Quantity": 32}}

sweets = {1: {"Price": 63, "Quantity": 22},
          2: {"Price": 59, "Quantity": 31}}


while True:

    print("Please, choose the grocery category: ")
    print("1.Dairy, 2.Fish, 3.Beverages, 4.Spirits, 5.Sweets")

    category_choice = int(input("Please, choose the category upper: "))
    cs = category_choice

    if cs == 1:
        while True:
               d = int(input("Choose the product: 1.Milk 2.Yoghurt "))
               if d == 1:
                   print("The price of this product is " + str(dairy[1]["Price"]) +". " " Quantity: " + str(dairy[1]["Quantity"]))
                   break
               elif d == 2:
                   print("The price of this product is " + str(dairy[2]["Price"]) +". " " Quantity: " + str(dairy[2]["Quantity"]))
                   break
               else:
                   print('Wrong Input')
                   break

    if cs == 2:
        while True:
               d = int(input("Choose the product: 1.Salmon 2.Mackerel "))
               if d == 1:
                   print("The price of this product is " + str(fish[1]["Price"]) +". " " Quantity: " + str(fish[1]["Quantity"]))
                   break
               elif d == 2:
                   print("The price of this product is " + str(fish[2]["Price"]) +". " " Quantity: " + str(fish[2]["Quantity"]))
                   break

               else:
                   print('Wrong Input')
                   break

    if cs == 3:
        while True:
               d = int(input("Choose the product: 1.Cola 2.Fanta "))
               if d == 1:
                   print("The price of this product is " + str(bever[1]["Price"]) +". " " Quantity: " + str(bever[1]["Quantity"]))
                   break
               elif d == 2:
                   print("The price of this product is " + str(bever[2]["Price"]) +". " " Quantity: " + str(bever[2]["Quantity"]))
                   break
               else:
                   print('Wrong Input')
                   break

    if cs == 4:
        while True:
               d = int(input("Choose the  1.Baileys 2.Johnie Walker "))
               if d == 1:
                   print("The price of this product is " + str(spirits[1]["Price"]) +". " " Quantity: " + str(spirits[1]["Quantity"]))
                   break
               elif d == 2:
                   print("The price of this product is " + str(spirits[2]["Price"]) +". " " Quantity: " + str(spirits[2]["Quantity"]))
                   break
               else:
                   print('Wrong Input')
                   break

    if cs == 5:
        while True:
               d = int(input("Choose the  1.Haribo 2.Trolli "))
               if d == 1:
                   print("The price of this product is " + str(sweets[1]["Price"]) +". " " Quantity: " + str(sweets[1]["Quantity"]))
                   break
               elif d == 2:
                   print("The price of this product is " + str(sweets[2]["Price"]) +". " " Quantity: " + str(sweets[2]["Quantity"]))
                   break
               else:
                   print('Wrong Input')
                   break

    else:
        print("Wrong Input!")
