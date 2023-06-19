texts = ["Привет", "ЗДОРОВО", "ПривяУ"]
res = map(lambda x: x.lower(), texts)
print(*res)     # Для распаковки map нужна звездочка *


numbers = [42, -73, 1024]
res = tuple(filter(lambda x: x > 0, numbers)) # выбор из последовательности элементов больше 0
print(res)          # чтобы не указывать звездочку в 7 строке указали, что на выходе нужен кортеж


names = ["Иван", "Николай", "Петр"]
salaries = [125_000, 96_000, 109_000] # Зарплата
awards = [0.1, 0.25, 0.13, 0.99] # премия
for name, salary, award in zip(names, salaries, awards):            # zip собирает значения с трех последовательностей
    print(f'{name} заработал {salary: .2f} денег и премию {salary * award: .2f} ')