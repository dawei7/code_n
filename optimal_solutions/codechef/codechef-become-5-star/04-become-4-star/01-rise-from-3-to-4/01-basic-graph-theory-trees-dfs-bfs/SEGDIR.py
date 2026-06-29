


def solve():
    mod = int(1e9) + 7
    mod2 = 998244353
    inf = int(1e18)

    t = int(input())
    for _ in range(t):
        n = int(input())
        r = []
        s = []
        m = {}
        for i in range(n):
            a, b, c = map(int, input().split())
            r.append((a, b))
            s.append(c)
            if c not in m:
                m[c] = []
            m[c].append((a, b))
        for v in m.values():
            temp = []
            for x in v:
                temp.append((x[0], 1))
                temp.append((x[1] + 1, -1))
            temp.sort()
            sum_ = 0
            for y in temp:
                sum_ += y[1]
                if sum_ > 2:
                    print("NO")
                    break
            else:
                continue
            break
        else:
            print("YES")


if __name__ == "__main__":
    solve()
