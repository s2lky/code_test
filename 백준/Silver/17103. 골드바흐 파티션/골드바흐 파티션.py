def get_primary(n):
    array = [True for i in range(n + 1)]

    for i in range(2, int(n ** 1/2) + 1):
        if array[i]:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    return array

tmp = [int(input()) for i in range(int(input()))]
array = get_primary(max(tmp))

for n in tmp:
    result = 0
    for i in range(2, n//2 + 1):
        if array[i] and array[n-i]:
          result += 1          
    print(result)  