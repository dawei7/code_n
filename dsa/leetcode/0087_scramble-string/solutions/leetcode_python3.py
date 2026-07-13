from functools import cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        length = len(s1)
        prefix1 = [[0] * (length + 1) for _ in range(26)]
        prefix2 = [[0] * (length + 1) for _ in range(26)]
        for index, (first, second) in enumerate(zip(s1, s2), start=1):
            for character in range(26):
                prefix1[character][index] = prefix1[character][index - 1]
                prefix2[character][index] = prefix2[character][index - 1]
            prefix1[ord(first) - ord("a")][index] += 1
            prefix2[ord(second) - ord("a")][index] += 1

        def same_inventory(first_start: int, second_start: int, size: int) -> bool:
            return all(
                prefix1[character][first_start + size]
                - prefix1[character][first_start]
                == prefix2[character][second_start + size]
                - prefix2[character][second_start]
                for character in range(26)
            )

        @cache
        def scramble(first_start: int, second_start: int, size: int) -> bool:
            if (
                s1[first_start : first_start + size]
                == s2[second_start : second_start + size]
            ):
                return True
            if not same_inventory(first_start, second_start, size):
                return False
            for split in range(1, size):
                if scramble(first_start, second_start, split) and scramble(
                    first_start + split, second_start + split, size - split
                ):
                    return True
                if scramble(
                    first_start, second_start + size - split, split
                ) and scramble(first_start + split, second_start, size - split):
                    return True
            return False

        return scramble(0, 0, length)
