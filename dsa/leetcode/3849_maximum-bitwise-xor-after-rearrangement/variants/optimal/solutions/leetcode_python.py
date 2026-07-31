class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        zeros = t.count("0")
        ones = len(t) - zeros
        result = []

        for bit in s:
            if bit == "0":
                if ones:
                    result.append("1")
                    ones -= 1
                else:
                    result.append("0")
                    zeros -= 1
            elif zeros:
                result.append("1")
                zeros -= 1
            else:
                result.append("0")
                ones -= 1

        return "".join(result)
