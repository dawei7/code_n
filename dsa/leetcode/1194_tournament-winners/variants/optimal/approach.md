## General
**Normalize both match roles.** Use `UNION ALL` to emit one `(player_id, score)` row for `first_player` and one for `second_player` from every match. Keeping both branches avoids role-specific logic in later aggregation and preserves duplicate score rows from different matches.

**Build complete player totals.** Left join `Players` to the normalized score rows, group by the player's group and ID, and sum the scores. `COALESCE` gives zero to a player with no recorded score rows. This step also attaches `group_id` once, after both match roles have been unified.

**Apply both winner rules explicitly.** Compute the maximum total score per group, join those maxima back to player totals, and retain only tied leaders. A final `MIN(player_id)` selects the required smallest identifier among them. This separates score maximization from tie-breaking and yields exactly one row per group.

## Complexity detail
The normalized stream contains $2m$ rows. With hash joins and aggregation, producing player totals, group maxima, and tie winners takes $O(p+m)$ logical time. The normalized score stream and per-player aggregation state occupy $O(p+m)$ space; the group-level state is $O(g)$ and is bounded by $O(p)$.

## Alternatives and edge cases
- **Correlated score lookup per player:** Rescanning `Matches` for each player is correct but can take $O(pm)$ time.
- **Window ranking:** `ROW_NUMBER()` partitioned by group and ordered by total score descending and `player_id` ascending is concise, but requires a per-group ordering step.
- **Tie:** Comparing only the maximum score can return several rows; `MIN(player_id)` implements the stated tie rule.
- **Both match roles:** A player may appear as the first participant in one match and the second in another, so both score columns must be normalized.
- **Repeated opponents:** Every match contributes independently, even when the same pair plays more than once.
- **Zero score:** A participating player with zero points still has a valid total and can win a zero-score tie by identifier.
- **Group isolation:** Since match opponents belong to the same group, their points never affect another group's winner.
- **Players without score rows:** A left join assigns them a zero total instead of silently removing them from consideration.
