# Find Minimum Operations to Make All Elements Divisible by Three

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3190 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/) |

## Problem Description

### Goal

You are given an integer array `nums`. In one operation, choose any one element
and either increase it by exactly $1$ or decrease it by exactly $1$.

Determine the minimum total number of operations needed so that every array
element is divisible by $3$. Operations on different elements are independent,
and the array itself does not need to satisfy any ordering condition.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \le n \le 50$ and
  $1 \le \texttt{nums[i]} \le 50$.

**Return value**

Return the minimum number of unit increments and decrements needed to make all
values divisible by $3$.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `3`
- Explanation: Decrement `1`, increment `2`, and decrement `4`; `3` already
  needs no change.

**Example 2**

- Input: `nums = [3, 6, 9]`
- Output: `0`
