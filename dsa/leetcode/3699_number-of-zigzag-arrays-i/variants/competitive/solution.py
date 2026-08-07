class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        modulus = 1_000_000_007
        value_count = r - l + 1

        ending_up = list(range(value_count))
        ending_down = [value_count - value - 1 for value in range(value_count)]

        for _ in range(2, n):
            next_up = [0] * value_count
            prefix = 0
            for value in range(value_count):
                next_up[value] = prefix
                prefix = (prefix + ending_down[value]) % modulus

            next_down = [0] * value_count
            suffix = 0
            for value in range(value_count - 1, -1, -1):
                next_down[value] = suffix
                suffix = (suffix + ending_up[value]) % modulus

            ending_up = next_up
            ending_down = next_down

        return (sum(ending_up) + sum(ending_down)) % modulus
