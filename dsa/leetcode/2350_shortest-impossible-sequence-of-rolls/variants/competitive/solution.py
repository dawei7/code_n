# Time:  O(n)
# Space: O(k)

# constructive algorithms
class Solution:
    def shortestSequence(self, rolls, k):
        """
        :type rolls: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        lookup = set()
        for x in rolls:
            lookup.add(x)
            if len(lookup) != k:
                continue
            lookup.clear()
            l += 1
        return l+1
