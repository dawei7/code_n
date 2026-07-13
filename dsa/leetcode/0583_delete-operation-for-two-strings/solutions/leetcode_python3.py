class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            longer, shorter = word2, word1
        else:
            longer, shorter = word1, word2

        previous = [0] * (len(shorter) + 1)
        for left_char in longer:
            current = [0] * (len(shorter) + 1)
            for column, right_char in enumerate(shorter, start=1):
                if left_char == right_char:
                    current[column] = previous[column - 1] + 1
                else:
                    current[column] = max(
                        previous[column],
                        current[column - 1],
                    )
            previous = current

        return len(word1) + len(word2) - 2 * previous[-1]

