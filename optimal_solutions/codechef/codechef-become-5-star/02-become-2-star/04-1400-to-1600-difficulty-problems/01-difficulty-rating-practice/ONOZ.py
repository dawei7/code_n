# cook your dish here


def solve():
    t = int(input())
    for _ in range(t):
        h, m = (int(i) for i in input().split())
        res = 0
        for i in range(h):
            a = list(set(list(str(i))))
            if len(a) != 1:
                continue
            for j in range(m):
                b = list(set(list(str(j))))
                if len(b) != 1:
                    continue
                if a[0] == b[0]:
                    res += 1
        print(res)


if __name__ == "__main__":
    solve()
