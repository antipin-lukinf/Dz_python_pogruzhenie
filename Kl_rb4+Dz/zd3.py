"""
Задание №3
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
"""

string_numb = "8 1"
uni_dict = {}


def my_dict(string_numb):
    string_numb = string_numb.split(" ")
    for i in string_numb:
        uni_dict[ord(i)] = i
    return uni_dict


print(my_dict(string_numb))