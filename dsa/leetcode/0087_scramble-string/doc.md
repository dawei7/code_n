# Scramble String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 87 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/scramble-string/) |

## Problem Description
### Goal
Define a recursive scramble operation on a string. A one-character string stays unchanged; a longer string may be split at any internal boundary into two nonempty substrings, each substring may be scrambled recursively, and the two results may either retain their order or swap places.

Given equal-length strings `s1` and `s2`, determine whether some sequence of these recursive choices transforms `s1` into `s2`. Characters are neither added nor removed, but matching character counts alone do not guarantee that the required split structure exists.

### Function Contract
**Inputs**

- `s1`: the original lowercase string
- `s2`: a lowercase string of the same length

**Return value**

`True` when `s2` is a recursive scramble of `s1`, otherwise `False`.

### Examples
**Example 1**

- Input: `s1 = "great", s2 = "rgeat"`
- Output: `True`

**Example 2**

- Input: `s1 = "abcde", s2 = "caebd"`
- Output: `False`

**Example 3**

- Input: `s1 = "a", s2 = "a"`
- Output: `True`
