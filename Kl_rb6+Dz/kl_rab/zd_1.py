"""
Вспомните какие модули вы уже проходили на курсе.
Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами. (3-7 строк импорта).

"""
import random as r
from random import randint as rd
from sys import argv as ar

my_number = r.randint(1, 10)
my_number_1 = rd.__eq__(1)
my_number_2 = ar.count(1)
