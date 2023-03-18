"""
Задачи из семинара
"""

"""
Сергей Сердюк: 1.Вводится список целых чисел в одну строчку через пробел. 
Необходимо оставить в нем только двузначные числа. 
Реализовать программу с использованием функции filter. 
Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.

пример - 8 11 0 -23 140 1 => 11 -23
"""

from random import randint

# Решение через метод filter
list_numbers = [randint(-200, 200) for i in
                range(int(input("Введите количество "
                                "элементов списка: ")))]
print(list_numbers)
print(list(filter(lambda x: abs(x) > 9 and abs(x) < 100, list_numbers)))


# Решение через свою функцию
def double_numbers(f, list_numbers):
    return [x for x in list_numbers if f(x)]


print(double_numbers(lambda x: abs(x) > 9 and abs(x) < 100, list_numbers))

# Решение преподавателя через строки
print(*filter(lambda x: len(str(abs(int(x)))) == 2, input("Введите "
                                                          "числа "
                                                          "чере "
                                                          "пробел: ").split()))

"""
Сергей Сердюк: Вводится натуральное число N. 
С помощью list comprehension сформировать двумерный список размером N x N, состоящий из нулей, 
а по главной диагонали - единицы. 
(Главная диагональ - это элементы, идущие по диагонали от верхнего левого угла матрицы до ее нижнего правого угла). 
Результат вывести в виде таблицы чисел как показано в примере ниже.


Sample Input:
4
Sample Output:
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
"""

# Решение преподавателя
n = 4
res = [[1 if i==j else 0 for i in range(n)] for j in range(n)] # Первая
# итерация i = 0, j = 0 True, i = 0, j = 1, i = 1, j = 2, i = 2, j = 3.
# Вторая итерация i = 1, j = 0 - False, i = 1, j = 1 - True и так далее по
# этажам
for i in res:
    print(*i)


# Решение студента
def get_matrix(n):
    return [[int(i == j) for i in range(n)] for j in range(n)]

print(*get_matrix(4), sep='\n')

"""
Сергей Сердюк: 3. Преобразовать набора списков
users = ['user1','user2','user3','user4','user5']
ids = [4, 5, 9, 14, 7]
salary = [111,222,333]
в другой набор

['user1', 4, 111]
['user2', 5, 222]
['user3', 9, 333]
"""

# Мое неверное решение
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
res = list(zip(users, ids, salary))
print(res)

res_new = list(zip(*res))
print(res_new)

# Решение преподавателя
users = ['user1','user2','user3','user4','user5']
ids = [4, 5, 9, 14, 7]
salary = [111,222,333]

a,b,c = map(list,zip(users, ids, salary))
print(a,b,c, sep="\n")
a,b,c= map(list,zip(a,b,c))

print(a,b,c, sep="\n")

"""
Сергей Сердюк: Вводится строка. Требуется, используя введенную строку, 
сформировать N=10 пар кортежей в формате:
(символ, порядковый индекс)
Первый индекс имеет значение 0. Строка может быть короче 10 символов, а может быть и длиннее. 
То есть, число пар может быть 10 и менее. 
Используя функцию zip сформируйте указанные кортежи и сохраните в список с именем lst.
"""

a = 'asasasasas'
lst = list(zip(a, range(0, 11)))
print(lst)

