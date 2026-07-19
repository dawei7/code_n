# Rank Teams by Votes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1366 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/rank-teams-by-votes/) |

## Problem Description

### Goal

Each string in `votes` is one ballot ranking the same set of teams from highest to lowest. Every team appears exactly once in every ballot, and uppercase letters identify the teams.

Rank the teams by comparing how many first-place votes they received. If two teams tie, compare their second-place counts, then third-place counts, and continue through every rank until they differ. If their complete count vectors are identical, the alphabetically smaller team comes first. Return all teams in final best-to-worst order.

### Function Contract

**Inputs**

- `votes`: $V$ equal-length ballot strings.
- Each ballot contains the same $T$ distinct uppercase team letters exactly once.

**Return value**

- One string containing all $T$ teams ordered by the positional vote rules and then alphabetical tie-breaking.

### Examples

**Example 1**

- Input: `votes = ["ABC","ACB","ABC","ACB","ACB"]`
- Output: `"ACB"`

**Example 2**

- Input: `votes = ["WXYZ","XYZW"]`
- Output: `"XWYZ"`

**Example 3**

- Input: `votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]`
- Output: `"ZMNAGUEDSJYLBOPHRQICWFXTVK"`
