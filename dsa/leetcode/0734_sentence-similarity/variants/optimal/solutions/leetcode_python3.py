from typing import List


class Solution:
    def areSentencesSimilar(
        self,
        sentence1: List[str],
        sentence2: List[str],
        similarPairs: List[List[str]],
    ) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        direct = set()
        for left, right in similarPairs:
            direct.add((left, right))
            direct.add((right, left))

        return all(
            first == second or (first, second) in direct
            for first, second in zip(sentence1, sentence2)
        )
