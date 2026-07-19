# Check if All Characters Have Equal Number of Occurrences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1941 |
| Difficulty | Easy |
| Topics | Hash Table, String, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/) |

## Problem Description
### Goal
You are given a string `s` containing only lowercase English letters. The
number of occurrences of a character is the number of positions in `s` that
contain that character. Characters that do not appear in the string are not
part of the comparison.

Determine whether all distinct characters present in `s` occur equally often.
Return `true` when their positive occurrence counts are identical, and return
`false` as soon as at least two present characters have different counts.

### Function Contract
**Inputs**

- `s`: a string of lowercase English letters with length $N$, where
  $1 \le N \le 1000$.

**Return value**

- `true` if every distinct character appearing in `s` has the same positive
  occurrence count; otherwise, `false`.

### Examples
**Example 1**

- Input: `s = "abacbc"`
- Output: `true`
- Explanation: `a`, `b`, and `c` each occur twice.

**Example 2**

- Input: `s = "aaabb"`
- Output: `false`
- Explanation: `a` occurs three times while `b` occurs twice.

**Example 3**

- Input: `s = "abcd"`
- Output: `true`
- Explanation: Every present character occurs once.
