class Solution:
    def freqAlphabets(self, s: str) -> str:
        decoded = []
        index = 0

        while index < len(s):
            if index + 2 < len(s) and s[index + 2] == "#":
                value = int(s[index : index + 2])
                index += 3
            else:
                value = int(s[index])
                index += 1
            decoded.append(chr(ord("a") + value - 1))

        return "".join(decoded)
