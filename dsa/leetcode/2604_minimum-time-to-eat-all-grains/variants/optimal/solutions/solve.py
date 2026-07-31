from typing import List


def solve(hens: List[int], grains: List[int]) -> int:
    hens.sort()
    grains.sort()
    grain_count = len(grains)

    def can_eat_all(time: int) -> bool:
        grain = 0
        for hen in hens:
            if grain == grain_count:
                return True

            if grains[grain] < hen:
                left_distance = hen - grains[grain]
                if left_distance > time:
                    return False
                right_reach = max(
                    hen + time - 2 * left_distance,
                    hen + (time - left_distance) // 2,
                )
            else:
                right_reach = hen + time

            while grain < grain_count and grains[grain] <= right_reach:
                grain += 1

        return grain == grain_count

    low = -1
    high = 2 * 10**9
    while high - low > 1:
        middle = (low + high) // 2
        if can_eat_all(middle):
            high = middle
        else:
            low = middle

    return high
