from functools import cache


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        modulus = 1_000_000_007
        evil_length = len(evil)
        prefix = [0] * evil_length
        for index in range(1, evil_length):
            matched = prefix[index - 1]
            while matched and evil[index] != evil[matched]:
                matched = prefix[matched - 1]
            if evil[index] == evil[matched]:
                matched += 1
            prefix[index] = matched

        transitions = [[0] * 26 for _ in range(evil_length)]
        for matched in range(evil_length):
            for code in range(26):
                letter = chr(ord('a') + code)
                next_matched = matched
                while next_matched and evil[next_matched] != letter:
                    next_matched = prefix[next_matched - 1]
                if evil[next_matched] == letter:
                    next_matched += 1
                transitions[matched][code] = next_matched

        @cache
        def count(position, matched, tight_low, tight_high):
            if position == n:
                return 1
            low = ord(s1[position]) if tight_low else ord('a')
            high = ord(s2[position]) if tight_high else ord('z')
            total = 0
            for letter_code in range(low, high + 1):
                next_matched = transitions[matched][letter_code - ord('a')]
                if next_matched < evil_length:
                    total += count(position + 1, next_matched, tight_low and letter_code == low, tight_high and letter_code == high)
            return total % modulus

        return count(0, 0, True, True)
