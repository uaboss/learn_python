#Задача: простенькая задачка на вывод слов в строке в обратном порядке.
# Слова разделены только пробелами.

I = input("Введите несколько слов: ")
W = I.split()
L = len(W)

for X in range(L-1,-1,-1):
    print(W[X])

