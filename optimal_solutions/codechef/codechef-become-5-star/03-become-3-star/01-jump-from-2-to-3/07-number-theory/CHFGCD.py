import math


def solve():
    t = int(input())

    for _ in range(t):
        x, y = map(int, input().split())


        gcd = math.gcd(x, y)

        if gcd > 1:
            print(0)
        else:
            if math.gcd(x + 1, y) > 1 or math.gcd(x, y + 1) > 1:
                print(1)
            else:
                print(2)


if __name__ == "__main__":
    solve()
