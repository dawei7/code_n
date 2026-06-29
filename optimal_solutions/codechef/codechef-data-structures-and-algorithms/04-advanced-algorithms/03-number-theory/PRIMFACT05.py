


def solve():
    def distinct_prime_factors(n):
        primes = set()
        x = n
        i = 2
        while i * i <= x:
            while n % i == 0:
                n //= i
                primes.add(i)
            i += 1

        if n > 2:
            primes.add(n)

        return len(primes)

    if __name__ == "__main__":
        t = int(input())
        for _ in range(t):
            num = int(input())
            print(distinct_prime_factors(num))


if __name__ == "__main__":
    solve()
