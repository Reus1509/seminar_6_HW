# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import randint

# number = int(input('Введите размер списка '))
# new_list = []
# result = []


# def create_new_list(number):
#     for i in range(number):
#         new_list.append(randint(0, 9))
#     return new_list


# def umnozh(new_list, number):
#     for i in range(len(new_list)):
#         while i < len(new_list)/2 and number > len(new_list)/2:
#             number = number - 1
#             a = new_list[i] * new_list[number]
#             result.append(a)
#             i += 1
#     return result


# new_list = create_new_list(number)
# print(new_list)
# result = umnozh(new_list, number)
# print(result)
import math
list_a = list(map(int, input('Введите числа, через пробел: ').split()))
print('Исходный список: ',list_a)
print('Результат: ',list([a*b for a,b in zip(list_a[0:math.ceil(len(list_a)/2)],list_a[::-1])]))