'''
Задание №7
📌 Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
📌 Для цифры верните её квадрат, например 5 - 25
📌 Для двузначного числа произведение цифр, например 30 - 0
📌 Для трёхзначного числа его зеркальное отображение, например 520 - 25
📌 Если число не из диапазона, запросите новое число
📌 Откажитесь от магических чисел
📌 В коде должны быть один input и один print
'''

def input_number():
    number = input("Введите число от 1 до 999 : ")


    if len(number) == 1:
        number = int(number) ** 2

    elif len(number) == 2:
        [int(i) for i in str(number)]
        y = number[0]
        x = number[1]
        number = int(x) * int(y)
        # number = number[0] * number[1]
        # number1 = number[1] * number[2]
        # number = number1

    elif len(number) == 3:
        [int(i) for i in str(number)]
        number1 = number[::-1]
        number = number1

    else: number = -1

    return number

if __name__ == '__main__':
    number = input_number()
    if number != -1:
        print(number)
    else: print('Данные не корректны')
