# String Compression II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1531 |
| Difficulty | Hard |
| Topics | String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/string-compression-ii/) |

## Problem Description
### Goal

Run-length encoding replaces every consecutive run of at least two equal characters by the character followed by its decimal run length. A one-character run is written as the character alone, without a trailing `1`; for example, `"aabccc"` becomes `"a2bc3"`.

Given a lowercase string `s`, delete at most `k` of its characters so that the run-length encoding of the remaining subsequence is as short as possible. Deletions close the gaps between retained characters, so formerly separate runs may merge. Return the minimum attainable encoded length.

### Function Contract
**Inputs**

- `s`: A lowercase English string of length $n$, where $1 \leq n \leq 100$.
- `k`: The maximum number of deletions, where $0 \leq k \leq n$.

**Return value**

Return the minimum length of the run-length encoded string after deleting at most `k` characters from `s`.

### Examples
**Example 1**

- Input: `s = "aaabcccd", k = 2`
- Output: `4`
- Explanation: Deleting `b` and `d` leaves `"aaaccc"`, encoded as `"a3c3"`.

**Example 2**

- Input: `s = "aabbaa", k = 2`
- Output: `2`
- Explanation: Deleting both `b` characters merges the `a` runs into `"a4"`.

**Example 3**

- Input: `s = "aaaaaaaaaaa", k = 0`
- Output: `3`
- Explanation: The unchanged string is encoded as `"a11"`.
