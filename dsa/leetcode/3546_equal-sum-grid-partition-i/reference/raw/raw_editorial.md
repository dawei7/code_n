### Approach 1: 2D Prefix Sum + Enumerating Boundary Elements

#### Intuition

The problem asks us to split the matrix into two parts using **one** horizontal or vertical dividing line, and determine whether such a division exists where the sum of elements in both parts is equal.

When dealing with submatrix sums, it is natural to use prefix sums for efficient preprocessing.

We compute a two-dimensional prefix sum matrix $\textit{sum}[m][n]$, and then perform the following checks:

1. **Vertical dividing line**:
   To check for a vertical split, we enumerate the elements $\textit{sum}[m][i]$ along the bottom boundary of the prefix sum matrix. Each value represents the sum of elements in the submatrix from $\textit{grid}[0][0]$ (top-left) to $\textit{grid}[m - 1][i - 1]$ (bottom-right). If twice this value equals the total sum, then a valid vertical split exists.

2. **Horizontal dividing line**:
   Similarly, to check for a horizontal split, we enumerate the elements along the right boundary of the prefix sum matrix and apply the same condition.

#### Implementation


```python
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        sum = [[0] * (n + 1) for _ in range(m + 1)]
        total = 0
        for i in range(m):
            for j in range(n):
                sum[i + 1][j + 1] = (
                    sum[i + 1][j] + sum[i][j + 1] - sum[i][j] + grid[i][j]
                )
                total += grid[i][j]
        for i in range(m - 1):
            if total == sum[i + 1][n] * 2:
                return True
        for i in range(n - 1):
            if total == sum[m][i + 1] * 2:
                return True
        return False
```


#### Complexity Analysis

Let $m$ be the number of rows and $n$ be the number of columns in the matrix $\textit{grid}$.

- Time complexity: $O(mn)$.
- Space complexity: $O(mn)$.

### Approach 2: Matrix Rotation + Row-wise Enumeration

#### Intuition

The problem involves checking both horizontal and vertical dividing lines. Instead of handling them separately, we can reuse the same logic by rotating the matrix by 90 degrees.

We first check for horizontal splits. Then, by rotating the matrix, vertical splits become horizontal splits in the rotated matrix, allowing us to reuse the same code.

The approach is as follows:

We iterate through each row of the matrix and maintain a running sum of elements from the first row up to the current row. After processing each row, we check whether twice this running sum equals the total sum. If so, a valid dividing line exists.

#### Implementation


```python
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                total += grid[i][j]
        for _ in range(2):
            sum_val = 0
            m = len(grid)
            n = len(grid[0])
            for i in range(m - 1):
                for j in range(n):
                    sum_val += grid[i][j]
                if sum_val * 2 == total:
                    return True
            grid = self.rotation(grid)
        return False

    def rotation(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        tmp = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                tmp[j][m - 1 - i] = grid[i][j]
        return tmp
```


#### Complexity Analysis

Let $m$ be the number of rows and $n$ be the number of columns in the matrix $\textit{grid}$.

- Time complexity: $O(mn)$.
- Space complexity: $O(mn)$.

---