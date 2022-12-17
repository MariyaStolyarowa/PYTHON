dict_znak_oper = {1:"+", 2:"-", 3:"*", 4:"/", 5:"^", 6:"sqrt"}
from logger import logging
def check_num(data):
    while data.lstrip('-').isdigit() == False:
        data = input("Ошибка! Попробуй еще раз: ")
        logging.warning('Stupid user cannot distinguish numbers from letters')
    data = int(data)
    return data

def check_type_num(data):
    while data.isdigit() == False or (int(data) != 1 and  int(data) != 2):
        data = input("Ошибка! Если хочешь рациональные выбери '1', если комплексные выбери '2'\n")
        logging.warning("Stupid user can't count up to two")
    data = int(data)
    return data

def check_oper(data):
    while data.isdigit() == False or (int(data) not in dict_znak_oper):
        data = input("Ошибка! Выбери число от 1 до 6, соответствующий номеру операции\n")
        logging.warning('Stupid user cannot distinguish numbers from letters')
    data = int(data)
    return data

def div_0(data, oper):
    while oper == 4 and data == 0:
       data = input("Ошибка! Делить на 0 нельзя! Введи другое число: \n")
       logging.warning('Stupid user wanted to divide by 0')
    data = int(data) 
    return data