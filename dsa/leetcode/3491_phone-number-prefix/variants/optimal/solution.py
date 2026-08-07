from typing import List


class Solution:
    def phonePrefix(self, numbers: List[str]) -> bool:
        root = {}

        for number in numbers:
            node = root
            for digit in number:
                if None in node:
                    return False
                node = node.setdefault(digit, {})

            if node:
                return False
            node[None] = {}

        return True
