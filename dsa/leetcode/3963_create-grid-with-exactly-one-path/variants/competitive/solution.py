# Time:  O(m * n)
# Space: O(1)

# array
class Solution:
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        result = [['#']*n for _ in range(m)]
        for j in range(n):
            result[0][j] = '.'
        for i in range(m):
            result[i][-1] = '.'
        return ["".join(row) for row in result]
