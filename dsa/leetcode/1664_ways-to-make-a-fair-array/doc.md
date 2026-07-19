# Ways to Make a Fair Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1664 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/ways-to-make-a-fair-array/) |

## Problem Description
### Goal
Choose exactly one 0-indexed position from `nums` and remove its element. Every later element shifts one position to the left, so its index parity changes, while earlier elements retain their indices.

An array is fair when the sum of values at even indices equals the sum at odd indices. Count how many removal positions produce a fair remaining array. Each position is a separate choice even when several values are equal.

### Function Contract
**Inputs**

- `nums`: an array of $n$ positive integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^4$.

**Return value**

Return the number of indices whose removal makes the shifted array fair.

### Examples
**Example 1**

- Input: `nums = [2, 1, 6, 4]`
- Output: `1`

Only removing index 1 leaves `[2, 6, 4]`, whose even and odd sums are both 6.

**Example 2**

- Input: `nums = [1, 1, 1]`
- Output: `3`

Removing any position leaves `[1, 1]`, which is fair.

**Example 3**

- Input: `nums = [1, 2, 3]`
- Output: `0`
