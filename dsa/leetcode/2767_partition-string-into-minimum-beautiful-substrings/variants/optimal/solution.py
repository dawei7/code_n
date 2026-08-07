class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)
        powers = set()
        value = 1

        while value < 1 << n:
            powers.add(value)
            value *= 5

        unreachable = n + 1
        minimum_parts = [unreachable] * (n + 1)
        minimum_parts[0] = 0

        for start in range(n):
            if minimum_parts[start] == unreachable or s[start] == "0":
                continue

            value = 0
            for end in range(start, n):
                value = value * 2 + int(s[end])

                if value in powers:
                    minimum_parts[end + 1] = min(
                        minimum_parts[end + 1],
                        minimum_parts[start] + 1,
                    )

        return minimum_parts[n] if minimum_parts[n] != unreachable else -1
