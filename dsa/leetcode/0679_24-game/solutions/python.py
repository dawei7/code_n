from fractions import Fraction
from functools import lru_cache


def solve(cards: list[int]) -> bool:
    @lru_cache(maxsize=None)
    def can_make(values: tuple[Fraction, ...]) -> bool:
        if len(values) == 1:
            return values[0] == 24

        for left_index in range(len(values)):
            for right_index in range(left_index + 1, len(values)):
                left = values[left_index]
                right = values[right_index]
                remaining = [
                    values[index]
                    for index in range(len(values))
                    if index not in (left_index, right_index)
                ]
                results = {
                    left + right,
                    left - right,
                    right - left,
                    left * right,
                }
                if right != 0:
                    results.add(left / right)
                if left != 0:
                    results.add(right / left)

                for result in results:
                    next_values = tuple(sorted([*remaining, result]))
                    if can_make(next_values):
                        return True
        return False

    return can_make(tuple(sorted(Fraction(card) for card in cards)))

