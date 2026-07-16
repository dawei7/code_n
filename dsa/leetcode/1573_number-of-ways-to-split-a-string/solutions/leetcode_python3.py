class Solution:
    def numWays(self, s: str) -> int:
        modulus = 1_000_000_007
        length = len(s)
        total_ones = s.count("1")

        if total_ones % 3 != 0:
            return 0
        if total_ones == 0:
            return ((length - 1) * (length - 2) // 2) % modulus

        target = total_ones // 3
        first_end = 0
        first_next = 0
        second_end = 0
        second_next = 0
        seen_ones = 0

        for index, bit in enumerate(s):
            if bit == "0":
                continue

            seen_ones += 1
            if seen_ones == target:
                first_end = index
            if seen_ones == target + 1:
                first_next = index
            if seen_ones == 2 * target:
                second_end = index
            if seen_ones == 2 * target + 1:
                second_next = index

        first_choices = first_next - first_end
        second_choices = second_next - second_end
        return (first_choices * second_choices) % modulus
