# cook your dish here


def solve():
    t = int(input())
    while(t > 0):
        n, s = list(map(int, input().split()))
        a = 0
        b = s
        while(not(b <= n)):
            a += 1
            b -= 1
        # print(a, b)
        print(abs(a - b))
        t -= 1


if __name__ == "__main__":
    solve()
