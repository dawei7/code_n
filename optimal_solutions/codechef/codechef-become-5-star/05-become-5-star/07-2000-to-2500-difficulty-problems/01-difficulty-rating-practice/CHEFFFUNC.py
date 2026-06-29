


def solve():
    def base_2(x):
        return bin(x)[2 : ]

    def f_plus_g(x):
        b = base_2(x)
        k = len(b) - 1
        c = b.count('0')
        return c + 2 ** (k + 1) + 2 ** k - 1 - x 

    for _ in range(int(input())):
        l, r = [int(x) for x in input().split()]
        assert l >= 1 and l <= r
        k = len(base_2(r)) - 1
        if 2 ** k >= l:
            print(k + 2 ** (k + 1) - 1)
            continue
        x = l
        mx = 0
        while x <= r:
            mx = max(mx, f_plus_g(x))
            i = (x ^ (x - 1)).bit_length() - 1
            x += 2 ** i
        print(mx)


if __name__ == "__main__":
    solve()
