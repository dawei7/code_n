# Compare Version Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 165 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/compare-version-numbers/) |

## Problem Description
### Goal
Given two version numbers represented as strings of decimal revisions separated by dots, compare corresponding revisions from left to right. Interpret each revision as a nonnegative integer, so leading zeroes do not affect its value, and treat missing revisions beyond the end of a version as zero.

Return `-1` when `version1` is smaller, `1` when it is larger, and `0` when both represent the same revision sequence. Stop at the first unequal revision; trailing zero-valued revisions do not make a version larger. Comparison is numeric rather than lexicographic, so a revision such as `10` is greater than `2` despite its leading character.

### Function Contract
**Inputs**

- `version1`: first sequence of decimal revisions
- `version2`: second sequence of decimal revisions

**Return value**

`-1` when the first version is smaller, `1` when it is larger, and `0` when both represent the same revision sequence.

### Examples
**Example 1**

- Input: `version1 = "1.2", version2 = "1.10"`
- Output: `-1`

**Example 2**

- Input: `version1 = "1.01", version2 = "1.001"`
- Output: `0`

**Example 3**

- Input: `version1 = "1.0", version2 = "1.0.0.0"`
- Output: `0`
