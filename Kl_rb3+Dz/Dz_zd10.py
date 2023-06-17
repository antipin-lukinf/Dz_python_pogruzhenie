"""
В большой текстовой строке подсчитать количество встречаемых
слов и вернуть 10 самых частых. Не учитывать знаки препинания
и регистр символов. За основу возьмите любую статью
из википедии или из документации к языку
"""

from collections import Counter

my_string = """Высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью,
ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ. Язык является полностью объектно-ориентированным в том плане, что всё является объектами.
Необычной особенностью языка является выделение блоков кода пробельными отступами.
Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к документации.
Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов.."""

# my_string1 = "на на на на па па ра ра ра пра пра пра пра я я я я я я я я  я я я я "

my_string = my_string.lower().replace(",", "").replace(".", "").replace("-", "").split(" ")  # удаление знаков препинания
print(my_string)
slov = Counter(my_string).most_common(10)
print(slov)

