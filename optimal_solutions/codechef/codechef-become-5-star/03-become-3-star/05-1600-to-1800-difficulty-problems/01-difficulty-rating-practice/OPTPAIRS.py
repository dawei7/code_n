# cook your dish here


def solve():
    def count_primes(n):
        result = 1
        for i in range(2,int(n**(0.5)) + 1):
            if n % i == 0:
                result += 1
                if n//i != i:
                    result += 1
        return result

    for _ in range(int(input())):
        n = int(input())
        print(count_primes(n)*2 - (1 if n % 2 == 0 else 0))


if __name__ == "__main__":
    solve()
