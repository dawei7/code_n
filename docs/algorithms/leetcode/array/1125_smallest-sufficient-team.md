# Smallest Sufficient Team

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1125 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Bit Manipulation, Bitmask |
| Official Link | [smallest-sufficient-team](https://leetcode.com/problems/smallest-sufficient-team/) |

## Problem Description & Examples
### Goal
Choose the fewest people so that every required skill appears in at least one chosen person's skill list.

### Function Contract
**Inputs**

- `req_skills`: list of required skill names.
- `people`: `people[i]` is the list of skills person `i` has.

**Return value**

Indices of a minimum-size sufficient team. Any one minimum team is acceptable.

### Examples
**Example 1**

- Input: `req_skills = ["java","nodejs","reactjs"]`, `people = [["java"],["nodejs"],["nodejs","reactjs"]]`
- Output: `[0,2]`

**Example 2**

- Input: `req_skills = ["algorithms","math","java","reactjs","csharp","aws"]`, `people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]`
- Output: `[1,2]`

**Example 3**

- Input: `req_skills = ["a","b"]`, `people = [["a"],["b"],["a","b"]]`
- Output: `[2]`

---

## Underlying Base Algorithm(s)
Bitmask dynamic programming.

---

## Complexity Analysis
- **Time Complexity**: `O(p * 2^s)` where `p` is the number of people and `s` is the number of required skills.
- **Space Complexity**: `O(2^s * p)` if teams are stored directly.
