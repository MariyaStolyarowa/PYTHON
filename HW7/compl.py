from logger import logging
global num1
global num2

def comp(a, b):
    num1 = a
    num2 = b
    logging.info(f'The user entered a complex number {complex(a, b)} ')
    return complex(a, b)
