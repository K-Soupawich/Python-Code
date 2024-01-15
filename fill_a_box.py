#create and put stars in a box from bottom to top and left to right

x = int(input("width : "))
y = int(input("height : "))
n = int(input("amount : "))

box = []
for i in range(0,y):
    box.append([])
    for j in range(0,x):
        box[i].append(" ")

col = 0
row = y-1
for _ in range(0,x*y):
    if n <= 0:
        break
    box[row][col] = "*"
    n -= 1
    row -= 1
    if row < 0:
        row = y-1
        col += 1

print("-"*(x+2))
for b in range(0,y):
    print("|",end="")
    for a in range(0,x):
        print(box[b][a],end = "")
    print("|")
print("_"*(x+2))
print(str(n)+" star"+"s"*(n>1)+" left")