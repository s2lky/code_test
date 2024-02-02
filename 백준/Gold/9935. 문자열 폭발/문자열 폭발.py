def stack2(s):
    stack = []
    B = list(input())
    b = len(B)
    for i in s:
        stack.append(i)
        if stack[len(stack) - b:len(stack)] == B:
            for _ in range(b):
                stack.pop()
    if len(stack) != 0:
        return stack
    else:
        return "FRULA"


if __name__ == "__main__":
    s = input()
    print(''.join(stack2(s)))