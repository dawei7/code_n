# Time:  O(n)
# Space: O(1)

class Solution:
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        result = [first]
        for x in encoded:
            result.append(result[-1]^x)
        return result
