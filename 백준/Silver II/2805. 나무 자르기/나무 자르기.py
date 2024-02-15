n, m = map(int, input().split())
trees = sorted(list(map(int, input().split())))

low, high = 1, trees[-1]

while low <= high:
    mid = (low + high) // 2
    result = 0
    for tree in trees:
        if tree > mid:
            result += (tree - mid)

    if m > result:
        high = (mid - 1)
    else:
        low = (mid + 1)
        
print(high)