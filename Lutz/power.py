L = [2 ** x for x in range(6)]
X = 5
Y = 2 ** X
if Y in L:
    print(L.index(2 ** X))
else:
    print("Net")
