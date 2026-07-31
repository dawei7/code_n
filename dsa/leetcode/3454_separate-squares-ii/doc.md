# Separate Squares II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3454 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Segment Tree, Sweep Line |
| Official Link | [LeetCode](https://leetcode.com/problems/separate-squares-ii/) |

## Problem Description
### Goal
Each entry `squares[i] = [x_i, y_i, l_i]` represents an axis-aligned square with bottom-left corner $(x_i, y_i)$ and side length $l_i$. Consider the geometric region covered by at least one square, and divide that union with a horizontal line into the portion above the line and the portion below it.

Find the minimum y-coordinate at which the two union areas are equal. Overlapping regions count only once, no matter how many squares cover them. If a vertical gap permits several balancing lines, choose the lowest one. An answer within $10^{-5}$ of the exact minimum is accepted.

### Function Contract
**Inputs**

- `squares`: A list of $n$ triples `[x_i, y_i, l_i]` giving each square's bottom-left coordinates and positive side length.

The constraints are $1 \le n \le 5 \cdot 10^4$, $0 \le x_i, y_i \le 10^9$, and $1 \le l_i \le 10^9$. The union area of all squares is at most $10^{15}$.

**Return value**

Return the minimum y-coordinate of a horizontal line that leaves equal union area above and below it.

### Examples
**Example 1**

- Input: `squares = [[0, 0, 1], [2, 2, 1]]`
- Output: `1.00000`

Every height from $1$ through $2$ balances the two disjoint unit squares, so the minimum is $1$.

**Example 2**

- Input: `squares = [[0, 0, 2], [1, 1, 1]]`
- Output: `1.00000`

The smaller square lies inside the area already covered by the larger square, so the union is bisected at $y=1$.
