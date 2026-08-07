class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        longest = -1
        for index, character in enumerate(s):
            if character in first:
                longest = max(longest, index - first[character] - 1)
            else:
                first[character] = index
        return longest
