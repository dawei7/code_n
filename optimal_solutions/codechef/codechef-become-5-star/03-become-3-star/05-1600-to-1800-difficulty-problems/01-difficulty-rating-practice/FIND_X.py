import math


def solve():
    t = int(input())



    for _ in range(t):
        a, b, c, d = [int(i) for i in input().split()]

        if (a%b < min(b,d) - 1):
            print(1)

        else:
            lcm = b*d//math.gcd(b, d)
            print(lcm - a%b)


if __name__ == "__main__":
    solve()
