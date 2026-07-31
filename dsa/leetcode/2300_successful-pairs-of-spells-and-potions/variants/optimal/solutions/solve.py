from bisect import bisect_left
from typing import List


def solve(
    spells: List[int],
    potions: List[int],
    success: int,
) -> List[int]:
    potions.sort()
    potion_count = len(potions)
    answer = []

    for spell in spells:
        required = (success + spell - 1) // spell
        first = bisect_left(potions, required)
        answer.append(potion_count - first)

    return answer
