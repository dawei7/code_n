from collections import deque


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        dq = deque(map(int, input().split()))

        ans = 0
        while len(dq) > 1:
            x = dq.popleft()
            y = dq.pop()
            if x == y:
                continue
            ans += 1
            if x < y:
                dq.append(y - x)
            else:
                dq.appendleft(x - y)

        print(ans)


if __name__ == "__main__":
    solve()
