from typing import List


class Solution:
    def stringSequence(self, target: str) -> List[str]:
        screen = []
        sequence = []

        for desired in target:
            screen.append("a")
            sequence.append("".join(screen))

            while screen[-1] != desired:
                screen[-1] = chr(ord(screen[-1]) + 1)
                sequence.append("".join(screen))

        return sequence
