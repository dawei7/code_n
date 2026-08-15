# Continuous Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2762 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Queue, Sliding Window, Heap (Priority Queue), Ordered Set, Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Continuous Subarrays](https://leetcode.com/problems/continuous-subarrays/) |

## Problem Description

### Goal

Given a 0-indexed integer array `nums`, call a non-empty contiguous subarray continuous when the absolute difference between every pair of values in that subarray is at most $2$.

Equivalently, a subarray is continuous exactly when its maximum value minus its minimum value is at most $2$. Count each qualifying contiguous index interval, and return the total number of continuous subarrays of `nums`.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1 \leq n \leq 10^5$ and $1 \leq \texttt{nums[i]} \leq 10^9$.

**Return value**

Return the number of non-empty contiguous subarrays whose values satisfy $\max - \min \leq 2$. The result may exceed a 32-bit integer.

### Examples

#### Example 1

- **Input:** `nums = [5,4,2,4]`
- **Output:** `8`
- **Explanation:** All four singletons, the three adjacent pairs, and `[4,2,4]` are continuous.

#### Example 2

- **Input:** `nums = [1,2,3]`
- **Output:** `6`
- **Explanation:** Every non-empty subarray has a maximum and minimum differing by at most $2$.

#### Example 3

- **Input:** `nums = [1,4]`
- **Output:** `2`
- **Explanation:** Each singleton is continuous, but `[1,4]` has range $3$.
