"""
✔ Напишите программу, которая получает целое
число и возвращает его шестнадцатеричное
строковое представление. Функцию hex
используйте для проверки своего результата
"""

def gonext(number, sustem):
    result = 0
    ost = 0
    rezString = ''
    while True:
        result = number // sustem
        ost = number % sustem
        if ost == 10: ost = 'A'
        if ost == 11: ost = 'B'
        if ost == 12: ost = 'C'
        if ost == 13: ost = 'D'
        if ost == 14: ost = 'E'
        if ost == 15: ost = 'F'


        if result < sustem:
            rezString = rezString + str(ost) + str(result)
            break
        else:
            number = result
            rezString = rezString + str(ost)

        prov = print(f'Проверка {hex(number)}')
    return rezString[::-1]     # СРЕЗ, реверс строки


integer1 = int(input('Введите целое число : '))

print(gonext(integer1, 16))


