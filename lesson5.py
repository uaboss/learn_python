#Задача: Написать функцию, ктр будет проверять можно ли преобразовать строку так, чтобы она стала палиндромом.

Pol = input('Input word: ')

CountPair = 0

if Pol == Pol[::-1]:
    print("Is A Palindrom!!!")
else:
    for X in Pol:
        CountChar = 0
        for W in Pol:
            if W == X:
                CountChar += 1
        if CountChar / 2 - CountChar // 2 > 0:
            CountPair +=1
    if CountPair > 1:
        print("Not palindrom-frendly word")
    else:
        print("Yes! Palindrom-frendly word")
