N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
B = []
for _ in range(M):
    B.append(list(map(int, input().split())))
    

t = []
for i in range(N):
    y = []
    for j in range(K):
        value = 0
        for k in range(M):
            value += A[i][k] * B[k][j]
        y.append(value)
    t.append(y)
    
for i in range(len(t)):
    print(*t[i])