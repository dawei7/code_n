# Find the Middle Index in Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1991 |
| Difficulty | Easy |
| Topics | Array, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-middle-index-in-array/) |

## Problem Description
### Goal
Given a 0-indexed integer array `nums`, an index is a middle index when the sum
of every element strictly before it equals the sum of every element strictly
after it. The value stored at the candidate index belongs to neither side.

An empty side has sum `0`, so the first or last position may qualify. Return the
leftmost valid middle index if one or more exist; return `-1` when no position
satisfies the equality.

### Function Contract
**Inputs**

- `nums`: a list of $N$ integers, where $1 \le N \le 100$ and
  $-1000 \le \texttt{nums[i]} \le 1000$.

**Return value**

- The smallest index `i` satisfying
  $\sum_{j=0}^{i-1}\texttt{nums[j]}
  = \sum_{j=i+1}^{N-1}\texttt{nums[j]}$, or `-1` if none exists.

### Examples
**Example 1**

- Input: `nums = [2, 3, -1, 8, 4]`
- Output: `3`

Both side sums at index `3` equal `4`.

**Example 2**

- Input: `nums = [1, -1, 4]`
- Output: `2`

The right side is empty and the left side sums to `0`.

**Example 3**

- Input: `nums = [2, 5]`
- Output: `-1`
