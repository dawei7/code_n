# Maximum Element-Sum of a Complete Subset of Indices

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2862 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/) |

## Problem Description

### Goal

Consider `nums` as a 1-indexed array. Select a nonempty subset of its indices. The subset is complete when the product of every pair of selected indices is a perfect square; in other words, any two distinct selected indices $i$ and $j$ must make $ij$ a perfect square.

The value of a selected subset is the sum of the array elements at those indices. Return the greatest value among all complete subsets. The condition concerns the indices, not the values stored in `nums`.

### Function Contract

**Inputs**

- `nums`: The positive element values, interpreted with indices from $1$ through $n$.

Let $n$ be the length of `nums`. The input satisfies $1 \le n \le 10^4$ and $1 \le \texttt{nums[i]} \le 10^9$.

**Return value**

- Return the maximum sum of values at indices whose every pairwise product is a perfect square.

### Examples

**Example 1**

- Input: `nums = [8, 7, 3, 5, 7, 2, 4, 9]`
- Output: `16`
- Explanation: Select 1-indexed positions $2$ and $8$. Their product is $2 \cdot 8 = 16$, and their values sum to `7 + 9 = 16`.

**Example 2**

- Input: `nums = [8, 10, 3, 8, 1, 13, 7, 9, 4]`
- Output: `20`
- Explanation: Positions $1$, $4$, and $9$ are pairwise compatible because $1 \cdot 4$, $1 \cdot 9$, and $4 \cdot 9$ are perfect squares. Their values sum to `8 + 8 + 4 = 20`.
