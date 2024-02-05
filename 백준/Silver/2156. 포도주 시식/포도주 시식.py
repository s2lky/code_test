wines = []
n = int(input())
for _ in range(n):
    wines.append(int(input()))

d = [0] * n

d[0] = wines[0]

if n > 1:
    d[1] = wines[0] + wines[1]

if n > 2:
    d[2] = max(wines[0] + wines[1], wines[1] + wines[2], wines[0] + wines[2])
    
for i in range(3, n):
    d[i] = max(d[i-1], wines[i] + wines[i-1] + d[i-3], wines[i] + d[i-2])
    
print(d[n-1])