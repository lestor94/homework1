# # #First task
str1 = input("Hello! What's your name? " )
if str1.strip():
    print("Your name", str1, 'has', len(str1), "symbols!")
elif input("Okay, anon, type something! ") :
    print("Okay, I'm sure, it's important information :D")
else:
    print("Okay, let it be empty!")

# Second task

num1 = input('I want some math! Type the first num ')
num2 = input('Type the second num ')

num1 = int(num1)
num2 = int(num2)
if num1 > 0 and num2 > 0:
    print(int(num1) + int(num2), int(num1)/int(num2), int(num1)*int(num2), int(num1)**int(num2))
else:
    print('Wrong input')

# Third task
u = int(input("How many pizza? "))
v = int(input("how many people? "))

pizza = int(u*8)
pizza = u
people = v

print("each person will have a ",pizza/people, ' slices of pizza')




#Fourth task
x = int(input("Convert X to Y "))
y = 26.9
z = int(x)/int(y)
if x > 0:
    print("you can buy ",z, "for ",x," by exchange ",y)
else:
    print("Wrong input")

#Fifth task