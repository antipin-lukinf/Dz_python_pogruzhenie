"""
3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
 Используйте правило для проверки:
 “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""

number = int(input("Введите число в диапазоне от 0 до 100 000  :  "))
j = 0
i = 1
if (100_000 > number) and (number > 0):

    for i in range(0, number):
        x = number % (i+1)
        # print(x)

        if (x == 0):
            j += 1
            print(j)
    if j <= 2:
        print("число простое")
    if j > 2:
        print("число составное")

else:
    print("Введены не корректные данные")
