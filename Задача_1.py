# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

n1 = int(input('Введите количество элементов первого набора чисел: '))
n2 = int(input('Введите количество элементов второго набора чисел: '))
arr1 = []
arr2 = []
for i in range(n1):
    arr1.append(int(input('Введите элемент первого массива: ')))
for j in range(n2):
    arr2.append(int(input('Введите элемент второго массива: ')))
arr3 = []
for i in arr1:
    if i in arr2 and i not in arr3:
            arr3.append(i)
arr3.sort()
print(arr3)