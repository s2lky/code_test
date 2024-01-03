a, b = map(int, input().split())

count = 0
answer = 0
for i in range(1, a+1):
    if a % i == 0:
        count += 1
    else:
        pass
    
    if count == b:
        answer += i
        break
    
print(answer)