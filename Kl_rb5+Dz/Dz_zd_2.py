"""
✔Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида «10.25%».
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии
"""

names = ['Dave', 'Kolia', 'Vasia']
solarys = [40_000, 20_000, 100_000]
bonus = ['15.25', '30.1', '10.15']


def gen_dict(names: list[str], solarys: list[int], bonus: list[str]):

    yield {d[0]: d[1] for d in
           list(map(lambda y: (y[0], ((y[1] * y[2] / 100) + y[1])), zip(names, solarys, map(lambda x: float(x), bonus))))}


print(names)
print(solarys)
print(bonus)
print(*gen_dict(names, solarys, bonus))