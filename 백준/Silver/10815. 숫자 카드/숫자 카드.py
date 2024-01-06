tmp = {}
results = []
int(input())
for i in list(map(int, input().split())):
    tmp[i] = 1
int(input())
for j in list(map(int, input().split())):
    try:
        tmp[j]
        results.append(1)
    except:
        results.append(0)
        
print(*results)