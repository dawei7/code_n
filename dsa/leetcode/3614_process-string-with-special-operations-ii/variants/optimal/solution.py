class Solution:
    def processStr(self, s: str, k: int) -> str:
        lengths = [0]

        for character in s:
            length = lengths[-1]
            if character == "*":
                length = max(0, length - 1)
            elif character == "#":
                length *= 2
            elif character != "%":
                length += 1
            lengths.append(length)

        if k >= lengths[-1]:
            return "."

        for index in range(len(s) - 1, -1, -1):
            character = s[index]
            previous_length = lengths[index]

            if character == "#":
                k %= previous_length
            elif character == "%":
                k = previous_length - 1 - k
            elif character != "*" and k == previous_length:
                return character

        return "."
