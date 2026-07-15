from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        def powers(base):
            values = [1]
            if base == 1:
                return values
            while values[-1] * base <= bound:
                values.append(values[-1] * base)
            return values

        answers = set()
        for x_power in powers(x):
            for y_power in powers(y):
                value = x_power + y_power
                if value <= bound:
                    answers.add(value)
        return list(answers)
