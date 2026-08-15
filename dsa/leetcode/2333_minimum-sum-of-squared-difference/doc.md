# Minimum Sum of Squared Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2333 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-sum-of-squared-difference/) |

## Problem Description

### Goal

Two 0-indexed integer arrays `nums1` and `nums2` have the same length. Their
sum of squared difference is

$$
\sum_{i=0}^{n-1}(\texttt{nums1[i]}-\texttt{nums2[i]})^2.
$$

You may apply at most `k1` operations to `nums1` and at most `k2` operations
to `nums2`. One operation selects any element of the corresponding array and
increments or decrements it by one. Modified values may become negative.
Return the smallest possible sum of squared difference after choosing how many
allowed operations to use and where to apply them.

### Function Contract

Let

$$
D=\max_{0\le i<n}\lvert\texttt{nums1[i]}-\texttt{nums2[i]}\rvert.
$$

**Inputs**

- `nums1`: An integer array of length $n$, where
  $1 \le n \le 10^5$ and every entry lies in $[0,10^5]$.
- `nums2`: An integer array with the same length and value bounds as `nums1`.
- `k1`: The operation allowance for `nums1`, with $0 \le k1 \le 10^9$.
- `k2`: The operation allowance for `nums2`, with $0 \le k2 \le 10^9$.

**Return value**

The minimum attainable sum of squared pairwise differences.

### Examples

#### Example 1

- **Input:** `nums1 = [1,2,3,4]`, `nums2 = [2,10,20,19]`, `k1 = 0`, `k2 = 0`
- **Output:** `579`
- **Explanation:** With no operations, the squared absolute differences are
  $1$, $64$, $289$, and $225$.

#### Example 2

- **Input:** `nums1 = [1,4,10,12]`, `nums2 = [5,8,6,9]`, `k1 = 1`, `k2 = 1`
- **Output:** `43`
- **Explanation:** The differences begin as `[4,4,4,3]`; reducing two of the
  values `4` to `3` leaves `[3,4,3,3]`.

#### Example 3

- **Input:** `nums1 = [1]`, `nums2 = [10]`, `k1 = 10`, `k2 = 10`
- **Output:** `0`
- **Explanation:** Nine of the available operations can eliminate the sole
  difference completely.
