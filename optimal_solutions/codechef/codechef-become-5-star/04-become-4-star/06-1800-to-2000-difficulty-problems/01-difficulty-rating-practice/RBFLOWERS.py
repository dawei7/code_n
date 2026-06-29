# cook your dish here


def solve():
    tc = int(input())

    while tc:
        a = int(input())
        r = list(map(int, input().split()))
        b = list(map(int, input().split()))

        mbr = {sum(r): 0}

        for i in range(a):
            updated = dict(mbr)
            for j in mbr:
                rs = j - r[i]
                bs = mbr[j] + b[i]
                if rs in updated:
                    updated[rs] = max(updated[rs], bs)
                else:
                    updated[rs] = bs
            mbr = dict(updated)

        ms = 0
        for i in mbr:
            ms = max(ms, min(i, mbr[i]))

        print(ms)
        tc -= 1


if __name__ == "__main__":
    solve()
