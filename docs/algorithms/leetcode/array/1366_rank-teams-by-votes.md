# Rank Teams by Votes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1366 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Sorting, Counting |
| Official Link | [rank-teams-by-votes](https://leetcode.com/problems/rank-teams-by-votes/) |

## Problem Description & Examples
### Goal
Rank teams from a list of ballots. A team is better if it receives more votes in the earliest position where the two teams differ; alphabetical order breaks a complete tie.

### Function Contract
**Inputs**

- `votes`: a list of equal-length strings, each string ordering all teams from best to worst.

**Return value**

A string containing the teams from highest rank to lowest rank.

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

---

## Underlying Base Algorithm(s)
Rank-vector counting with custom sorting. For every team, count how many votes it received at each rank, then sort teams by descending count vector and ascending team letter.

---

## Complexity Analysis
- **Time Complexity**: `O(v * t + t log t * t)`, where `v` is the number of votes and `t` is the number of teams.
- **Space Complexity**: `O(t^2)` for rank counts.
