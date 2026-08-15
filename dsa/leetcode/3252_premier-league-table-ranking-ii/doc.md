# Premier League Table Ranking II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3252 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/premier-league-table-ranking-ii/) |

## Problem Description

### Goal

The \`TeamStats\` table stores one row per Premier League team, identified by the unique column \`team_id\`. Each row also contains the team's name and its numbers of matches, wins, draws, and losses.

Produce a league table with \`team_name\`, \`points\`, \`position\`, and \`tier\`. Award three points per win, one per draw, and none per loss. Rank teams by descending points using competition positions, so equal totals share a position and later positions may have gaps.

Split positions into three point-based tiers: Tier 1 covers the top 33% of teams, Tier 2 the middle 33%, and Tier 3 the bottom 34%. Round each boundary upward; when a tied position reaches across a boundary, keep every team at that position in the higher tier. Return rows by descending points and then ascending \`team_name\`.

### Function Contract

**Inputs**

- \`TeamStats\`: A table with unique integer \`team_id\`, text \`team_name\`, and integer columns \`matches_played\`, \`wins\`, \`draws\`, and \`losses\`.

Let $t$ be the number of teams.

**Return value**

- A table with columns \`team_name\`, \`points\`, \`position\`, and \`tier\`, ordered by \`points\` descending and \`team_name\` ascending.
- \`points\` equals \`3 * wins + draws\`.
- \`position\` uses competition ranking by points.
- \`tier\` is the string \`Tier 1\`, \`Tier 2\`, or \`Tier 3\`.

### Examples

#### Example 1

- **Input:** Ten teams whose point totals are \`56, 55, 43, 41, 27, 24, 12, 12, 11, 9\`.
- **Output:** Positions \`1, 2, 3, 4, 5, 6, 7, 7, 9, 10\`; positions through 4 are Tier 1, positions through 7 are Tier 2, and the remaining positions are Tier 3.

#### Example 2

- **Input:** Three teams with 9, 6, and 3 points.
- **Output:** They occupy positions 1, 2, and 3 in Tier 1, Tier 2, and Tier 3 respectively.

#### Example 3

- **Input:** Four teams tied on 3 points.
- **Output:** Every team has position 1 and belongs to Tier 1; their names determine row order.
