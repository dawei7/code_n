from collections import defaultdict
from typing import List


class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        changes = defaultdict(int)
        for position, radius in lights:
            changes[position - radius] += 1
            changes[position + radius + 1] -= 1

        brightness = 0
        maximum = 0
        answer = 0
        for position in sorted(changes):
            brightness += changes[position]
            if brightness > maximum:
                maximum = brightness
                answer = position

        return answer
