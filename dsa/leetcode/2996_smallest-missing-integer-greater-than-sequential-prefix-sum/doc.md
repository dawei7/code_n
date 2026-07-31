# Smallest Missing Integer Greater Than Sequential Prefix Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2996 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/) |

## Problem Description
### Goal
You are given a 0-indexed integer array `nums`. A prefix is **sequential** when
each element after the first is exactly one greater than its predecessor. The
one-element prefix containing only `nums[0]` is always sequential.

Find the longest sequential prefix and compute its sum. Starting from that
sum, return the smallest integer that does not occur anywhere in `nums`; the
answer must be greater than or equal to the prefix sum.

### Function Contract
**Inputs**

- `nums`: the positive integer array

Let $N=\lvert\texttt{nums}\rvert$. The contract guarantees $1\le N\le50$ and
$1\le\texttt{nums[i]}\le50$.

**Return value**

Return the first integer at or above the longest sequential-prefix sum that is
absent from the complete array.

### Examples
**Example 1**

- Input: `nums = [1,2,3,2,5]`
- Output: `6`

**Example 2**

- Input: `nums = [3,4,5,1,12,14,13]`
- Output: `15`
- Explanation: The prefix sum is `12`, while `12`, `13`, and `14` are present.

**Example 3**

- Input: `nums = [5]`
- Output: `6`
