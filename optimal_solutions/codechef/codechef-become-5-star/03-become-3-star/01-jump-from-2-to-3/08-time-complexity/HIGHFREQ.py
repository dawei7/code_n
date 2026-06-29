


def solve():
    t = int(input())


    while t > 0:

        n = int(input())

        arr = map(int,input().split())

        d = {}

        for i in arr:
            d.setdefault(i,0)

            d[i] += 1

        mx = 0
        minmx = 0

        for i in d.values():

            if mx < i:
                minmx = mx
                mx = i
            else:
                minmx = max(i,minmx)


        # print(d)
        # print(mx,minmx)

        ans = (mx+1)//2

        if ans > minmx:
            print(ans)
        else:
            print(minmx)
        # print(ans)


        t -= 1


if __name__ == "__main__":
    solve()
