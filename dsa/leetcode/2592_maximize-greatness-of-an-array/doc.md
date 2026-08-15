# Maximize Greatness of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2592 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-greatness-of-an-array/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums`. Rearrange all of its elements into a permutation `perm` of your choice.

The greatness of that arrangement is the number of indices `i` for which `perm[i] > nums[i]`. The comparison is strict, so assigning an equal value to a position does not contribute. Every original element must appear exactly once in `perm`, including duplicate values.

Return the largest greatness achievable by any permutation.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $1 \leq n \leq 10^5$ and $0 \leq \texttt{nums[i]} \leq 10^9$.

**Return value**

- The maximum number of positions whose assigned permutation value is strictly greater than the original value at that position.

### Examples

#### Example 1

- **Input:** `nums = [1,3,5,2,1,3,1]`
- **Output:** `4`

For example, `perm = [2,5,1,3,3,1,1]` wins at indices `0`, `1`, `3`, and `4`.

#### Example 2

- **Input:** `nums = [1,2,3,4]`
- **Output:** `3`

The permutation `[2,3,4,1]` wins at the first three positions.
