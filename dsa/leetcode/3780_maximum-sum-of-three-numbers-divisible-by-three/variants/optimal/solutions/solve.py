from typing import List


def solve(nums: List[int]) -> int:
    best = [[-1, -1, -1] for _ in range(4)]
    best[0][0] = 0
    for value in nums:
        remainder = value % 3
        for chosen in range(2, -1, -1):
            for current_remainder in range(3):
                current = best[chosen][current_remainder]
                if current < 0:
                    continue
                next_remainder = (current_remainder + remainder) % 3
                best[chosen + 1][next_remainder] = max(best[chosen + 1][next_remainder], current + value)
    return max(0, best[3][0])
