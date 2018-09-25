# Задача: Написать функцию, ктр "сжимает" строку. Если полученная строка оказалась больше исходной, то вывести исходную.
# Например, дана строка "ZZZABBEEE", получить строку вида "Z3A1B2E3k", т.е. подставить счетчик вхождения символа.

T = input("Введите строку для сжатия: ")
L = len(T)
ZipText = ""

StartPos = 0
StopPos = 0

while StopPos != L:
    while T[StopPos] == T[StartPos]:
        StopPos += 1
        if StopPos == L:
            break
    if StopPos-StartPos == 1:
        ZipText = ZipText + T[StartPos]
        StartPos = StopPos
    else:
        ZipText = ZipText + T[StartPos] + str(StopPos-StartPos)
        StartPos = StopPos

print(ZipText)



