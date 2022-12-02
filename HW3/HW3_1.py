# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
from random import sample
list = []
def create_list (n):
    list = sample(range(100), k=n)
    return list
def sum(list):
    s = 0
    for i in range(0, len(list), 2):
        s = s + list[i]
    return s 
list = create_list(int(input('Введите количество элементов в списке n = ')))
print(list)
print(sum(list)) 