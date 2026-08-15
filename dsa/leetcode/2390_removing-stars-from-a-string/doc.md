# Removing Stars From a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2390 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/removing-stars-from-a-string/) |

## Problem Description

### Goal

Given a string `s` containing lowercase English letters and stars, repeatedly choose a star, remove that star, and also remove the closest non-star character to its left. Continue until no stars remain, then return the resulting string.

The input is guaranteed to make every required removal possible: whenever a star must be handled, an unmatched letter exists to its left. Although stars could be selected in different orders, the final string is guaranteed to be unique.

### Function Contract

**Inputs**

- `s`: A string of length $n$, where $1 \le n \le 10^5$, containing lowercase letters and `'*'`.

**Return value**

- Return the letters left after every star and its closest unmatched letter to the left have been removed.

**Removal semantics**

- Each star deletes exactly one preceding letter and itself.
- A deleted letter cannot be used by a later star.
- The result may be empty.

### Examples

#### Example 1

- **Input:** `s = "leet**cod*e"`
- **Output:** `"lecoe"`

#### Example 2

- **Input:** `s = "erase*****"`
- **Output:** `""`
