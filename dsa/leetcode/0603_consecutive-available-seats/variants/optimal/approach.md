## General

A seat belongs in the answer when two statements are simultaneously true:

- that seat is free;
- at least one immediately adjacent seat ID—one less or one greater—is also free.

The table contains one row per seat, so the query joins `Cinema` to itself. Alias `a` represents the seat being considered for output, while alias `b` represents a possible free neighbor.

**Matching adjacent IDs**

The join condition:

```sql
ABS(a.seat_id - b.seat_id) = 1
```

accepts both directions:

- `b.seat_id = a.seat_id - 1`;
- `b.seat_id = a.seat_id + 1`.

Absolute difference one means numerical adjacency. Difference zero would pair a seat with itself and must not count. A larger difference leaves at least one seat ID between them and is not consecutive.

The schema calls `seat_id` auto-incrementing and models the $i$th seat with that ID. The problem’s consecutive-seat rule is therefore based on consecutive ID values.

**Both endpoints must be available**

The rest of the join condition is:

```sql
AND a.free
AND b.free
```

In MySQL Boolean context, a stored 1 is true and 0 is false. Requiring both filters out:

- an occupied candidate `a` beside a free seat;
- a free candidate beside only an occupied `b`;
- two occupied adjacent seats.

Only a free-free adjacent pair creates joined rows.

**Why `DISTINCT` is necessary**

Consider three free seats 3, 4, and 5. Alias `a` at seat 4 matches both `b = 3` and `b = 5`, so the join produces two rows whose selected `a.seat_id` is 4. The answer should list seat 4 once.

`SELECT DISTINCT a.seat_id` removes duplicate candidate IDs after all matching neighbors have established eligibility. Endpoint seats 3 and 5 each have one matching neighbor and also appear once.

The join is symmetric, so adjacent pair 3–4 produces one result with `a=3,b=4` and another with `a=4,b=3`. This is intentional: both seats belong in the answer.

**Ordering**

`ORDER BY 1` refers to the first selected expression, `a.seat_id`, and ascending is the default. It produces the required increasing seat-ID order.

For the sample, seats 3, 4, and 5 are free. Joined free pairs are oriented 3–4, 4–3, 4–5, and 5–4. Projection gives `3,4,4,5`; `DISTINCT` gives `3,4,5`; ordering preserves that ascending sequence.

**Why the query is correct**

If a seat ID appears in the result, it came from a joined row. The predicates guarantee `a` is free, `b` is free, and their IDs differ by one. Thus, the selected seat has a free consecutive neighbor and must be returned.

Conversely, suppose a seat is free and has at least one free adjacent seat. Choosing that row as `a` and the adjacent row as `b` satisfies every join predicate, so the join produces at least one selected occurrence of its ID. `DISTINCT` may merge duplicates but cannot remove its only value. Therefore, every qualifying seat is returned.

Sorting then establishes the requested order. The query does not need to identify whole free runs or their lengths; existence of one matching neighbor is exactly the membership condition for runs of length at least two.

The statement says tests contain more than two consecutively available seats, but the logic also correctly handles a run of exactly two: both endpoints would be returned.

## Complexity detail

Let $n$ be the number of cinema rows. SQL is declarative, so physical cost depends heavily on how the optimizer executes the self-join.

If the engine can exploit seat-ID ordering or transform adjacency into indexed lookups, matching each row to neighbors can take $O(n\log n)$ time—or expected/ordered $O(n)$ with suitable structures—followed by deduplication/order work bounded by $O(n\log n)$. This aligns with the manifest’s intended $O(n\log n)$ time and $O(n)$ materialization space.

However, the exact predicate wraps the difference in `ABS` and is a non-equality expression. A naive nested-loop plan may test $n^2$ row pairs, giving $O(n^2)$ worst-case time. The SQL text alone cannot guarantee the manifest bound. Writing two direct neighbor lookups or using window functions can make the intended access pattern clearer to an optimizer.

The join output is linear for unique seat IDs because each seat has at most two numeric neighbors, though an engine may examine more candidate pairs to discover it. `DISTINCT` and ordering can store/sort $O(n)$ rows.

## Alternatives and edge cases

- **`LAG` and `LEAD`:** Order rows by `seat_id` and inspect neighboring IDs/free flags. Avoids a self-join but must verify ID difference one, not merely row adjacency if gaps are possible.
- **Two explicit joins or `EXISTS`:** Check for a free row at `seat_id - 1` or `seat_id + 1`. Equality predicates can use an index more directly than `ABS`.
- **Union oriented neighbor pairs:** Select both endpoints of every free pair with `UNION`. Naturally deduplicates but repeats query structure.
- **Missing `DISTINCT`:** A middle seat in a run appears once per free neighbor and would be duplicated.
- **Occupied middle seat:** Breaks the run; free seats on opposite sides are two IDs apart and do not match directly.
- **Run of two:** Both seats qualify because each has the other as a neighbor.
- **Run of three or more:** Every endpoint has one match and every interior seat has two; all appear once after deduplication.
- **Isolated free seat:** Has no joined row and is correctly excluded.
- **First or last seat:** Needs only its one possible in-range neighbor; no boundary special case is required in a relational join.
- **ID gaps:** Difference one, not physical row adjacency, controls qualification.
- **Boolean semantics:** `a.free` and `b.free` rely on 1/0 truth values stated by the schema.
- **Ordinal ordering:** `ORDER BY 1` means selected seat ID ascending.
- **Physical-plan caveat:** An `ABS` join can degrade to quadratic pair testing; asymptotic performance is not guaranteed solely by the manifest.
