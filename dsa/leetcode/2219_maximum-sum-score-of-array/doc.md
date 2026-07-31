# Maximum Sum Score of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2219 |
| Difficulty | Medium |
| Topics | Array, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-sum-score-of-array/) |

## Problem Description
### Goal

For every index $i$ in a 0-indexed integer array, consider two inclusive sums: the sum of the first $i+1$ elements and the sum of the last $n-i$ elements. The element at index $i$ belongs to both of these ranges.

The sum score at $i$ is the larger of its prefix sum and suffix sum. Return the largest sum score attained at any index. Array values may be negative, so the answer is not necessarily nonnegative.

### Function Contract
**Inputs**

- `nums`: A nonempty list of integers.

Let $n=\lvert\texttt{nums}\rvert$.

**Return value**

Return the maximum, over all indices $i$, of the inclusive prefix sum through $i$ and the inclusive suffix sum beginning at $i$.

### Examples
**Example 1**

- Input: `nums = [4, 3, -2, 5]`
- Output: `10`

**Example 2**

- Input: `nums = [-3, -5]`
- Output: `-3`

**Example 3**

- Input: `nums = [7]`
- Output: `7`
