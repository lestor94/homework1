# print(1 + 'a')

# try:
#     print(1 + 'A')
# except TypeError:
#     print("Error occured")
# def fun1(x):
#     try:
#         return x/12
#     except ArithmeticError:
#         print("Wrong Input")
#     except:
#         print("Something Wrong")
#     finally:
#         print("You're fool!")
# fun1(x)

# class Test():
#     def __init__(self,x):
#         self.x = x
#
#     def making_magic(self):
#         print(f'Magic - {self.x}')
#
# inst_test1 = Test(1)
# inst_test2 = Test(2)
#
# Test.making_magic(inst_test1)

# class Human():
#
#     country = 'Ukraine'
#     population = 0
#
#     def __init__(self,gender, age):
#
#         self.gender = gender
#         self.age = age
#
#     def add_pop(self):
#         self.population += 1
#         print(self.population)
#
#     def get_info(self):
#         return f'Gender - {self.gender}. Age - {self.age}'
#
#
# petro = Human('M',32)
# oksana = Human('f',15)
# igor = Human('M',0)
#
# class Employee(Human):
#
#     def __init__(self, gender, age, position, salary):
#         super().__init__(gender,age)
#         self.position = position
#         self.salary = salary
#         self.add_pop()
#
#     def get_info(self):
#         # human_info = super(Employee, self).get_info()
#         human_1 = super().get_info()
#         return f'{human_1}. Position - {self.position}. Salary - {self.salary}'
#
# igor = Human("M",0)
# print(igor.get_info())
# orest = Employee("M",25,"manager","30000")
# print(orest.get_info())

# class A:
#
#     def __init__(self,val):
#         self.val = val
#
#     def __add__(self, other):
#         return self.val + other.val + 1
#
# a1 = A(2)
# a2 = A(2)
# print(a1 + a2)
#
# class A:
#
#     def __init__(self,val):
#         self.val = val
#
#     def __str__(self):
#         return(f'The Value i"ve got is {self.val}!')
#
# a1 = A(2)
# print(a1)

# class A:
# # витягую обєкт
#     def __init__(self, val):
#         self.val = val
#
#     def __getattr__(self, item):
#         # if item not in dir(self):
#         #     print(f'The is no such attribule - {item}')
#         #     self.item = 1
#         if self.item:
#             print("Yes")
#
#     def __setattr__(self, key, value):
#         self.__dict__[key] = value
#         print('Yes u did it')
#
#     def __call__(self, num1, num2):
#         return num1 + num2
#
# a1 = A(2)
# print(a1(1,1))

from Storage import FileStorage
from Task import Task

class TodoApp():

    def __init__(self,storage):
        self.storage = storage

    def add_task(self):

        while True:
            task = input('Please enter task: ')
            priority = input('Enter priority: ')
            deadline = input("Is any deadline?: ")
            if task and priority:
                task = Task(task, priority, deadline)
                self.storage.save_data(task)
            if not input('Press enter to exit'):
                break

    def get_tasks(self):
        data = self.storage.get_data()


file_storage = FileStorage()
