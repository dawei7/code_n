# Maximize the Total Height of Unique Towers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3301 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/) |

## Problem Description

### Goal

You are given `maximumHeight`, where position $i$ supplies the greatest height allowed for tower $i$. Assign every tower a positive integer height no greater than its own limit. All assigned heights must be pairwise distinct.

Among all assignments satisfying those rules, return the largest possible sum of assigned heights. If the limits cannot support a positive distinct height for every tower, return `-1`. Towers may be considered in any order while constructing the assignment, but each chosen height must remain within the limit of its corresponding tower.

### Function Contract

**Inputs**

- `maximumHeight`: A list of positive upper bounds, one for each tower.

The list length is from 1 through $10^5$, and every upper bound is from 1 through $10^9$.

**Return value**

- The maximum possible sum of pairwise distinct positive tower heights, or `-1` when no valid assignment exists.

### Examples

#### Example 1

- **Input:** `maximumHeight = [2,3,4,3]`
- **Output:** `10`
- **Explanation:** Heights `[1,2,4,3]` respect their corresponding limits and are all distinct.

#### Example 2

- **Input:** `maximumHeight = [15,10]`
- **Output:** `25`
- **Explanation:** Both towers can take their full limits, 15 and 10.

#### Example 3

- **Input:** `maximumHeight = [2,2,1]`
- **Output:** `-1`
- **Explanation:** Three distinct positive heights cannot fit within these limits.
