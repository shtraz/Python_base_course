"""
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
"""

"""
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
"""


def action():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Удалить запись из справочника\n"
          "6. Сохранить справочник в текстовом формате\n"
          "7. Закончить работу\n")


def show_menu() -> int:
    choice = int(input())

    return choice


def work_with_phonebook():
    choice = show_menu()
    file_name = 'phonebook.csv'
    phone_book = read_csv(file_name)
    # phone_book = 'phonebook.csv'

    while (choice != 7):
        if choice == 1:
            print_result(file_name)
            action()
        elif choice == 2:
            surename = get_search_name()
            # print(*(find_by_name(phone_book, surename))) # или так
            print(find_by_name(phone_book, surename))
            action()
        elif choice == 3:
            number = get_search_number()
            print(find_by_number(phone_book, number))
            action()
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_csv(file_name, user_data)
            action()
        elif choice == 5:
            user = get_delete_user()
            # print(delete_user(phone_book, user))
            update_data = delete_user(phone_book, user)
            update_csv(file_name, update_data)
            action()
        elif choice == 6:
            new_file_name = get_file_name()
            write_txt(new_file_name, phone_book)
            action()
        choice = show_menu()


# Считываю первичный файл
def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)

    return data


# Вывожу в консоль информацию из фала
def print_result(filename) -> list:
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            print(line)


# Или так делаем, но тогда phone_book = read_csv('phonebook.csv')
# def print_result(data) -> list:
# print(*data, sep='\n')

# Ввожу фамилию для поиска
def get_search_name():
    surename = input("Введите фамилию для поиска: ")
    return surename


# Осуществоляю поиск по фамилии
def find_by_name(data, surename) -> str:
    for contact in data:
        if contact['Фамилия'].lower() == surename.lower():
            return (f"Фамилия: {contact['Фамилия']}\nИмя:"
                    f" {contact['Имя']}\nТелефон: "
                    f"{contact['Телефон']}\nОписание: {contact['Описание']}")
    return "Такого пользователя нет"

    # Или так
    # for key in data:
    #     if key['Фамилия'].lower() == surename.lower():
    #         return list(key.values())
    #     return "Такого пользователя нет"


# Ввожу телефон для поиска
def get_search_number():
    number = input("Введите телефон для поиска: ")
    return number


# Осуществоляю поиск по телефону
def find_by_number(data, number) -> str:
    for contact in data:
        if contact['Телефон'] == number:
            return (f"Телефон: {contact['Телефон']}\nФамилия:"
                    f" {contact['Фамилия']}\nИмя: "
                    f"{contact['Имя']}\nОписание: {contact['Описание']}")
    return 'Такого телефона нет в базе'


# Запрашиваю данные для нового контакта
def get_new_user() -> dict:
    surname = input("Введите фамилию нового контакта: ")
    name = input(f"Введите имя для контакта {surname}: ")
    number = input(f"Введите телефон для контакта {surname} {name}: ")
    description = input(f"Введите описание для контакта {surname} {name}: ")
    user_data = {
        'Фамилия': surname,
        'Имя': name,
        'Телефон': number,
        'Описание': description
    }
    print(f"Контакт {surname} {name} успешно добавлен!")

    return user_data


# Добавляю новый контакт в список в виде словаря
def add_user(data, user_data) -> dict:
    data.append(user_data)
    return data


# Записываю изменения в исходный файл
def write_csv(filename, user_data) -> list:
    with open(filename, 'a', encoding='utf-8', newline='') as fin:
        fin.write('\n')
        fin.write(','.join(user_data.values()))


# Запрашиваю телефон пользователя на удаление
def get_delete_user() -> str:
    delete_user = input("Введите телефон пользователя для удаления: ")
    return delete_user


# Удаляю пользователя из списка data
def delete_user(data: list, delete_user: str) -> str:
    for i in range(len(data)):
        if data[i].get('Телефон') == delete_user:
            del data[i]
            print(f'Контакт с номером {delete_user} успешно удален!')
            return data
        return f'Номера {delete_user} нет в справочнике!'


# Перезаписываю файл .csv српвочника с учетом удаленных пользователей
# Не работает на новые (добавленные записи в процессе программы) записи.
# Так как их нет в сформированном ранее списке data при помощи read_csv()
# Удаляет все данные из файла. Не решил проблему. Прошу подсказать как
# обновить список data.
def update_csv(filename, data) -> list:
    with open(filename, 'w', encoding='utf-8') as fin:
        for line in data:
            fin.write(','.join(line.values()))
            fin.write('\n')


# Запрашиваю название файла .txt в который хочу сохранить данные
def get_file_name() -> str:
    file_name = input("Введите название нового файла: ")
    file_extension = '.txt'
    new_file_name = ''.join([file_name, file_extension])
    return new_file_name


# Сохраняю данные справочника в новый файл .txt
def write_txt(new_file_name, data) -> str:
    with open(new_file_name, 'a', encoding='utf-8', newline='') as fin:
        for line in data:
            fin.write(','.join(line.values()))
            fin.write('\n')
    print(f'Файл успешно сохранен с названием {new_file_name}!')


action()
work_with_phonebook()
