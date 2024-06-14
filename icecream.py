"""TEST"""
size = int(input())
flavour = input()

def build_icecream(x,y):
    """BUILD ICECREAM"""
    a = 1
    for i in range(1,x+1):
        print(" "*(x-i) + y * (a))
        a += 2
    b = (x*2)-3
    for j in range(1,x):
        print(" "*(j) + "_" * (b))
        b -= 2
build_icecream(size, flavour)
