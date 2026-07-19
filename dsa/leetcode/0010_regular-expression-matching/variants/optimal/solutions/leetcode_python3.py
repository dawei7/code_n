class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        previous = [False] * (len(p) + 1)
        previous[0] = True
        for j in range(2, len(p) + 1):
            if p[j - 1] == "*":
                previous[j] = previous[j - 2]

        for char in s:
            current = [False] * (len(p) + 1)
            for j in range(1, len(p) + 1):
                token = p[j - 1]
                if token == "*":
                    repeated = p[j - 2]
                    current[j] = current[j - 2] or (
                        (repeated == "." or repeated == char) and previous[j]
                    )
                else:
                    current[j] = previous[j - 1] and (token == "." or token == char)
            previous = current
        return previous[-1]
