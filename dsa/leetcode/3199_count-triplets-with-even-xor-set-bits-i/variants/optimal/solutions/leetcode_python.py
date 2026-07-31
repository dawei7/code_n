class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        def parity_counts(values: List[int]) -> tuple[int, int]:
            odd = sum(value.bit_count() & 1 for value in values)
            return len(values) - odd, odd

        even_a, odd_a = parity_counts(a)
        even_b, odd_b = parity_counts(b)
        even_c, odd_c = parity_counts(c)

        return (
            even_a * even_b * even_c
            + even_a * odd_b * odd_c
            + odd_a * even_b * odd_c
            + odd_a * odd_b * even_c
        )
