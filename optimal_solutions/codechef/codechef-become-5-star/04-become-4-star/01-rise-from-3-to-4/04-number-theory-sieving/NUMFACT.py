def sieve(max_size):
    is_prime = [True] * (max_size + 1)
    smallest_prime_factor = [0] * (max_size + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, max_size + 1):
        if is_prime[i]:
            smallest_prime_factor[i] = i
            for j in range(i * 2, max_size + 1, i):
                is_prime[j] = False
                if smallest_prime_factor[j] == 0:
                    smallest_prime_factor[j] = i
    return smallest_prime_factor

def solve():
    max_size = 10 ** 6
    smallest_prime_factor = sieve(max_size)
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        count = {}
        x_values = list(map(int, input().split()))
        for x in x_values:
            while x > 1:
                spf = smallest_prime_factor[x]
                count[spf] = count.get(spf, 0) + 1
                x //= spf
        ans = 1
        for freq in count.values():
            ans *= freq + 1
        results.append(ans)
    print('\n'.join(map(str, results)))


if __name__ == "__main__":
    solve()
