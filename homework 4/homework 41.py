#task 1

import math

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def pitch(x,y):
    return x ** y

def root(x):
    return math.sqrt(x)

def cuber(x):
    return x**(1/3)

while True:
    print("Basic Operations: " + "1.Add" + " " + "2.Subtract" + " " + "3.Multiply" + " " + "4.Divide")
    print("Advanced Operations: " + "5.Pitch" + " " + "6.Square Root" + " " + "7.Cube Root")
    choise = int(input("Choose the operation, provided upper: "))

    if choise == 1:
        x = float(input("1st argument: "))
        y = float(input("2nd argument: "))
        print(x," + ",y," = ",add(x,y))
    elif choise == 2:
        x = float(input("1st argument: "))
        y = float(input("2nd argument: "))
        print(x," - ",y," = ",subtract(x,y))
    elif choise == 3:
        x = float(input("1st argument: "))
        y = float(input("2nd argument: "))
        print(x," * ",y," = ",multiply(x,y))
    elif choise == 4:
        x = float(input("1st argument: "))
        y = float(input("2nd argument: "))
        print(x," / ",y," = ",divide(x,y))
    elif choise == 5:
        x = float(input("1st argument: "))
        y = float(input("2nd argument: "))
        print(x," ** ",y," = ",pitch(x,y))
    elif choise == 6:
        x = float(input("Argument to be square rooted: "))
        print("sqrt", " = ", math.sqrt(x))
    elif choise == 7:
        x = float(input("Argument to be cube rooted: "))
        print("cuberoot", " = ", cuber(x))
    else:
        print("Invalid input!")

    restart = input("One more operation? (y/n): ")
    if restart == "n":
        print("As you wish!")
        break
