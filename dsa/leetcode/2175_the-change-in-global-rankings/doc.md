# The Change in Global Rankings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2175 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/the-change-in-global-rankings/) |

## Problem Description

### Goal

`TeamPoints` stores each national team's identifier, unique country name, and
current global-ranking points. `PointsChange` contains exactly one signed
points adjustment for every team: a positive value adds points, a negative
value removes points, and zero leaves the total unchanged.

A ranking orders teams by points in descending order. When point totals tie,
the country name in lexicographical order breaks the tie. Apply every points
change, rank the teams again under the same rules, and report how far each team
moved. Define `rank_diff` as the old rank minus the new rank, so an improvement
is positive, a decline is negative, and an unchanged position is zero. Return
one row per team in any order.

### Function Contract

**Inputs**

`TeamPoints` contains:

- `team_id`: a unique team identifier.
- `name`: the unique country name represented by the team.
- `points`: the team's points before the update.

`PointsChange` contains:

- `team_id`: a unique identifier that also appears in `TeamPoints`.
- `points_change`: the signed adjustment applied to that team's points.

**Return value**

Return columns `team_id`, `name`, and `rank_diff` for every team, where
`rank_diff = old_rank - new_rank` under descending points and ascending-name
tie-breaking.

### Examples

**Example 1**

- Input: Senegal starts first, Croatia second, Algeria third, and New Zealand
  fourth; the adjustments make Algeria and Croatia tie at `1830`.
- Output: Senegal `0`, Croatia `-1`, Algeria `1`, and New Zealand `0`, because
  Algeria wins the updated tie lexicographically.

**Example 2**

- Input: every `points_change` is `0`.
- Output: every `rank_diff` is `0`.

**Example 3**

- Input: two updated point totals become equal.
- Output: their new relative positions follow ascending `name`, regardless of
  their original order.
