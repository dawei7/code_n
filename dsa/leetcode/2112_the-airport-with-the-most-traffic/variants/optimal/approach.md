## General

**Normalize departures and arrivals into one airport column**

Every flight row contributes `flights_count` traffic to two endpoint roles: its departure airport and its arrival airport. Aggregating only one original column would miss half of the traffic.

The CTE `T` creates rows in both orientations:

- `SELECT * FROM Flights` keeps `departure_airport` as the first column;
- `SELECT arrival_airport, departure_airport, flights_count FROM Flights` swaps the endpoints, making the original arrival airport the first column.

Although the column retains the name `departure_airport` from the first query, after normalization it means “the airport receiving this traffic contribution.” The second column is no longer used by the later aggregation.

For route 1 to 2 with count 4, the normalized data includes a row whose first airport is 1 and another whose first airport is 2. Both airports consequently receive a contribution of 4.

**Aggregate all contributions by airport**

The second CTE `P` groups `T` by its first column and calculates

`SUM(flights_count) AS cnt`.

This combines outbound and inbound traffic contributions into one total for each airport.

In the first example, airport 1 receives 4 from departing on route 1 to 2 and 5 from arriving on route 2 to 1, totaling 9. Airport 2 receives contributions 4, 5, and 5 from its incident routes, totaling 14.

`GROUP BY 1` means group by the first selected expression, which is `departure_airport`. Writing the name explicitly would be equivalent and somewhat more verbose.

**Select every airport tied for the maximum**

The scalar subquery `SELECT MAX(cnt) FROM P` finds the greatest aggregated traffic total.

The outer query keeps every row of `P` whose `cnt` equals that maximum. This equality, rather than a one-row `ORDER BY ... LIMIT 1`, preserves ties.

The airport column is renamed `airport_id` to match the required result schema. No `ORDER BY` is needed because any row order is allowed.

**Why the intended normalization works**

Conceptually, each original route should produce two traffic events:

- one event credited to the departure airport;
- one event credited to the arrival airport.

After those events are combined, grouping computes the total incident flight count. Comparing against the global maximum then returns exactly all airports with greatest traffic.

This is a useful SQL pattern: normalize multiple semantic roles into a shared key column, aggregate once, then filter by the aggregate maximum.

**The exact query's `UNION` limitation**

The source uses `UNION`, which removes duplicate result rows, rather than `UNION ALL`, which preserves every contribution.

That can change the intended arithmetic. Suppose `Flights` contains both `(1, 2, 4)` and `(2, 1, 4)`. The original and swapped selections each produce the same two triples. `UNION` collapses duplicates, so each airport may receive only 4 instead of the correct combined 8.

The composite primary key prevents duplicate rows with the same directed endpoint pair, but it does not forbid reciprocal routes. Therefore, the exact SQL is not universally correct under the reference schema.

For a robust solution, the normalization should use `UNION ALL` so every original flight-count contribution is retained. This approach document explains the exact source while explicitly identifying this material failure mode rather than hiding it.

If no reciprocal normalized triples coincide, the `UNION` result happens to match `UNION ALL` and the intended proof applies.

**Why the maximum subquery preserves ties**

`MAX(cnt)` returns one numeric value, not an airport. The outer equality selects every airport whose total reaches it. This handles examples where four airports share the same maximum without needing ranking functions.

Using a strict greater-than comparison cannot express this selection, and limiting a sorted result to one row would violate the tie rule.

## Complexity detail

Let $N$ be the number of `Flights` rows.

Both normalization branches scan $N$ rows. `UNION` performs duplicate elimination, commonly through sorting or hashing. Under the manifest's conservative comparison-based model, normalization and grouping cost $O(N\log N)$ time.

The CTEs can materialize $O(N)$ normalized and grouped rows, so auxiliary database working space is $O(N)$. A hash-based plan may run in expected linear time, while physical execution depends on the optimizer and indexes.

The final maximum and filter operate over at most $O(N)$ airport groups.

## Alternatives and edge cases

- **Use `UNION ALL`:** This is the correct weighted-event normalization because every route must contribute independently to both endpoints.
- **Separate departure and arrival aggregates:** Aggregate each role, combine airport totals, and aggregate again. It is correct but more verbose than a safe `UNION ALL` normalization.
- **Window rank:** `DENSE_RANK` over descending traffic can select rank one and preserve ties, but the scalar maximum is simpler.
- **`ORDER BY cnt DESC LIMIT 1`:** Incorrect when multiple airports tie for maximum.
- **Reciprocal equal-count routes:** The exact `UNION` may collapse contributions and undercount traffic.
- **Primary key interpretation:** It prevents duplicate directed pairs but does not make all normalized endpoint triples unique.
- **Airport appearing only as arrival:** The swapped branch brings it into the aggregate.
- **Airport appearing only as departure:** The original branch includes it.
- **Tied totals:** Equality with the global maximum returns every tied airport.
- **Any result order:** No sort is required.
- **Exact output alias:** The selected column must be named `airport_id`.
- **Empty input:** `P` is empty and the query returns no airport rows.
