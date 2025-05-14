def RPN(text): # reversed polish notation
    stack = []

    for action in text.split():
        try:
            stack.append(int(action))
        except ValueError:
            temp = stack.pop()
        if action == 'M':   # mnożenie (multiplication)
            stack[-1] *= temp
        elif action == 'D': # dodawanie (adding)
            stack[-1] += temp
        else:               # odejmowanie (subtracting)
            stack[-1] -= temp

        return stack[0] # returns result


n = int(input())
checks = []
for _ in range(n):
    checks.append(input().strip())

for check in checks:
    print(RPN(check))