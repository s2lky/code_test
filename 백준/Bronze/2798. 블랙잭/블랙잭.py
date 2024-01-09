from itertools import combinations

a, b = map(int, input().split())

cards = list(map(int, input().split()))

comb = list(combinations(cards, 3))
value = 0
for i in range(len(comb)):
    if sum(comb[i]) > b:
        pass
    else:
        if value < sum(comb[i]):
            value = sum(comb[i])
        
print(value)