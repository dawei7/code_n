from math import sqrt


def solve():
    def divisor(n):
        di = set()
        for i in range(1, int(sqrt(n))+1):
            if n % i == 0:
                if i % 2:
                    di.add(i)
                x = n // i
                if x % 2:
                    di.add(x)
        return sum(di)


    for _ in range(int(input())):
        l, r = [int(i) for i in input().split()]
        r += 1
        s = 0
        for i in range(l, r):
            s += divisor(i)
        print(s)


if __name__ == "__main__":
    solve()
