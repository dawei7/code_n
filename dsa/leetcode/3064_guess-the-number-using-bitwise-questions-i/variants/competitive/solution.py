# Time:  O(logn):
# Space: O(1)

# bit manipulation
class Solution:
    def findNumber(self):
        """
        :rtype: int
        """
        return reduce(lambda accu, x: accu|x, (1<<i for i in range(30) if commonSetBits(1<<i)))
