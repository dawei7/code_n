# Count Pairs in Two Arrays

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/count-pairs-in-two-arrays/) |
| Frontend ID | 1885 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Two integer arrays, `nums1` and `nums2`, have the same length $N$. Choose two distinct positions in increasing index order, $(i,j)$ with $i<j$, and compare the sum of the two values selected from `nums1` with the sum at those same positions in `nums2`.

Count how many index pairs satisfy the strict inequality

$$
\texttt{nums1[i]}+\texttt{nums1[j]} >
\texttt{nums2[i]}+\texttt{nums2[j]}.
$$

Pairs whose two sums are equal do not count. Return the total over all possible index pairs.

### Function Contract

**Inputs**

- `nums1`: a length-$N$ array of positive integers.
- `nums2`: a length-$N$ array of positive integers corresponding position by position with `nums1`.
- $1 \le N \le 10^5$, and every array value lies between $1$ and $10^5$, inclusive.

**Return value**

- Return the number of pairs $(i,j)$ with $i<j$ whose `nums1` sum is strictly larger than the corresponding `nums2` sum.

### Examples

**Example 1**

- Input: `nums1 = [2,1,2,1], nums2 = [1,2,1,2]`
- Output: `1`

Only pair `(0,2)` satisfies the required inequality.

**Example 2**

- Input: `nums1 = [1,10,6,2], nums2 = [1,4,1,5]`
- Output: `5`

Every pair except `(0,3)` has a strictly positive combined difference.

**Example 3**

- Input: `nums1 = [5,1], nums2 = [3,3]`
- Output: `0`

The two sides are equal, so the strict comparison rejects the pair.
