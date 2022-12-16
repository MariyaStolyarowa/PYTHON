# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше
#  предыдущего элемента. Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10] 
# [16, 3, 7, 10]
import random
n = int(input("Введите количество элементов списка: "))
list1 = [i for i in random.choices(range(1, 2*n), k=n)]
list2 = [list1[i] for i in range(1, len(list1)) if list1[i] > list1[i-1]]
print(list1)
print(list2)
