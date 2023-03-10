"""
Задание 1.

Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.

Пример:
Введите ваше имя: Василий
Введите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
"""

user_name = input("Введите ваше имя: ")
user_password = input("Введите ваш пароль: ")
user_age = int(input("Введите ваш возраст: "))

if user_age < 18:
    print(f'Регистрация доступна лицам достигшим 18-и лет!\n Ваш '
          f'возраст: {user_age}')
else:
    print(f'Спасибо за регистрацию!\n Ваш login: '
          f'{user_name[0].upper()}{user_name[1::]}\n Ваш '
          f'пароль: {user_password}\n Ваш возраст: {user_age}')

"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

user_time = int(input("\nВведите количество секунд: "))

print(f'Ваше время в формате ч:м:с: - {user_time // 3600} : '
      f'{(user_time // 60)} : {user_time}')

print(f'Точное время ч:м:с - {user_time // 3600}:'
      f'{(user_time % 3600) // 60}:'
      f'{user_time % 3600 % 60}')

"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

user_number = input("\nВведите число n: ")
second_number = int(user_number) * 2
last_number = int(user_number) * 3

print(f'Результат соединения строк: '
      f'{user_number + str(second_number) + str(last_number)}')

"""
Задание 4.

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.

Пример:
Введите выручку фирмы: 1000
Введите издержки фирмы: 500
Финансовый результат - прибыль. Ее величина: 500
Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
Рентабельность выручки = 0.5
Введите численность сотрудников фирмы: 10
Прибыль фирмы в расчете на одного сотрудника = 50.0
"""

income = int(input("\nВведите выручку фирмы: "))
expense = int(input("Введите издержки фирмы: "))

if income > expense:
    print(f'Прибыль фирмы больше чем издержки.\nПрибыль = '
          f'{income - expense}₽\nРентабельность фирмы: '
          f'{round((expense / income) * 100, 2)}%\n')

    employees = int(input("Введите численность сотрудников фирмы: "))
    print(f'Прибыль фирмы в расчете на одного сотрудника = '
          f'{(income - expense) / employees}')

elif income == expense:
    print(f'Прибыль фирмы равна сумме затрат.\nПрибыль = '
          f'{income - expense}₽\nРентабельность фирмы: '
          f'{0}%')

else:
    print(f'Прибыль фирмы меньше суммы затрат.\nПотери = '
          f'{income - expense}₽\nРентабельность фирмы: '
          f'{round((income / expense) * 100, 2)}%')
