from collections import deque


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()

        dq = deque()
        L, R = 0, n - 1

        while L <= R:
            if s[L] == '0':
                dq.appendleft('0')
            else:
                dq.append('1')

            if L < R:
                if s[R] == '1':
                    dq.appendleft('1')
                else:
                    dq.append('0')

            L += 1
            R -= 1

        print(''.join(dq))


if __name__ == "__main__":
    solve()
