# #Multiplying fuction
# # def multipled(arg1,arg2,arg3):
# #     return (arg1*arg2*arg3)
# # print(multipled(1,2,3))
#
# #exmpl with arguments
# # def funct1(y=0, x=1):
# #     print(y,x)
# # funct1(1,x = 2)
#
# #practice
# #
# # def funct(y = "*"):
# #     return(y)
# # print(funct())
# # print(funct()*2)
# # print(funct()*3)
# # print(funct()*4)
# # print(funct()*5)
#
# # def my_funct()
# # lst = [10,11,7,5,8,2]
#
#
# # def my_funct(x = 20):
# #     return(x,x+1)
# # print(my_funct())
#
# # x = 320
# # y = 8
# # def funct1(x,y):
# #     return(x//y)
# # print(funct1(x,y))
#
# lst = [1,3,6,2,4,7]
# def is_ascended(*lst):
#     for el in lst:
#         list(lst) == sorted(lst)
#         return True
#     return False
# print(is_ascended(*lst))
#
# x = 7
# def my_func():
#     global x
#     x += 3
#     print(x)
# my_func()
# print(x)

# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2
# f1()()
#
# def maker(n):
#     def action(x):
#         return x ** n
#     return action
# f = maker(3)
# f(4)
# def name(name):
#     def surname_cap(surn):
#         print(f'{name.upper}{surn.upper}')
#     return surname_cap
# n = name("Arsen")
# n("Kakheli")
# print(n)
# print(n)
# n("Kakheli")

from test import tests1
print(tests1.x)
