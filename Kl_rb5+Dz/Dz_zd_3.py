"""
✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).
"""


# Фвкториал
def factorial(n):
    number = 1
    result = []
    for i in range(1, n + 1):
        number *= i
        result.append(number)
    return result


# for i, num in enumerate(factorial(10), start=1):
#     print(f'{i}! = {num}')


# Фибоначи
def gen_fib(n):
    n1, n2 = 1, 1
    for i in range(1, n + 1):
        if i < 3:
            yield 1
        else:
            yield n1 + n2
            n1, n2 = n2, n1 + n2

print(*(gen_fib(10)))



