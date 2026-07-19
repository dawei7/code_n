## General
The output asks one question per email value: how many source rows contain it? `GROUP BY email` collects all equal addresses into one group, and `COUNT(*)` gives that group's exact multiplicity. Keep only groups with `COUNT(*) > 1` using `HAVING`, then alias the grouped value as `Email`.

`HAVING` is the correct stage because the duplicate condition depends on an aggregate result. `WHERE` filters individual input rows before groups and therefore cannot test the final group count.

Grouping also provides the requested output cardinality automatically. If an address appears two, three, or a thousand times, it forms one group and produces one result row rather than one row for every duplicate occurrence.

Each group contains all and only `Person` rows with one particular email. Its count is therefore greater than one exactly when that email is duplicated. The `HAVING` predicate retains every duplicated-email group and rejects every unique-email group. Since each retained group emits its key once, the result contains every duplicated address exactly once.

## Complexity detail
A sort-based grouping plan takes $O(n \log n)$ time and up to $O(n)$ intermediate storage. A hash aggregate can run in expected $O(n)$ time with $O(u)$ storage for `u` distinct emails. The actual choice depends on indexes and the optimizer.

## Alternatives and edge cases
- A self-join on equal email values may generate quadratically many row pairs for a frequent address and still needs `DISTINCT`.
- A window count can annotate every row, but requires a final deduplication step to meet the one-row-per-email result.
- `WHERE COUNT(*) > 1` is invalid SQL because aggregate filtering occurs after grouping.
- A one-row or all-unique table yields no rows; any multiplicity above one still yields one row.
- The contract states emails are non-null. With nullable emails, the desired treatment of the single SQL null group would need to be specified.
