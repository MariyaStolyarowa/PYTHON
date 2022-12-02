# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
n = int(input("Введите число n =  ")) 
list = [0, 1]
for i in range (n-1):
    if list[0] == 0:
        list.append(list[i]+list[i+1])
        list.insert(0, 1)
    else:
        list.insert(0, list[1]-list[0])
        list.append(list[-1]+list[-2])
list.insert(0, list[1]-list[0])
for i in list:
    print(i, end = " ")
