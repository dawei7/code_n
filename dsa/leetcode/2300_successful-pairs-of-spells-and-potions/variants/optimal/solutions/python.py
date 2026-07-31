from bisect import bisect_left
from typing import List


def solve(
    spells: List[int],
    potions: List[int],
    success: int,
) -> List[int]:
    ordered_potions = sorted(potions)
    count = len(ordered_potions)
    return [
        count
        - bisect_left(
            ordered_potions,
            (success + spell - 1) // spell,
        )
        for spell in spells
    ]
