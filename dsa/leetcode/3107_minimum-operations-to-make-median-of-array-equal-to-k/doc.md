# Minimum Operations to Make Median of Array Equal to K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3107 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [minimum-operations-to-make-median-of-array-equal-to-k](https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/) |

## Problem Description

### Goal

You are given an integer array `nums` and an integer `k`. In one operation, choose any element and either increase it by $1$ or decrease it by $1$. You may perform this operation any number of times.

Sort an array in non-decreasing order and let $n$ be its length. Its median is the element at index $\lfloor n/2 \rfloor$. In particular, when $n$ is even and there are two middle elements, this definition selects the larger one rather than their average.

Return the minimum number of operations needed to make the median of `nums` equal to `k`.

### Function Contract

**Inputs**

- `nums`: A nonempty list of $n$ integers, where $1 \le n \le 2 \cdot 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.
- `k`: The required median, where $1 \le k \le 10^9$.

**Return value**

- The minimum total number of unit increases and decreases required to make the median exactly `k`.

### Examples

#### Example 1

- **Input:** `nums = [2, 5, 6, 8, 5], k = 4`
- **Output:** `2`
- **Explanation:** Decreasing the two values equal to $5$ once produces an array whose sorted form has median $4$.

#### Example 2

- **Input:** `nums = [2, 5, 6, 8, 5], k = 7`
- **Output:** `3`
- **Explanation:** Increasing one $5$ twice and the $6$ once makes the median $7$.

#### Example 3

- **Input:** `nums = [1, 2, 3, 4, 5, 6], k = 4`
- **Output:** `0`
- **Explanation:** For an even-length array the larger middle value is used, so the median is already $4$.
