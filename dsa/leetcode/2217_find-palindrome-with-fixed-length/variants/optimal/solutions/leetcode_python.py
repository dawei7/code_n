from typing import List


class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        half_length = (intLength + 1) // 2
        first_half = 10 ** (half_length - 1)
        limit = 10**half_length
        answers = []
        for query in queries:
            prefix = first_half + query - 1
            if prefix >= limit:
                answers.append(-1)
                continue
            text = str(prefix)
            answers.append(int(text + text[-1 - intLength % 2 :: -1]))
        return answers
