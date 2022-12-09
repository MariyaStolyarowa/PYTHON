# ** 5. Даны два файла, в каждом из которых находится запись многочленов.
#  Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0
# in
# "poly.txt"
# "poly_2.txt"
# out
# The contents of the files do not match!
with open('poly_1.txt', 'w', encoding='utf-8') as file:
    file.write('5*x^7 + 2*x^2')
with open('poly_2.txt', 'w', encoding='utf-8') as file:
    file.write('15*x^3 - 9*x^5')

with open('poly_1.txt','r') as file:
    poly_1 = file.readline()
    #list_of_poly_1 = poly_1.split()


with open('poly_2.txt','r') as file:
    poly_2 = file.readline()
    #list_of_poly_2 = poly_2.split()

print(f'{poly_1} + {poly_2}')
sum_poly = poly_1 + " + " + poly_2

with open('sum_poly.txt', 'w', encoding='utf-8') as file:
    file.write(f'{sum_poly} = 0')
