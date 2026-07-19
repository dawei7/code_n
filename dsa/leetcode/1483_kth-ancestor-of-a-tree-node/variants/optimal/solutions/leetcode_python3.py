from typing import List


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        levels = max(1, n.bit_length())
        self.up = [list(parent)]

        for _ in range(1, levels):
            previous = self.up[-1]
            current = [
                -1 if ancestor == -1 else previous[ancestor]
                for ancestor in previous
            ]
            self.up.append(current)

    def getKthAncestor(self, node: int, k: int) -> int:
        bit = 0

        while k and node != -1:
            if k & 1:
                node = self.up[bit][node]
            k >>= 1
            bit += 1

        return node
