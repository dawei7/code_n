# Check if Strings Can be Made Equal With Operations I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2839 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/) |

## Problem Description
### Goal

Two strings `s1` and `s2` each contain exactly four lowercase English letters. On either string, an operation chooses indices $i$ and $j$ whose difference is exactly two and swaps the characters at those positions. An operation may be performed any number of times, including zero times.

Determine whether the allowed swaps can make the two strings equal. Because the only possible index pairs are $(0,2)$ and $(1,3)$, a character always stays among positions having the same index parity.

### Function Contract
**Inputs**

- `s1`: A string of exactly four lowercase English letters.
- `s2`: A string of exactly four lowercase English letters.

**Return value**

Return `true` if some sequence of the permitted distance-two swaps can transform the strings into the same value; otherwise return `false`.

### Examples
**Example 1**

- Input: `s1 = "abcd", s2 = "cdab"`
- Output: `true`
- Explanation: Swap positions `0` and `2`, then positions `1` and `3`, in `s1` to obtain `s2`.

**Example 2**

- Input: `s1 = "abcd", s2 = "dacb"`
- Output: `false`
- Explanation: The target places characters into opposite-parity positions, which no allowed swap can do.
