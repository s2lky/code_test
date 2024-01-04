while True:
    num = int(input())
    if num == -1:
        break
    
    measure = []
    for i in range(1, num+1):
        if num % i == 0:
            measure.append(i)
    
    if sum(measure[:-1]) == num:
        tmp = ' + '.join(str(j) for j in measure[:-1])
        print(num, '=', tmp)
    else:
        print(f"{num} is NOT perfect.")
