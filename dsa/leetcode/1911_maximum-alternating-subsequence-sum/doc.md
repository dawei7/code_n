# Maximum Alternating Subsequence Sum

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-alternating-subsequence-sum/) |
| Frontend ID | 1911 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

For a 0-indexed array, its alternating sum adds the values at even indices and subtracts the values at odd indices. You may form a subsequence of `nums` by deleting any number of elements without changing the relative order of those retained.

After the chosen elements are reindexed from zero, compute their alternating sum and maximize it over all possible subsequences. Return that maximum value. Every input value is positive, although subtracting a selected value can enable a larger later addition.

### Function Contract

**Inputs**

- `nums`: a list of $N$ positive integers.
- $1 \le N \le 10^5$.
- $1 \le \texttt{nums[i]} \le 10^5$.

**Return value**

- Return the maximum alternating sum of any subsequence of `nums`.

### Examples

**Example 1**

- Input: `nums = [4,2,5,3]`
- Output: `7`

Choosing `[4,2,5]` gives $4 - 2 + 5 = 7$.

**Example 2**

- Input: `nums = [5,6,7,8]`
- Output: `8`

The one-element subsequence `[8]` is optimal.

**Example 3**

- Input: `nums = [6,2,1,2,4,5]`
- Output: `10`

Choosing `[6,1,5]` gives $6 - 1 + 5 = 10$.
