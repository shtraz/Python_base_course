"""Транспонирование матрицы"""

old_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
new_list = zip(*old_list)
print(list(new_list))  # -> [('a', 'c', 'e'), ('b', 'd', 'f')]
