def max_of_min_in_windows(arr, n):
    left = [-1] * n
    right = [n] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        right[i] = stack[-1] if stack else n
        stack.append(i)
    res = [0] * (n + 1)
    for i in range(n):
        len_window = right[i] - left[i] - 1
        res[len_window] = max(res[len_window], arr[i])
    for i in range(n - 1, 0, -1):
        res[i] = max(res[i], res[i + 1])
    return res[1:]
import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        ans = max_of_min_in_windows(arr, n)
        results.append(' '.join(map(str, ans)))
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
