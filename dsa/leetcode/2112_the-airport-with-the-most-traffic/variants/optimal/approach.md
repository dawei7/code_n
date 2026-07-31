## General

**Normalize both endpoint roles**

Each `Flights` row contributes `flights_count` to two traffic totals: one for `departure_airport` and one for `arrival_airport`. Project both roles into a common `(airport_id, flights_count)` shape and combine them with `UNION ALL`. Keeping duplicates is essential because separate route contributions must be added rather than deduplicated.

**Aggregate once per airport**

Group the normalized endpoint rows by `airport_id` and sum `flights_count`. This produces one row per airport with its complete incoming-plus-outgoing traffic, including airports that appear in only one role.

**Retain every maximum**

Apply `DENSE_RANK()` in descending traffic order and select rank one. Equal totals receive the same rank, so all airports tied at the maximum survive. Project only `airport_id`; no final ordering is needed because the contract permits any order.

## Complexity detail

Let $N$ be the number of `Flights` rows. Endpoint normalization creates $2N$ rows. A typical grouped and ranked database plan takes $O(N\log N)$ time and $O(N)$ execution space; hash aggregation can provide linear expected grouping time. Exact physical behavior remains database-dependent.

## Alternatives and edge cases

- **Aggregate departures and arrivals separately:** Group each role, join or union the summaries, and aggregate again. This is correct but requires more relational stages.
- **Correlated traffic calculation:** Enumerate airports, then rescan all flights to total each one's traffic. It is correct but an unoptimized plan takes $O(N^2)$ time.
- **Maximum scalar subquery:** After computing totals, compare each row with `MAX(total_flights)` instead of ranking. This has equivalent semantics when the totals CTE is reused efficiently.
- `UNION ALL` is required; plain `UNION` could discard equal endpoint contributions from distinct routes.
- Airports appearing only as departures or only as arrivals must still be included.
- Tied maximum totals produce multiple result rows, not an arbitrary single airport.
- `flights_count` must be summed as a weight; counting route rows alone gives the wrong traffic.
