# Типы данных
# Strings (строки)
# Numbers (числа)
# Tuples (кортежи)
# Lists (списки)
# Dictionaries (словари)
# Sets (множества)
# Boolean (логический тип данных)

# Эти типы данных можно, в свою очередь, классифицировать по нескольким признакам:
# изменяемые (списки, словари и множества)
# неизменяемые (числа, строки и кортежи)
# упорядоченные (списки, кортежи, строки и словари)
# неупорядоченные (множества)

i1 = 'Строка'
i2 = "Тоже строка"
i3 = '''И это строка, но 
можно писать в несколько строк'''

print(i1 + i2)
print(i1 * 3)
print(i3[0:5])
print(i3[0::2])

# Методы upper(), lower(), swapcase(), capitalize() выполняют преобразование регистра строки
# Методу find() можно передать подстроку или символ, и он покажет, на какой позиции находится первый символ подстроки (для первого совпадения)
# Проверка на то, начинается или заканчивается ли строка на определенные символы (методы startswith(), endswith())
# Замена последовательности символов в строке на другую последовательность (метод replace())

# Существует несколько вариантов форматирования строк:
# с оператором % — более старый вариант
# метод format() — относительно новый вариант
# f-строки — новый вариант, который появился в Python 3.6.
# F-строки позволяют не только подставлять какие-то значения в шаблон, но и позволяют выполнять вызовы функций, методов и т.п.
print('Моя первая переменная: {}'.format(i1))
print(f'Моя первая переменная: {i1.upper()}')

i4 = 1

# Кортеж
# последовательность элементов, которые разделены между собой запятой и заключены в скобки
# неизменяемый упорядоченный тип данных
i5 = ()
i6 = (1,2,3)
i7 = tuple([1, 2, 3])
i8 = ('a', 'b', 'c')
i9 = (1, 'a')
# i9[0] = 9

# Списки
# Так как список - это упорядоченный тип данных, то, как и в строках, в списках можно обращаться к элементу по номеру, делать срезы:
i10 = []
i11= list()

i12 = [1, 2, 3]
i12[0] = 4
i12.pop(-1)
i12.reverse()

i13 = [5, 6, 7]
i13.append(8)

print(i12 + i13)

#Словари
#Словари - это изменяемый упорядоченный тип данных:

# данные в словаре - это пары ключ: значение
# доступ к значениям осуществляется по ключу, а не по номеру, как в списках
# данные в словаре упорядочены по порядку добавления элементов
# так как словари изменяемы, то элементы словаря можно менять, добавлять, удалять
# ключ должен быть объектом неизменяемого типа: число, строка, кортеж
# значение может быть данными любого типа

i13 = {
    'sport': 'football',
    'player': 'Romeros'
}

i14 = i13

print(f'i13 id is {id(i13)} and i14 id is {id(i14)}')

i14 = i13.copy()

print(f'i13 id is {id(i13)} and i14 id is {id(i14)}')

# Методы keys, values, items

# Множества
# Множество - это изменяемый неупорядоченный тип данных. В множестве всегда содержатся только уникальные элементы.

i15 = [1, 2, 3, 5, 1, 3, 4, 9, 9]
i16 = set(i15)
i16.add(6)
i16.discard(1)

i15 = list(i16)
i15.sort()
print(i15)
print(sorted(i16))

# Булевы значения в Python это две константы True и False.

# В Python истинными и ложными значениями считаются не только True и False.

# истинное значение:
# любое ненулевое число
# любая непустая строка
# любой непустой объект
# ложное значение:
# 0
# None
# пустая строка
# пустой объект

i17 = True
i18 = False
print(i17 == i18)
print(i17 != i18)

# Переменные
# имя переменной может состоять только из букв, цифр и знака подчёркивания;
# имя не может начинаться с цифры;
# имя не может содержать специальных символов @, $, %.
a = 5
b = 6

# Встроенные функции (https://docs.python.org/3/library/functions.html)
print(a + b)
print(abs(-5))

# c = input()
# d = input()
# my_sum = sum(c,d)
# !!error - все потеряно))

c = int(input())
d = int(input())
my_sum = sum([c,d])

print(my_sum)
# 

# if/elif/else
# Конструкция if/elif/else позволяет делать ответвления в ходе программы. Программа уходит в ветку при выполнении определенного условия.
# В этой конструкции только if является обязательным, elif и else опциональны

# for
# Цикл for перебирает по одному элементы указанной последовательности и выполняет действия, которые указаны в блоке for, для каждого элемента.
# for key, value in r1.items():

# while
# Цикл while - это еще одна разновидность цикла в Python.
# В цикле while, как и в выражении if, надо писать условие. Если условие истинно, выполняются действия внутри блока while. При этом, в отличие от if, после выполнения кода в блоке, while возвращается в начало цикла.

# break, continue, pass

# for/else, while/else
# В циклах for и while опционально может использоваться блок else.

