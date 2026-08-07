from collections import Counter


class Solution:
    def largestPalindromic(self, num: str) -> str:
        counts = Counter(num)
        left_parts = []

        for digit in "987654321":
            pairs = counts[digit] // 2
            if pairs:
                left_parts.append(digit * pairs)
                counts[digit] -= 2 * pairs

        if left_parts:
            zero_pairs = counts["0"] // 2
            if zero_pairs:
                left_parts.append("0" * zero_pairs)
                counts["0"] -= 2 * zero_pairs

        left = "".join(left_parts)
        center = next(
            (digit for digit in "9876543210" if counts[digit] > 0),
            "",
        )

        if not left:
            return center or "0"
        return left + center + left[::-1]
