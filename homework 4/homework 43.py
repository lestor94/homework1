# task 3

def s():
    with open("homework 443",'r') as file:
        file_content = file.read()
        f = file_content.count(".")
        s = file_content.capitalize()
        print(file_content)
        print("")
        # print(s)
        print("This file contains " + str(f) + " sentences")
s()
