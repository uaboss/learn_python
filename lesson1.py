X = input('Please enter string for analyse: ')
DataSet = []
Counter = 0
for Y in X:
    if Y in DataSet:
        Counter += 1
        print("Repeated symbol ",Counter," detected => its a \""+Y+"\"")
    DataSet.append(Y)
if Counter == 0: print("Repeated symbol not detected")


