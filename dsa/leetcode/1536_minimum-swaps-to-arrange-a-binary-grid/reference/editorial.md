### Approach: Greedy

#### Intuition

We determine each row sequentially from top to bottom. Suppose the rows from $0 \ldots i - 1$ have already been fixed. Then, the $i$-th row must satisfy the condition that the number of trailing zeros is greater than or equal to $n - i - 1$.

Next, we consider which row in the range $[i \ldots n - 1]$ should be swapped into the $i$-th position. If multiple rows satisfy the condition for the $i$-th row, we should choose the one that is closest to the $i$-th position to minimize the total number of swaps.

You might wonder whether this greedy choice is always correct. Suppose there are several rows that satisfy the condition for the $i$-th row. These rows must also satisfy the requirements for rows $i + 1 \ldots n - 1$, because as $i$ increases, the constraint on the number of trailing zeros becomes weaker. Therefore, any row that can be placed at position $i$ can also be placed at later positions. As a result, making the greedy choice at each step will not prevent us from successfully arranging the remaining rows.

Finally, consider the implementation details. To avoid repeatedly traversing each row from right to left to count trailing zeros, we first preprocess the position of the last '1' in each row using an $O(n^2)$ pass. Let this position be denoted by $\textit{pos}[i]$.

Then, we simulate the greedy strategy row by row from top to bottom. For each $i$, we find the nearest row $j$ in the range $[i \ldots n - 1]$ such that $\textit{pos}[j] \le i$. We then bring that row to position $i$. The number of swaps required for this step is $j - i$.

#### Implementation

```python
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pos = [-1] * n
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    pos[i] = j
                    break

        ans = 0
        for i in range(n):
            k = -1
            for j in range(i, n):
                if pos[j] <= i:
                    ans += j - i
                    k = j
                    break

            if k != -1:
                for j in range(k, i, -1):
                    pos[j], pos[j - 1] = pos[j - 1], pos[j]
            else:
                return -1

        return ans
```

#### Complexity Analysis

Let $n$ be the number of rows in the grid.

- Time complexity: $O(n^2)$.

  Preprocessing the $\textit{pos}$ array requires $O(n^2)$ time. The greedy process may also take $O(n^2)$ time in the worst case. Therefore, the overall time complexity is $O(n^2)$.

- Space complexity: $O(n)$.

  The $\textit{pos}$ array requires $O(n)$ space.

---