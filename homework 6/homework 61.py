with open("homework 661.txt", "w+", encoding="utf-8") as file:
    file.write('Hello! My name is Arsen! Nice to meet you! Currently, I"m residing in Kyiv city and working as a Data\n'
'Mining specialist in Influ2, inc. For this moment I"m studying Python language ane doing this task.\n'
'I"m going to be a Data Engineer. That"s why I started to learn this adorable language. It"s quite difficult, but I"m\n'
'doing my best. I want to automatize some processes to create the comfortable conditions from my department. As I"m working\n'
'with data, I need to learn more than Python. BTW, firstly I need to pass the basic course of Python development\n'
'Wish me good luck, as I"m going to learn something difficult and interesting in my life!!')

ffile = open("homework 661.txt", "r")

rows_num = 0
words_num = 0
chr_num = 0
for line in ffile:
  row = line.strip("\n")

  words = line.split()
  rows_num += 1
  words_num += len(words)
  chr_num += len(row)

print("This file contains ", rows_num," rows, ", words_num, " words and ",chr_num, " characters")


# print(str(q) + str(row) + str(dots))