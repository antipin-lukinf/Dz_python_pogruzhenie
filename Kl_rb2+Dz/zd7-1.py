"""
Напишите программу, которая принимает две строки
вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму
и *произведение дробей. Для проверки своего
кода используйте модуль fractions
"""


pars_str = input("Ведите простую дробь через / : ")
pars_str_1 = input("Ведите простую дробь через / : ")

numb_0 = pars_str.split('/')
numb_1 = int(numb_0[0])
numb_2 = int(numb_0[1])

numb_00 = pars_str_1.split('/')
numb_3 = int(numb_00[0])
numb_4 = int(numb_00[1])  # 1/2 + 3/5

if numb_4 == numb_2:
    sum_chislit = numb_1 + numb_3
    sum_znamenat = numb_4
    mult_chislit = numb_1 * numb_3
    mult_znamenat = numb_2 * numb_4

    print(f'Сумма дробей', sum_chislit,'/',sum_znamenat)
    print(f'Произведение дробей', mult_chislit, '/', mult_znamenat)

if numb_4 != numb_2:
    sum_chislit = (numb_1 * numb_4) + (numb_3 * numb_2)
    sum_znamenat = numb_4 * numb_2                              #2/2 + 3/2
    mult_chislit = numb_1 * numb_3
    mult_znamenat = numb_2 * numb_4

    print(f'Сумма дробей', sum_chislit, '/', sum_znamenat)
    print(f'Произведение дробей', mult_chislit, '/', mult_znamenat)
