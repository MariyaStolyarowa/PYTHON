# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
from random import uniform
list = []
list_dr = []
def create_list (n):
    for i in range(n):
        list.append((round(uniform(1, n), 2)))
    return list
def fil_list_dr(list):
    for i in range(len(list)):
        list_dr.append((round((list[i]-int(list[i])), 2)))
    return list_dr
list = create_list(int(input("Введите количество элементов списка n =  ")))
fil_list_dr(list)
print(list)
Max = list_dr[0]
Min = list_dr[0]
for i in range(len(list_dr)):
    if list_dr[i] > Max:
        Max = list_dr[i]
    if list_dr[i] < Min:
        Min = list_dr[i]
print(f'Max =  {Max}')
print(f'Min =  {Min}')      
print(f'Разница между максимальным и минимальным значением дробной части элементов =  {round((Max-Min), 2)}')

