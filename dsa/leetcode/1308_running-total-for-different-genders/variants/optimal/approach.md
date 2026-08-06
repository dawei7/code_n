## General

**Derive a chronological prefix for each team**

The required value is not a daily subtotal: for a row with gender $g$ and date $d$, it is the sum of every `score_points` value whose gender is $g$ and whose date is at most $d$. A window aggregate fits this shape because it annotates every source row without collapsing the dates needed in the output.

Use `SUM(score_points)` with `PARTITION BY gender` so the female and male totals have independent state. Within each partition, `ORDER BY day` places contributions in chronological order. The explicit frame `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` then includes exactly the prefix ending at the current date. The primary key (`gender`, `day`) makes each position unique, so there is one unambiguous current row.

For any output row, the window excludes every row of the other gender, includes every earlier row of the same gender, includes the current row, and excludes every later row. Its sum is therefore exactly the required cumulative score. Since a window aggregate preserves its input rows, every recorded gender-and-day pair appears exactly once.

**Keep calculation order and result order distinct**

The order inside the window defines the frame but does not guarantee presentation order. The final `ORDER BY gender, day` independently enforces the contract's ascending output order.

## Complexity detail

Let $n$ be the number of rows in `Scores`. Partitioning and ordering the rows for the window, followed by the required result ordering, takes $O(n\log n)$ time under the comparison-sorting model. The ordered window operation and result materialization can use $O(n)$ working space.

## Alternatives and edge cases

- **Correlated prefix sum:** For each outer row, summing rows of the same gender with `day <= current_day` is correct, but it can rescan a growing prefix for every result and take $O(n^2)$ time.
- **Self-join and group:** Joining each score row to all earlier rows of the same gender and grouping gives the same totals while creating a potentially quadratic intermediate relation.
- **Plain `GROUP BY gender, day`:** Grouping only the current date computes daily scores, not the cumulative prefix, and cannot derive prior contributions.
- **Missing partition:** A single global running sum incorrectly allows one team's points to contribute to the other team's total.
- **Required presentation order:** Window ordering alone is insufficient; omitting the outer sort violates the explicit `gender`, then `day`, ordering contract.
- **Empty input:** With no score rows, the query returns no rows.
- **First row and one-row partitions:** The earliest score for a gender has a total equal to its own `score_points`.
- **Date gaps:** Only recorded dates appear; elapsed calendar days do not create rows or otherwise change the running sum.
- **Signed and zero scores:** The cumulative sum follows ordinary integer addition, so it may stay unchanged or decrease when the corresponding values occur.
- **Repeated player names:** `player_name` does not define either partition membership or chronological order; only `gender` and `day` do.
