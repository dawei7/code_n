## General

**Create an independent timeline for each player**

Partition the rows by `player_id`, preventing one player's games from contributing to another player's total. Within
each partition, order rows by `event_date`; the composite primary key makes each player-date position unique.

**Sum every chronological prefix without collapsing rows**

Apply `SUM(games_played)` over the explicit frame from `UNBOUNDED PRECEDING` through `CURRENT ROW`. A window aggregate
preserves every input activity row while adding the inclusive total of its player's earlier and current records. The
explicit `ROWS` frame states the intended record prefix directly.

For a row on date `d`, that frame contains exactly the same player's recorded login dates no later than `d`. Its sum
is therefore the requested games total through that date. Partitioning excludes other players, chronological ordering
excludes later activity, and the outer `ORDER BY` merely makes local serialization deterministic even though the
source permits any result order.

## Complexity detail

Let $A$ be the number of `Activity` rows. A typical window plan sorts by player and date in $O(A \log A)$ time and
stores ordered partitions in $O(A)$ space. A suitable index or already ordered access path may let the database
stream the window with less sorting work.

## Alternatives and edge cases

- **Correlated prefix subquery:** returns the same totals but may rescan an expanding history for every output row,
  causing quadratic work.
- **Self-join on earlier dates plus grouping:** supports older SQL versions but can materialize a quadratic number of
  row pairs.
- **Recursive CTE:** can advance through each player's dates but is more complex than a supported window aggregate.
- **First activity:** its cumulative value equals its own `games_played` value.
- **Zero games:** preserves the previous total while still producing the source activity row.
- **Interleaved players:** remain independent because of `PARTITION BY player_id`.
- **Insertion order:** is irrelevant; `event_date` defines the cumulative prefix.
- **Empty table:** produces an empty result table.
