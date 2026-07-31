from typing import List


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested = 0
        for battery in batteryPercentages:
            if battery > tested:
                tested += 1
        return tested
