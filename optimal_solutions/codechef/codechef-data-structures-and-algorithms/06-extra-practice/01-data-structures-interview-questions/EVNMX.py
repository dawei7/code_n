from collections import deque
import sys


def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    k = int(input_data[1])
    arr = list(map(int, input_data[2:]))

    dq = deque()
    result = []

    for i in range(n):
        # add current element if even
        if arr[i] % 2 == 0:
            dq.append(i)
        # remove indices outside the current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        if i >= k - 1:
            if dq:
                result.append(str(arr[dq[0]]))
            else:
                result.append("-1")
    print(" ".join(result))


if __name__ == "__main__":
    solve()
