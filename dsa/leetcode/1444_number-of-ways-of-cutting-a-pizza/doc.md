# Number of Ways of Cutting a Pizza

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1444 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Memoization, Matrix, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/) |

## Problem Description
### Goal

A rectangular pizza is represented by an $m \times n$ grid of characters.
An `A` marks a cell containing an apple, while `.` marks an empty cell.
Make exactly $k-1$ straight cuts along cell boundaries so that the pizza is
divided among $k$ people.

At each step, choose either a horizontal or vertical cut through the currently
remaining rectangle. A horizontal cut gives the upper part to the next person
and keeps the lower part for later cuts; a vertical cut gives away the left
part and keeps the right part. The final remaining rectangle goes to the last
person. Count the cutting sequences in which every delivered piece contains
at least one apple, and return the count modulo $10^9+7$.

### Function Contract
**Inputs**

- `pizza`: a list of $m$ equal-length strings, each of length $n$, containing
  only `A` and `.`, where $1 \le m,n \le 50$.
- `k`: the exact number of final pieces, where $1 \le k \le 10$.

**Return value**

Return the number of valid ordered cutting sequences modulo $10^9+7$. A
sequence is valid only when all $k$ pieces contain at least one apple.

### Examples
**Example 1**

- Input: `pizza = ["A..", "AAA", "..."], k = 3`
- Output: `3`

**Example 2**

- Input: `pizza = ["A..", "AA.", "..."], k = 3`
- Output: `1`

**Example 3**

- Input: `pizza = ["A..", "A..", "..."], k = 1`
- Output: `1`
- Explanation: No cut is required, and the one delivered piece contains
  apples.
