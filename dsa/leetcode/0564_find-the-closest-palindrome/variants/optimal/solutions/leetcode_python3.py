class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        value = int(n)
        prefix_length = (length + 1) // 2
        prefix = int(n[:prefix_length])

        candidates = {
            10 ** (length - 1) - 1,
            10**length + 1,
        }

        for nearby_prefix in (prefix - 1, prefix, prefix + 1):
            text = str(nearby_prefix)
            if length % 2:
                palindrome = text + text[-2::-1]
            else:
                palindrome = text + text[::-1]
            candidates.add(int(palindrome))

        candidates.discard(value)
        candidates = {
            candidate for candidate in candidates if candidate >= 0
        }
        best = min(
            candidates,
            key=lambda candidate: (abs(candidate - value), candidate),
        )
        return str(best)

