import sys
import collections

def solve():
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(input_data[index])
        x = int(input_data[index + 1])
        index += 2
        arr = list(map(int, input_data[index:index + n]))
        index += n
        dq = collections.deque()
        max_vals = []
        for i in range(n):
            if dq and dq[0] == i - x:
                dq.popleft()
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()
            dq.append(i)
            if i >= x - 1:
                max_vals.append(str(arr[dq[0]]))
        results.append(' '.join(max_vals))
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
