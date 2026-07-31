from bisect import bisect_left
from typing import List


def solve(hp: int, damage: List[int], requirement: List[int]) -> int:
    prefix_damage = [0]
    total_damage = 0
    answer = 0
    for room_damage, room_requirement in zip(damage, requirement):
        total_damage += room_damage
        minimum_prefix = total_damage + room_requirement - hp
        first_valid = bisect_left(prefix_damage, minimum_prefix)
        answer += len(prefix_damage) - first_valid
        prefix_damage.append(total_damage)
    return answer
