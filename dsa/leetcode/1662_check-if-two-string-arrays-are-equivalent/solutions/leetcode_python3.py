from itertools import chain, zip_longest
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        first = chain.from_iterable(word1)
        second = chain.from_iterable(word2)
        return all(left == right for left, right in zip_longest(first, second))
