from itertools import accumulate


def solve(n: int, l: int, r: int) -> int:
    mod = 1_000_000_007
    value_count = r - l + 1

    def count(alphabet_size: int) -> int:
        up = list(range(alphabet_size))
        down = list(reversed(range(alphabet_size)))
        for _ in range(3, n + 1):
            up, down = list(map(mod.__rmod__, list(accumulate(down, initial=0))[:-1])), list(reversed(list(map(mod.__rmod__, list(accumulate(reversed(up), initial=0))[:-1]))))
        return (sum(up) + sum(down)) % mod

    if value_count <= n:
        return count(value_count)

    samples = [0] + [count(alphabet_size) for alphabet_size in range(1, n + 1)]

    factorial = [1] * (n + 1)
    inverse_factorial = [1] * (n + 1)
    for value in range(1, n + 1):
        factorial[value] = factorial[value - 1] * value % mod

    inverse_factorial[n] = pow(factorial[n], mod - 2, mod)
    for value in range(n, 0, -1):
        inverse_factorial[value - 1] = inverse_factorial[value] * value % mod

    prefix_product = [1] * (n + 2)
    suffix_product = [1] * (n + 2)
    for value in range(n + 1):
        prefix_product[value + 1] = (
            prefix_product[value] * (value_count - value) % mod
        )
    for value in range(n, -1, -1):
        suffix_product[value] = (
            suffix_product[value + 1] * (value_count - value) % mod
        )

    answer = 0
    for value, sample in enumerate(samples):
        term = sample * prefix_product[value] % mod
        term = term * suffix_product[value + 1] % mod
        term = term * inverse_factorial[value] % mod
        term = term * inverse_factorial[n - value] % mod
        if (n - value) % 2:
            answer -= term
        else:
            answer += term

    return answer % mod
