# Задача: Дан отсортированный по возрастанию массив, но циклически сдвинут.
# Пример, [3, 4, 5, 6, 7, 8, 1, 2]
# Написать алгоритм, ктр оптимально находит минимальный элемент в таком массиве.
# Buble Sort Algoritm for search minimal number in sorted list

Dim = [5,6,7,9,10,11,12,13,14,1,2,3,4]

Start = 0
End = len(Dim)
Mid = End // 2

while (End - Start) > 1:
    if Dim[Start] < Dim[Mid]:
        Start = Mid
        Mid = (End - Start) // 2 + Start
    elif Dim[Start] > Dim[Mid]:
        End = Mid
        Mid = (End - Start) // 2 + Start
    else:
        break
    print("Start = ", Start, "Mid = ", Mid)

print("Наименьший элемент = ", Dim[Mid+1], "Он находится в позиции ", Mid+1)