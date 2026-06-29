


def solve():
    class Solution:
        def longestUniqueSubstring(self, s: str) -> int:
            freq = {}
            left = 0
            longest = 0

            for right in range(len(s)):
                freq[s[right]] = freq.get(s[right], 0) + 1

                while freq[s[right]] > 1:
                    freq[s[left]] -= 1
                    left += 1

                longest = max(longest, right - left + 1)

            return longest


if __name__ == "__main__":
    solve()
