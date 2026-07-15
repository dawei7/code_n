class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        bounded = "L" + dominoes + "R"
        pieces = []
        left = 0

        for right in range(1, len(bounded)):
            if bounded[right] == ".":
                continue

            if left > 0:
                pieces.append(bounded[left])

            gap = right - left - 1
            if bounded[left] == bounded[right]:
                pieces.append(bounded[left] * gap)
            elif bounded[left] == "L":
                pieces.append("." * gap)
            else:
                half = gap // 2
                pieces.append("R" * half)
                if gap % 2 == 1:
                    pieces.append(".")
                pieces.append("L" * half)

            left = right

        return "".join(pieces)
