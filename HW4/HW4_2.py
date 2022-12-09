# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# in
# 54
# out
# [2, 3, 3, 3]
# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]
# in
# 650
# out
# [2, 5, 5, 13]
numb = int(input("Введите целое число: "))
list_of_simpe = []
count = 0
for i in range(2, numb):
    while numb % i == 0:
        if i != 2:
            for j in range(2, i):
                if i % j == 0:
                    count = count + 1
            if count == 0:
                list_of_simpe.append(i)
                numb = numb/i
        else:
            list_of_simpe.append(i)
            numb = numb/i
print(list_of_simpe)