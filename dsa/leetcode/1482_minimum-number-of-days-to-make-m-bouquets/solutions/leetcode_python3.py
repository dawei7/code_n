from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        flower_count = len(bloomDay)
        if m * k > flower_count:
            return -1

        def can_make(day: int) -> bool:
            bouquets = 0
            adjacent = 0

            for bloom in bloomDay:
                if bloom <= day:
                    adjacent += 1
                    if adjacent == k:
                        bouquets += 1
                        if bouquets == m:
                            return True
                        adjacent = 0
                else:
                    adjacent = 0

            return False

        left = min(bloomDay)
        right = max(bloomDay)

        while left < right:
            middle = left + (right - left) // 2
            if can_make(middle):
                right = middle
            else:
                left = middle + 1

        return left
