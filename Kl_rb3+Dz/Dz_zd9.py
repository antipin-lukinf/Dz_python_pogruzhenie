"""
 Дан список повторяющихся элементов. Вернуть список
с дублирующимися элементами. В результирующем списке
не должно быть дубликатов.
"""
from itertools import count

my_list = [1, 1, 1, 5, 5, 9, "hi", "di", "hi"]
double_list = []

for el in my_list:
    count = my_list.count(el)
    if count > 1:
        if el not in double_list:
            double_list.append(el)

print(double_list)
