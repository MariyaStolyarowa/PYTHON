# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, записать в файл
#  полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# in
# 0
# -1
# 4
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0
from random import randint
file_name = input('Введите имя файла для записи: ')
n = int(input('Сколько хотите сформировать многочленов: '))   
with open(file_name, 'w', encoding='UTF-8') as file:
    
    for i in range(n):
        k = int(input(f"Введите степень {i+1}-го многочлена k= "))
        string = ""
        list = []
        for i in range(k+1):
            list.insert(0, randint((-k)*2, k*2))
        
        for i in range(len(list)):
            if k == 0:
                if list[i] > 0:
                    string = string + f' + {list[i]}'
                if list[i] < 0:
                    string = string + f' {list[i]}'
                k = k-1
            if k > 0:
                if list[i] == 0:
                    k = k-1
                elif list[i] < 0:
                    string = string + f'{list[i]}*x^{k}'
                    k = k-1
                else:
                    if i > 0:
                        sum = 0
                        for j in range(i):
                            sum = sum + list[j]
                        if sum == 0:
                            string = string + f'{list[i]}*x^{k}'
                        else:
                            string = string + f' + {list[i]}*x^{k}'
                    elif i == 0:
                        string = string + f'{list[i]}*x^{k}'
                    k = k-1
        file.writelines(f'{string} = 0\n')
    print(f"Посмотрите файл {file_name}")
     
   
   
