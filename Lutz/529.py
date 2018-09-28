def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg,res):
            res = arg
    return res

def menshe(x,y): return x < y
def bolshe(x,y): return x > y

print(minmax(menshe, 4,2,1,5,6,3))
print(minmax(bolshe, 4,2,1,5,6,3))
