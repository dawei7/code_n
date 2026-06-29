


def solve():
    for _ in range(int(input())):
        n = int(input())
        ai = sorted(int(i) for i in input().split())
        tot = 0
        for i in range(1, n):
            left = 0
            for j in range(i):
                left += (1000 - ai[j])
            right = 0
            for j in range(i, n):
                right += ai[j]
            tot = max(tot, right * left)
        print(tot)


if __name__ == "__main__":
    solve()
