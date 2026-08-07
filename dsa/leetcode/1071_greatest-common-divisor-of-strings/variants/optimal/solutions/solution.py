from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        divisor_length = gcd(len(str1), len(str2))
        candidate = str1[:divisor_length]

        for index, character in enumerate(str1):
            if character != candidate[index % divisor_length]:
                return ""
        for index, character in enumerate(str2):
            if character != candidate[index % divisor_length]:
                return ""
        return candidate
