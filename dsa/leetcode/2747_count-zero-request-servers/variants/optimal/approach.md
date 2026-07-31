## General

Answer the queries offline so their time windows move only forward. Sort `logs` by request time, and sort pairs of `(query time, original index)` by time. Two pointers delimit the log entries inside the current inclusive interval. Before answering a query at time $t$, advance the right pointer while log times are at most $t$. Then advance the left pointer while log times are less than $t-x$.

Maintain a request frequency for every server represented inside this window. Adding a log whose server had frequency zero makes that server active; removing the server's last in-window log makes it inactive. The number of keys with positive frequency is therefore exactly the number of servers that received at least one request in `[t - x, t]`, so subtracting it from `n` gives the requested zero-request count. Store that count at the query's original index.

After each update, every retained log has time at least $t-x$ and at most $t$, while all excluded logs fall outside the interval. Sorting query times makes both interval endpoints non-decreasing, so neither pointer ever needs to move backward. This establishes the window invariant for every query and proves each reported complement is correct.

## Complexity detail

Let $m$ be the number of logs and $q$ the number of queries. Sorting costs $O(m\log m+q\log q)$ time. Each log enters and leaves the window at most once, adding $O(m+q)$ processing after sorting. The indexed queries, answer, and active-frequency structure use $O(n+q)$ auxiliary space in the stated bound; a hash map stores only servers that are currently active.

## Alternatives and edge cases

- **Scan all logs for every query:** Directly building the active-server set for each interval is simple and correct, but takes $O(mq)$ time.
- **Binary search per server:** Grouping sorted request times by server and searching every server for every query still costs $O(nq\log m)$ in the worst case.
- **Segment tree over time:** A tree can aggregate some time data, but distinct server identities make the sliding frequency window substantially simpler.
- Logs and queries may arrive unsorted; both must be processed in chronological order while answer indices remain original.
- Both endpoints are inclusive, so remove times strictly less than `query - x`, not times equal to it.
- Repeated logs from one server require frequencies; removing one request must not mark the server inactive while another remains in the window.
- A window may contain no logs, in which case all `n` servers have zero requests.
- Servers with no entries anywhere are absent from every active-frequency map and are always counted in the complement.
