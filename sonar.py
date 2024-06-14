"""Test"""
def main():
    """man"""
    size = int(input())
    for i in range(1,size+1):
        print("   "*(size-i),end = "")
        num = size
        while True:
            print(f"{num:>02}",end = " ")
            num -= 1
            if not num >= size-i+1:
                break
        num += 1
        while num < size:
            num += 1
            print(f"{num:>02}",end = " ")
        print()
    for j in range(1,size-1):
        print("   "*(j),end = "")
        num = size
        while True:
            print(f"{num:>02}",end = " ")
            num -= 1
            if num <= j+1:
                break
        while num <= size:
            print(f"{num:>02}",end = " ")
            num += 1
        print()
    if size != 1:
        print("   "*(size-1),end = "")
        print(f"{size:>02}")
main()
