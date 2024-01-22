n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

total = 0
coins.sort(reverse=True)
for coin in coins:
    cnt = k // coin
    total += cnt
    k -= cnt * coin

print(total)