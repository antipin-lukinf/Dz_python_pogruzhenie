"""
Задание №7
✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
"""

dict_of_company = {'intel': (1000, 2997455, 213254847, 147236),
                   'balalaika_company': (454231, 65412158, 555555555555555),
                   'QWE': (12345, 536, 789)}


def sum_items(list):
    summa = 0
    for value in list:
        summa += value
    return summa


def get_plus_of_companis(dict_of_company):
    redy = True
    for value in dict_of_company.values():
        if sum(value) < 0:
            return False
    return True


print(get_plus_of_companis(dict_of_company))
