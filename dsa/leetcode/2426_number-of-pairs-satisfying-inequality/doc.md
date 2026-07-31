# Number of Pairs Satisfying Inequality

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2426 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Number of Pairs Satisfying Inequality](https://leetcode.com/problems/number-of-pairs-satisfying-inequality/) |

## Problem Description

### Goal

You are given two 0-indexed integer arrays `nums1` and `nums2`, both with the same length $n$, together with an integer `diff`. Consider ordered index choices in which the first index appears strictly before the second.

Count the pairs $(i,j)$ satisfying $0 \le i < j \le n-1$ for which `nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff`. Values and `diff` may be negative, and equality satisfies the inequality.

### Function Contract

**Inputs**

- `nums1`: A list of $n$ integers.
- `nums2`: A list of $n$ integers aligned by index with `nums1`.
- `diff`: The signed tolerance added to the right side of the inequality.

The constraints are $2 \le n \le 10^5$, $-10^4 \le \texttt{nums1[i]},\texttt{nums2[i]} \le 10^4$, and $-10^4 \le \texttt{diff} \le 10^4$.

**Return value**

- The number of qualifying pairs $(i,j)$ with $i<j$.

### Examples

**Example 1**

- Input: `nums1 = [3,2,5], nums2 = [2,2,1], diff = 1`
- Output: `3`

All three possible index pairs satisfy the inequality.

**Example 2**

- Input: `nums1 = [3,-1], nums2 = [-2,2], diff = -1`
- Output: `0`

The only possible pair fails after the negative tolerance is applied.

**Example 3**

- Input: `nums1 = [1,2,3], nums2 = [0,0,0], diff = 0`
- Output: `3`

The transformed differences are increasing, so every earlier value is at most every later value.
