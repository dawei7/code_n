from collections import defaultdict


class Solution:
    def maxSameLengthRuns(self, s: str) -> int:
        length_frequency = defaultdict(int)
        answer = 0
        run_length = 1

        for index in range(1, len(s) + 1):
            if index < len(s) and s[index] == s[index - 1]:
                run_length += 1
                continue
            length_frequency[run_length] += 1
            answer = max(answer, length_frequency[run_length])
            run_length = 1

        return answer
