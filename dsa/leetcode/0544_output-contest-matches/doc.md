# Output Contest Matches

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 544 |
| Difficulty | Medium |
| Topics | String, Recursion, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/output-contest-matches/) |

## Problem Description
### Goal
Given `n` teams ranked from `1` through `n`, where `n` is a power of two and a smaller number is stronger, construct the contest pairing that prevents the strongest teams from meeting until the latest possible rounds. In each round, pair the strongest remaining team or group with the weakest, the second strongest with the second weakest, and so on.

Return the fully parenthesized match string. A first-round match is written `(a,b)`, and later rounds recursively place prior match strings inside the same comma-separated form. Include every team exactly once, preserve the prescribed strongest-versus-weakest pairings, and add no spaces or redundant outer text.

### Function Contract
**Inputs**

- `n`: the number of teams, guaranteed to be a power of two

**Return value**

- A string representing the complete bracket, with each match written as `(left,right)`

### Examples
**Example 1**

- Input: `n = 2`
- Output: `"(1,2)"`

**Example 2**

- Input: `n = 4`
- Output: `"((1,4),(2,3))"`

**Example 3**

- Input: `n = 8`
- Output: `"(((1,8),(4,5)),((2,7),(3,6)))"`
