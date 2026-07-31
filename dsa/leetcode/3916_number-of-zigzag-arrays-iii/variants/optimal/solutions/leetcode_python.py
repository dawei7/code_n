class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 1_000_000_007
        value_count = r - l + 1

        samples = [0] * (n + 1)
        for alphabet_size in range(1, n + 1):
            up = list(range(alphabet_size))
            down = [alphabet_size - 1 - value for value in range(alphabet_size)]

            for _ in range(3, n + 1):
                prefix = 0
                next_up = [0] * alphabet_size
                for value in range(alphabet_size):
                    next_up[value] = prefix
                    prefix = (prefix + down[value]) % mod

                suffix = 0
                next_down = [0] * alphabet_size
                for value in range(alphabet_size - 1, -1, -1):
                    next_down[value] = suffix
                    suffix = (suffix + up[value]) % mod

                up, down = next_up, next_down

            samples[alphabet_size] = (sum(up) + sum(down)) % mod

        if value_count <= n:
            return samples[value_count]

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
