# Check if Strings Can be Made Equal With Operations II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2840 |
| Difficulty | Medium |
| Topics | Hash Table, String, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/) |

## Problem Description

### Goal

Two lowercase English strings `s1` and `s2` have the same length $n$. On either string, an operation may choose indices $i<j$ whose difference $j-i$ is even and swap the characters at those positions. Any number of operations, including zero, may be performed on either string.

Determine whether the strings can be made equal. An even index difference means the two chosen indices always have the same parity, so operations can rearrange characters among even positions or among odd positions but can never transfer a character from one parity group to the other.

### Function Contract

**Inputs**

- `s1`: A lowercase English string of length $n$, where $1 \le n \le 10^5$.
- `s2`: A lowercase English string with the same length $n$ as `s1`.

**Return value**

Return `true` if the allowed swaps can make `s1` and `s2` equal; otherwise return `false`.

### Examples

#### Example 1

- **Input:** `s1 = "abcdba", s2 = "cabdab"`
- **Output:** `true`
- **Explanation:** Characters can be rearranged independently within the even and odd index groups to obtain `s2`.

#### Example 2

- **Input:** `s1 = "abe", s2 = "bea"`
- **Output:** `false`
- **Explanation:** Matching the target would require at least one character to move between index parities.
