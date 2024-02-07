n = int(input())
graph = [[] for _ in range(n+1)]

e = int(input())

for i in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
hacked = [False] * (n+1)
need_visit = []

need_visit.append(1)

while need_visit:
    node = need_visit.pop()
    if not hacked[node]:
        hacked[node] = True
        need_visit.extend(graph[node])

# root node인 본인 제외 감염시킨 컴퓨터 수
result = -1

for i in range(len(hacked)):
    if hacked[i]:
        result += 1
        
print(result)