# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности 
# в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# in
# -1
# out
# Negative value of the number of numbers!
# []
# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]
from random import randint
list1 = []
list2 = []
def create_list(n: int):
    for i in range(n):
        list1.append(randint(0, n*2))
    return list1

def create_list2(list: list):
    for i in range(len(list)):
        count = 0
        for j in range(len(list)):
            if list[i] == list[j]:
                count = count + 1
        if count == 1:
            list2.append(list[i])
    return list2
n = int(input("Введите количество элементов последовательности n = "))
if n < 0:
    print("Отрицательное значение количества элементов!") 
else:
    list1 = create_list(n)
    print(list1)
print(create_list2(list1))
