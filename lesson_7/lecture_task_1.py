# В списке хранятся числа. Нужно выбрать только четные числа и составить
# список пар (число, квадрат числа).

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
#
# for i in data:
#     if i % 2 == 0:
#         res.append((i, i * i))
#
# print(res)



#=========================================================
# def select(f, col):
#     return [f(x) for x in col]


# def where(f, col):
#     return [x for x in col if f(x)]


data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# res = map(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
res = list(filter(lambda x: x % 2 == 0, data))
print(res)
# res = select(lambda x: (x, x * x), res)
res = list(map(lambda x: (x, x * x), res))
print(res)
#=========================================================