# Interleaving String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 97 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/interleaving-string/) |

## Problem Description
### Goal
You are given source strings `s1` and `s2` and a proposed result `s3`. An interleaving divides each source into a sequence of nonempty substrings, with the two sequence lengths differing by at most one, then alternates whole substrings from the two sources starting with either one.

Determine whether some such alternating sequence produces `s3` exactly. The substrings from each source must remain in their original left-to-right order and together consume every character of both inputs. Empty sources follow the same order-preservation rule, and equal characters may allow several valid choices of substring boundaries.

### Function Contract
**Inputs**

- `s1`: the first source string
- `s2`: the second source string
- `s3`: the proposed interleaving

**Return value**

`True` exactly when `s3` is a valid interleaving of `s1` and `s2`.

### Examples
**Example 1**

- Input: `s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"`
- Output: `True`

**Example 2**

- Input: `s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"`
- Output: `False`

**Example 3**

- Input: `s1 = "", s2 = "", s3 = ""`
- Output: `True`
