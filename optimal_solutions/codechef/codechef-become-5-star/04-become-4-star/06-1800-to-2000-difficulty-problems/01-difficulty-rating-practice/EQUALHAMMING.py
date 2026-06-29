


def solve():
    md = 10 ** 9 + 7

    def bcm(x, y, md):
        rv = 1
        for i in range(y):
            rv = (rv * (x - i)) % md
            rv = (rv * pow(i + 1, -1, md)) % md
        return rv

    for _ in range(int(input())):
        n = int(input())
        a = input()
        b = input()
        assert len(a) == n and len(b) == n
        z = list(zip(a, b))
        s = z.count(('0', '0')) + z.count(('1', '1'))
        d = n - s
        if d % 2 != 0:
            print(0)
        else:
            print((pow(2, s, md) * bcm(d, d // 2, md)) % md)


if __name__ == "__main__":
    solve()
