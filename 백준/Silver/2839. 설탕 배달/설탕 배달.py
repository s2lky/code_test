n = int(input())

result = 0

def recursive(n, result):
    if n < 0:
        return -1
    
    if n % 5 == 0:
        result += (n // 5)
        return result
    else:
        result += 1
        n -= 3
        return recursive(n, result)
    
    
print(recursive(n, result))