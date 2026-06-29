import sys

def solve():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        expr = data[index]
        index += 1
        stack = []
        for ch in expr:
            if ch.isdigit():
                stack.append(int(ch))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if ch == '+':
                    stack.append(op1 + op2)
                elif ch == '-':
                    stack.append(op1 - op2)
                elif ch == '*':
                    stack.append(op1 * op2)
        results.append(str(stack[0]))
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
