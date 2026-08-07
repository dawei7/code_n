from typing import List


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        target_length = len(target)
        longest = [0] * target_length

        for word in words:
            combined = word + "{" + target
            z = [0] * len(combined)
            left = right = 0
            for index in range(1, len(combined)):
                if index <= right:
                    z[index] = min(right - index + 1, z[index - left])
                while index + z[index] < len(combined) and combined[z[index]] == combined[index + z[index]]:
                    z[index] += 1
                if index + z[index] - 1 > right:
                    left = index
                    right = index + z[index] - 1

            offset = len(word) + 1
            for start in range(target_length):
                if z[offset + start] > longest[start]:
                    longest[start] = z[offset + start]

        pieces = 0
        current_end = 0
        farthest = 0
        for start, match_length in enumerate(longest):
            if start > farthest:
                return -1
            farthest = max(farthest, start + match_length)
            if start == current_end:
                if farthest == start:
                    return -1
                pieces += 1
                current_end = farthest
                if current_end >= target_length:
                    return pieces

        return -1
