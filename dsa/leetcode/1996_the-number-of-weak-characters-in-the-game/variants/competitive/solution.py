from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda character: (-character[0], character[1]))

        maximum_defense = 0
        weak = 0
        for _, defense in properties:
            if defense < maximum_defense:
                weak += 1
            else:
                maximum_defense = defense

        return weak
