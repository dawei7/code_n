from collections import defaultdict
from typing import List


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        ordered = sorted(words)
        by_first = defaultdict(list)
        by_corners = defaultdict(list)

        for word in ordered:
            by_first[word[0]].append(word)
            by_corners[(word[0], word[3])].append(word)

        squares = []
        for top in ordered:
            for left in by_first[top[0]]:
                if left == top:
                    continue
                for right in by_first[top[3]]:
                    if right == top or right == left:
                        continue
                    for bottom in by_corners[(left[3], right[3])]:
                        if bottom != top and bottom != left and bottom != right:
                            squares.append([top, left, right, bottom])

        return squares
