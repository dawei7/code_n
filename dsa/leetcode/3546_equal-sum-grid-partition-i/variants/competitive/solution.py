# Time:  O(m * n)
# Space: O(1)

# array
class Solution:
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        def check(range1, range2, get):
            curr = 0
            for i in range1:
                curr += sum(get(i, j) for j in range2)
                if curr == total:
                    return True
                elif curr > total:
                    break
            return False
    
        total = sum(sum(row) for row in grid)
        if total%2:
            return False
        total //= 2
        return check(range(len(grid)), range(len(grid[0])), lambda i, j: grid[i][j]) or \
               check(range(len(grid[0])), range(len(grid)), lambda i, j: grid[j][i])
