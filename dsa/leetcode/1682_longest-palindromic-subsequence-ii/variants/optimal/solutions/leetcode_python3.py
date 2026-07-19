class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        alphabet_size = 26

        length_minus_two = [[0] * alphabet_size for _ in range(n + 1)]
        length_minus_one = [[0] * alphabet_size for _ in range(n)]

        for length in range(2, n + 1):
            interval_count = n - length + 1
            current = [[0] * alphabet_size for _ in range(interval_count)]

            for left in range(interval_count):
                right = left + length - 1
                for letter in range(alphabet_size):
                    current[left][letter] = max(
                        length_minus_one[left][letter],
                        length_minus_one[left + 1][letter],
                    )

                if s[left] == s[right]:
                    outer = ord(s[left]) - ord("a")
                    best_inner = max(
                        length_minus_two[left + 1][letter]
                        for letter in range(alphabet_size)
                        if letter != outer
                    )
                    current[left][outer] = max(
                        current[left][outer], 2 + best_inner
                    )

            length_minus_two, length_minus_one = length_minus_one, current

        return max(length_minus_one[0]) if n >= 2 else 0
