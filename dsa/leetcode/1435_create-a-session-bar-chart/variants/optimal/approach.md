## General

**Convert the minute boundaries to stored units.** `Sessions.duration` is measured in seconds, so the four lower boundaries are `0`, `300`, `600`, and `900`. An ascending `CASE` expression using `< 300`, `< 600`, `< 900`, and `ELSE` assigns every row to exactly one interval and gives exact-boundary values to the interval that begins there.

**Aggregate each observed interval once.** Group the classifications and count their rows. Because the `CASE` branches are mutually exclusive and exhaustive, every session contributes to one total without overlap or omission.

**Drive the result from the complete bin dimension.** Grouping `Sessions` alone would omit an interval with no rows. The fixed four-row `bins` common table expression instead supplies every required output label and a numeric presentation key. A left join attaches observed totals, and `COALESCE` converts an absent aggregate to zero. This guarantees exactly four rows even for an empty `Sessions` table.

The source permits any output order. Sorting the four fixed bin rows by their numeric key is optional constant work that makes the chart deterministic without exposing the key. The fourth interval is described as “15 minutes or more” in the narrative, while its exact output label remains `15 or more` as shown by the source result.

## Complexity detail

Let $n$ be the number of session rows. Classification and grouping perform one logical scan of `Sessions`, so the query takes $O(n)$ time. The grouped domain, bin dimension, join, and optional final sort contain at most four rows, giving $O(1)$ auxiliary state apart from database-engine execution details.

## Alternatives and edge cases

- **Four conditional counts with `UNION ALL`:** This is correct and asymptotically linear because the bin count is fixed, but it scans `Sessions` four times instead of classifying once.
- **Group only by the `CASE` label:** This omits every zero-count interval and therefore violates the four-row contract.
- **Correlated work per session:** Recomputing a prefix or count from `Sessions` for every source row can take $O(n^2)$ time before the final aggregation.
- **Exact 300 seconds:** It belongs to `[5-10>`, not `[0-5>`.
- **Exact 600 seconds:** It belongs to `[10-15>`.
- **Exact 900 seconds:** It belongs to `15 or more`.
- **Repeated durations:** Distinct session rows count independently even when their durations are equal.
- **Empty input or empty interval:** Preserve all four labels and report zero for every interval without a matching row.
- **Unrestricted output order:** Do not require the deterministic display order when validating a correct result.
