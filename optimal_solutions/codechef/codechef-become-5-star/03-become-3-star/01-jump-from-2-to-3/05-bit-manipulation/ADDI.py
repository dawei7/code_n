


def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())

        count = 0
        while(n > 0):
            if n % 2 == 0:
                count += 1
                n //= 2
            else:
                n //= 2
        print(count)


if __name__ == "__main__":
    solve()
