MODULO = 1_000_000_007


class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        length = len(s)
        reduction_steps = [0] * (length + 1)
        for ones in range(2, length + 1):
            reduction_steps[ones] = reduction_steps[ones.bit_count()] + 1

        less_counts = [0] * (length + 1)
        exact_ones = 0

        for position, bit in enumerate(s):
            next_counts = [0] * (length + 1)
            for ones in range(position + 1):
                ways = less_counts[ones]
                next_counts[ones] = (next_counts[ones] + ways) % MODULO
                next_counts[ones + 1] = (next_counts[ones + 1] + ways) % MODULO

            if bit == "1":
                next_counts[exact_ones] = (next_counts[exact_ones] + 1) % MODULO
                exact_ones += 1

            less_counts = next_counts

        return sum(less_counts[ones] for ones in range(1, length + 1) if reduction_steps[ones] < k) % MODULO
