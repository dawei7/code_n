# Count Good Triplets in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2179 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-good-triplets-in-an-array/) |

## Problem Description

### Goal

Two arrays `nums1` and `nums2` each contain every integer from $0$ through
$n-1$ exactly once, but potentially in different orders. A triplet is formed
from three distinct values rather than from three shared array indices.

A triplet is good when those three values occur from left to right in the same
order in both permutations. Equivalently, there must be indices
$0\le i<j<k<n$ in `nums1` whose values appear at strictly increasing positions
in `nums2`. Count every such ordered choice of three values.

### Function Contract

**Inputs**

- `nums1`: a permutation of the integers in $[0,n-1]$.
- `nums2`: another permutation of the same integers.

Both arrays have the same length $n$, where $3\le n\le10^5$.

**Return value**

Return the number of triplets whose relative order is identical in the two
permutations.

### Examples

#### Example 1

- **Input:** `nums1 = [2,0,1,3]`, `nums2 = [0,1,2,3]`
- **Output:** `1`
- **Explanation:** the values `(0,1,3)` are the only three that occur in the same
  relative order.

#### Example 2

- **Input:** `nums1 = [4,0,1,3,2]`, `nums2 = [4,1,0,2,3]`
- **Output:** `4`

#### Example 3

- **Input:** `nums1 = [0,1,2]`, `nums2 = [2,1,0]`
- **Output:** `0`
