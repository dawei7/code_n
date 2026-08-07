from math import gcd


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        common = gcd(p, q)
        horizontal_rooms = p // common
        vertical_rooms = q // common

        if horizontal_rooms % 2 == 1:
            return 1 if vertical_rooms % 2 == 1 else 0
        return 2
