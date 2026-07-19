class Solution:
    def thousandSeparator(self, n: int) -> str:
        digits = str(n)
        groups = []

        while digits:
            groups.append(digits[-3:])
            digits = digits[:-3]

        return ".".join(reversed(groups))
