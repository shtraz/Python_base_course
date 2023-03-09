list_1 = [x for x in range(1, 21)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)

# Превратить list строк в list список

data = '15 156 96 3 5 8 52 5'
# print(data)
# data = data.split()
# print(data)
# res = []
#
# for i in data:
#     res.append(int(i))
# print(res)

data = list(map(int, data.split()))
print(data)
