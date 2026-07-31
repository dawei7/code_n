# Delete Greatest Value in Each Row

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2500 |
| Difficulty | Easy |
| Topics | Array, Sorting, Heap (Priority Queue), Matrix, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/delete-greatest-value-in-each-row/) |

## Problem Description
### Goal
You are given an $m \times n$ matrix `grid` whose entries are positive integers.

Repeat an operation until the matrix is empty. During one operation, delete an element with the greatest value from every row; when a row contains that greatest value more than once, any one occurrence may be deleted. Among all values removed in that operation, add the maximum to an answer. Every operation therefore reduces the number of columns by exactly one.

Return the accumulated answer after all $n$ operations.

### Function Contract
**Inputs**

- `grid`: An $m \times n$ matrix of positive integers, where $1 \le m,n \le 50$ and every entry is between $1$ and $100$ inclusive.

**Return value**

An integer equal to the sum of the largest value removed during each operation.

### Examples
**Example 1**

- Input: `grid = [[1,2,4],[3,3,1]]`
- Output: `8`
- Explanation: The per-operation removed maxima are $4$, $3$, and $1$, so the answer is $4+3+1=8$.

**Example 2**

- Input: `grid = [[10]]`
- Output: `10`
- Explanation: The only value is removed and added in the single operation.

**Example 3**

- Input: `grid = [[5,5,1],[5,2,2],[4,4,4]]`
- Output: `14`
- Explanation: Ties may be broken arbitrarily; the three contributions are $5$, $5$, and $4$.
