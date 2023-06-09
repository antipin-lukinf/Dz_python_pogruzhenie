"""
Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.


5.
Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками.
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

6.
Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
Функция формирует словарь с информацией о результатах отгадывания.
Для хранения используйте защищённый словарь уровня модуля.
Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
Для формирования результатов используйте генераторное выражение.

"""

def zagadka(sagadka: str, answers: list, count: int=5):
    print(sagadka)
    try_ = 1
    while count:
        user_ansver = input('Ваш ответ: ').lower()


        if user_ansver in answers:
            return try_

        try_ += 1
        count -= 1

    return 0


def puzzle():
    puzzles = {'Зимой и летом одним цветом': ['ёлка', 'ель', 'елка'],
               'Висит груша - нельзя скушать': ['лампочка', 'лампа'],
               'Не лает не кусает - в дом не пускает': ['замок', 'замочек'],
               }

    for key, value in puzzles.items():
        fun_2(key, zagadka(key, value))

    print(_result_dict)


_result_dict = {}
def fun_2(zagad: str, number: int):
    _result_dict[zagad] = number

def result_():
    for key, item in _result_dict.items():
        print(f'Загадка - {key}, угадана с {item} раз')




