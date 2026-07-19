# Sum of Subsequence Widths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 891 |
| Difficulty | Hard |
| Topics | Array, Math, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-subsequence-widths/) |

## Problem Description
### Goal
The width of a sequence is its maximum element minus its minimum element. A subsequence of `nums` is formed by deleting any number of elements without changing the order of those that remain.

Consider every non-empty subsequence, including distinct index selections that may contain equal values. Single-element subsequences are included and have width zero. Sum all widths and return the result modulo $10^9+7$.

### Function Contract
Let $n=\lvert\texttt{nums}\rvert$.

**Inputs**

- `nums`: an integer array where $1 \leq n \leq 10^5$ and $1 \leq \texttt{nums[i]} \leq 10^5$.

**Return value**

Return the sum of `maximum - minimum` over every non-empty subsequence, reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `nums = [2,1,3]`
- Output: `6`

The seven non-empty subsequences have widths `0, 0, 0, 1, 1, 2, 2`.

**Example 2**

- Input: `nums = [2]`
- Output: `0`

**Example 3**

- Input: `nums = [1,2]`
- Output: `1`

Only the subsequence containing both values has nonzero width.
