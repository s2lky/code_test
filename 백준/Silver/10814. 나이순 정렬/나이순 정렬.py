x = []

for _ in range(int(input())):
    a, b = input().split()
    x.append([int(a), b])

x.sort(key=lambda x: (x[0]))

for i in x:
    print(f"{i[0]} {i[1]}")