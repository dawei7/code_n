from sympy import isprime


def solve():
    for _ in range(int(input())):
        h = int(input())
        p = 1
        m = 0
        if h==1:
            print(1)
            continue
        if h==0:
            print(-1)
            continue
        while h > 0 and not isprime(h):
            h = h - p
            p *= 2
            m += 1

        if h < 0:
            m = -1
        elif isprime(h):
            m += 1

        print(m)


if __name__ == "__main__":
    solve()
