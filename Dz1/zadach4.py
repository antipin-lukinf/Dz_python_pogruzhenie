"""
4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
 Программа должна подсказывать «больше» или «меньше» после каждой попытки.
"""

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)

for i in range(10):
    inp_numb = int(input('Введите число, которое я загадал (диапазон 0-1000) :'))
    print(f'у вас осталось {9 - i} попыток')

    if inp_numb < num:
        print('Ваше число меньше ')

    if inp_numb > num:
        print('Ваше число больше')

    if inp_numb == num:
        print('Вы угадали')
        break

print(f'я загадал число {num}')