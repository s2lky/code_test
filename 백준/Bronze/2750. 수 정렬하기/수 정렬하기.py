tmp = []
for _ in range(int(input())):
    tmp.append(int(input()))
    
results = sorted(list(set(tmp)))

for result in results:
    print(result)