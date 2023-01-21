# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# # - 6782 -> 23
# # - 0,56 -> 11
# import os
# os.system('cls')
# num = float(input("Введите число: "))
# s = list(str(num))
# result = 0
# for i in s:
#     if i.isdigit():
#         result += int(i)
# print(result)

import os
os.system('cls')

num = input('Введите вещественное число: ')
sum = sum(map(int, num.replace('.', '')))
print (sum)