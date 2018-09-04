# Задача: Дана строка, слова в ней указаны через пробел. Вывести слова в порядке убывания длины.
# Пример: "My favorite music band is Rammstein",
# Вывод: 1. Rammstein 2. favorite 3. music 4. band 5. My 6. is

S1 = "My favorite music band is Rammstein"
S1 = S1.split(" ")
L = len(S1)

MS = {}

for X in S1:
    MS[len(X)] = X

for X in sorted(MS, reverse=True):
    print(X, MS[X])

