SL = {1:"mama", 3:"papa", 2:"sema", 0:"turist"}

for x in sorted(SL):
    print(x, SL[x])


SS = list(SL.keys())
SS.sort()

for x in SS:
    print(x, SL[x])
