


def solve():
    for _ in range(int(input())):
        n, y = map(int, input().split())
        a = list(map(int, input().split()))
        orsum = 0
        for x in a: orsum |= x
        if (orsum & y) == orsum: print(y ^ orsum)
        else: print(-1)


if __name__ == "__main__":
    solve()
