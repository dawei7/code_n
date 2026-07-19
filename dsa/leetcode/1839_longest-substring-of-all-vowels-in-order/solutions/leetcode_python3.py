class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        best = 0
        current_length = 1
        distinct_groups = 1

        for index in range(1, len(word)):
            if word[index] < word[index - 1]:
                current_length = 1
                distinct_groups = 1
            else:
                current_length += 1
                if word[index] > word[index - 1]:
                    distinct_groups += 1

            if distinct_groups == 5:
                best = max(best, current_length)

        return best
