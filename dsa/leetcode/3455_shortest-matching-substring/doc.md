# Shortest Matching Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3455 |
| Difficulty | Hard |
| Topics | Two Pointers, String, Binary Search, String Matching |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-matching-substring/) |

## Problem Description
### Goal
The pattern `p` contains lowercase English letters and exactly two `*` characters. Each `*` may represent any sequence of characters, including an empty sequence. All ordinary letters must match literally and in their original order.

Find the minimum length among all contiguous substrings of `s` that the complete pattern can match. Return `-1` when no substring works. The empty substring is eligible, so a pattern whose two stars can both match empty sequences and which has no literal letters has answer $0$.

### Function Contract
**Inputs**

- `s`: A lowercase English string of length $n$ in which matching substrings are sought.
- `p`: A pattern of length $m$ containing lowercase English letters and exactly two `*` characters.

The constraints are $1 \le n \le 10^5$ and $2 \le m \le 10^5$.

**Return value**

Return the length of the shortest substring of `s` matched by all of `p`, or `-1` if none exists.

### Examples
**Example 1**

- Input: `s = "abaacbaecebce", p = "ba*c*ce"`
- Output: `8`

The shortest match is `baecebce`: its three literal blocks are `ba`, `c`, and `ce`.

**Example 2**

- Input: `s = "baccbaadbc", p = "cc*baa*adb"`
- Output: `-1`

No substring contains the required literal blocks in a compatible order.

**Example 3**

- Input: `s = "a", p = "**"`
- Output: `0`

Both stars may match empty sequences, so the empty substring is optimal.

**Example 4**

- Input: `s = "madlogic", p = "*adlogi*"`
- Output: `6`
