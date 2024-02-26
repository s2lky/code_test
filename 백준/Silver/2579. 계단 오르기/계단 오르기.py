stair = []

n = int(input())

for _ in range(n):
    stair.append(int(input()))
    
d = [0] * n

d[0] = stair[0]

if n > 1:
    d[1] = stair[0] + stair[1]

if n > 2:
    d[2] = max(stair[0] + stair[2], stair[1] + stair[2])

for i in range(3, n):
    d[i] = max(stair[i] + stair[i-1] + d[i-3], stair[i] + d[i-2])
    
print(d[n-1])