decimal = 34
float1 = 4.0
string1 = 'Hello'
boolean1 = True
print('var: ', decimal, 'Type is :', type(decimal))
print('var: ', float1, 'Type is :', type(float1))
print('var: ', string1, 'Type is :', type(string1))
print('var: ', boolean1, 'Type is :', type(boolean1))

"""
Задание №2
Создайте в переменной data список значений разных типов перечислив их
запятую внутри квадратных скобок. Для каждого элемента в цикле выведи
✔ порядковый номер начиная с единицы
✔ значение
✔ адрес в памяти
✔ размер в памяти
✔ хэш объекта
✔ результат проверки на целое число только если он положительный
✔ результат проверки на строку только если он положительный
Добавьте в список повторяющиеся элементы и сравните на результаты
"""
number = 0
data = [4, 6.0, 'String', False, 6, 6.0]
integer = ''
string = ''
for el in data:
    if isinstance(el, int):
        integer = 'True'
    if isinstance(el, str):
        string = 'True'

    print('number: ', number, 'var: ', el, 'Type is :', type(el),
          'id : ', id(el), 'hash : ', hash(el), 'is integer: ', integer, )
    number += 1
    integer = ''

    """
    Задание №3
✔ Напишите программу, которая получает целое число
его двоичное, восьмеричное строковое представлен
✔ Функции bin и oct используйте для проверки своего
результата, а не для решения.
Дополнительно:
✔ Попробуйте избежать дублирования кода
в преобразованиях к разным системам счисления
✔ Избегайте магических чисел
✔ Добавьте аннотацию типов где это возможно
    """
def gonext(number, sustem):
    result = 0
    ost = 0
    rezString = ''
    while True:
        result = number // sustem
        ost = number % sustem
        if result < sustem:
            rezString = rezString + str(ost) + str(result)
            break
        else:
            number = result
            rezString = rezString + str(ost)
    return rezString[::-1]       # СРЕЗ, реверс строки


integer1 = int(input('Введите целое число : '))

print(gonext(integer1, 8))

