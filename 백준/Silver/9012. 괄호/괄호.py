def solution(brackets):
    tmp = []
    for bracket in brackets:
        if bracket == "(":
            tmp.append(bracket)
        elif bracket == ")":
            if len(tmp) == 0:
                return "NO"
            
            if tmp[-1] == "(":
                tmp.pop()
            else:
                return "NO"
            
    if len(tmp) != 0:
        return "NO"
    
    return "YES"

for _ in range(int(input())):
    print(solution(input()))
