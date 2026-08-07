from typing import List


class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        shipments = 0
        maximum = 0

        for value in weight:
            if value < maximum:
                shipments += 1
                maximum = 0
            else:
                maximum = value

        return shipments
