"""
Задание №4
✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды.
"""

my_list = [1, 3, 0, 5, 4, 2, 5, 5, 0, 2, 5, 3]
i = 0
while i < len(my_list):
    if my_list.count(i) == 2:
        my_list.remove(i)
        my_list.remove(i)
    else:
        i += 1

print(my_list)