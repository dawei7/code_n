## General
**Translate minutes into exact second boundaries.** Five, ten, and fifteen minutes correspond to 300, 600, and 900 seconds. Classify each `duration` with a `CASE` expression using `< 300`, `< 600`, `< 900`, and an `ELSE` branch. Testing in ascending order makes the boundary ownership explicit.

**Aggregate the observed classifications once.** Group the classified rows by their label and compute `COUNT(*)`. Each session enters exactly one branch of the `CASE` expression, so it contributes once to one count and cannot be double-counted at a boundary.

**Materialize the complete bin dimension.** A grouped query alone omits a label when no session falls in that interval. Create a four-row `bins` common table expression containing every exact label and a numeric display order, then left join the observed counts onto it. Replace a missing aggregate with zero using `COALESCE`.

**Why the result has exactly the required rows.** The left side of the final join contains one row for each required bin and no other labels. Classification maps every source row to one of those labels, so each joined count is complete. A missing match means the bin truly received no sessions, and `COALESCE(..., 0)` supplies its required zero. Ordering by the hidden numeric key produces a stable bar-chart sequence without adding that key to the output.

## Complexity detail
The classification and grouping scan the $n$ session rows once. Joining at most four aggregate rows to four fixed bin rows is constant work, so the logical query cost is $O(n)$ time. The grouping domain and result both contain exactly four rows, giving $O(1)$ auxiliary state apart from database-engine execution details.

## Alternatives and edge cases
- **Four independent conditional queries:** Combining four `COUNT(*)` statements with `UNION ALL` is correct and still linear because the number of bins is fixed, but it scans `Sessions` four times.
- **Group only by the CASE label:** This is concise but fails the contract by omitting empty bins.
- **Correlated counting per session:** Repeatedly scanning `Sessions` from each source row can take $O(n^2)$ time before aggregation.
- **Exact 300 seconds:** It belongs to `[5-10>`, not `[0-5>`.
- **Exact 600 seconds:** It belongs to `[10-15>`.
- **Exact 900 seconds:** It belongs to `15 or more`.
- **Zero sessions in a bin:** Preserve the label and return `0` rather than dropping the row.
- **Units:** Compare seconds to 300, 600, and 900; do not compare the stored values directly with 5, 10, and 15.
