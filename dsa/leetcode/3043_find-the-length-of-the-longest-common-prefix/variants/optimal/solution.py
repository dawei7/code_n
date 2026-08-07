class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()

        for value in arr1:
            while value:
                prefixes.add(value)
                value //= 10

        longest = 0

        for value in arr2:
            while value and value not in prefixes:
                value //= 10

            if value:
                longest = max(longest, len(str(value)))

        return longest
