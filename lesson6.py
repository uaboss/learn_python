# Задача: Написать функцию, которая определяет, является ли одна строка перестановкой другой.

S1 = "мама мыла раму"
S2 = "раму мыла мама"

MS1 = {}
MS2 = {}
count = 1

for X in S1:
    if MS1.get(X) == None:
        MS1[X]=1
    else:
        MS1[X] += 1

for X in S2:
    if MS2.get(X) == None:
        MS2[X]=1
    else:
        MS2[X] += 1

for X in MS1:
    if MS1[X] != MS2[X]:
        print('Это не перестановка')
        count = 0
        break

if count == 1:
    print("Это перестановка!")
