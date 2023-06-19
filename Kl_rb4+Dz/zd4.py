"""
Задание №4
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
"""

numbers = [2, 10, 6, 5, 9]


def sort_number(*args):
    min_number = numbers[1]
    for i in range(0, len(numbers) - 1):
        for j in range(0, len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp

    return numbers

print(sort_number(numbers))