import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        arr = list(map(int, data[idx:idx + n]))
        idx += n
        left_max = [0] * n
        right_max = [0] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            left_max[i] = i + 1 if not stack else i - stack[-1]
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            right_max[i] = n - i if not stack else stack[-1] - i
            stack.append(i)
        left_min = [0] * n
        right_min = [0] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            left_min[i] = i + 1 if not stack else i - stack[-1]
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            right_min[i] = n - i if not stack else stack[-1] - i
            stack.append(i)
        total_max = 0
        total_min = 0
        for i in range(n):
            total_max += arr[i] * left_max[i] * right_max[i]
            total_min += arr[i] * left_min[i] * right_min[i]
        out.append(str(total_max - total_min))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
