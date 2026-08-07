from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        frequency = [0] * 10
        for digit in digits:
            frequency[digit] += 1

        total = 0
        for hundreds in range(1, 10):
            if frequency[hundreds] == 0:
                continue
            frequency[hundreds] -= 1

            for tens in range(10):
                if frequency[tens] == 0:
                    continue
                frequency[tens] -= 1

                for units in range(0, 10, 2):
                    if frequency[units] > 0:
                        total += 1

                frequency[tens] += 1

            frequency[hundreds] += 1

        return total
