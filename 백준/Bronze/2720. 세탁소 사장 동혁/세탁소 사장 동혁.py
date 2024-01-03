n = int(input())

quarter = 25
dime = 10
nickel = 5
penny = 1

for _ in range(n):
    money = int(input())
    
    quarter_count = 0
    dime_count = 0
    nickel_count = 0
    penny_count = 0
    
    while True:
        if money >= 25:
            money -= quarter
            quarter_count += 1
        elif money >= 10:
            money -= dime
            dime_count += 1
        elif money >= 5:
            money -= nickel
            nickel_count += 1
        else:
            money -= penny
            penny_count += 1
            
        if money == 0:
            break
            
    print(f"{quarter_count} {dime_count} {nickel_count} {penny_count}")