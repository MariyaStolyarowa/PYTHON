import emojis
import random
x = "\U0000274C"
O = "\U00002B55"
list = ['\U0001D7D9', '\U0001D7DA', '\U0001D7DB', '\U0001D7DC', '\U0001D7DD', '\U0001D7DE', '\U0001D7DF', '\U0001D7E0', '\U0001D7E1']
for i in range(9):
    if i == 2 or i == 5:
        print(list[i], end = "  \n")
    else:
        print(list[i], end = "  ")
print()     
print("Кто первый? Нажмите enter чтобы узнать")
input()
chey_hod = random.randrange(0,2)

if chey_hod == 0:
    print(F"Первый ход за {O}")
    chey_hod = O
else:
    print(F"Первый ход за {x}")
    chey_hod = x

for i in range(9):
    print()
    num_poz = int(input(f'{chey_hod} , выберите номер позиции: ')) - 1
    while list[num_poz] == O or list[num_poz] == x:
        num_poz = int(input('Там уже занято, попробуйте другую: ')) - 1
    list[num_poz]= chey_hod
    print()
    for i in range(9):
        if i == 2 or i == 5:
            print(list[i], end = "  \n")
        else:
            print(list[i], end = "  ")
    print() 
    if (list[0] == list[1] == list[2] == O) or (list[3] == list[4] == list[5] == O) or (list[6] == list[7] == list[8] == O) or (list[0] == list[3] == list[6] == O) or (list[1] == list[4] == list[7] == O) or (list[2] == list[5] == list[8] == O) or (list[0] == list[4] == list[8] == O) or (list[2] == list[4] == list[6] == O):
        print(f"CТОП! Победил {O}! \U0001F3C6")
        break
    if (list[0] == list[1] == list[2] == x) or (list[3] == list[4] == list[5] == x) or (list[6] == list[7] == list[8] == x) or (list[0] == list[3] == list[6] == x) or (list[1] == list[4] == list[7] == x) or (list[2] == list[5] == list[8] == x) or (list[0] == list[4] == list[8] == x) or (list[2] == list[4] == list[6] == x):
        print(f"CТОП! Победил {x} ! \U0001F3C6" ) 
        break

    if chey_hod == O:
        chey_hod = x
    else:
        chey_hod = O
   