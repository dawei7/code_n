# Minimum Equal Sum of Two Arrays After Replacing Zeros

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2918 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/) |

## Problem Description

### Goal

You are given two integer arrays, `nums1` and `nums2`, whose entries are
non-negative. Replace every zero in both arrays with a strictly positive
integer. Nonzero entries cannot be changed.

Choose the replacements so that the two resulting array sums are equal, and
return the minimum common sum that can be obtained. If no assignment of
positive replacements can make the sums equal, return `-1`.

### Function Contract

**Inputs**

- `nums1`: The first non-empty array of non-negative integers.
- `nums2`: The second non-empty array of non-negative integers.

Let $n=\lvert\texttt{nums1}\rvert$ and
$m=\lvert\texttt{nums2}\rvert$. The constraints are
$1\le n,m\le 10^5$ and
$0\le\texttt{nums1[i]},\texttt{nums2[i]}\le 10^6$.

**Return value**

- The minimum attainable equal sum, or `-1` when equality is impossible.

### Examples

#### Example 1

- **Input:** `nums1 = [3, 2, 0, 1, 0], nums2 = [6, 5, 0]`
- **Output:** `12`
- **Explanation:** Replacing the first array's zeros with `2` and `4`, and
  the second array's zero with `1`, gives sums of 12. No smaller common sum
  is possible.

#### Example 2

- **Input:** `nums1 = [2, 0, 2, 0], nums2 = [1, 4]`
- **Output:** `-1`
- **Explanation:** The first array has minimum attainable sum 6, while the
  zero-free second array is fixed at 5 and cannot be increased.
