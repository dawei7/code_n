from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []

        for candidate in range(left, right + 1):
            working = candidate
            while working:
                digit = working % 10
                if digit == 0 or candidate % digit != 0:
                    break
                working //= 10
            else:
                result.append(candidate)

        return result
