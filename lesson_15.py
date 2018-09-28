# Задача: Дана гистограмма, она представлена числовым массивом:
# [ 3, 6, 2, 4, 2, 3, 2, 10, 10, 4 ]
# Нужно посчитать объем воды (1 блок в гистограмме), ктр наберется внутри нее.

V = [3,6,2,4,2,3,2,10,10,4]

def waterVolume(arr):
    leftMax=rightMax=volume=left=right=0
    leftLocalMaxArr = []
    rightLocalMaxArr = []

    for i in range(0,len(V)-1):
        left = i
        right = len(V)-2-i
        if arr[left] > leftMax:
            leftMax = arr[left]
        leftLocalMaxArr.append(leftMax)
        if arr[right] > rightMax:
            rightMax = arr[right]
        rightLocalMaxArr.insert(0,rightMax)
        print("left="+str(i)+" right="+str(right)+", leftMax="+str(leftMax)+" rightMax="+str(rightMax))

    for j in range(0,len(V)-1):
        if leftLocalMaxArr[j] <= rightLocalMaxArr[j]:
            volume += leftLocalMaxArr[j] - arr[j]
            print(j, volume)
        else:
            volume += rightLocalMaxArr[j] - arr[j]
            print(j, volume)
    return volume

print(waterVolume(V))
