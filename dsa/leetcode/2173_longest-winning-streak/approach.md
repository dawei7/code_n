## General

The rows for each player must first be understood in chronological order. A winning streak is not merely a count of wins; it is a consecutive block of wins with no draw or loss between them.

The SQL query solves this as a consecutive-groups problem. It assigns a stable label to each uninterrupted run of the same result, counts wins inside every label, and then chooses the largest count for each player.

The exact query uses a difference of two `ROW_NUMBER` values. It does not use the cumulative non-win label described by the manifest summary, although both ideas can solve the task.

**Create a chronological row number**

Inside CTE `S`, the first window expression is

`ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY match_day)`.

For each player independently, this numbers all matches one, two, three, and so forth in date order. Different players restart at one. The primary key guarantees only one match per player per day, so `match_day` provides an unambiguous order.

Call this sequence the overall position. It advances on every result: win, draw, or loss.

**Create a row number within each result**

The second window expression also partitions by `result`:

`ROW_NUMBER() OVER (PARTITION BY player_id, result ORDER BY match_day)`.

It counts how many times that player has produced this particular result up to the current row. A player's first win has win-number one, the second win has win-number two, even if a draw occurs between them. Draws and losses have their own independent sequences.

**Subtract the sequences to label consecutive runs**

The query stores overall position minus result-specific position as `rk`. Within consecutive rows having the same result, both row numbers increase by one at every next row, so their difference stays constant.

Suppose a player begins `Win, Win, Win`. The overall positions are `1, 2, 3` and the win-specific positions are also `1, 2, 3`, giving `rk = 0` for all three rows. A following draw has overall position four and draw-specific position one, so its difference is three. If another win follows, its overall position is five and its win-specific position is four, giving difference one rather than zero. The later win therefore does not merge with the opening streak.

For win rows in particular, `rk` equals the number of earlier non-win rows. Every interruption increases that number, so distinct winning streaks for the same player receive distinct labels.

**Count wins in each label**

CTE `T` groups rows by `player_id` and `rk`. It calculates `SUM(result = 'Win') AS s`.

In MySQL, the comparison `result = 'Win'` evaluates to one for a win and zero for a draw or loss. Summing it therefore counts win rows in the group.

The grouping key does not include `result`. This may look surprising because a non-win row can occasionally share an `rk` value with an adjacent run of another result. Such a row contributes zero to `s`, so it cannot inflate a winning streak. More importantly, two different winning streaks for the same player cannot share `rk` because each intervening non-win increases the number of earlier non-wins. Therefore all wins combined within one group belong to one uninterrupted winning run.

**Keep players who never win**

The query starts from every row in `Matches` and does not filter non-wins before grouping. A player with only draws or losses still creates one or more groups in `T`. Each such group's sum is zero.

The outer query groups by `player_id` and selects `MAX(s)`. For a player with winning runs, this picks the longest run length. For a player with no wins, the maximum of the available zero values is zero. This is why the query does not need a separate player list or an outer join to restore winless players.

**Why the maximum is the requested streak**

Within one consecutive run of wins, the row-number difference is constant, so all its rows reach the same `T` group and contribute one each. The resulting `s` equals that run's exact length.

An interruption changes the label used by later wins, so no `T` group combines wins from two separate streaks. Non-win rows contribute zero even if their label coincides with another result's group. Hence the positive `s` values for a player are precisely that player's winning-streak lengths, possibly alongside zeros. Taking their maximum returns the longest one.

The final output has exactly the requested columns: `player_id` and the alias `longest_streak`. The problem permits any row order, so no final `ORDER BY` is required.

**Understand the example groups**

For player one, the first three wins share one label and sum to three. The draw interrupts that label. The later win receives a different win label and sums to one. The outer maximum chooses three.

For player two, both rows are losses. Their groups contain no win predicates, so their sums are zero and the maximum is zero. Player three has one win group of length one.

## Complexity detail

Let $N$ be the number of rows in `Matches`. The two window functions must organize rows by player and date and ordinarily require sorting work. This gives an $O(N\log N)$ time bound in the general case. The two grouping stages then process $O(N)$ intermediate rows.

The window-function and grouping machinery may materialize or sort $O(N)$ rows, giving $O(N)$ auxiliary working space as an algorithmic bound. Actual database memory and disk use depend on the optimizer, indexes, and available sort buffers.

An index beginning with `player_id, match_day` can help chronological access, but the result-partitioned window has a different partition order, so one should not promise both sorts disappear. The manifest's overall $O(N\log N)$ time and $O(N)$ space are consistent, even though its stated cumulative-label mechanism differs from the exact SQL.

## Alternatives and edge cases

- **Cumulative non-win labels:** Sum a one for each draw or loss over each player's chronological rows, then group wins by that cumulative value. This matches the manifest summary and often makes the streak reset especially explicit.
- **Lag plus cumulative starts:** Compare each row with its predecessor, mark the start of a win run, cumulatively number runs, and aggregate. It is flexible but needs additional window stages.
- **Correlated subqueries:** Counting neighboring wins per row is harder to reason about and can become quadratic without careful indexing.
- **Player with no wins:** Retaining non-win rows makes `SUM(result = 'Win')` zero, so the player still appears with longest streak zero.
- **Player with one win:** Its run sum and final maximum are one.
- **Draw and loss both interrupt:** Both make the next win's number of preceding non-wins larger, even though the second row-number window partitions the two result labels separately.
- **Alternating results:** Every isolated win receives a different `rk` from the next isolated win, so the maximum is one.
- **All wins:** Both row-number sequences advance together, `rk` stays constant, and one group counts every row.
- **Same calendar day across players:** Partitioning by `player_id` keeps their sequences independent.
- **Unique day per player:** The composite primary key makes chronological row numbering deterministic without an extra tie-breaker.
- **Boolean arithmetic:** `SUM(result = 'Win')` is MySQL-specific. Other SQL dialects may require `SUM(CASE WHEN result = 'Win' THEN 1 ELSE 0 END)`.
- **Follow-up for non-losing streaks:** Classify both wins and draws as one “non-loss” category before constructing the row-number difference, and count that category. Merely changing the final sum while still partitioning by the three original results would incorrectly split alternating wins and draws.
- **No output order:** Omitting `ORDER BY` complies with the “any order” contract.
- **Manifest discrepancy:** The stored query labels runs with row-number differences rather than a cumulative non-win count; the explanation follows the actual SQL.
