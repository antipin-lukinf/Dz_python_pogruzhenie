"""
Задание №5
✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии.
"""

names = ["Иванов", "Петров", "Сидоров"]
salarys = [50_000, 70_000, 200_000]
prizes = ["50%", "40%", "10.25%"]




def that_zp(names, salarys, prizes):
    for name, salary, prize in zip(names, salarys, prizes):
        print(f'имя : {name}, оклад : {salary}, премия : {prize}')
        # print(f'имя : {name}, оклад + премия : {salary * (salary/100 * prize)}')



that_zp(names, salarys, prizes)
