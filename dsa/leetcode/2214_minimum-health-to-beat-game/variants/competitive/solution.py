# Time:  O(n)
# Space: O(1)

# greedy
class Solution:
    def minimumHealth(self, damage, armor):
        """
        :type damage: List[int]
        :type armor: int
        :rtype: int
        """
        return sum(damage)-min(max(damage), armor)+1
