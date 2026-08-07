from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = [""] * len(s)
        for character, destination in zip(s, indices):
            shuffled[destination] = character
        return "".join(shuffled)
