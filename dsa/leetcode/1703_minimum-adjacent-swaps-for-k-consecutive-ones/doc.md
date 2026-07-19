# Minimum Adjacent Swaps for K Consecutive Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1703 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/) |

## Problem Description
### Goal

You are given a binary array `nums` and an integer `k`. One move swaps the values at any two adjacent indices. Swaps may move ones across zeros in either direction, and the array may contain more than the `k` ones that ultimately form the desired group.

Return the minimum number of adjacent swaps needed to make some `k` ones occupy consecutive positions. The chosen ones must preserve their relative order: crossing two indistinguishable ones never helps, while each crossed zero contributes one required adjacent swap.

### Function Contract
**Inputs**

- `nums`: a binary array of length $n$, where $1 \le n \le 10^5$
- `k`: the required number of consecutive ones, with $1 \le k \le \sum_i \texttt{nums[i]}$

Let $m$ be the total number of ones in `nums`.

**Return value**

The minimum adjacent-swap count over every possible choice of `k` ones and every consecutive destination block.

### Examples
**Example 1**

- Input: `nums = [1, 0, 0, 1, 0, 1], k = 2`
- Output: `1`

The last two ones can become adjacent by moving the final one left once.

**Example 2**

- Input: `nums = [1, 0, 0, 0, 0, 0, 1, 1], k = 3`
- Output: `5`

Moving the first one right five places produces three consecutive ones at the end.

**Example 3**

- Input: `nums = [1, 1, 0, 1], k = 2`
- Output: `0`

The first two entries already satisfy the requirement.
