#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
#  является ли этот день выходным.
#*Пример:*
#- 6 -> да
#- 7 -> да
#- 1 -> нет
a = int(input('Введите число от 1 до 7: '))
while a < 1 or a > 7:
    print('Введено неверное число')
    a = int(input('Введите число от 1 до 7: '))
if a == 6 or a == 7:
        print('Да')
else:
    print('Нет')