from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        largest1 = largest2 = largest3 = float("-inf")
        smallest1 = smallest2 = float("inf")

        for value in nums:
            if value >= largest1:
                largest1, largest2, largest3 = value, largest1, largest2
            elif value >= largest2:
                largest2, largest3 = value, largest2
            elif value > largest3:
                largest3 = value

            if value <= smallest1:
                smallest1, smallest2 = value, smallest1
            elif value < smallest2:
                smallest2 = value

        return int(max(
            largest1 * largest2 * largest3,
            largest1 * smallest1 * smallest2,
        ))
