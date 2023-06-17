"""
Создайте словарь со списком вещей для похода в качестве
ключа и их массой в качестве значения. Определите какие
вещи влезут в рюкзак передав его максимальную
грузоподъёмность. Достаточно вернуть один допустимый вариант.
"""

back_pack = {"Спички": 2,
             "Вода": 5,
             "Гитара": 10,
             "Спининг": 9
             }

back_pack_size = int(input("Введите размер рюкзака : "))


def loading(back_pack, back_pack_size):
    max_size = 0
    temp_size = 0
    exit_back = []
    for value in back_pack.values():
        max_size += value

    if max_size <= back_pack_size:
        print("Ура, влезли все вещи")
    else:
        for key, value in back_pack.items():
            if (temp_size + value) < back_pack_size:
                temp_size += value

                exit_back.append(key)

    return print(exit_back)




loading(back_pack, back_pack_size)
