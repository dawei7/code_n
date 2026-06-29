# cook your dish here


def solve():
    t = int(input())
    for _ in range(t):
        s = int(input())
        a = list(map(int, input().split()))
        res = 0
        angles = []
        for i in range(s):
            if i == s - 1:
                angles.append(360 - a[i] + a[0])
                break
            tmp = a[i + 1] - a[i]
            angles.append(tmp)
        if angles[-1] == 0:
            angles.pop()
        n = 0
        angles.sort()
        nangles = angles
        while len(list(set(nangles))) != 1:
            tmparr = []
            nangles.sort()
            m = nangles[0]
            for i in nangles:
                if i > m:
                    tmp = int(i / m)
                    mod = i % m
                    if mod == 0:
                        tmp -= 1
                    else:
                        tmparr.append(mod)
                    n += tmp
            tmparr += [nangles[0]] * (n + 1)
            nangles = tmparr
            res += n
            n = 0
        print(res)


if __name__ == "__main__":
    solve()
