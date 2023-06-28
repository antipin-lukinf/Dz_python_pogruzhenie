"""
Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях.
 Известно, что на доске 8×8 можно расставить 8 ферзей так,
  чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
  определите, есть ли среди них пара бьющих друг друга. Программа получает
  на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
  Если ферзи не бьют друг друга верните истину, а если бьют - ложь. []
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел
 для случайной расстановки ферзей в задаче выше.
  Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""
import random

desc = [['*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*', '*', '*'],
        ]

DESC_SIZE = 8

# Координаты для проверки a7, b4, c2, d8, e6, f1, g3, h5

x_sp = []
y_sp = []
def inp_x_y_rand(DESC_SIZE):
    for i in range(DESC_SIZE):
        # x = int(input("Введите координату х (от 1 до 8, вкл) : "))
        # if 1 <= x < 9:
        #     x_sp.append(x)
        # else:
        #     print('координата введена не корректно')
        #     break
        # y = int(input("Введите координату y (от 1 до 8, вкл) : "))
        # if 1 <= x < 9:
        #     y_sp.append(y)
        # else:
        #     print('координата введена не корректно')
        #     break
        x_sp.append(random.randint(1, 8))
        y_sp.append(random.randint(1, 8))

    # print(f'Координаты x : {x_sp}')
    # print(f'Координаты y : {y_sp}')
    return x_sp, y_sp


def queens_8_rand(inp_x_y_rand, DESC_SIZE):
    inp_x_y_rand(DESC_SIZE)
    zn = True
    for i in range(DESC_SIZE):
        for j in range(i + 1, DESC_SIZE):
            if x_sp[i] == x_sp[j] or y_sp[i] == y_sp[j] or (x_sp[i] - x_sp[j]) == (y_sp[i] - y_sp[j]):
                zn = False

    return zn, x_sp, y_sp



print()
spis_position_x = []
spis_position_y = []
count = 0
while True:
    if queens_8_rand(inp_x_y_rand, DESC_SIZE):
        spis_position_x.append(x_sp)
        spis_position_y.append(y_sp)
        count += 1
    if count == 4:
        print(spis_position_x)
        print(count)
        print(spis_position_y)
        break