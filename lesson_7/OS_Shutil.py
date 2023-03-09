import os
import shutil

# os.chdir(path) - смена тикущей дириктории
# os.chdir('C:/Users/123123132/Python/asdasd')

# os.getcwd() - текущая рабочая директория
print(os.getcwd())


# os.path - вложенный модуль в os
# os.path.basename(path) - базовое имя пути
print(os.path.basename('E:\GB\Python\Python base practice\lesson_7/file.txt'))


# os.path.abspath(path) - возвращает абсолютный путь
path = 'file.txt'
print(os.path.abspath(path))


#===========================================================
# shutil - содержит набор функций высоко порядка для обработки файлов,
# групп файлов и папок.

# shutil.copyfile(src, dst) - копирует содержимое (но не метаданные) файла
# scr в файл dst

# shutil.copy(src, dst) - копирует содержимое файла src в файл или папку dst

# shutil.rmtree(path) - удаляет текущую дтректорию и все поддиректории. path
# должен указывать на директорию, а не на символическую ссылку