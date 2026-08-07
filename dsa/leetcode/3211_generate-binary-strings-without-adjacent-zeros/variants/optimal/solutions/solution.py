from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        valid: List[str] = []
        path: List[str] = []

        def generate() -> None:
            if len(path) == n:
                valid.append("".join(path))
                return

            path.append("1")
            generate()
            path.pop()

            if not path or path[-1] != "0":
                path.append("0")
                generate()
                path.pop()

        generate()
        return valid
