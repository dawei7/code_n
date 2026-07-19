# Widest Pair of Indices With Equal Range Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1983 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/widest-pair-of-indices-with-equal-range-sum/) |

## Problem Description
### Goal
You are given two 0-indexed binary arrays `nums1` and `nums2` of the same
length. Choose indices `i` and `j` with $i \le j$ so that the sum of
`nums1[i:j + 1]` equals the sum over the identical inclusive range in `nums2`.
Only corresponding ranges with the same endpoints may be compared.

The width of such a pair is $j - i + 1$. Return the greatest achievable width
over all qualifying index pairs. If no nonempty range has equal sums in the two
arrays, return `0`.

### Function Contract
**Inputs**

- `nums1`: a binary list of length $N$.
- `nums2`: another binary list of the same length $N$, where
  $1 \le N \le 10^5$.

**Return value**

- The maximum length of a nonempty corresponding range whose sums in `nums1`
  and `nums2` are equal, or `0` if no such range exists.

### Examples
**Example 1**

- Input: `nums1 = [1, 1, 0, 1], nums2 = [0, 1, 1, 0]`
- Output: `3`

The range from index `1` through index `3` sums to `2` in both arrays.

**Example 2**

- Input: `nums1 = [0, 1], nums2 = [1, 1]`
- Output: `1`

The values at index `1` match, so that single-position range qualifies.

**Example 3**

- Input: `nums1 = [0], nums2 = [1]`
- Output: `0`
