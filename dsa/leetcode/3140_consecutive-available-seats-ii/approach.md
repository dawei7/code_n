## General

**Filter to available seats, then identify consecutive islands**

Only rows with `free = 1` can belong to an available-seat sequence, so CTE `T` filters occupied seats first.

Among the remaining rows, seats are ordered by `seat_id`. Because `seat_id` is an auto-increment identifier and therefore unique, `RANK() OVER (ORDER BY seat_id)` produces consecutive ranks 1, 2, 3, and so on. In this query, `RANK` behaves exactly like `ROW_NUMBER` because ties cannot occur.

For a consecutive run of seat identifiers, both `seat_id` and its rank increase by one from row to row. Their difference remains constant:

$$
\texttt{gid}=\texttt{seat\_id}-\operatorname{rank}.
$$

For example, available seats 3, 4, and 5 may receive ranks 2, 3, and 4 after an earlier available seat 1. Their differences are all 1. If the next available seat is 8 with rank 5, its difference is 3, so it begins a new group.

This “value minus consecutive row number” pattern converts every island of consecutive integers into one group key.

**Aggregate each island**

CTE `P` groups the rows by `gid`. Within each group:

- `MIN(seat_id)` is the first seat;
- `MAX(seat_id)` is the last seat;
- `COUNT(1)` is the consecutive run length.

The grouping is valid in both directions. Consecutive available identifiers keep the same difference. If two available identifiers have a gap greater than one, `seat_id` jumps by more than rank does, so the difference changes. Therefore, a group contains exactly one maximal consecutive available sequence.

**Select every longest sequence**

Within the grouped runs, the query computes

`RANK() OVER (ORDER BY COUNT(1) DESC) AS rk`.

The longest length sorts first and receives rank 1. If several runs have that same maximum length, `RANK` assigns rank 1 to all of them. The outer `WHERE rk = 1` therefore returns every tied longest sequence.

Finally, `ORDER BY 1` orders by the first selected column, `first_seat_id`, in ascending order as required.

The local description contains two lines that appear inconsistent: it says there is at most one longest sequence, then says to include all sequences when lengths tie. The exact query robustly follows the latter rule and returns all ties. If the uniqueness guarantee always holds, the tie support simply has no visible effect.

**Why occupied seats create the correct breaks even though they are filtered out**

Suppose seats 3 and 5 are free while seat 4 is occupied. After filtering, 3 and 5 are adjacent rows in `T`, but their identifiers differ by two while their ranks differ by one. Therefore:

$$
3-r \ne 5-(r+1).
$$

They receive different `gid` values. The method does not need occupied rows to remain present; gaps in the numeric identifiers preserve the break.

**Example**

For seats 1 through 5 with availability `[1,0,1,1,1]`, the free identifiers are 1, 3, 4, 5. Their ranks are 1, 2, 3, 4, giving group differences 0, 1, 1, 1. The groups are therefore `[1]` and `[3,4,5]`. Their lengths are 1 and 3, and the latter alone receives rank 1 by descending length. The output is first seat 3, last seat 5, length 3.

## Complexity detail

Let $r$ be the total number of rows in `Cinema` and $f$ the number of free-seat rows.

Filtering reads up to $r$ rows. The first window function orders the $f$ free rows by `seat_id`. The primary/auto-increment index may allow an ordered scan, but the conservative database-plan bound is $O(f\log f)$ for sorting. Grouping costs $O(f)$ with hashing or may require ordered processing. Ranking the resulting $g$ groups by count can cost $O(g\log g)$, where $g\le f$.

Thus a safe overall worst-case bound is $O(r+f\log f)$, commonly summarized as $O(r\log r)$ or the manifest's $O(n\log n)$ when $n=r$.

Window and grouping stages may materialize up to $O(f)$ rows or group state, so auxiliary working space is $O(f)$ and hence $O(r)$ in the worst case. The returned output contains at most $g$ tied groups; under a strict unique-longest guarantee it contains one row.

Actual SQL costs depend on indexes and the optimizer. An ordered index on `seat_id` can reduce explicit sorting work, but the second rank still orders group aggregates by length.

## Alternatives and edge cases

- **`LAG` break detection:** Compare each free `seat_id` with the previous one, mark a new group when the difference is not 1, and use a cumulative sum of break flags. This is explicit but uses another window layer.
- **Recursive traversal:** Follow seat identifiers one by one and build runs. It is more complicated and usually less optimizer-friendly.
- **Self-join run starts and ends:** Detect free seats without free predecessors or successors, then pair boundaries. Correct pairing can become cumbersome.
- **`ROW_NUMBER` instead of `RANK` in T:** Because `seat_id` is unique, it produces identical group identifiers and communicates the intent more directly.
- **Tied longest runs:** The second `RANK` deliberately returns all ties. Replacing it with `ROW_NUMBER` would incorrectly keep only one.
- **Single free seat:** It forms a run with identical first and last IDs and length 1.
- **All seats free and consecutive:** All rows have one `gid` and form one group.
- **Occupied gap:** Filtering does not merge across it because the numeric `seat_id` jump changes `gid`.
- **Missing numeric IDs:** Even if an identifier is absent rather than occupied, the gap also breaks consecutiveness, as the definition is based on consecutive seat IDs.
- **No free seats:** Both CTEs produce no groups and the result is empty. The statement does not specify a synthetic zero-length row.
- **Ordering ties:** `ORDER BY 1` is positional SQL syntax for ascending `first_seat_id` and ensures deterministic required order.
- **Unique identifier assumption:** If duplicate `seat_id` values were allowed, `RANK` gaps could distort `gid`. The auto-increment contract rules duplicates out.
