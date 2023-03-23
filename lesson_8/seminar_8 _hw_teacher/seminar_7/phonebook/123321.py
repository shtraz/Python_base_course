import logging

logging.basicConfig(level=logging.ERROR)

name = input("Введите свое имя: ")
logging.info("Произведен вход в систему")
opros = input("Пройдите опрос: 1 или 2?")
logging.error("Опрос пройден")