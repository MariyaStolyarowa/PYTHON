import User_interface
import calc_rac
import calc_comp
import compl
import exep
from logger import logging
global oper
global result
global type_nums
dict_znak_oper = {1:"+", 2:"-", 3:"*", 4:"/", 5:"^", 6:"sqrt"}
def run():
    logging.info('Start')
    User_interface.hello()
    type_nums = User_interface.choice_type_num()
    oper = User_interface.choice_oper()
    if type_nums == 1:
        num_1 = User_interface.get_num()
        if oper in range(1,6):
            num_2 = exep.div_0(User_interface.get_num(), oper)
        else:
            num_2 = 1
    else:
        a, b = User_interface.get_complex()
        num_1 = compl.comp(a, b)
        if oper in range(1,6):
            a, b = User_interface.get_complex()
            num_2 = compl.comp(a, b)
        else: 
            num_2 = 1
    
    if type_nums == 1 and num_1 > 0:
        result = calc_rac.init(num_1, num_2, oper)
    else:
        result = calc_comp.init(num_1, num_2, oper)
    return num_1, num_2, oper, result
    

  