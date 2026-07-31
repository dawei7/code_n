from typing import List


def solve(brackets: List[List[int]], income: int) -> float:
    previous_upper = 0
    tax_in_percent_dollars = 0

    for upper, percent in brackets:
        taxable_amount = min(income, upper) - previous_upper
        if taxable_amount > 0:
            tax_in_percent_dollars += taxable_amount * percent
        if upper >= income:
            break
        previous_upper = upper

    return tax_in_percent_dollars / 100
