from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        for asteroid in sorted(asteroids):
            if mass < asteroid:
                return False
            mass += asteroid
        return True
