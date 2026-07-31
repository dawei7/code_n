MOD = 1_000_000_007


def solve(n: int, m: int, k: int) -> int:
    even_values = m // 2
    odd_values = m - even_values

    end_even = [0] * (k + 1)
    end_odd = [0] * (k + 1)
    end_even[0] = even_values
    end_odd[0] = odd_values

    for _ in range(n - 1):
        next_even = [0] * (k + 1)
        next_odd = [0] * (k + 1)

        for even_pairs in range(k + 1):
            next_odd[even_pairs] = (
                (end_even[even_pairs] + end_odd[even_pairs]) * odd_values
            ) % MOD

            next_even[even_pairs] = end_odd[even_pairs] * even_values % MOD
            if even_pairs > 0:
                next_even[even_pairs] = (
                    next_even[even_pairs]
                    + end_even[even_pairs - 1] * even_values
                ) % MOD

        end_even = next_even
        end_odd = next_odd

    return (end_even[k] + end_odd[k]) % MOD
