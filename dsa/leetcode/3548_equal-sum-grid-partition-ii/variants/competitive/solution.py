# Time:  O(m * n)
# Space: O(m * n)

# array, hash table
class Solution:
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        def check(range1, range2, get):
            curr = 0
            lookup = set()
            begin = -1
            for i in range1:
                if begin == -1:
                    begin = i
                for j in range2:
                    curr += get(i, j)
                    lookup.add(get(i, j))
                diff = curr-(total-curr)
                if diff == 0:
                    return True
                if i != begin and j != 0:
                    if diff in lookup:
                        return True
                elif i == begin:
                    if diff in [get(begin, 0), get(begin, j)]:
                        return True
                else:
                    if diff in [get(begin, 0), (get(i, 0))]:
                        return True
            return False
    
        total = sum(sum(row) for row in grid)
        return check(range(len(grid)), range(len(grid[0])), lambda i, j: grid[i][j]) or \
               check(reversed(range(len(grid))), range(len(grid[0])), lambda i, j: grid[i][j]) or \
               check(range(len(grid[0])), range(len(grid)), lambda i, j: grid[j][i]) or \
               check(reversed(range(len(grid[0]))), range(len(grid)), lambda i, j: grid[j][i])
