# Separate Squares I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3453 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/separate-squares-i/) |

## Problem Description
### Goal
Each entry `squares[i] = [x_i, y_i, l_i]` describes an axis-aligned square whose bottom-left corner is $(x_i, y_i)$ and whose side length is $l_i$. Choose a horizontal line and add, across every square, the portion of its area lying below that line and the portion lying above it.

Find the minimum possible y-coordinate for which those two totals are equal. Squares may overlap, but their areas remain independent contributions: a region covered by several squares is counted once for each covering square. An answer within $10^{-5}$ of the exact minimum is accepted.

### Function Contract
**Inputs**

- `squares`: A list of $n$ triples `[x_i, y_i, l_i]` describing bottom-left coordinates and positive side lengths.

The constraints are $1 \le n \le 5 \cdot 10^4$, $0 \le x_i, y_i \le 10^9$, and $1 \le l_i \le 10^9$. The sum of all square areas is at most $10^{12}$. Let $R$ be the vertical search range from the lowest bottom edge to the highest top edge.

**Return value**

Return the minimum y-coordinate of a horizontal line for which the total counted area above equals the total counted area below.

### Examples
**Example 1**

- Input: `squares = [[0, 0, 1], [2, 2, 1]]`
- Output: `1.00000`

Every height from $1$ through $2$ balances the two unit squares, so the minimum valid height is $1$.

**Example 2**

- Input: `squares = [[0, 0, 2], [1, 1, 1]]`
- Output: `1.16667`

At $y = 7/6$, the counted area on each side is $5/2$; the geometric overlap still contributes once for each square.
