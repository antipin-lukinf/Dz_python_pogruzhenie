"""
Задание №8
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""

first_variable = 1
second_s = "kgkhgiyg"
third_variable = True
forth_var_s = 3.7
s = 0

def my_replace(**kwargs):
    globals()
    for i, e in kwargs.items():
        result_dict = []
        if len(i) != 1 and i.endswith("s"):
            i = i[:len(i)-1]
            e = None
        result_dict.append(e)
    return result_dict

print(my_replace(first_variable=1, second_s="kgkhgiyg", third_variable = True, forth_var_s = 3.7, s = 0))

a = 5
b = 7
cs = "sldfnsld"

for item in globals().copy():
    if not item.startswith('__'):      # если переменная не начинается с __
        if item.endswith('s'):        # если переменная заканчивается на 's'
            if len(item) > 1:
                new_name = item[:-1]    # убираем последний символ переменной
                globals()[new_name] = None
            else:
                globals()[item] = globals().get(item)  # если переменная s возвращаем s обратно

print(globals())

