


def solve():
    def gcd(a,b):

        if b == 0:
            return a
        return gcd(b,a%b)


    t = int(input())

    while t > 0:

        n,k = map(int,input().split())

        g = gcd(n,k)

        l = (n*k)//g

        ans = l//k
        print(ans)
        t -= 1


if __name__ == "__main__":
    solve()
