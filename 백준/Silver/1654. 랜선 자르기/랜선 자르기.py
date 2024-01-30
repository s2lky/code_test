K, N = map(int, input().split())

lans = list(int(input()) for _ in range(K))

low, high = 1, max(lans)

while low <= high:
    mid = (low + high) // 2
    result = 0
    for lan in lans:
        result += lan // mid
    
    if result >= N:
        low = mid + 1
    else:
        high = mid - 1
    

print(high)