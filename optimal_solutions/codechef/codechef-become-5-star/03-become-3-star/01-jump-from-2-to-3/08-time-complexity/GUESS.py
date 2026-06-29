from fractions import Fraction


def solve():
    def gd(a,b):
        if b == 0:
            return a
        return gd(b,a%b)


    t = int(input())


    while t > 0:

        n,m = map(int,input().split())
        dn = n*m
        nn = dn // 2
        g = gd(dn,nn)

        dn = dn// g
        nn = nn // g
        if nn == 0:
            print('0'+'/'+str(dn))
        else:
            print(Fraction(nn,dn))

        t -= 1


if __name__ == "__main__":
    solve()
