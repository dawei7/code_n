# Longest Non-decreasing Subarray From Two Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2771 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [2771. Longest Non-decreasing Subarray From Two Arrays](https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/) |

## Problem Description

### Goal

Two 0-indexed integer arrays `nums1` and `nums2` have the same length $n$. Construct a third array `nums3` by independently choosing, at every index $i$, either `nums1[i]` or `nums2[i]`. Exactly one of the two available values is placed at each position.

Choose all positions so that the longest non-decreasing subarray of `nums3` is as long as possible, then return that maximum length. The measured sequence must be a contiguous, non-empty subarray; it may begin and end at any indices, and adjacent selected values inside it must never decrease.

### Function Contract

**Inputs**

- `nums1`: The first integer list of length $n$.
- `nums2`: The second integer list, also of length $n$.

Both arrays satisfy $1 \le n \le 10^5$ and $1 \le \texttt{nums1}[i],\texttt{nums2}[i] \le 10^9$.

**Return value**

Return the greatest length of a non-decreasing contiguous subarray obtainable in any valid construction of `nums3`.

### Examples

#### Example 1

- **Input:** `nums1 = [2, 3, 1], nums2 = [1, 2, 1]`
- **Output:** `2`
- **Explanation:** Choosing `[2, 2, 1]` gives a non-decreasing prefix of length $2$.

#### Example 2

- **Input:** `nums1 = [1, 3, 2, 1], nums2 = [2, 2, 3, 4]`
- **Output:** `4`
- **Explanation:** The choices `[1, 2, 3, 4]` make the complete array non-decreasing.

#### Example 3

- **Input:** `nums1 = [1, 1], nums2 = [2, 2]`
- **Output:** `2`
- **Explanation:** Selecting both entries from either source produces a non-decreasing array of length $2$.
