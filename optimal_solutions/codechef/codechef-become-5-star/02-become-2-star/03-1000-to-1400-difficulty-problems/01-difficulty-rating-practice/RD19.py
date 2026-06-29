


def solve():
    def gcd(a , b):
        if b == 0:
            return a
        else:
            return gcd(b , a % b)

    for _ in range(int(input())):
        n = int(input())
        a = list(map(int,input().split()))
        if n == 2:
            if gcd(a[0] , a[1] ) == 1:
                print(0)
            else:
                print(-1)
        else:
            g = gcd(a[0] , a[1] )
            for i in range(2 , len(a)):
                g = (gcd(g , a[i]))
            if g == 1:
                print(0)
            elif g > 1:
                print(-1)


if __name__ == "__main__":
    solve()
