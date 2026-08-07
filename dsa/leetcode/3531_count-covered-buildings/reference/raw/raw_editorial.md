### Approach: Simulation

#### Intuition

According to the problem statement, we are given a two-dimensional array `buildings` and need to count how many buildings are **covered**. A building is considered **covered** if there is at least one other coordinate in each of the four directions: left, right, up, and down. If we treat the scattered coordinates as forming an area, we are essentially counting how many of them are not located on the **edges** of that area.

All coordinates lie within an `n × n` grid, and each coordinate `(x, y)` satisfies
`1 ≤ x ≤ n` and `1 ≤ y ≤ n`. This allows us to determine which coordinates lie on the **edges** by examining whether `x` or `y` is equal to `1` or `n` within their respective rows and columns.

+ If a coordinate is the leftmost in its row, there is no coordinate to its left because all coordinates are unique; similarly, if it is the rightmost, there is no coordinate to its right.

+ If a coordinate is the topmost in its column, there is no coordinate above it; if it is the bottommost, there is no coordinate below it.

+ If a coordinate is neither the leftmost nor rightmost in its row, and also neither the topmost nor bottommost in its column, then it has neighbors in all four directions and is therefore covered.

Based on this observation, the computation proceeds as follows:

+ Traverse all building coordinates and record, for each row, the minimum and maximum `x` values, and for each column, the minimum and maximum `y` values.

+ For a coordinate `(x, y)`, if `x` lies strictly between the row's minimum and maximum, and `y` lies strictly between the column's minimum and maximum, then the coordinate is covered and we increment the answer.

The final result is the value of `ans`.

#### Implementation


```python
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        max_row = [0] * (n + 1)
        min_row = [n + 1] * (n + 1)
        max_col = [0] * (n + 1)
        min_col = [n + 1] * (n + 1)

        for p in buildings:
            x, y = p[0], p[1]
            max_row[y] = max(max_row[y], x)
            min_row[y] = min(min_row[y], x)
            max_col[x] = max(max_col[x], y)
            min_col[x] = min(min_col[x], y)

        res = 0
        for p in buildings:
            x, y = p[0], p[1]
            if (
                x > min_row[y]
                and x < max_row[y]
                and y > min_col[x]
                and y < max_col[x]
            ):
                res += 1

        return res
```


#### Complexity Analysis

Let $m$ be the length of `buildings` and $n$ be the given grid size.

- Time complexity: $O(m)$.
  
  Only two passes over the array are required.

- Space complexity: $O(n)$.
  
  We store the minimum and maximum values for each of the `n` rows and `n` columns.
  
---