# Generate Schedule

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3680 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/generate-schedule/) |

## Problem Description

### Goal

Create a match schedule for `n` teams numbered from 0 through `n - 1`. Every ordered pair of distinct teams must appear exactly once: each pair of teams plays twice overall, with each team serving as the home team once.

The schedule contains exactly one match on each consecutive day. Two neighboring days may not share a team, so neither participant from one match may play again the next day. Any schedule satisfying all conditions is acceptable; return an empty list when no such arrangement exists.

### Function Contract

**Inputs**

- `n`: the number of teams, satisfying $2\le n\le50$.

**Return value**

Return a list of $n(n-1)$ two-element matches when a schedule exists. In each match, the first identifier is the home team and the second is the away team. Return `[]` if the conditions are impossible.

### Examples

#### Example 1

- **Input:** `n = 3`
- **Output:** `[]`

Every pair of matches among three teams shares a participant, so consecutive-day play cannot be avoided.

#### Example 2

- **Input:** `n = 5`
- **Output:** any valid list of 20 directed matches

All 20 home-away fixtures can be ordered so neighboring matches use four distinct teams.

#### Example 3

- **Input:** `n = 4`
- **Output:** `[]`

Each two-team matchup has only its complementary pair as a disjoint neighbor, splitting the matchup graph into components that cannot cover the full schedule.
