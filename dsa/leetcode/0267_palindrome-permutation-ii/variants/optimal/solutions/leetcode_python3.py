from collections import Counter
from typing import List


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counts = Counter(s)
        odd = [character for character, count in counts.items() if count % 2]
        if len(odd) > 1:
            return []
        center = odd[0] if odd else ""
        half = sorted(
            character
            for character, count in counts.items()
            for _ in range(count // 2)
        )
        used = [False] * len(half)
        path = []
        palindromes = []

        def generate() -> None:
            if len(path) == len(half):
                left = "".join(path)
                palindromes.append(left + center + left[::-1])
                return
            for index, character in enumerate(half):
                if used[index] or (index and half[index - 1] == character and not used[index - 1]):
                    continue
                used[index] = True
                path.append(character)
                generate()
                path.pop()
                used[index] = False

        generate()
        return palindromes
