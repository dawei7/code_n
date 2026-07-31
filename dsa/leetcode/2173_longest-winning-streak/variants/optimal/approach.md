## General

**Turn interruptions into segment labels**

For each player, process matches in `match_day` order. Maintain a cumulative
count of rows whose result is not `Win`. Every draw or loss increases that
count, while a win leaves it unchanged. Consequently, all wins in one
uninterrupted streak share the same `(player_id, segment_id)` pair, and wins
separated by any non-win cannot share a segment.

This grouping does not depend on consecutive calendar dates. The relevant
sequence is the player's ordered matches, so two wins remain consecutive even
when many idle days lie between them.

**Measure each winning segment**

Filter the labeled rows to `Win`, group by player and segment, and count the
rows in every surviving group. Each count is exactly one winning streak's
length. Taking the maximum count per player therefore gives the requested
longest streak.

**Restore players without a winning segment**

Filtering to wins would otherwise remove a player whose history contains only
draws and losses. Start the final result from the distinct players in
`Matches`, left join their measured streaks, and replace a missing maximum with
zero. Grouping by player also collapses multiple equal maximum streaks into one
output row.

## Complexity detail

Let $n$ be the number of rows in `Matches`. The partitioned window operation
orders matches by player and date, taking $O(n\log n)$ time in a typical
database plan. The subsequent filtering, grouping, and join are linear after
that ordering. Intermediate window and grouped results require $O(n)$
execution space. Exact physical costs depend on indexes and the database
optimizer.

## Alternatives and edge cases

- **Row-number difference grouping:** Assign row numbers to all matches and to
  wins within each player, then group wins by their difference. This can also
  identify consecutive runs, but its filtering and numbering order is easier
  to express incorrectly.
- **Recursive chronological scan:** Carry the current and maximum streak from
  one match to the next. It mirrors an imperative solution but is more
  cumbersome and less portable than window aggregation.
- **Correlated prefix counts:** For every win, rescan earlier matches to locate
  the latest interruption. It is correct but may require $O(n^2)$ work.
- A `Draw` and a `Lose` have identical streak-breaking behavior.
- Players with no wins must remain in the output with `longest_streak = 0`.
- Missing calendar dates do not interrupt a streak; only recorded non-win
  matches do.
- Window ordering must be partitioned by `player_id`, or matches belonging to
  different players would affect one another.
- Input row order is irrelevant; chronology comes from `match_day`.
