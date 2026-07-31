from typing import List


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def occurrences(pattern: str) -> List[int]:
            failure = [0] * len(pattern)
            matched = 0
            for index in range(1, len(pattern)):
                while matched and pattern[matched] != pattern[index]:
                    matched = failure[matched - 1]
                if pattern[matched] == pattern[index]:
                    matched += 1
                failure[index] = matched

            result = []
            matched = 0
            for index, character in enumerate(s):
                while matched and pattern[matched] != character:
                    matched = failure[matched - 1]
                if pattern[matched] == character:
                    matched += 1
                if matched == len(pattern):
                    result.append(index - len(pattern) + 1)
                    matched = failure[matched - 1]
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
