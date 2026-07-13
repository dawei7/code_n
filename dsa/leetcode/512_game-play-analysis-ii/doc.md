# Game Play Analysis II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 512 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/game-play-analysis-ii/) |

## Problem Description
### Goal
The `Activity` table records `player_id`, `device_id`, `event_date`, and `games_played`, with at most one activity row for a player on a given date. A player may use different devices on different login dates.

Return one row per player containing `player_id` and the `device_id` from that player's earliest `event_date`. Do not return the device from a later session or aggregate device identifiers. Because the player-date pair is unique, the first login determines one device; return the result rows in any order.

### Function Contract
**Inputs**

- `Activity(player_id, device_id, event_date, games_played)`: one activity record per player and date

**Return value**

- A result grid with columns `player_id` and `device_id`, containing the device from each player's earliest activity row

### Examples
**Example 1**

- Input rows: player `1` uses device `2` on `2016-03-01` and device `3` on `2016-05-02`
- Output row: `[1, 2]`

**Example 2**

- Input rows: player `7` has one activity using device `9`
- Output row: `[7, 9]`

**Example 3**

- Input rows: a later activity is listed before the first chronological activity
- Output: the device attached to the earlier date, not the first inserted row

### Required Complexity

- **Time:** $O(A)$
- **Space:** $O(P)$

<details>
<summary>Approach</summary>

#### General

**Find each player's first date**

Group `Activity` by `player_id` and compute `MIN(event_date)` as `first_login`. This derived relation has one row per player and identifies the exact date whose device is required.

**Join the date back to its source row**

Join the derived relation to `Activity` on both `player_id` and `event_date = first_login`. Matching on the player prevents equal dates from different players from mixing, and matching on the date selects the earliest row rather than an arbitrary activity.

**Why the returned device is associated correctly**

The table key permits only one activity row for a given player and date. The grouped minimum identifies one earliest date per player, and the two-column join therefore matches exactly that player's unique earliest row. Selecting `device_id` from the matched source row preserves the required association.

#### Complexity detail

An expected hash aggregate followed by a hash join scans `A` activity rows a constant number of times and stores one first-date entry per `P` players, for $O(A)$ time and $O(P)$ auxiliary space. Actual SQL costs depend on indexes and the optimizer; sort aggregation can require $O(A \log A)$ work.

#### Alternatives and edge cases

- **Correlated minimum subquery:** is concise but may rescan `Activity` for every outer row and take $O(A^2)$ work.
- **Tuple membership against grouped minima:** `(player_id, event_date) IN (...)` expresses the same selection where row-value syntax is supported.
- **Window `ROW_NUMBER`:** correctly retains the complete earliest row but generally sorts each player's partition.
- **Aggregate `MIN(device_id)`:** is incorrect because the numerically smallest device need not belong to the first date.
- **One activity:** that row's device is returned directly.
- **Input order:** does not determine which activity is first.
- **Same date across players:** is safe because the join also matches `player_id`.

</details>
