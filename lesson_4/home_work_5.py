"""
Урок 4. Словари, множества и профилирование
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
"""

from random import randint

list_one = [randint(0, 20) for i in range(int(input("Введите количество "
                                                    "элементов первого списка: ")))]

list_two = [randint(0, 20) for i in range(int(input("Введите количество "
                                                    "элементов второго списка: ")))]

result = set(list_one).intersection(set(list_two))

# Для проверки:
# print(list_one)
# print(list_two)
# print(result)

if len(list(result)) > 0:
    for i in sorted(list(result)):
        print(i, end=' ')
else:
    print("Повторяющихся значений не найдено")

"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
Она растет на круглой грядке, причем кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. 
Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора 
на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, 
которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.
"""

count_bush = int(input("\nВведите количество кустов: "))
bush_list = []
list_berries = []
max_berries = 0

for el in range(count_bush):
    berries = int(input(f'Введите количество ягод на кусте № {el + 1}: '))
    bush_list.append(berries)

for i in range(len(bush_list)):
    print(f'На кусте № {i + 1} растет {bush_list[i]} ягод')

for i in range(len(bush_list) - 1):
    list_berries.append(bush_list[i] + bush_list[i - 1] + bush_list[i + 1])
list_berries.append(bush_list[-2] + bush_list[-1] + bush_list[0])

for el in list_berries:
    if el > max_berries:
        max_berries = el

print(f'Максимум можно собрать ягод: {max_berries} шт.')
