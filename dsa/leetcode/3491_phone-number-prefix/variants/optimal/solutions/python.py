class Solution:
    def phonePrefix(self, numbers: list[str]) -> bool:
        root: dict[str | None, dict] = {}

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


def solve(numbers: list[str]) -> bool:
    return Solution().phonePrefix(numbers)
