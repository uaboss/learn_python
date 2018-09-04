X = input('Please enter string for analyse: ').upper()
Y = dict.fromkeys(X)
if len(X) != len(Y):
    print("Repeated symbol!!! ", len(X)-len(Y))
else:
    print("Not repeated")

