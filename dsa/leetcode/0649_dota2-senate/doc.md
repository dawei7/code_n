# Dota2 Senate

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 649 |
| Difficulty | Medium |
| Topics | String, Greedy, Queue |
| Official Link | [LeetCode](https://leetcode.com/problems/dota2-senate/) |

## Problem Description
### Goal
The Dota2 senate contains members of the `Radiant` and `Dire` parties in the order represented by the characters of `senate`. Voting proceeds in repeated rounds, with every senator who still has rights acting in that established circular order.

On a turn, a senator may ban one opposing senator's rights for the current and all later rounds, or announce victory once every senator who still has rights belongs to the same party. Assume all senators make optimal choices. Return `"Radiant"` or `"Dire"` to name the party that eventually wins.

### Function Contract
**Inputs**

- `senate`: a nonempty string where `R` denotes a Radiant senator and `D` denotes a Dire senator in initial speaking order
- Senators make optimal choices; an active senator can ban one active opponent or declare victory when no opponent remains

**Return value**

- `"Radiant"` or `"Dire"`, naming the party that eventually retains voting rights

### Examples
**Example 1**

- Input: `senate = "RD"`
- Output: `"Radiant"`

**Example 2**

- Input: `senate = "RDD"`
- Output: `"Dire"`

**Example 3**

- Input: `senate = "DRD"`
- Output: `"Dire"`
