# Minimum Index Sum of Common Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3682 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-index-sum-of-common-elements/) |

## Problem Description

### Goal

Given two integer arrays `nums1` and `nums2` of the same length, call an index pair `(i, j)` good when `nums1[i]` equals `nums2[j]`.

Among every good pair, find the minimum possible index sum $i+j$. Values may occur more than once in either array, so all matching occurrences are conceptually eligible. Return `-1` if the arrays have no value in common.

### Function Contract

**Inputs**

- `nums1`: an integer list of length $n$.
- `nums2`: another integer list of the same length $n$.

The common length satisfies $1\le n\le10^5$, and every element lies between $-10^5$ and $10^5$.

**Return value**

Return the smallest $i+j$ over all pairs with `nums1[i] == nums2[j]`, or `-1` when no good pair exists.

### Examples

#### Example 1

- **Input:** `nums1 = [3, 2, 1], nums2 = [1, 3, 1]`
- **Output:** `1`

Value 3 occurs at indices 0 and 1, producing the minimum sum 1.

#### Example 2

- **Input:** `nums1 = [5, 1, 2], nums2 = [2, 1, 3]`
- **Output:** `2`

Both common values 1 and 2 yield an index sum of 2.

#### Example 3

- **Input:** `nums1 = [6, 4], nums2 = [7, 8]`
- **Output:** `-1`

No value appears in both arrays.
