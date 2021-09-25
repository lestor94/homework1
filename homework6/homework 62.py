# string input

while True:
    i = int(input("Please, write the number from 0 to 50: "))

    if i >= 51:
        print("Too much!")
        break

    elif i <= 0:
        print("Not enough!")
        break

    elif i <=50 and i>= 0:

            if i % 3 == 0 and i % 5 == 0:
                print("Fizzbuzz")
                break
            if i % 3 == 0:
                print("fizz")
                break
            if i % 5 == 0:
                print("buzz")
                break


            # elif i % 5 == 0:
            #     print("buzz")
            #     break
            #
            # elif i % 3 == 0 or i % 5 == 0:
            #     print("fizzbuzz")

            else:
                print(i)
                break