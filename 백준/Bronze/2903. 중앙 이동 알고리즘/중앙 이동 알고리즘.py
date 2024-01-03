trials = int(input())
beginning = 2

for i in range(trials):
    beginning += (2 ** i)

print(beginning * beginning)