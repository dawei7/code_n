# Uncrossed Lines

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1035 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/uncrossed-lines/) |

## Problem Description

### Goal

Write the integers of `nums1` and `nums2`, in their given orders, on two separate horizontal lines.

You may connect `nums1[i]` to `nums2[j]` with a straight line only when `nums1[i] == nums2[j]`. No chosen connecting line may intersect another non-horizontal connecting line, even at an endpoint, so each array element can participate in at most one connection.

Return the maximum number of connecting lines that can be drawn under these rules.

### Function Contract

**Inputs**

- `nums1`: an integer array of length $M$, where $1 \le M \le 500$.
- `nums2`: an integer array of length $N$, where $1 \le N \le 500$.
- Every value in both arrays lies between $1$ and $2000$, inclusive.

**Return value**

- The largest number of equal-value pairs that can be connected without crossings or shared endpoints.

### Examples

**Example 1**

- Input: `nums1 = [1,4,2], nums2 = [1,2,4]`
- Output: `2`
- Explanation: Connecting all three equal values would force the lines for `4` and `2` to cross.

**Example 2**

- Input: `nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]`
- Output: `3`

**Example 3**

- Input: `nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]`
- Output: `2`
