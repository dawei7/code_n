


def solve():
    t = int(input())

    for _ in range(t):
        x = int(input())

        xq = dict()
        xq['normal'] = 'huge'
        xq['huge'] = 'small'
        xq['small'] = 'normal'

        s = 'normal'

        for i in range(x):
            s = xq[s]
        print(s)


if __name__ == "__main__":
    solve()
