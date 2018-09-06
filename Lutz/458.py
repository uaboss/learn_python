S = input('Input string: ')
AVG = 0

for X in S:
    print(X + " => " +str(ord(X)))
    AVG += ord(X)

print("Sum all codes = "+str(AVG))

for y in map(ord, S):
    print(y)
