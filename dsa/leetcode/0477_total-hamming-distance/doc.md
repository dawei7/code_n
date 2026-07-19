# Total Hamming Distance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 477 |
| Difficulty | Medium |
| Topics | Array, Math, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/total-hamming-distance/) |

## Problem Description
### Goal
Given an array of nonnegative integers, consider every unordered pair of distinct indices $i < j$. The Hamming distance of their values is the number of binary bit positions where one value has `0` and the other has `1`.

Return the sum of these distances across all index pairs. Duplicate values at different positions still define a pair but contribute zero between themselves, while each differing bit contributes independently to every cross-group pair at that position. Leading zeroes common to all values add nothing. The function returns the aggregate total, not individual pair distances.

### Function Contract
**Inputs**

- `nums`: nonnegative integers

**Return value**

- The sum, over all index pairs $i < j$, of the bit positions where `nums[i]` and `nums[j]` differ

### Examples
**Example 1**

- Input: `nums = [4, 14, 2]`
- Output: `6`

**Example 2**

- Input: `nums = [4, 14, 4]`
- Output: `4`

**Example 3**

- Input: `nums = [0, 7]`
- Output: `3`
