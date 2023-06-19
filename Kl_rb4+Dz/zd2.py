"""
Задание №2
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""

from operator import itemgetter

string_str = "Напишите функцию, которая принимает строку текста"
uni_list = list()


def my_list(string_str):
    mod_str = list(string_str)
    for i in mod_str:
        uni_list.append([ord(i)])

    return uni_list.sort()


my_list(string_str)

print(uni_list)
