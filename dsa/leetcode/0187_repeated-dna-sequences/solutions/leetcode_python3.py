from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        repeated = set()
        answer = []
        for start in range(len(s) - 9):
            sequence = s[start : start + 10]
            if sequence in seen:
                if sequence not in repeated:
                    repeated.add(sequence)
                    answer.append(sequence)
            else:
                seen.add(sequence)
        return answer
