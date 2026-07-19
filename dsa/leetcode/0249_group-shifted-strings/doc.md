# Group Shifted Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 249 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/group-shifted-strings/) |

## Problem Description
### Goal
Two lowercase strings belong to the same shifting sequence when one can be transformed into the other by advancing every character by the same number of alphabet positions, wrapping cyclically from `z` back to `a`. A shift never changes a string's length or the relative differences between adjacent characters.

Given a list of nonempty strings, partition all entries into equivalence groups under this rule. Return every input string in exactly one group; group order and member order are unrestricted. Identical strings share a group, while equal-length strings with different cyclic difference patterns do not, even if their sets of letters look similar.

### Function Contract
**Inputs**

- `strings`: a list of non-empty lowercase strings

**Return value**

All equivalence groups; group order and member order may be arbitrary.

### Examples
**Example 1**

- Input: `strings = ["abc","bcd","acef","xyz","az","ba","a","z"]`
- Output: `[["abc","bcd","xyz"],["acef"],["az","ba"],["a","z"]]`

**Example 2**

- Input: `strings = ["a"]`
- Output: `[["a"]]`

**Example 3**

- Input: `strings = ["ab","za"]`
- Output: `[["ab","za"]]`
