## General
Sort intervals by left endpoint and pair each query with its original index before sorting the queries by value. Sweep queries from small to large. Before answering query $x$, add every interval with `left <= x` to a min-heap keyed first by interval size and then by right endpoint.

Some added intervals may have expired because their right endpoint is less than $x$. Remove expired intervals while one is at the heap top. An expired interval hidden below the top cannot affect the answer; if it later reaches the top, it will be removed before use.

After this cleanup, every remaining heap entry started no later than $x$, and the top also ends no earlier than $x$. It therefore covers the query. Since interval size is the primary heap key, the top is the smallest covering interval. If the heap is empty, no interval covers $x$. Store the result at the query's saved original index.

## Complexity detail
Sorting takes $O(n\log n+q\log q)$. Every interval is pushed once and popped at most once, adding $O(n\log n)$; answering queries adds $O(q)$ heap inspections. This is $O((n+q)\log(n+q))$ time. Sorted queries, answers, and the heap use $O(n+q)$ space.

## Alternatives and edge cases
- **Scan every interval per query:** Directly test coverage and keep the shortest length, but costs $O(nq)$ time.
- **Sort by interval size:** Processing intervals shortest-first can work with a disjoint-set query structure, but is more involved.
- **Closed endpoints:** A query equal to either endpoint is included.
- **No covering interval:** Return `-1`, not zero.
- **Duplicate queries:** Preserve one answer per input position.
- **Duplicate or nested intervals:** Heap ordering naturally selects the minimum size.
- **Original order:** Sorting queries is only an internal sweep; restore answers by saved indices.
- **Expired non-top entries:** They may remain lazily because they cannot win while a smaller valid interval is above them.
