# Minimum Operations to Transform String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3675 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-transform-string/) |

## Problem Description
### Goal

Given a string `s` of lowercase English letters, an operation chooses one letter currently appearing in the string and changes every occurrence of that letter to its alphabetic successor. The alphabet is circular, so changing `z` produces `a`.

Apply the operation any number of times and determine the minimum count needed to turn every character into `a`. Occurrences of the chosen letter always move together, and they may merge with occurrences already holding the successor letter.

### Function Contract

**Inputs**

- `s`: a non-empty lowercase English string of length $n$, where $1\le n\le5\cdot10^5$.

**Return value**

Return the minimum number of global letter-successor operations required to make `s` consist only of `a` characters.

### Examples

**Example 1**

- Input: `s = "yz"`
- Output: `2`

Changing `y` merges both positions at `z`; changing `z` once more wraps both to `a`.

**Example 2**

- Input: `s = "a"`
- Output: `0`

The target condition already holds.

**Example 3**

- Input: `s = "abz"`
- Output: `25`

The `b` group must advance through the alphabet to `a`; it absorbs the `z` group along the way, while the original `a` remains unchanged.
