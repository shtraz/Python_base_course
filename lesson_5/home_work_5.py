"""
Задание 1. Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""

# flag = True

def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    else:
        return a / b


def is_correct_operator(operator):
    return operator == '0' or operator == '+' or operator == '-' or operator == '*' or operator == '/'


def get_operator():
    return input('operator: ')


def run_calculator(a=None, b=None):
    if a is None:
        a = float(input('a: '))
    if b is None:
        b = float(input('b: '))
    operator = get_operator()

    if not is_correct_operator(operator):
        print('Wrong operator')
        run_calculator(a, b)
        return
    elif operator == '0':
        return
    elif operator == '/' and b == 0:
        print('No division by zero')
        run_calculator()
        return
    else:
        print(calculate(a, b, operator))
        run_calculator()


run_calculator()


# def calc():
#     operation = input("Введите операцию (+, -, *, / или 0 для выхода): ")
#     number_one = int(input("Введите первое число: "))
#     number_two = int(input("Введите второе число: "))
#     if operation == 0:
#         print("END")
#     else:
#         if operation == '+':
#             return number_one + number_two
#         elif operation == '-':
#             return number_one - number_two
#         elif operation == '*':
#             return number_one * number_two
#         elif operation == '/':
#             return number_one / number_two
#         calc()
#
# print(calc())

# while flag:
#     number_one = int(input("Введите первое число: "))
#     operation = input("Введите операцию ('0' - выход, '+' - сложить, '-' - вычесть, '*' - умножить, '/' - разделить: ")
#     number_two = int(input("Введите втоное число: "))
#     continue_operation = int(input("Для выхода из программы введите '0': "))
#     if continue_operation == 0:
#         flag = False
#         print("Программа завершена")
#
#
# def calculate(number_one, operation, number_two):
#     if operation == '+':
#         return number_one + number_two
#     elif operation == '-':
#         return number_one - number_two
#     elif operation == '*':
#         return number_one * number_two
#     else:
#         return number_one / number_two
#
# print(calculate(number_one, operation, number_two))