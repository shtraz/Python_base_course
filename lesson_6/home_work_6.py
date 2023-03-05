"""
Урок 6. Повторение списков
Задача 30:  Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""

a1 = int(input("Введите значение начальное число а1: "))
d = int(input("Введите значение разности d: "))
n = int(input("Введите количество элементов n: "))
an = None

for i in range(n):
    an = a1 + i * d
    print(an)

"""
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""

from random import randint

number_list = [randint(-9, 9) for i in range(int(input("Введите количество "
                                                 "элементов списка: ")))]
print(number_list)

min_number = int(input("Введите значение минимума: "))
max_number = int(input("Введите значение максимума: "))

for i in range(len(number_list)):
    if min_number <= number_list[i] and min_number <= max_number:
        print(i)