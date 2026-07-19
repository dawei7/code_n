# Number of Ways to Split a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1573 |
| Difficulty | Medium |
| Topics | Math, String |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-to-split-a-string/) |

## Problem Description
### Goal

Given a binary string `s`, place two cuts between characters so that the string becomes three nonempty contiguous substrings. Different pairs of cut positions count as different splits.

The character order remains unchanged, the first cut must precede the second, and neither cut may leave an empty part. Zeros may occur anywhere in the three substrings and do not need to be distributed equally.

Count the splits for which all three substrings contain the same number of `1` characters. Two splits are distinct when either cut occupies a different gap, even if their one-counts are identical. Return the count modulo $1{,}000{,}000{,}007$.

### Function Contract
**Inputs**

- `s`: A binary string of length $N$, where $3 \le N \le 10^5$.

**Return value**

Return the number of pairs of cut positions that create three nonempty substrings with equal one-counts, modulo $1{,}000{,}000{,}007$.

### Examples
**Example 1**

- Input: `s = "10101"`
- Output: `4`

**Example 2**

- Input: `s = "1001"`
- Output: `0`

**Example 3**

- Input: `s = "0000"`
- Output: `3`
