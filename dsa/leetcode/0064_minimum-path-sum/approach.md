## General

**Define the best cost for every destination cell**

`f[i][j]` is the minimum sum of values along any valid path from the top-left cell to `(i,j)`, including both endpoints. Because moves are only right or down, an interior cell can be entered only from above or from the left.

If the best costs to those two predecessors are known, every path to the current cell is one of those predecessor paths plus `grid[i][j]`. Choosing the cheaper predecessor gives

$$
f[i][j]=\min(f[i-1][j],f[i][j-1])+\texttt{grid}[i][j].
$$

The method stores this recurrence in a full table with the same dimensions as the input.

**Initialize the start with its own value**

The path sum includes both endpoints. Therefore, the cost to reach `(0,0)` is `grid[0][0]`, not zero. Setting `f[0][0]` correctly anchors every later prefix sum.

The contract guarantees a non-empty rectangular grid, so both `grid[0][0]` and the matching DP cell exist.

**First-column cells have only one possible predecessor**

For row `i > 0` and column 0, no left cell exists. The robot can arrive only from `(i-1,0)`, so

$$
f[i][0]=f[i-1][0]+\texttt{grid}[i][0].
$$

The first initialization loop builds the cumulative cost of moving straight down. A minimum operation would be inappropriate here because there is only one legal route.

**First-row cells also have one possible predecessor**

For column `j > 0` and row 0, only the left cell exists. The second initialization loop adds values from left to right, producing the cost of the unique all-right path.

Separating these boundaries prevents invalid negative-index accesses and avoids pretending that an outside-grid route has cost zero, which could incorrectly beat a real positive path.

**Fill the interior after its dependencies**

The nested loops start at row 1 and column 1. Row-major order ensures the entire previous row is complete and the current row's left cell is complete before each recurrence is evaluated.

For `[[1,3,1],[1,5,1],[4,2,1]]`, first-column costs become `[1,2,6]` and first-row costs become `[1,4,5]`. Interior values then yield second row `[2,7,6]` and final row `[6,8,7]`. The bottom-right answer is 7.

**Why retaining only the cheaper predecessor is safe**

Every continuation from `(i,j)` adds the same future cell values regardless of which path reached `(i,j)`. If one prefix has a larger sum than another at the same coordinate, it can never become better later because both have identical available suffix moves. Keeping only the minimum cost loses no globally optimal solution.

The non-negative constraint makes this intuition especially direct, but the acyclic right/down recurrence would remain valid even with negative cell values because paths cannot loop back and exploit them repeatedly.


After each DP cell is filled in the initialization or row-major traversal, it contains the exact minimum cost to that coordinate. The base and single-predecessor boundaries are exact because they have only one path.

For an interior cell, any valid path's final move comes from above or left. By induction, the table holds the best cost to each predecessor. Adding the current value to the smaller one produces a valid path and cannot exceed any alternative path. Thus the recurrence is exact.

When all cells are processed, `f[-1][-1]` is the exact minimum sum to the required destination.

**A source-versus-manifest space mismatch**

The selected source allocates $mn$ DP integers. Its auxiliary space is $O(mn)$, not the manifest's $O(n)$. A rolling one-row implementation can meet $O(n)$ because each state needs only the previous row and current left value, but that optimization is not present here.

## Complexity detail

Boundary initialization and the interior loops together fill each of the $mn$ table cells once, with constant work per cell. Time is $O(mn)$.

The DP table contains $mn$ integers, so auxiliary space is $O(mn)$. The returned answer is one scalar, and the input grid is unchanged. Thus the manifest's time bound is accurate, while its $O(n)$ space bound is not accurate for this exact source.

## Alternatives and edge cases

- **Rolling one-dimensional DP:** Reuse an array where `dp[j]` is above before update and current after update. It reduces space to $O(n)$.
- **Modify the grid in place:** Replace each cell with its minimum arrival cost. This achieves $O(1)$ auxiliary space but destroys the original grid values.
- **Top-down memoization:** Recursively choose right/down and cache results. It has $O(mn)$ states plus recursion-stack overhead.
- **Naive recursion:** It recomputes overlapping suffix states exponentially.
- **One cell:** The initialized starting value is returned directly.
- **One row:** Only the first-row prefix loop runs, summing the unique path.
- **One column:** Only the first-column prefix loop runs.
- **Zero-valued cells:** They contribute no additional cost and require no special handling.
- **Endpoint inclusion:** Initializing with `grid[0][0]` and adding every visited cell ensures both start and destination are counted.
- **Input preservation:** All accumulated costs live in `f`, not in `grid`.
