class Solution:
    def numberOfWays(self, s: str) -> int:
        singles = [0, 0]
        pairs = [0, 0]
        ways = 0
        for character in s:
            building = ord(character) - ord("0")
            other = 1 - building
            ways += pairs[other]
            pairs[building] += singles[other]
            singles[building] += 1
        return ways
