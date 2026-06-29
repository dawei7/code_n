import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    T = int(input_data[0])
    results = []
    for i in range(1, T + 1):
        s = input_data[i].strip()
        max_length = 0
        stack = [-1]
        for index, char in enumerate(s):
            if char == '(':
                stack.append(index)
            else:
                if stack:
                    stack.pop()
                if not stack:
                    stack.append(index)
                else:
                    max_length = max(max_length, index - stack[-1])
        results.append(str(max_length))
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
