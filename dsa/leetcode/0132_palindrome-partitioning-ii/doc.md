# Palindrome Partitioning II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 132 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/palindrome-partitioning-ii/) |

## Problem Description
### Goal
Given a nonempty string, insert cuts between selected adjacent characters so that every resulting contiguous substring is a palindrome. Each character must belong to exactly one piece, the pieces retain their original order, and no rearrangement is permitted.

Return the minimum number of cuts needed for any valid palindrome partition. The answer counts boundaries rather than substrings, so a string that is already a palindrome requires `0` cuts, while separating all `n` characters would use $n - 1$. Only the best partition matters; the function does not return the pieces or enumerate alternative minimum-cut divisions.

### Function Contract
**Inputs**

- `s`: a nonempty lowercase string

**Return value**

The minimum number of boundaries inserted so every resulting substring is a palindrome.

### Examples
**Example 1**

- Input: `s = "aab"`
- Output: `1`

**Example 2**

- Input: `s = "a"`
- Output: `0`

**Example 3**

- Input: `s = "ab"`
- Output: `1`
