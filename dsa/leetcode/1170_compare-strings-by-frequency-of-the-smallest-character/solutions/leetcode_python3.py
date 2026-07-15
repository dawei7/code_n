from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def frequency(value: str) -> int:
            smallest = "{"
            count = 0
            for character in value:
                if character < smallest:
                    smallest = character
                    count = 1
                elif character == smallest:
                    count += 1
            return count

        counts = [0] * 11
        for word in words:
            counts[frequency(word)] += 1
        greater = [0] * 11
        for score in range(9, 0, -1):
            greater[score] = greater[score + 1] + counts[score + 1]
        return [greater[frequency(query)] for query in queries]
