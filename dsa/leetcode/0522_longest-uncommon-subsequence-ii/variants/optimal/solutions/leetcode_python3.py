from collections import Counter
from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        frequencies = Counter(strs)

        def is_subsequence(candidate: str, container: str) -> bool:
            index = 0
            for character in container:
                if index < len(candidate) and candidate[index] == character:
                    index += 1
            return index == len(candidate)

        ordered = sorted(enumerate(strs), key=lambda item: len(item[1]), reverse=True)
        for candidate_index, candidate in ordered:
            if frequencies[candidate] != 1:
                continue
            if all(
                other_index == candidate_index or not is_subsequence(candidate, other)
                for other_index, other in enumerate(strs)
            ):
                return len(candidate)
        return -1
