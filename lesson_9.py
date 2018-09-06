# print fibonachi
N0 = 0
N1 = 1
N2 = 0
Count = 0

try:
    while Count < 800:
        N2 = N0 + N1
        print(N2)
        N0 = N1
        N1 = N2
        Count += 1
except Exception:
    print("ERROR - Overflow")
