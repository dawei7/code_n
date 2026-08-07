from typing import List


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def occurrences(pattern: str) -> List[int]:
            result = []
            index = s.find(pattern)
            while index != -1:
                result.append(index)
                index = s.find(pattern, index + 1)
            return result

        first = occurrences(a)
        second = occurrences(b)
        answer = []
        second_index = 0

        for index in first:
            while second_index < len(second) and second[second_index] < index - k:
                second_index += 1
            if second_index < len(second) and second[second_index] <= index + k:
                answer.append(index)

        return answer
