def solution(friends, gifts):
    d1 = dict()
    d2 = dict()
    answer = 0
    
    for i in friends:
        d1[i] = [0, 0, 0]
        d2[i] = []
        
    for g in gifts:
        a, b = g.split(" ")
        d1[a][0], d1[a][2] = d1[a][0] + 1, d1[a][2] + 1
        d1[b][1], d1[b][2] = d1[b][1] + 1, d1[b][2] - 1
        d2[a].append(b)
    for d in d2:
        cnt = 0
        for i in friends:
            if d2[i].count(d) > d2[d].count(i):
                pass
            elif d2[i].count(d) < d2[d].count(i):
                cnt += 1
            else:
                if d1[i][2] < d1[d][2]:
                    cnt += 1
                else:
                    pass
        if answer < cnt:
            answer = cnt

    return answer