#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
#10 -> 1 2 4 8

N = int(input('Введите целое число - '))
for i in range(N):
    n = 2**i
    if n > N:
        break
    else:
        print(n)