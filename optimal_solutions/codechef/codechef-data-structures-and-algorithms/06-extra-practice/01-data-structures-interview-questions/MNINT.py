import sys
import math

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return primes

def solve():
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    nums = list(map(int, input_data[1:]))
    primes = sieve(31623)
    res = []
    for X in nums:
        original = X
        ans = 1
        temp = X
        for p in primes:
            if p * p > temp:
                break
            if temp % p == 0:
                ans *= p
                while temp % p == 0:
                    temp //= p
            if temp == 1:
                break
        if temp > 1:
            ans *= temp
        res.append(str(ans))
    sys.stdout.write('\n'.join(res))


if __name__ == "__main__":
    solve()
