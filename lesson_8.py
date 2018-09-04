# Задача: Дан массив целых чисел. Вывести максимальную сумму элементов в массиве. Суммировать элементы можно только последовательно.
# Пример: [-1, 10, -9, 5, 6, -10]
# Вывод: 11

MS = [-2,-4,-5,-6,-5,-9,-2,-3,-1]

MaxPlusValue = 0
MaxMinusValue = -100000
Dlina = len(MS)

for X in range(0, Dlina - 1):
    X1 = MS[X]
    X2 = MS[X+1]
    MPV = X1+X2
    print(MPV)
    if MPV > 0:
        if MaxPlusValue < MPV:
            MaxPlusValue = MPV
    elif MPV < 0:
        if MaxMinusValue < MPV:
            MaxMinusValue = MPV

if MaxPlusValue != 0:
    print(MaxPlusValue)
else:
    print(MaxMinusValue)
