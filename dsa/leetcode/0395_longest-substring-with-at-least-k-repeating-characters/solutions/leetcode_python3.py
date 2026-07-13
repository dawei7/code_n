class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        best = 0
        base = ord("a")

        for target_unique in range(1, len(set(s)) + 1):
            counts = [0] * 26
            left = 0
            unique = 0
            qualified = 0

            for right, character in enumerate(s):
                index = ord(character) - base
                if counts[index] == 0:
                    unique += 1
                counts[index] += 1
                if counts[index] == k:
                    qualified += 1

                while unique > target_unique:
                    left_index = ord(s[left]) - base
                    if counts[left_index] == k:
                        qualified -= 1
                    counts[left_index] -= 1
                    if counts[left_index] == 0:
                        unique -= 1
                    left += 1

                if unique == target_unique == qualified:
                    best = max(best, right - left + 1)

        return best
