# Maximum Value Sum by Placing Three Rooks II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3257 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Matrix, Enumeration |
| Official Link | [maximum-value-sum-by-placing-three-rooks-ii](https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/) |

## Problem Description & Examples
### Goal
Given an $m \times n$ 2D grid `board` containing integers, place three rooks on the board such that no two rooks attack each other. This means all three rooks must be placed in pairwise distinct rows and pairwise distinct columns. Find and return the maximum possible sum of the values of the cells where the three rooks are placed.

### Function Contract
**Inputs**

- `board`: `List[List[int]]` - A 2D grid of size $m \times n$ where $3 \le m, n \le 500$ and $-10^9 \le board[i][j] \le 10^9$.

**Return value**

- `int` - The maximum sum of three non-attacking rooks.

### Examples
**Example 1**

- Input: `board = [[-3, 1, 1, 1], [-3, 1, -3, 1], [-3, 2, 1, 1]]`
- Output: `4`
- Explanation: We can place the rooks at `(0, 2)` with value 1, `(1, 3)` with value 1, and `(2, 1)` with value 2. The sum is $1 + 1 + 2 = 4$.

**Example 2**

- Input: `board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
- Output: `15`
- Explanation: We can place the rooks at `(0, 2)` with value 3, `(1, 1)` with value 5, and `(2, 0)` with value 7. The sum is $3 + 5 + 7 = 15$.

**Example 3**

- Input: `board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]`
- Output: `3`
- Explanation: Any valid placement of three rooks will yield a sum of 3.

---

## Underlying Base Algorithm(s)
The problem can be solved efficiently using **Prefix/Suffix Maximums** combined with **Greedy Filtering**.

Since we need to place exactly three rooks in distinct rows and columns, we can designate one rook as the "middle" rook in row $i$ (where $1 \le i \le m-2$). The other two rooks must be placed in some row $r_1 < i$ (prefix) and some row $r_3 > i$ (suffix).

To optimize the search:
1. For each row, we only need to keep track of the top 3 cells with the largest values, because we only have 3 rooks in total.
2. We can precompute a prefix array `prefix` where `prefix[i]` stores the top 3 cells with distinct columns from rows $0 \dots i$.
3. Similarly, we precompute a suffix array `suffix` where `suffix[i]` stores the top 3 cells with distinct columns from rows $i \dots m-1$.
4. Finally, we iterate through each possible middle row $i$ from $1$ to $m-2$. For each $i$, we try all combinations of choosing one cell from `prefix[i-1]`, one cell from the top 3 of row $i$, and one cell from `suffix[i+1]`. We check if their columns are pairwise distinct, and if so, we update our maximum sum.

This reduces the search space from $O(m^3 \cdot n^3)$ to $O(m \cdot n)$ time, which is highly optimal and easily runs within the time limit.

---

## Complexity Analysis
- **Time Complexity**: $O(m \cdot n)$. Finding the top 3 elements for each row takes $O(m \cdot n)$ time. Computing the prefix and suffix arrays takes $O(m)$ steps, where each step merges two small lists of size 3. The final search takes $O(m)$ steps, with $3^3 = 27$ combinations checked per step. Thus, the overall time complexity is dominated by $O(m \cdot n)$.
- **Space Complexity**: $O(m \cdot n)$ to store the input board, and $O(m)$ auxiliary space to store the top 3 elements of each row, prefix, and suffix arrays.
