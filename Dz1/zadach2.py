"""
2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
 Дано a, b, c - стороны предполагаемого треугольника.
  Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
  Если хотя бы в одном случае отрезок окажется больше суммы двух других,
   то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""

a = 2
b = 2
c = 2

if (a + b) > c and (b+c) > a and (c + a) > b:
    print("фигура abc является треугольником", end=" ")

    if a == b == c:
        print("равносторонним")
    elif a == b or b == c or c == a:
        print("равнобедренным")

    else:
        print("разносторонним")
else:
    print("фигура abc НЕ является треугольником")
