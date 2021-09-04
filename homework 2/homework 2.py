#Task 1

word = str(input("Please, write your sentence "))
for letter in word:
    if letter in str("aiueoy") :
        print(word.count(letter))
#
#
# #Task 2
#Користувач вводить стрічку. Всі літери в верхньому реєстрі перевести в
#нижній і навпаки. Вивести результат до і після змін.

str = input("please, write your sentence ")
print(str)
print(str.swapcase())

# #task 3
# витащити домен з "http://github.com/carbonfive/test"

from urllib.parse import urlparse

domans = urlparse(input("Type the url "))
print(domans.netloc)

# #task 4
#
nam = input("Type the words ")
for letter in nam:
    if letter in ('"ABCDEFGHIJKLMNOPQRSTUVWXYZ"'):
        print("This letter is capitalized: " + letter)
    elif nam.islower():
        print("All letters are lowercase")
        break