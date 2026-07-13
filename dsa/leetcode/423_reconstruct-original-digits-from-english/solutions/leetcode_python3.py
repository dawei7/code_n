from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        letters = Counter(s)
        counts = [0] * 10

        counts[0] = letters["z"]
        counts[2] = letters["w"]
        counts[4] = letters["u"]
        counts[6] = letters["x"]
        counts[8] = letters["g"]
        counts[3] = letters["h"] - counts[8]
        counts[5] = letters["f"] - counts[4]
        counts[7] = letters["s"] - counts[6]
        counts[1] = letters["o"] - counts[0] - counts[2] - counts[4]
        counts[9] = letters["i"] - counts[5] - counts[6] - counts[8]

        return "".join(str(digit) * count for digit, count in enumerate(counts))
