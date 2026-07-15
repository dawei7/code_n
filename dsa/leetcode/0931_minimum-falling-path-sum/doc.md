# Minimum Falling Path Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 931 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-falling-path-sum/) |

## Problem Description

### Goal

Given an $n \times n$ integer `matrix`, find the minimum sum among all falling paths through the matrix. A falling path begins at any element in the first row and includes exactly one element from every row until it reaches the last row.

After selecting position `(row, col)`, the next element must be in row `row + 1` and may be directly below at column `col`, diagonally left at `col - 1`, or diagonally right at `col + 1`, provided that column exists. Return the smallest possible sum of the selected values; matrix entries may be negative.

### Function Contract

**Inputs**

- `matrix`: an $n \times n$ integer matrix, where $1 \le n \le 100$ and every entry lies between $-100$ and $100$ inclusive.

**Return value**

Return the minimum sum of any valid falling path from the first row through the last row.

### Examples

**Example 1**

- Input: `matrix = [[2,1,3],[6,5,4],[7,8,9]]`
- Output: `13`
- Explanation: A minimum path can take values $1$, $5$, and $7$, or $1$, $4$, and $8$.

**Example 2**

- Input: `matrix = [[-19,57],[-40,-5]]`
- Output: `-59`
- Explanation: The path using $-19$ followed by $-40$ has the minimum sum.

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Summarize every path ending in the previous row.** Let `previous[col]` be the minimum sum of a falling path that ends at column `col` of the row already processed. For the first row, these values are simply the matrix entries because a path may start at any column.

**Extend only from legal predecessors.** For each cell in the next row, inspect the available predecessor totals at columns `col - 1`, `col`, and `col + 1`. Add the current matrix value to their minimum and store the result in `current[col]`. Boundary columns omit the nonexistent diagonal predecessor. Every path reaching this cell must use exactly one of these predecessors, and extending the cheapest one is therefore optimal; conversely, that predecessor followed by the current cell constructs a valid path with the stored total.

**Finish anywhere in the last row.** Replace `previous` after each row. By induction, it contains the optimum for every possible endpoint of that row. A complete falling path may end at any last-row column, so the answer is `min(previous)` after all rows have been processed. Negative entries require no special treatment because the recurrence compares complete path sums rather than making a locally greedy choice.

#### Complexity detail

There are $n^2$ cells and each considers at most three predecessors, giving $O(n^2)$ time. Two arrays of $n$ path totals are retained, so the auxiliary-space cost is $O(n)$.

#### Alternatives and edge cases

- **In-place bottom-up dynamic programming:** Add the cheapest predecessor directly into each matrix cell. This keeps $O(n^2)$ time and uses $O(1)$ extra space but mutates the input.
- **Memoized depth-first search:** Explore the three downward moves from every state and cache results. It has the same asymptotic bounds but adds recursion overhead and $O(n^2)$ cached state.
- **Unrestricted predecessor scan:** Checking every column of the previous row and discarding nonadjacent ones remains correct but wastes $O(n^3)$ time.
- **Single-cell matrix:** The only entry is both the start and end, so it is the answer.
- **Negative values:** The minimum path may deliberately include them; no pruning based on a partial positive or negative sum is valid.

</details>
