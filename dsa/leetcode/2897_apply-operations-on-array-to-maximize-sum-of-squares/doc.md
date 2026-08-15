# Apply Operations on Array to Maximize Sum of Squares

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2897 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums` and a positive integer `k`. You may repeatedly choose two distinct indices $i$ and $j$ and update both values simultaneously:

- Set `nums[i]` to `nums[i] AND nums[j]`.
- Set `nums[j]` to `nums[i] OR nums[j]`, using the two values from before the operation.

After applying any number of operations, choose exactly `k` elements from the resulting array. Maximize the sum of their squares and return that maximum modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.
- `k`: The exact number of final-array elements whose squares are added.

The shared bounds are $1 \le k \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$, where $n=\lvert\texttt{nums}\rvert$. Let $V=\max(\texttt{nums})$.

**Return value**

Return the maximum achievable sum of `k` squared values, reduced modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `nums = [2, 6, 5, 8], k = 2`
- **Output:** `261`
- **Explanation:** The bit occurrences can be concentrated to produce values $15$ and $6$; their squares sum to $225+36=261$.

#### Example 2

- **Input:** `nums = [4, 5, 4, 7], k = 3`
- **Output:** `90`
- **Explanation:** Choosing $7$, $5$, and $4$ already gives the optimal sum $49+25+16=90$.
