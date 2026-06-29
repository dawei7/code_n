import sys
from collections import deque


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, w = data[0], data[1]
    arr = data[2:2 + n]
    minq: deque[int] = deque()
    maxq: deque[int] = deque()
    ans = 0
    for i, value in enumerate(arr):
        while minq and arr[minq[-1]] >= value:
            minq.pop()
        minq.append(i)
        while maxq and arr[maxq[-1]] <= value:
            maxq.pop()
        maxq.append(i)
        while minq[0] <= i - w:
            minq.popleft()
        while maxq[0] <= i - w:
            maxq.popleft()
        if i >= w - 1 and arr[maxq[0]] - arr[minq[0]] == w - 1:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
