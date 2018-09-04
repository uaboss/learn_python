# Задача: Дан отсортированный по возрастанию, но циклически сдвинутый массив.
# Нужно вывести индекс заданного элемента X (если такой элемент есть) в массиве.

Dim = [5,6,7,9,10,11,12,13,14,1,2,3,4]
Search = 3
Start = 0
End = len(Dim)
Mid = End // 2

while (End - Start) > 1:
    if Dim[Mid] < Search:
        Start = Mid
        Mid = (End - Start) // 2 + Start
    elif Dim[Mid] > Search:
        End = Mid
        Mid = (End - Start) // 2 + Start
    else:
        break
    print("Start = ", Start, "Mid = ", Mid)

print("Искомый элемент = ", Dim[Mid+1], "Он находится в позиции ", Mid+1)