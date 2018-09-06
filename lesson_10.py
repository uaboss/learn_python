#Задача: Если элемент матрицы равен 0, то всю строку и весь столбец нужно обнулить.

MS = [[1, 0, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 0, 1]]

Rows = len(MS)
Cols = len(MS[0])

Zrows = set()
Zcols = set()

for X in range(Rows):
    for Y in range(Cols):
        if MS[X][Y] == 0:
            Zrows.add(X)
            Zcols.add(Y)

for X in Zrows:
    for Y in range(Cols):
        MS[X][Y] = 0

for Y in Zcols:
    for X in range(Rows):
        MS[X][Y] = 0

for X in range(Rows):
    for Y in range(Cols):
        print(MS[X][Y], end = " ")
    print('')
