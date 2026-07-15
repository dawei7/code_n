# Tournament Winners

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1194 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/tournament-winners/) |

## Problem Description

### Goal

The `Players` table assigns every uniquely identified player to a tournament group. The `Matches` table records two players and their respective point totals for each match; both participants in a match always belong to the same group.

Within each group, add all points scored by each player across every match. The group winner is the player with the greatest total score. When several players share that maximum, the player with the smallest `player_id` wins. Return the winning player for every group in any order.

### Function Contract

**Input tables**

- `Players(player_id, group_id)`: `player_id` is the primary key, and each row assigns that player to one group.
- `Matches(match_id, first_player, second_player, first_score, second_score)`: `match_id` is the primary key; the two player columns identify same-group opponents, and the score columns give the points they earned in that match.
- Let $p$ be the number of players, $m$ the number of matches, and $g$ the number of groups.

**Return value**

- One row per group with columns `group_id` and `player_id`, identifying the maximum-total scorer and using the smallest `player_id` to break a tie.

### Examples

**Example 1**

`Players`

| player_id | group_id |
|---:|---:|
| 15 | 1 |
| 25 | 1 |
| 30 | 1 |
| 45 | 1 |
| 10 | 2 |
| 35 | 2 |
| 50 | 2 |
| 20 | 3 |
| 40 | 3 |

`Matches`

| match_id | first_player | second_player | first_score | second_score |
|---:|---:|---:|---:|---:|
| 1 | 15 | 45 | 3 | 0 |
| 2 | 30 | 25 | 1 | 2 |
| 3 | 30 | 15 | 2 | 0 |
| 4 | 40 | 20 | 5 | 2 |
| 5 | 35 | 50 | 1 | 1 |

Output:

| group_id | player_id |
|---:|---:|
| 1 | 15 |
| 2 | 35 |
| 3 | 40 |

**Example 2**

If two players in one group finish with equal total scores, the smaller `player_id` is returned.

**Example 3**

Scores earned as `first_player` and as `second_player` both contribute to the same player's total.

### Required Complexity

- **Time:** $O(p+m)$
- **Space:** $O(p+m)$

<details>
<summary>Approach</summary>

#### General

**Normalize both match roles.** Use `UNION ALL` to emit one `(player_id, score)` row for `first_player` and one for `second_player` from every match. Keeping both branches avoids role-specific logic in later aggregation and preserves duplicate score rows from different matches.

**Build complete player totals.** Left join `Players` to the normalized score rows, group by the player's group and ID, and sum the scores. `COALESCE` gives zero to a player with no recorded score rows. This step also attaches `group_id` once, after both match roles have been unified.

**Apply both winner rules explicitly.** Compute the maximum total score per group, join those maxima back to player totals, and retain only tied leaders. A final `MIN(player_id)` selects the required smallest identifier among them. This separates score maximization from tie-breaking and yields exactly one row per group.

#### Complexity detail

The normalized stream contains $2m$ rows. With hash joins and aggregation, producing player totals, group maxima, and tie winners takes $O(p+m)$ logical time. The normalized score stream and per-player aggregation state occupy $O(p+m)$ space; the group-level state is $O(g)$ and is bounded by $O(p)$.

#### Alternatives and edge cases

- **Correlated score lookup per player:** Rescanning `Matches` for each player is correct but can take $O(pm)$ time.
- **Window ranking:** `ROW_NUMBER()` partitioned by group and ordered by total score descending and `player_id` ascending is concise, but requires a per-group ordering step.
- **Tie:** Comparing only the maximum score can return several rows; `MIN(player_id)` implements the stated tie rule.
- **Both match roles:** A player may appear as the first participant in one match and the second in another, so both score columns must be normalized.
- **Repeated opponents:** Every match contributes independently, even when the same pair plays more than once.
- **Zero score:** A participating player with zero points still has a valid total and can win a zero-score tie by identifier.
- **Group isolation:** Since match opponents belong to the same group, their points never affect another group's winner.
- **Players without score rows:** A left join assigns them a zero total instead of silently removing them from consideration.

</details>
