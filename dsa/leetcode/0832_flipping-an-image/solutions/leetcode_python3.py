from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[value ^ 1 for value in reversed(row)] for row in image]
