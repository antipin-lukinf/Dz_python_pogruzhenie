"""
Задание №8
✔ Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.
"""
import collections

gear = {"Dima": ("вода", "соль", "палатка", "спички"),
        "Oleg": ("спички", "вода", "удочка", "соль"),
        "Vasia": ("мясо", "вода", "спининг", "спички"),
        }

gear_people = tuple()

for value in gear.values():
    gear_people += value


print(gear_people)
count_gear = collections.Counter(gear_people)
print("Все вещи, с указанием количества : ", count_gear)


for value in count_gear:
    if gear_people.count(value) == 1:
        print("Уникальный элемент : ", value)
    if gear_people.count(value) == 2:
        print("Вещь есть у двух друзей : ", value)


gear_people_set = set(gear_people)  # убираем копии вещей


for value in gear.values():
    gear_people_set.intersection_update(set(value))

print("Вещи, которые есть у всех : ", gear_people_set)
