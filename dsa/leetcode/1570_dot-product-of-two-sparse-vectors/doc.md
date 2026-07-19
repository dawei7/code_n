# Dot Product of Two Sparse Vectors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1570 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Two Pointers, Design |
| Official Link | [LeetCode](https://leetcode.com/problems/dot-product-of-two-sparse-vectors/) |

## Problem Description
### Goal

Design a `SparseVector` from a dense integer array while retaining an efficient representation of its nonzero entries. Two vectors used together always have the same dimension.

The method `dotProduct(vec)` must return the sum of the products of values at matching indices. Most values may be zero, so the multiplication stage should take advantage of sparsity instead of examining every coordinate again.

### Function Contract
**Inputs**

- `nums1`: The dense values of the first vector of dimension $N$.
- `nums2`: The dense values of the second vector with the same dimension $N$.
- Every value is an integer from `0` through `100`. Let $K_1$ and $K_2$ be the numbers of nonzero entries in `nums1` and `nums2` respectively.

The native interface constructs `SparseVector(nums1)` and `SparseVector(nums2)`, then calls `first.dotProduct(second)`. The app-local adapter receives `nums1` and `nums2` directly and performs the same construction and operation.

**Return value**

Return

$$
\sum_{i=0}^{N-1} \texttt{nums1[i]}\,\texttt{nums2[i]}.
$$

### Examples
**Example 1**

- Input: `nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]`
- Output: `8`

**Example 2**

- Input: `nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]`
- Output: `0`

**Example 3**

- Input: `nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]`
- Output: `6`
