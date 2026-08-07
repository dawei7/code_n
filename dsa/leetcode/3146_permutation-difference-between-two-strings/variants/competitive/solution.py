class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        positions = {character: index for index, character in enumerate(t)}
        return sum(abs(index - positions[character]) for index, character in enumerate(s))
