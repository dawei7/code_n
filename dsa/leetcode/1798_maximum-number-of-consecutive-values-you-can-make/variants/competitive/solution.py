class Solution:
    def getMaximumConsecutive(self, coins: list[int]) -> int:
        coins.sort()
        reach = 1

        for coin in coins:
            if coin > reach:
                break
            reach += coin

        return reach
