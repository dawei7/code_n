class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = 0
        yx = 0

        for left, right in zip(s1, s2):
            if left == right:
                continue
            if left == "x":
                xy += 1
            else:
                yx += 1

        if (xy + yx) % 2:
            return -1
        return xy // 2 + yx // 2 + 2 * (xy % 2)
