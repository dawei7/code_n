from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        waits = [0] * len(temperatures)
        unresolved = []

        for index, temperature in enumerate(temperatures):
            while unresolved and temperatures[unresolved[-1]] < temperature:
                previous = unresolved.pop()
                waits[previous] = index - previous
            unresolved.append(index)

        return waits
