# Задача: Вывести уникальные символы в строке.

String = "Мама мыла раму и ела борщь"

X = set(String)
MS = {}

for Y in X:
    C = String.count(Y)
    MS[Y] = C

print(MS)

for X in MS:
    if MS[X] == 1:
        print("Symbol "+ X + " is unique")
