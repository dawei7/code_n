from typing import List


class Solution:
    def expand(self, s: str) -> List[str]:
        groups = []
        index = 0
        while index < len(s):
            if s[index] == "{":
                end = s.index("}", index)
                groups.append(sorted(s[index + 1 : end].split(",")))
                index = end + 1
            else:
                groups.append([s[index]])
                index += 1

        result = []
        path = []

        def visit(position: int) -> None:
            if position == len(groups):
                result.append("".join(path))
                return
            for choice in groups[position]:
                path.append(choice)
                visit(position + 1)
                path.pop()

        visit(0)
        return result
