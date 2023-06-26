"""
Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и
пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

"""
import random

number_up = int(input('Введите верхнюю границу диапазона : '))
number_down = int(input('Введите нижнюю границу диапазона : '))
count = int(input('Введите количество попыток : '))

def wtf(number_up, number_down, count):
    numb_rand = random.randint(number_down, number_up)

    for i in range(count):
        my_number = int(input(f'Угадай число, которое я загадал, у тебя осталось {count - i} попыток :'))
        if my_number < numb_rand:
            print(f'мое число больше, у тебя осталось {count - i - 1} попыток')
        elif my_number > numb_rand:
            print(f'мое число меньше, у тебя осталось {count - i - 1} попыток')
        elif my_number == numb_rand:
            return True

print(wtf(number_up, number_down, count))