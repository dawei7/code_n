## General

The desired rows belong to runs of at least three consecutive `id` values, and every row in such a run must have `people >= 100`. Consecutiveness is about IDs, not calendar dates. The solution uses the “gaps and islands” technique:

1. remove low-attendance rows;
2. assign increasing row numbers to the remaining rows in ID order;
3. subtract row number from ID to label each consecutive run;
4. count rows in each run and keep runs of size at least three.

**Filter before identifying runs**

The first common table expression reads:

```sql
FROM Stadium
WHERE people >= 100
```

A low-attendance row must break a qualifying run even if its ID is numerically between two high-attendance rows. Filtering first removes it, but the remaining IDs still retain the numeric gap. The gaps-and-islands label will detect that jump.

For the sample, IDs 2, 3, 5, 6, 7, and 8 remain. ID 4’s removal creates the gap between 3 and 5.

**Why `id - ROW_NUMBER()` is constant on a consecutive run**

`ROW_NUMBER() OVER (ORDER BY id)` assigns 1, 2, 3, ... to filtered rows in increasing ID order. Define:

$$
\texttt{rk}=\texttt{id}-\operatorname{row\_number}.
$$

When both ID and row number increase by one, their difference stays fixed. For IDs 5, 6, 7, and 8 with row numbers 3, 4, 5, and 6, the difference is always two.

At a gap, ID jumps by more than one while row number still advances by exactly one, so the difference changes. IDs 2 and 3 have differences one, while ID 5 starts difference two. Thus, equal `rk` values identify exactly maximal consecutive-ID islands among qualified rows.

This works because `id` values define an ordered integer sequence. The date can skip a day—as between sample IDs 7 and 8—without affecting the island, exactly as the problem states.

**Annotating each island with its size**

The second CTE computes:

```sql
COUNT(1) OVER (PARTITION BY rk) AS cnt
```

Window counting retains every original row while attaching the total size of its island. A grouped query would reduce an island to one row and lose the individual records that must be returned.

Every row in the 5–8 island receives `cnt = 4`. Rows 2 and 3 receive count two. The outer `WHERE cnt >= 3` therefore keeps all four rows from the long island and removes both rows from the short island.

**Final ordering**

`ORDER BY 1` refers to the first selected column, `id`, and sorts ascending by default. The requested ordering is ascending `visit_date`. The schema guarantees that dates increase as IDs increase, so ordering by ID is equivalent for valid input.

Spelling `ORDER BY visit_date` would mirror the request more directly, but the exact query’s ordering is correct under the stated monotonic relationship.

**Why the algorithm is correct**

After filtering, only rows meeting the attendance threshold remain. In ID order, two adjacent filtered rows share the same `id - row_number` exactly when their IDs differ by one. Therefore, each constant-`rk` partition is one maximal consecutive-ID run, and no run crosses a missing or filtered-out ID.

The window count equals each run’s number of rows. Filtering for count at least three retains exactly every row belonging to a qualifying run. Projection returns the requested columns, and ascending ID produces ascending visit date by schema guarantee.

Longer runs are handled without special overlap logic. A four-row run is one island of size four, so every row—including both endpoints—is retained.

## Complexity detail

Let $n$ be the number of `Stadium` rows. The window row numbering requires rows ordered by ID; absent a reusable index order, sorting costs $O(n\log n)$. Partitioning/counting by `rk` may require additional hashing or sorting but remains within $O(n\log n)$ under a standard plan.

The CTEs can materialize or maintain window state for $O(n)$ rows, giving $O(n)$ working space, matching the manifest. Filtering and final projection are linear. A suitable index on ID can reduce sorting work, but SQL does not mandate the physical plan.

## Alternatives and edge cases

- **`LEAD`/`LAG` neighbors:** Attach the previous two and next two qualified IDs, then retain a row if it occupies any position in a consecutive triple. Effective for fixed run length three but less scalable.
- **Three-way self-join:** Match triples of high-attendance rows with IDs one apart and use `DISTINCT` to return all members. More expensive and verbose.
- **Recursive run tracking:** A recursive CTE can propagate run IDs, but row-number subtraction is simpler.
- **Filter after row numbering:** Incorrect: low-attendance rows would consume row numbers and could distort which qualified IDs form islands. The intended sequence is the filtered set.
- **Exactly two consecutive high rows:** Their count is two, so neither appears.
- **Exactly three:** All three receive count three and are returned.
- **Longer run:** Every row shares one label and is returned.
- **Low-attendance row inside numeric sequence:** It is filtered and creates an ID gap between remaining rows, splitting islands.
- **Date gap with consecutive IDs:** Does not break the run; only ID consecutiveness matters.
- **Order by ordinal:** `ORDER BY 1` means ascending ID. It relies on the schema guarantee that date increases with ID.
- **Threshold boundary:** `people = 100` qualifies because the comparison is inclusive.
- **No qualifying island:** The output is empty.
- **Unique dates:** The schema’s unique `visit_date` and monotonic relation make the final ordering deterministic.
