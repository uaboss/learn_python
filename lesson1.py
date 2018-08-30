X = input('Please enter string for analyse: ')
DataSet = []
Counter = 0
for Y in X:
    if Y in DataSet:
        Counter += 1
        print("Дубликат ",Counter," обнаружен => это буква \""+Y+"\"")
    DataSet.append(Y)
if Counter == 0: print("Дубликатов не обнаружено")


