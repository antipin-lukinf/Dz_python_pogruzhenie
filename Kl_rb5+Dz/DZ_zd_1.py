"""
✔Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
 Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""
from typing import Tuple

# link = 'https://docs.python.org/3/faq/programming.html#how-can-i-pass-optional-or-keyword-parameters-from-one-function-to-another'
# prefix, *_, suffix = link.split('/')
#
#
# print(*(_))

absolut_path = "C:\\Users\\antip\\PycharmProjects\\DZ_python\\Kl_rb5+Dz\\DZ_zd_1.py"

def put(path: str) -> tuple[str, str, str]:
    # my_tuple = (prefix, *_, suffix = absolut_path.split('\'))

    path_only, _, file_name = path.rpartition('\\')
    file_name, _, file_ext = file_name.rpartition(".")
    return path_only, file_name, file_ext

print(put(absolut_path))