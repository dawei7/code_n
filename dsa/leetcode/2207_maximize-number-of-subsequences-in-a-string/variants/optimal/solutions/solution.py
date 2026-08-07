class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        first_count = 0
        second_count = 0
        existing = 0

        for character in text:
            if character == pattern[1]:
                existing += first_count
                second_count += 1
            if character == pattern[0]:
                first_count += 1

        return existing + max(first_count, second_count)
