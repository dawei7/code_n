# Minimum Total Cost to Make Arrays Unequal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2499 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/) |

## Problem Description

### Goal

Two 0-indexed integer arrays `nums1` and `nums2` have the same length `n`. An operation chooses any two indices `i` and `j`, swaps their values in `nums1`, and costs `i + j`. The second array never changes.

Perform any number of these swaps so that `nums1[i] != nums2[i]` at every index. The total cost is the sum of all operation costs, so an index contributes its index each time it participates in a swap.

Return the minimum total cost that can achieve the required inequality at every position. If no rearrangement of `nums1` can avoid all corresponding values in `nums2`, return `-1`.

### Function Contract

**Inputs**

- `nums1`: The array whose values may be swapped.
- `nums2`: The fixed comparison array, with the same length as `nums1`.

Both arrays have length $n$, where $1 \leq n \leq 10^5$, and every element lies from $1$ through $n$.

**Return value**

Return the minimum total index cost required to make `nums1[i] != nums2[i]` for all indices, or `-1` when this is impossible.

### Examples

**Example 1**

- Input: `nums1 = [1, 2, 3, 4, 5]`, `nums2 = [1, 2, 3, 4, 5]`
- Output: `10`
- Explanation: Every index initially conflicts, and a feasible rearrangement can involve them with total index contribution `0 + 1 + 2 + 3 + 4 = 10`.

**Example 2**

- Input: `nums1 = [2, 2, 2, 1, 3]`, `nums2 = [1, 2, 2, 3, 3]`
- Output: `10`
- Explanation: The conflicting indices require safe additional positions so the repeated values can be reassigned without creating new equalities.

**Example 3**

- Input: `nums1 = [1, 2, 2]`, `nums2 = [1, 2, 2]`
- Output: `-1`
- Explanation: Value `2` dominates the required positions, and no safe additional index exists to receive enough copies.
