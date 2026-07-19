from typing import List


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        columns = len(seats[0])
        dp = {0: 0}

        for row in seats:
            usable = 0
            for column, seat in enumerate(row):
                if seat == ".":
                    usable |= 1 << column

            valid_masks = [
                mask
                for mask in range(1 << columns)
                if mask & ~usable == 0 and mask & (mask << 1) == 0
            ]
            next_dp = {}
            for mask in valid_masks:
                students = mask.bit_count()
                next_dp[mask] = max(
                    total + students
                    for previous, total in dp.items()
                    if mask & (previous << 1) == 0
                    and mask & (previous >> 1) == 0
                )
            dp = next_dp

        return max(dp.values())
