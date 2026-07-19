# Check If a String Can Break Another String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1433 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/check-if-a-string-can-break-another-string/) |

## Problem Description

### Goal

Two strings of equal length contain lowercase English letters. A permutation `x` can break a permutation `y` when `x[i]` is lexicographically greater than or equal to `y[i]` at every index.

Determine whether the characters of `s1` and `s2` can be rearranged so that a permutation of `s1` breaks a permutation of `s2`, or a permutation of `s2` breaks a permutation of `s1`. The direction only needs to work one way, but it must remain consistent across every paired position.

### Function Contract

**Inputs**

- `s1` and `s2`: lowercase English strings of the same length $n$, where $1 \le n \le 10^5$.

**Return value**

- `true` if some permutation of either string can break a permutation of the other; otherwise `false`.

### Examples

**Example 1**

- Input: `s1 = "abc", s2 = "xya"`
- Output: `true`

**Example 2**

- Input: `s1 = "abe", s2 = "acd"`
- Output: `false`

**Example 3**

- Input: `s1 = "leetcode", s2 = "interview"`
- Output: `true`
