import main
import exep
from logger import logging
global type_nums
global oper
global rezult
global num_1
global num_2
global result
global num1
global num2
global s
dict_znak_oper = {1:"+", 2:"-", 3:"*", 4:"/", 5:"^", 6:"sqrt"}
dict_num = {1:"rational numbers", 2:"complex numbers"}
def hello():
    return print("Привет!\n"
    "Это я, твой калькулятор.\n"
    "С какими числами будем работать? Выбери пункт меню:\n"
    "1. Рациональные\n"
    "2. Комплексные\n")


def choice_type_num():
    type_nums = 0
    type_nums = input()
    type_nums = exep.check_type_num(type_nums)
    logging.info(f'The user chose {dict_num[type_nums]} ')
    return type_nums

def choice_oper():
    print("Выбери операцию:\n"
    "1. Сложение\n"
    "2. Вычитание\n"
    "3. Умножение\n"
    "4. Деление\n"
    "5. Возведение в степень\n"
    "6. Квадратный корень\n")
    oper = 0
    oper = input()
    oper = exep.check_oper(oper)
    logging.info(f'The user chose operation {dict_znak_oper[oper]} ')
    return oper

def get_num():
    num = input("Введи число = ")
    num = exep.check_num(num)
    logging.info(f'The user entered a number {num} ')
    return num

def get_complex():
    num1 = input("Введи действительную часть = ")
    num1 = exep.check_num(num1)
    num2 = input("Введи мнимую часть = ")
    num2 = exep.check_num(num2)
    return num1, num2


num_1, num_2, oper, result = main.run()
if oper in range(1,6):
    print(f"{num_1} {dict_znak_oper[oper]} {num_2} = {result} ")
    logging.info(f"{num_1} {dict_znak_oper[oper]} {num_2} = {result} ")
else:
    print(f" sqrt{num_1}  = {result} ")
    logging.info(f" sqrt{num_1}  = {result} ")



