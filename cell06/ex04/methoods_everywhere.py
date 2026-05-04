def shrink(n) :
    n = n[:8]
    print(n)
def enlarge(n) :
    for i in range(8-len(n)) :
        n = n + "Z"
    print(n)
n = str(input())
if len(n) > 8 :
    shrink(n)
elif len(n) < 8 :
    enlarge(n)



