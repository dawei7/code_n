# Find Maximum Non-decreasing Array Length

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2945 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Stack, Queue, Monotonic Stack, Prefix Sum, Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-maximum-non-decreasing-array-length/) |

## Problem Description

### Goal

You are given a 0-indexed positive-integer array `nums`. In one operation,
choose any nonempty subarray and replace that entire contiguous segment with
one element equal to the segment's sum. Apply this operation any number of
times, including zero times.

Return the maximum possible length of a resulting non-decreasing array.
Equivalently, partition the original array into contiguous nonempty blocks,
replace every block by its sum, and maximize the number of blocks subject to
those block sums being non-decreasing.

### Function Contract

**Inputs**

- `nums`: the positive integers that may be merged in contiguous groups

Let $N=\lvert\texttt{nums}\rvert$. The contract guarantees
$1\le N\le10^5$ and $1\le\texttt{nums[i]}\le10^5$.

**Return value**

The largest number of contiguous block sums that can form a non-decreasing
array.

### Examples

#### Example 1

- **Input:** `nums = [5,2,2]`
- **Output:** `1`
- **Explanation:** Every partition into two or three blocks has a decrease, so all
  values must be merged into the single sum `9`.

#### Example 2

- **Input:** `nums = [1,2,3,4]`
- **Output:** `4`
- **Explanation:** The original array is already non-decreasing.

#### Example 3

- **Input:** `nums = [4,3,2,6]`
- **Output:** `3`
- **Explanation:** Merging `[3,2]` gives the non-decreasing array `[4,5,6]`.
