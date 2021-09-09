#task 1
mylist = [1,2,3,4,5,6,7]
x = 0
if mylist == sorted(mylist):
    x = 1
if x:
    print (True)
else:
    print (False)

# #task 2
def MyMultiple(n):
    multiple = 1
    num = str(n)
    for x in num:
        multiple = multiple * int(x)

    return multiple

n = input('Type your digits ')
print(list(n))
print(MyMultiple(n))


#task 3
lst = ['Red', 'Green', 'Blue', 'White', 'Black']
s = ' '.join(lst)[::-1]
lst1 = s.split()
print(lst1[::-1])

# # #task 4

# prd1 = {}
# prd = {"salt":"2",
#        "meat": "25",
#        "apples": "6",
#        "banana":"3",
#        "milk": "4.5",
#        "bread": "2.5"}
# for keys,values in prd:
#     if values in prd > 4.5:
#         print(keys)


# # #task 5
hotels = {"Continental Hotel": "****",
          "Big Street Hotel": "**",
          "Corner Hotel": "**",
          "Trashviews Hotel": "*",
          "Hazbins": "****",
          "Hazbins Deluxe": "*****"}
stars = int(input("Type the hotels stars(digit only):"))
for key,value in hotels.items():
    if value == "*" * stars:
         print("We have such hotels with " + value + " stars: " + key)