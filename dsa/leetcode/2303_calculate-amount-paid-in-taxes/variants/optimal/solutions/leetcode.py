from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        lower = 0

        for upper, rate in brackets:
            taxed = min(upper, income) - lower
            if taxed > 0:
                tax += taxed * rate
            if income <= upper:
                return tax / 100
            lower = upper

        return tax / 100
