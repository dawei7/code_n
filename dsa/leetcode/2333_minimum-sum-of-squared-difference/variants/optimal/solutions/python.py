from collections import Counter
from typing import List


def solve(nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
    differences = [abs(first - second) for first, second in zip(nums1, nums2)]
    operations = k1 + k2
    if operations >= sum(differences):
        return 0

    frequency = Counter(differences)
    levels = sorted(frequency, reverse=True)
    leveled_count = 0

    for level_index, level in enumerate(levels):
        leveled_count += frequency[level]
        next_level = levels[level_index + 1] if level_index + 1 < len(levels) else 0
        cost = (level - next_level) * leveled_count
        if operations >= cost:
            operations -= cost
            continue

        full_steps, partially_reduced = divmod(operations, leveled_count)
        final_level = level - full_steps
        answer = (
            (leveled_count - partially_reduced) * final_level * final_level
            + partially_reduced * (final_level - 1) * (final_level - 1)
        )
        for lower_level in levels[level_index + 1 :]:
            answer += frequency[lower_level] * lower_level * lower_level
        return answer

    return 0
