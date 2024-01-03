location = int(input())

rooms = 1
lines = 1
count = 1

while True:
    if location == 1:
        break
    
    if count < location:
        count += lines * 6
        lines += 1
        rooms += 1
    else:
        break
    
print(rooms)