from collections import Counter as Cn


def solve():
    for _ in range(int(input())):
        n = int(input())
        l = list(map(int,input().split()))

        d = Cn(l)

        f = 1
        for i in d:
            if d[i]&1:
                f = 0
                break

        print("YES") if f else print("NO")


if __name__ == "__main__":
    solve()
