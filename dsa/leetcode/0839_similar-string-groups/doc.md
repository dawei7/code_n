# Similar String Groups

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 839 |
| Difficulty | Hard |
| Topics | Array, Hash Table, String, Depth-First Search, Breadth-First Search, Union-Find |
| Official Link | [LeetCode](https://leetcode.com/problems/similar-string-groups/) |

## Problem Description
### Goal
Two strings `X` and `Y` are similar when they are identical or when swapping letters at at most two distinct positions within `X` makes the strings equal. For example, `"tars"` is similar to `"rats"`, and `"rats"` is similar to `"arts"`, while `"star"` is not directly similar to any of those three.

Similarity links strings into connected groups. Thus `"tars"` and `"arts"` belong to the same group through `"rats"` even though they are not directly similar. Given `strs`, where every string has the same length and all strings are anagrams of one another, return the number of connected similarity groups.

### Function Contract
**Inputs**

- `strs`: a list of $g$ lowercase strings, with $1 \leq g \leq 300$.
- Every string has the same length $\ell$, where $1 \leq \ell \leq 300$.
- All strings in the list are anagrams of one another.

**Return value**

Return the number of connected components formed by direct-similarity links among the strings.

### Examples
**Example 1**

- Input: `strs = ["tars", "rats", "arts", "star"]`
- Output: `2`

The first three strings form one connected group, while `"star"` forms another.

**Example 2**

- Input: `strs = ["omv", "ovm"]`
- Output: `1`

**Example 3**

- Input: `strs = ["abcd", "badc"]`
- Output: `2`

The strings differ at four positions, so one swap cannot connect them.
