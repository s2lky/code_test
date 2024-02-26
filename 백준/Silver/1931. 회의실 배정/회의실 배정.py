# 그리디 회의실

n = int(input())
times = []
for _ in range(n):
    i = list(map(int, input().split()))
    times.append(i)
    
times.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end = times[0][1]

for i in range(1, n):
    if times[i][0] >= end:
        cnt += 1
        end = times[i][1]

print(cnt)