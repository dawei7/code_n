from typing import List


class Solution:
    def canMakePaliQueries(
        self, s: str, queries: List[List[int]]
    ) -> List[bool]:
        masks = [0]
        for character in s:
            masks.append(masks[-1] ^ (1 << (ord(character) - ord("a"))))

        answers = []
        for left, right, replacements in queries:
            odd_count = (masks[right + 1] ^ masks[left]).bit_count()
            answers.append(odd_count // 2 <= replacements)
        return answers
