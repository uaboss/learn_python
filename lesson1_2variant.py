X = input('Please enter string for analyse: ').upper()
Y = dict.fromkeys(X)
if len(X) != len(Y):
    print("Есть дубликаты символов", len(X)-len(Y))
else:
    print("Нет дубликатов символов")

