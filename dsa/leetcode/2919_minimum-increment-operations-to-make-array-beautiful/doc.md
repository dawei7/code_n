# Minimum Increment Operations to Make Array Beautiful

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2919 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums` and an integer `k`. In one
operation, choose any valid index and increase its value by one. You may perform
this operation any number of times, including zero.

The array is beautiful when the maximum element of every contiguous subarray
whose size is at least three is greater than or equal to `k`. Return the
minimum number of increment operations required to make `nums` beautiful. A
subarray is a contiguous, non-empty sequence of array elements.

### Function Contract

**Inputs**

- `nums`: A 0-indexed list of non-negative integers.
- `k`: The threshold that every qualifying subarray maximum must reach.

Let $n=\lvert\texttt{nums}\rvert$. The constraints are
$3\le n\le 10^5$, $0\le\texttt{nums[i]}\le 10^9$, and
$0\le\texttt{k}\le 10^9$.

**Return value**

- The minimum total number of unit increments needed to make the array
  beautiful.

### Examples

#### Example 1

- **Input:** `nums = [2, 3, 0, 0, 2], k = 4`
- **Output:** `3`
- **Explanation:** Raise the value at index 1 once and the value at index 4 twice.
  The resulting `[2, 4, 0, 0, 4]` has a value at least four in every
  subarray of size three or more.

#### Example 2

- **Input:** `nums = [0, 1, 3, 3], k = 5`
- **Output:** `2`
- **Explanation:** Raising index 2 from 3 to 5 covers both length-three windows,
  and therefore every longer subarray as well.

#### Example 3

- **Input:** `nums = [1, 1, 2], k = 1`
- **Output:** `0`
- **Explanation:** The only subarray of size at least three already has maximum 2.
