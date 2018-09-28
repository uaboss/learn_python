# Задача: Дан числовой массив. Проверить, есть ли такие два числа в массиве,
# перемножив которые мы получим заданное число X.

MS = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,1,2,3,4]

HS = list(set(MS))

N = int(input('Введите число: '))
L = len(HS)
flag = 0

for X in range(L):
    NX = HS[X]
    for Y in range(X,L):
        R = NX * HS[Y]
        # print(NX, HS[Y], "=>" ,R)
        if R == N:
            print(NX, HS[Y])
            flag = 1
    if flag == 1:
        break




