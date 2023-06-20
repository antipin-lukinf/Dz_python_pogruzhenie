"""
✔ Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление.
"""
dict_key = {}

def my_dict(**kwargs):
    for key, value in kwargs.items():
        dict_key[key] = value
        dict_key[value] = key
    return dict_key



print(my_dict(arg_1=5, arg_2=9))
