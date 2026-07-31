## General

Let $q$ be the number of queries.

**Represent the current shortest route as a linked chain**

Initially the unique route is `0 -> 1 -> ... -> n - 1`. Store `next_city[u]`, the next city after `u` on the maintained shortest route. Its initial value is `u + 1`, and the route length starts at $n-1$.

For a new road `[u, v]`, examine the current successor of `u`. While that successor lies before `v`, the new road bypasses it. Save the successor, redirect `next_city[u]` to `v`, move `u` to the saved city, and reduce the route length by one. This walks through precisely the route edges replaced by the shortcut.

**Why removed cities never need to return**

The noncrossing guarantee is the crucial distinction from Queries I. Once an interval bypasses part of the maintained route, a later interval cannot begin inside that removed part and end beyond the enclosing interval; that would create forbidden crossing endpoints. A later road wholly inside the bypassed interval cannot improve the maintained route, while an enclosing road can bypass the whole segment from an active endpoint. Thus a city removed from the route never becomes necessary again.

If `next_city[u]` is already at or beyond `v`, the new interval lies within a shortcut already represented by the route and changes nothing. Otherwise, every loop iteration permanently removes one route edge. The counter after processing a query is consequently the exact number of edges on the best route from $0$ to $n-1$.

## Complexity detail

Initialization takes $O(n)$. Although a single query may bypass many cities, each loop iteration permanently removes one city from the maintained route, so at most $n-1$ iterations occur across all queries. Including the $O(1)$ work per query, total time is $O(n+q)$. The successor array uses $O(n)$ space.

## Alternatives and edge cases

- **BFS after every query:** This works without the noncrossing guarantee but costs $O(q(n+q))$ time and ignores the stronger interval structure.
- **Ordered set of active cities:** Removing all active cities strictly inside `[u, v]` also achieves near-linear behavior, but a successor array provides simpler constant-amortized traversal.
- **Assume every query helps:** A nested interval whose endpoints are already bypassed leaves the shortest distance unchanged.
- Disjoint shortcuts remove independent portions of the route and their savings add.
- Nested shortcuts may arrive from inner to outer or outer to inner; only newly bypassed active cities reduce the counter.
- Intervals that share a source or destination satisfy the noncrossing rule.
- Once `0 -> n - 1` is represented, the distance is one and all later queries are ineffective.
- Every legal query skips at least one city, so it is not an original chain edge.
- The answer sequence is nonincreasing because roads are never removed.
