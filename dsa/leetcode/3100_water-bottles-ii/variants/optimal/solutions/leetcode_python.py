class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk = numBottles
        empty = numBottles

        while empty >= numExchange:
            empty -= numExchange
            numExchange += 1
            empty += 1
            drunk += 1

        return drunk
