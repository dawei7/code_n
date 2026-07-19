from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        characters = list(s)
        permutations = []

        def generate(index: int) -> None:
            if index == len(characters):
                permutations.append("".join(characters))
                return
            if characters[index].isalpha():
                original = characters[index]
                characters[index] = original.lower()
                generate(index + 1)
                characters[index] = original.upper()
                generate(index + 1)
                characters[index] = original
            else:
                generate(index + 1)

        generate(0)
        return permutations
