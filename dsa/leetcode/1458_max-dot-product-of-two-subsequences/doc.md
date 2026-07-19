# Max Dot Product of Two Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1458 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/max-dot-product-of-two-subsequences/) |

## Problem Description
### Goal

You are given two integer arrays, `nums1` and `nums2`. Choose a non-empty
subsequence from each array so that the two chosen subsequences have the same
length. A subsequence may delete any number of elements while preserving the
relative order of those that remain; selected positions do not need to be
contiguous.

If the selected subsequences are
$[x_1,x_2,\ldots,x_t]$ and $[y_1,y_2,\ldots,y_t]$, their dot product is

$$
\sum_{r=1}^{t} x_r y_r.
$$

Return the maximum dot product obtainable under these rules. At least one pair
must be selected, so returning zero by choosing two empty subsequences is not
allowed. This matters when every possible paired product is negative.

### Function Contract
**Inputs**

- `nums1`: an integer array of length $m$, where $1 \le m \le 500$.
- `nums2`: an integer array of length $n$, where $1 \le n \le 500$.
- Every value in either array lies in $[-1000,1000]$.

**Return value**

Return the greatest integer dot product of two non-empty, equal-length
subsequences, one drawn from each input while retaining each array's original
order.

### Examples
**Example 1**

- Input: `nums1 = [2,1,-2,5], nums2 = [3,0,-6]`
- Output: `18`
- Explanation: Pair subsequences `[2,-2]` and `[3,-6]`, producing
  $2\cdot3+(-2)\cdot(-6)=18$.

**Example 2**

- Input: `nums1 = [3,-2], nums2 = [2,-6,7]`
- Output: `21`
- Explanation: The one-element subsequences `[3]` and `[7]` produce the
  maximum.

**Example 3**

- Input: `nums1 = [-1,-1], nums2 = [1,1]`
- Output: `-1`
- Explanation: Every pair is negative, but the subsequences must be non-empty.
