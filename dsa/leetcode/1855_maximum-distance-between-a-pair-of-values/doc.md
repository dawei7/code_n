# Maximum Distance Between a Pair of Values

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/) |
| Frontend ID | 1855 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Two integer arrays `nums1` and `nums2` are each sorted in non-increasing order. Choose an index `i` from the first array and an index `j` from the second array. The pair is valid only when $i\le j$ and `nums1[i] <= nums2[j]`.

The distance of a valid pair is $j-i$. Return the largest distance over all valid pairs. A zero-distance pair may be the best available choice, and the answer is also zero when no pair with positive distance satisfies both the index and value conditions.

### Function Contract

**Inputs**

- `nums1`: a non-increasing list of $n$ integers.
- `nums2`: a non-increasing list of $m$ integers.
- $1\le n,m\le10^5$.
- Every value lies between 1 and $10^5$, inclusive.

**Return value**

- Return $\max(j-i)$ over indices satisfying $0\le i<n$, $0\le j<m$, $i\le j$, and $\texttt{nums1[i]}\le\texttt{nums2[j]}$.
- Return 0 when no positive distance is valid.

### Examples

**Example 1**

- Input: `nums1 = [55, 30, 5, 4, 2]`, `nums2 = [100, 20, 10, 10, 5]`
- Output: `2`

Indices `(2, 4)` form a valid pair because $5\le5$.

**Example 2**

- Input: `nums1 = [2, 2, 2]`, `nums2 = [10, 10, 1]`
- Output: `1`

**Example 3**

- Input: `nums1 = [30, 29, 19, 5]`, `nums2 = [25, 25, 25, 25, 25]`
- Output: `2`
