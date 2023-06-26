"""
Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и
пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

3.
Улучшаем задачу 2.
Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.


"""
import random


# number_up = int(input('Введите верхнюю границу диапазона : '))
# number_down = int(input('Введите нижнюю границу диапазона : '))
# count = int(input('Введите количество попыток : '))

def gues_f(minimum, maximum, tries):
    numb_rand = random.randint(minimum, maximum)

    while tries:
        my_number = int(input('Угадай число, которое я загадал :'))
        if my_number == numb_rand:
            print('Угадал')
            break
        else:
            if my_number < numb_rand:
                print('мое число больше')
            else:
                print('мое число меньше')

        tries -= 1

    else:
        print(f'Вы не угадали, было загаданно число {numb_rand}')


# if __name__ == "__main__":
#     print(wtf(number_up, number_down, count))