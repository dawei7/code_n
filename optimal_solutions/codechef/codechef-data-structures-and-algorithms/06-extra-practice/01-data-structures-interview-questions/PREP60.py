def previous_smaller_elements(arr):
    n = len(arr)
    result = [-1] * n
    stack = []
    for i in range(n):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        result[i] = stack[-1] if stack else -1
        stack.append(arr[i])
    return result
import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    index = 0
    t = int(data[index])
    index += 1
    outputs = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        res = previous_smaller_elements(arr)
        outputs.append(' '.join(map(str, res)))
    sys.stdout.write('\n'.join(outputs))


if __name__ == "__main__":
    solve()
