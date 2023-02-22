import random

num=random.randint(1,99)
#print(num)
hellTry=5
firstTry=0

while hellTry>firstTry:
    qestion=int(input('какое число я загадал? (от 1 до 99): '))
    if qestion>num:
        print('загаданное число меньше')
    elif qestion<num:
        print('загаданное число больше')
    else:
        print('ты угадал!')
        break
    firstTry+=1
if hellTry<=firstTry:
    print('!GAME OVER!')
    print("загаданное число было", num)