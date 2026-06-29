


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        sum = 0
        while n != 0:
            d = n % 10
            sum += d
            n //= 10
        print(sum)


if __name__ == "__main__":
    solve()
