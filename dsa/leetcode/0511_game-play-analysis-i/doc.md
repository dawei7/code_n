# Game Play Analysis I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 511 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/game-play-analysis-i/) |

## Problem Description
### Goal
The `Activity` table records a player's identifier, device, login date, and games played. A player may have activity on several dates, while the `(player_id, event_date)` pair is unique, so at most one row represents that player on a particular date.

For every player appearing in the table, return columns `player_id` and `first_login`, where `first_login` is that player's earliest recorded `event_date`. Include one row per player and return the result table in any order. Later logins and game counts do not affect the selected date.

### Function Contract
**Inputs**

- `Activity(player_id, device_id, event_date, games_played)`: one activity record per player and date

**Return value**

- A result grid with columns `player_id` and `first_login`, containing one row per player

### Examples
**Example 1**

- Input rows: player `1` appears on `2016-03-01` and `2016-05-02`; player `2` appears on `2017-06-25`
- Output rows: `[1, 2016-03-01]`, `[2, 2017-06-25]`

**Example 2**

- Input rows: player `7` has only one activity on `2024-01-09`
- Output rows: `[7, 2024-01-09]`

**Example 3**

- Input rows: player `3` appears on dates supplied out of chronological order
- Output: the earliest date, independent of input order

### Required Complexity

- **Time:** $O(A)$
- **Space:** $O(P)$

<details>
<summary>Approach</summary>

#### General

**Form one group per player**

Use `GROUP BY player_id` so every distinct player contributes exactly one output row. All activity rows belonging to that player are then available to one aggregate computation.

**Select the chronologically earliest date**

Apply `MIN(event_date)` within each group and alias the expression as `first_login`. SQL date values use chronological ordering, so the minimum is the first recorded login regardless of insertion order or device.

**Why the aggregation produces the contract**

Each input row belongs to exactly one `player_id` group, and every player present in `Activity` creates one such group. `MIN` returns a member date no later than every other date in that group. Consequently each output row contains precisely one player and that player's earliest recorded event date.

#### Complexity detail

An expected hash-aggregation plan scans `A` activity rows once and keeps one aggregate state for each of `P` players, giving $O(A)$ time and $O(P)$ auxiliary space. A database may instead choose sort aggregation with $O(A \log A)$ work depending on indexes, statistics, and its physical plan.

#### Alternatives and edge cases

- **Correlated minimum subquery:** can produce the same result but may rescan `Activity` for every outer row and take quadratic work.
- **Window function with `ROW_NUMBER`:** can select the first row per player, but sorting full partitions is unnecessary when only the minimum date is needed.
- **Join against a grouped subquery:** is useful when other columns from the first activity are required, but adds a join that this output does not need.
- **One activity:** its date is automatically that player's minimum.
- **Input order:** has no effect on `MIN`.
- **Shared dates across players:** remain in separate groups.
- **Empty table:** yields an empty result because there are no player groups.

</details>
