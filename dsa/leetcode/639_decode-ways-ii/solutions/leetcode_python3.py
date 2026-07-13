class Solution:
    def numDecodings(self, s: str) -> int:
        modulus = 1_000_000_007

        def single_count(character):
            if character == "*":
                return 9
            return 0 if character == "0" else 1

        def pair_count(first, second):
            if first == "*" and second == "*":
                return 15
            if first == "*":
                return 2 if second <= "6" else 1
            if second == "*":
                if first == "1":
                    return 9
                if first == "2":
                    return 6
                return 0
            return int(10 <= int(first + second) <= 26)

        two_back = 1
        one_back = single_count(s[0])
        for index in range(1, len(s)):
            current = (
                single_count(s[index]) * one_back
                + pair_count(s[index - 1], s[index]) * two_back
            ) % modulus
            two_back, one_back = one_back, current
        return one_back
