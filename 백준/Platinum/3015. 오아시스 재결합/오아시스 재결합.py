import sys

heights = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
result = 0
stack = []

for h in heights:
    # 스택 끝 값보다 키 크면 pop
    while stack and stack[-1][0] < h:
        result += stack.pop()[1]

    # 스택이 비어있으면 해당 키 append하고 continue
    if not stack:
        stack.append((h, 1))
        continue

    # 스택 끝 값의 키와 같을 때
    if stack[-1][0] == h:
        cnt = stack.pop()[1]
        result += cnt

        if stack: 
            result += 1
        stack.append((h, cnt + 1))

    # 스택 끝 값의 키보다 작을 때
    else:
        stack.append((h, 1))
        result += 1

print(result)