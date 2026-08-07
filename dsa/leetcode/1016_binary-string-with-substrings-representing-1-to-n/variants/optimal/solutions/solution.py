class Solution:
    def queryString(self, s: str, n: int) -> bool:
        maximum_length = n.bit_length()
        found = set()

        for start, character in enumerate(s):
            if character == "0":
                continue
            value = 0
            for end in range(start, min(len(s), start + maximum_length)):
                value = value * 2 + int(s[end])
                if value > n:
                    break
                found.add(value)

        return len(found) == n
