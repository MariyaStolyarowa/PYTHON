import math
import cmath

num_1 = 0
num_2 = 0

def init(a, b, c):
    global num_1
    global num_2
    global oper
    global result
    num_1 = a
    num_2 = b
    oper = c
    dict_oper = {1: sum(num_1, num_2), 2: sub(num_1, num_2), 3: mult(num_1, num_2), 4: div(num_1, num_2),
        5: pow(num_1, num_2), 6 :sqrt(num_1, num_2) }
    result = dict_oper[oper]
    return result

     
def sum(num_1, num_2):
    return num_1 + num_2
   
def sub(num_1, num_2):
    return num_1 - num_2
    
    
def mult(num_1, num_2):
    return num_1 * num_2
  
def div(num_1, num_2):
    return num_1 / num_2
    
def pow(num_1, num_2):
    return num_1 ** num_2

def sqrt(num_1, num_2):
    result = math.sqrt(num_1) * num_2 
    return result