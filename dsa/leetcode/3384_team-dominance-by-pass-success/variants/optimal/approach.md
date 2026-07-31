## General

Each pass needs two independent team lookups: one for `pass_from`, which determines the team receiving the score, and one for `pass_to`, which determines whether that score is positive or negative. Join `Passes` to `Teams` twice under distinct aliases so both endpoint team names are available in the same row.

Because timestamps have a fixed, zero-padded `MM:SS` format, lexical comparison preserves chronological order. Assign `half_number = 1` when `time_stamp <= '45:00'`; every later valid timestamp belongs to half two. The inclusive comparison is essential because a pass at exactly `45:00` remains in the first half.

For each joined pass, emit $+1$ when the endpoint team names match and $-1$ otherwise. Group those values by the passer's `team_name` and the derived half number, then sum them. Starting from `Passes` intentionally produces only groups with at least one outgoing pass, which matches the remote contract. Finally, order by team name and half number as required.

## Complexity detail

Let $t$ be the number of players, $p$ the number of passes, and $g$ the number of emitted team-half groups. With the unique index on `Teams.player_id`, the two endpoint lookups cost $O(p\log t)$ under a comparison-index model. Aggregation is linear in the joined pass rows, and ordering the groups costs $O(g\log g)$, for $O(p\log t+g\log g)$ time. The grouped result uses $O(g)$ working space; database join and sort implementation details may add engine-managed buffers.

The benchmark defines `size` as $p$, supplies $2p$ player rows, and uses tiers of 16, 64, and 256 passes. The accepted-class query joins each endpoint once and aggregates the resulting rows. A correct slower baseline resolves endpoint teams through correlated subqueries for every pass, repeatedly scanning the growing `Teams` table and exhibiting quadratic growth when no supporting fixture index is present.

## Alternatives and edge cases

- **Correlated endpoint subqueries:** They can return the same teams but may rescan `Teams` twice per pass instead of sharing indexed joins.
- **Score the receiver's team:** The dominance belongs to the team that attempted the pass, so grouping by `pass_to` reverses interceptions.
- **Count only successful passes:** Interceptions must contribute $-1$ rather than being ignored.
- **Split at `45:00` with `<`:** That incorrectly assigns the boundary timestamp to the second half; first-half membership is inclusive.
- **Generate every team-half pair:** Teams without an outgoing pass in a half do not produce a result row under the verified contract.
- **Several players on one team:** Group by `team_name`, not player ID, so their contributions combine.
- **Zero dominance:** Equal positive and negative contributions still produce a row with zero because passes exist in that group.
- **Negative dominance:** A team with more intercepted than successful passes retains its negative sum.
- **Ordering:** Explicitly sort by `team_name` and `half_number`; insertion order is not a result guarantee.
