import pandas as pd
import random

# Задание 44
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data.head())

# Решение. Запускать в Collab Notebooks
data = pd.DataFrame(random.sample(['robot', 'human'], counts=[10, 10],
                                  k=20), columns={'whoAmI'})
print(data.head(20))
