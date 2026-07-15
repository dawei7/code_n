# Minimum Falling Path Sum II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1289 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-falling-path-sum-ii/) |

## Problem Description
### Goal
Given an $n \times n$ integer matrix `grid`, form a falling path with non-zero shifts by choosing exactly one element from every row. The elements chosen from any two adjacent rows must come from different columns.

Return the minimum possible sum of the $n$ selected values. Values may be negative, and for a one-row grid the only selected value is the answer.

### Function Contract
**Inputs**

- `grid`: an $n \times n$ integer matrix, where $1 \le n \le 200$ and $-99 \le \texttt{grid[r][c]} \le 99$.

**Return value**

The minimum sum among all choices of one cell per row whose column differs between every pair of adjacent rows.

### Examples
**Example 1**

- Input: `grid = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `13`
- Explanation: Selecting 1, 5, and 7 uses different columns in adjacent rows and gives the minimum sum.

**Example 2**

- Input: `grid = [[7]]`
- Output: `7`

**Example 3**

- Input: `grid = [[-19,57],[-40,-5]]`
- Output: `-24`
- Explanation: The best valid choice is $-19 + (-5)$; the two row minima share a column and cannot both be selected.

### Required Complexity
- **Time:** $O(n^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

Let the previous-row dynamic-programming value for column $c$ be the minimum sum of a valid path ending there. To extend into the next row at column $c$, add the current grid value to the smallest previous value whose column is not $c$.

**Reduce each transition to two minima.** Find the smallest and second-smallest values in the previous DP row, remembering the smallest value's column. For a current cell outside that column, the smallest previous value is legal. For a current cell in that same column, use the second-smallest value instead. This rule also handles tied minima: scanning all columns makes the second minimum equal to the first when another column has the same value.

Every computed state considers the cheapest legal predecessor. By induction over rows, it is therefore the minimum valid path sum ending at its column. Taking the minimum state after the final row chooses the best endpoint and yields the global minimum.

#### Complexity detail

Each of $n$ rows contains $n$ cells. Finding two previous minima and constructing the next DP row both take $O(n)$ per row, for $O(n^2)$ total time. Only the previous and current DP rows are needed, so the auxiliary space is $O(n)$.

#### Alternatives and edge cases

- **Try every predecessor:** For every cell, scanning all previous columns except its own gives the same recurrence but takes $O(n^3)$ time.
- **Sort every DP row:** Sorting can expose two minima in $O(n \log n)$ per row, which is unnecessary compared with one linear scan.
- **One-cell grid:** No adjacency restriction is applied because the path contains only one row.
- **Tied minima:** The second minimum may equal the first when it comes from another column; values, not only distinct values, must be tracked.
- **Negative values:** The recurrence minimizes ordinary sums and requires no special handling for negative entries.

</details>
