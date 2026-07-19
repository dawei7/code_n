## General
**Express the boarding process as a prefix sum.** Order the rows by `turn` and use a windowed `SUM(weight)` from the first row through the current row. The resulting value is precisely the bus weight immediately after that person boards because every earlier turn contributes once.

**Keep only feasible prefixes.** Positive passenger weights make cumulative weight non-decreasing. Rows whose running total is at most 1000 are exactly the people who can board before the capacity would be exceeded. The platform guarantee that the first person fits ensures this filtered set is nonempty.

**Choose the final feasible turn.** Sort the feasible rows by `turn` in descending order and take one row. It has the greatest boarding position whose prefix remains within the limit, so its `person_name` is the requested last passenger.

## Complexity detail
Without relying on an index for `turn`, ordering the $n$ rows for the window calculation costs $O(n\log n)$ time; the window scan and final selection are linear. The ordered window state may use $O(n)$ auxiliary space. A database engine with a suitable physical order or index may execute the scan more cheaply, but the stated bound does not assume one.

## Alternatives and edge cases
- **Correlated prefix subquery:** Summing all rows with `turn <= current.turn` for every candidate is correct, but it can rescan the table $n$ times and take $O(n^2)$ time.
- **Self-join and aggregation:** Joining each row to all preceding turns and grouping by the candidate row also computes prefixes, but materializes up to quadratically many pairs.
- **Recursive CTE:** Simulating boarding turn by turn is possible, though more verbose and less direct than a window sum.
- **Exact capacity:** A cumulative weight equal to 1000 is allowed because boarding must not exceed the limit.
- **First person only:** The guarantee that turn 1 fits means the query always has a feasible row, even if turn 2 crosses the limit.
- **All people fit:** The row with the largest `turn` is returned.
- **Unordered storage:** Window ordering must use `turn`; neither insertion order nor `person_id` determines boarding order.
