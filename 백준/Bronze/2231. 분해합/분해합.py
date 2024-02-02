N = int(input())
n = N
answers = []

while n != 0:
    n -= 1
    count = n
    for i in list(str(n)):
        count += int(i)
    if count == N:
        answers.append(n)
    
print(min(answers) if answers else 0)