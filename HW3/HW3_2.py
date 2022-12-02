# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]
from random import sample
list1 = []
list2 = []
def create_list (n):
    list = sample(range(10), k=n)
    return list
def Proiz_par(list):
    if len(list) % 2 == 0:
        for i in range(0, int(len(list)/2)):
            list2.append(list1[i] * list1[len(list)-1-i])
    else:
        for i in range(0, int((len(list)-1)/2)):
            list2.append(list1[i] * list1[len(list)-1-i])
        list2.append(list1[int(len(list)/2)])
    return list2
list1 = create_list(int(input('Введите количество элементов в списке n = ')))
list2 = Proiz_par(list1)
print(list1)
print(list2)