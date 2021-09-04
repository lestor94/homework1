#Multiplying fuction
# def multipled(arg1,arg2,arg3):
#     return (arg1*arg2*arg3)
# print(multipled(1,2,3))

#exmpl with arguments
# def funct1(y=0, x=1):
#     print(y,x)
# funct1(1,x = 2)

#practice
#
# def funct(y = "*"):
#     return(y)
# print(funct())
# print(funct()*2)
# print(funct()*3)
# print(funct()*4)
# print(funct()*5)

# def my_funct()
# lst = [10,11,7,5,8,2]


# def my_funct(x = 20):
#     return(x,x+1)
# print(my_funct())

# x = 320
# y = 8
# def funct1(x,y):
#     return(x//y)
# print(funct1(x,y))

lst = [1,3,6,2,4,7]
def is_ascended(*lst):
    for el in lst:
        list(lst) == sorted(lst)
        return True
    return False
print(is_ascended(*lst))