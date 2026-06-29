


def solve():
    t = int(input())

    while t > 0:
        n = int(input())

        arr = list(map(int,input().split()))

        arr.sort()
        tot = 0
        c = 0
        for i in arr:
            tot += i
            if tot < n:
                c += 1
            else:
                break
        print(c)

        t -= 1


if __name__ == "__main__":
    solve()
