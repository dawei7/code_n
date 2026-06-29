# cook your dish here


def solve():
    def bsl(pl, tar):
        l = 0
        r = len(pl) - 1
        while l <= r:
            mid = (l + r) // 2
            if pl[mid] < tar:
                l = mid + 1
            else:
                r = mid - 1
        return (l + r) // 2


    def bsr(pl, tar):
        l = 0
        r = len(pl) - 1
        while l <= r:
            mid = (l + r) // 2
            if pl[mid] <= tar:
                l = mid + 1
            else:
                r = mid - 1
        return (l + r) // 2

    import sys

    input = sys.stdin.readline

    _ = int(input())
    while _:
        lim = 0
        _ -= 1
        n, k = [int(i) for i in input().split()]
        ar = []
        for i in range(n):
            x = [int(i) for i in input().split()]
            ar.append([x[0] - 1, x[1] - 1])
            lim = max(lim, max(x))
        ar.sort()
        las = 0
        tot = 0
        total = [0] * lim
        ch = [0] * lim
        for i in range(lim):
            while las < n:
                if ar[las][0] == i:
                    tot += 1
                    ch[ar[las][1]] += 1
                    las += 1
                else:
                    break
            if i:
                tot -= ch[i - 1]
            total[i] = tot
        tot = 0
        ex = []
        no = []
        for i in range(lim):
            if total[i] == k:
                ex.append(i)
                tot += 1
            elif total[i] == k + 1:
                no.append(i)
        ans = 0
        # print(total[:10])
        # print(ex)
        # print(no)
        for i in range(n):
            e1 = bsl(ex, ar[i][0])
            e2 = bsr(ex, ar[i][1])
            n1 = bsl(no, ar[i][0])
            n2 = bsr(no, ar[i][1])
            # print(ar[i], n1, n2, e1, e2)
            ans = max(ans, tot + ((n2 - n1) - (e2 - e1)))
        print(ans)


if __name__ == "__main__":
    solve()
