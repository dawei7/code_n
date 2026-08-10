## General

**Turn every start row into one complete running interval**

The table records events, not durations. A row whose `session_status` is `'start'` tells us when a server began running, while the corresponding `'stop'` row tells us when that run ended. Therefore, the useful quantity is the difference between two consecutive timestamps belonging to the same server.

The query first builds the common table expression `T`. For every row, `LEAD(status_time)` looks one row ahead and copies that later timestamp into `next_status_time`. Two clauses define exactly what “one row ahead” means:

- `PARTITION BY server_id` keeps different servers completely separate. The next event for server 3 can never be borrowed from server 4.
- `ORDER BY status_time` puts each server's events in chronological order before choosing the next one.

Suppose one server has these events:

| `session_status` | `status_time` | `next_status_time` |
|---|---|---|
| `start` | 08:00 | 10:30 |
| `stop` | 10:30 | 13:00 |
| `start` | 13:00 | 14:15 |
| `stop` | 14:15 | `NULL` |

Only the first and third rows describe the beginnings of running intervals. Their next timestamps are exactly their matching stop times, so their durations are 2.5 hours and 1.25 hours. The values generated for stop rows are irrelevant.

This explains why the outer query applies `WHERE session_status = 'start'` only after `LEAD` has been evaluated in the CTE. Filtering starts before evaluating the window would remove all stop rows. Then a start row would look ahead to the next start, which would measure downtime and running time together and produce a wrong answer. Keeping all events during the window calculation preserves the start-to-stop adjacency; filtering afterward selects only actual uptime intervals.

**Measure in seconds, add globally, and round only once**

For every retained start row, `TIMESTAMPDIFF(SECOND, status_time, next_status_time)` measures the complete interval in seconds. `SUM` then combines intervals from every server because the requested result is total fleet uptime, not one result per `server_id`.

It is important to sum the raw seconds before converting to days. Rounding each session separately would discard partial days that can combine into a full day. For example, two 18-hour sessions contribute 36 hours in total, which contains one full day. If each session were independently rounded down, both would become zero and that day would be lost.

There are 86,400 seconds in a day, so the query divides the grand total by `86400`. `FLOOR` removes the remaining fractional day and implements “rounded down to the nearest number of full days.” For 129,600 accumulated seconds, the division gives 1.5 and `FLOOR` returns 1.

**Why each running second is counted exactly once**

Under the table contract, events for a server form complete start/stop sessions in chronological order. Consider any such session. Its start event receives the immediately following stop timestamp from `LEAD`, so the query includes that session's entire duration. No other retained row can include the same session: the stop row is filtered out, and the next start begins a different interval. Thus every complete running interval contributes once and only once.

The partition boundary matters at the end of a server's history. The last row has no later row in its partition, so `LEAD` produces `NULL`. With properly paired sessions, that final event is a stop and is filtered out. A malformed unmatched final start would create a `NULL` duration, which `SUM` ignores rather than inventing an ending time. The problem's event guarantees are what make the intended pairing valid.

**Relation to the exact submitted query**

The query is not the “add stop timestamps and subtract start timestamps in one scan” technique described by the manifest summary. It explicitly materializes the next event with a window function and then sums start-to-next-event differences. Both ideas can compute the same mathematical total when sessions are well formed, but the explanation and cost must follow the code that is actually present.

## Complexity detail

Let $r$ be the number of rows in `Servers`.

The window function must process all $r$ rows. In the general database execution model, rows must be ordered by `server_id` and `status_time` so that `LEAD` can identify each successor. If no useful ordering is already available, that sort costs $O(r \log r)$ time. The following filter and aggregation cost $O(r)$. Therefore, the safe worst-case time bound for the exact query is $O(r \log r)$.

The composite primary key begins with `server_id` and `status_time`, so a MySQL optimizer may be able to read a suitable index in the required order and avoid an explicit sort. In that favorable physical plan, the processing time can approach $O(r)$. This is an execution-plan optimization, not a reason to promise linear time independently of storage and indexing.

The window stage can require $O(r)$ intermediate storage in the worst case for sorting or materializing rows. The final aggregate itself uses only $O(1)$ scalar state. Consequently, the manifest's $O(r)$ time and $O(1)$ space describe an ideal ordered scan or only the aggregation state; they do not express the conservative worst-case cost of the exact window-function query.

The returned result has exactly one row and one value, so output space is $O(1)$.

## Alternatives and edge cases

- **Signed timestamp aggregation:** Add every stop timestamp and subtract every start timestamp, then convert the resulting total duration. This can avoid explicitly pairing rows when sessions are guaranteed balanced, but timestamp arithmetic is less direct and still relies on the event contract.
- **Self-join with row numbers:** Number starts and stops per server and join matching sequence numbers. It makes pairing visible, but requires more machinery and usually the same ordering work as `LEAD`.
- **Correlated next-stop lookup:** For every start, search for the earliest later stop of the same server. This is intuitive but may perform repeated index searches and is easier to get wrong when several sessions exist.
- **Filter placement:** The `session_status = 'start'` condition must remain outside the CTE that computes `LEAD`. Applying it before the window calculation changes “next event” into “next start.”
- **Multiple servers:** Partitioning is essential. Without `PARTITION BY server_id`, a late event from one server could be paired with an early event from another.
- **Several short sessions:** Durations must be added before `FLOOR`. Fractional days from separate sessions are allowed to combine into full days.
- **Session crossing midnight:** Nothing special is needed. `TIMESTAMPDIFF` measures elapsed seconds across dates correctly.
- **Last stop event:** Its `next_status_time` is `NULL`, but the stop row is removed by the outer filter.
- **Unmatched final start:** The exact query silently excludes its `NULL` duration through SQL aggregate semantics. The intended data contract should prevent this malformed history; the query does not choose an artificial end time.
- **Empty input:** If the table were empty, `SUM` would return `NULL` and so would the final expression. The problem normally supplies valid session data; returning zero for a potentially empty table would require `COALESCE`.
