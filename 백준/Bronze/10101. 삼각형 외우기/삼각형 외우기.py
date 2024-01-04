tmp = []
for _ in range(3):
    tmp.append(int(input()))

if sum(tmp) != 180:
    print("Error")
else:
    if tmp[0] == tmp[1] and tmp[1] == tmp[2]:
        print("Equilateral")
    elif tmp[0] == tmp[1] or tmp[1] == tmp[2] or tmp[0] == tmp[2]:
        print("Isosceles")
    else:
        print("Scalene")