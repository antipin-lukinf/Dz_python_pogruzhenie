"""
Задание №6
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""

spis_number = [1, 6, 7, 8, 3, 18, 2]


def sum_numb(spis_number, index_start=2, index_stop=6):
    new_spis_number = spis_number[index_start:index_stop+1]
    print(new_spis_number)

    return sum(new_spis_number)


print(sum_numb(spis_number, 1, 3))
