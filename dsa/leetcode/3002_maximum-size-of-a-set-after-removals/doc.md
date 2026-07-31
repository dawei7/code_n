# Maximum Size of a Set After Removals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3002 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-size-of-a-set-after-removals/) |

## Problem Description
### Goal
You are given two integer arrays `nums1` and `nums2`, both having the same
even length $N$. Remove exactly $N/2$ elements from each array. Insert every
remaining value from both arrays into one set.

Choose the removals to maximize the number of distinct values in that final
set, and return its maximum possible size.

The removals are chosen separately in the two arrays, but exactly half of each
array must be discarded. Repeated retained values contribute only once because
the final collection is a set, including values appearing in both arrays.

### Function Contract
**Inputs**

- `nums1`: the first length-$N$ integer array
- `nums2`: the second length-$N$ integer array

The common length is even and satisfies $1\le N\le2\cdot10^4$. Every array
value lies between 1 and $10^9$ inclusive.

**Return value**

Return the greatest possible number of distinct retained values after exactly
half of each array is removed.

### Examples
**Example 1**

- Input: `nums1 = [1,2,1,2], nums2 = [1,1,1,1]`
- Output: `2`

One retained array can contribute 2 and the other can contribute 1.

**Example 2**

- Input: `nums1 = [1,2,3,4,5,6], nums2 = [2,3,2,3,2,3]`
- Output: `5`

The first array can retain three values unique to the result while the second
adds 2 and 3.

**Example 3**

- Input: `nums1 = [1,1,2,2,3,3], nums2 = [4,4,5,5,6,6]`
- Output: `6`

Each array contributes three distinct values, and the two groups are disjoint.
