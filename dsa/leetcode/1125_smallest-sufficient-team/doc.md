# Smallest Sufficient Team

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1125 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/smallest-sufficient-team/) |

## Problem Description

### Goal

A project has a list `req_skills` of required skills and a list `people`, where `people[i]` contains every required skill possessed by person `i`. A team is sufficient when, for each skill in `req_skills`, at least one selected person has that skill. Represent a team by the indices of its selected people; for example, `[0,1,3]` selects `people[0]`, `people[1]`, and `people[3]`.

Return any sufficient team having the smallest possible number of people. The indices may appear in any order, and more than one minimum team may be valid. Every person's listed skills belong to `req_skills`, skill names are unique within each relevant list, and a sufficient team is guaranteed to exist.

### Function Contract

**Inputs**

- `req_skills`: a list of $s$ distinct lowercase skill names, where $1 \le s \le 16$ and each name has length from $1$ through $16$.
- `people`: a list of $p$ people, where $1 \le p \le 60$; `people[i]` contains between $0$ and $16$ distinct names drawn from `req_skills`.

**Return value**

The indices of any smallest sufficient team, in any order.

### Examples

**Example 1**

- Input: `req_skills = ["java","nodejs","reactjs"]`, `people = [["java"],["nodejs"],["nodejs","reactjs"]]`
- Output: `[0,2]`

**Example 2**

- Input: `req_skills = ["algorithms","math","java","reactjs","csharp","aws"]`, `people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]`
- Output: `[1,2]`
