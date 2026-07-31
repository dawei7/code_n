# Minimum Operations to Make Subarray Elements Equal

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/) |
| Frontend ID | 3422 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Sliding Window, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

An integer array `nums` may be changed any number of times. In one operation, choose any element and either increase it by `1` or decrease it by `1`. The changes may affect any positions, but the goal concerns one contiguous window.

Among every subarray containing exactly `k` elements, choose the one that can be made constant with the fewest operations. All elements in that window may be changed to any common integer. Return the minimum operation count over all eligible windows; elements outside the chosen window need not be equal.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $2 \le n \le 10^5$ and $-10^6 \le \texttt{nums[i]} \le 10^6$.
- `k`: The required subarray length, where $2 \le k \le n$.

**Return value**

Return the minimum number of unit increments and decrements needed to make all elements of at least one length-`k` subarray equal.

### Examples

**Example 1**

- Input: `nums = [4,-3,2,1,-4,6]`, `k = 3`
- Output: `5`
- Explanation: In the window `[-3,2,1]`, raise `-3` to `1` using four operations and lower `2` to `1` using one.

**Example 2**

- Input: `nums = [-2,-2,3,1,4]`, `k = 2`
- Output: `0`
- Explanation: The first length-two window already contains equal values.
