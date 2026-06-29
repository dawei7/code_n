


def solve():
    def count_divisors(n):
        divisors = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                if i * i == n:
                    divisors += 1
                else:
                    divisors += 2
            i += 1
        return divisors

    if __name__ == "__main__":
        t = int(input())
        for _ in range(t):
            num = int(input())
            print(count_divisors(num))


if __name__ == "__main__":
    solve()
