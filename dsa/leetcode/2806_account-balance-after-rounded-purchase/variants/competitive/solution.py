# Time:  O(1)
# Space: O(1)

# math
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        return 100-(purchaseAmount+5)//10*10
