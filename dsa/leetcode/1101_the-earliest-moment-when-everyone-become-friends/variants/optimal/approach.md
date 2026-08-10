## General

**Process friendship events chronologically**

Acquaintance can only grow as friendships are added. The earliest moment when everyone is connected must therefore be found while replaying events in timestamp order. `sorted(logs)` sorts each three-element row lexicographically; because timestamps are the first field and are unique, this is exactly chronological order.

At any chronological prefix, acquaintance groups are connected components of an undirected graph. A disjoint-set union structure tracks these components without explicitly traversing the graph after every event.

**Represent each component by a root**

`p = list(range(n))` initially makes every person their own parent, representing $n$ singleton components. `find(x)` follows parent links to the root. Its recursive assignment `p[x] = find(p[x])` applies path compression, making every visited node point directly to the root so later queries are faster.

For event `t, x, y`, equal roots mean the people are already acquainted through existing friendships. Adding their direct edge does not merge components, so the algorithm continues without changing the count.

Different roots mean the event connects two previously separate groups. `p[find(x)] = find(y)` attaches the first root to the second. The local variable `n` is then decremented; after initialization it serves as the number of current components rather than merely the original population size.

**Return on the first transition to one component**

Every successful union reduces the component count by exactly one. Redundant edges leave it unchanged. When the count reaches one, all people share a root and are mutually acquainted through friendship chains.

Because events are processed chronologically, this is the first timestamp whose prefix is connected. Returning immediately gives the earliest possible answer. If all logs are exhausted while more than one component remains, no later provided friendship exists to connect them, so `-1` is correct.

**Why connectivity matches acquaintance**

Direct friendship is an undirected edge. The definition of acquaintance is transitive through friends, which is exactly graph reachability. DSU places two people in one set exactly when processed edges provide a path between them. Therefore, the component count reaches one exactly when every person is acquainted with every other person.

The monotonic nature of the process is equally important. Friendships are never removed, so two components that have merged can never separate at a later timestamp. Once the count reaches one, it stays one forever. That is why a single forward chronological pass can return immediately; it does not need to compare the successful timestamp with any future state.

## Complexity detail

Let $m$ be the number of logs. Creating parents costs $O(n)$, and sorting costs $O(m\log m)$ time and $O(m)$ storage for Python’s sorted result. Each event performs a constant number of `find` operations and at most one union.

The manifest states $O(n + m\log m + m\alpha(n))$ time, the standard bound for DSU with path compression and rank or size balancing. The exact code uses path compression but no rank or size heuristic. It remains efficient for the constraints, but the formal inverse-Ackermann guarantee normally assumes both techniques; a conservative bound for path compression alone is weaker. Adding union by rank would align the implementation directly with the manifest.

The calls to `find` are repeated after the root-equality test when a union is needed. Path compression makes these repetitions cheap, and storing the two roots would be a constant-factor optimization rather than an algorithmic change.

Parents use $O(n)$ space, and the sorted log copy uses $O(m)$, for $O(m+n)$ total auxiliary space. Recursive `find` can use stack proportional to a temporarily tall parent chain, though compression shortens paths after access.

## Alternatives and edge cases

- **DSU with rank or size:** Attach the smaller tree under the larger root. Combined with path compression, this supplies the standard $O(\alpha(n))$ amortized operation bound.
- **Graph traversal after every event:** Add edges and run BFS or DFS to test connectivity. Repeating a full traversal can be much more expensive than maintaining components incrementally.
- **Binary search over timestamps:** Test connectivity for prefixes and binary-search the first successful prefix. Each test rebuilds a graph or DSU, so the one-pass chronological method is simpler and faster.
- **Logs already sorted:** The explicit sort still preserves the order; asymptotically it remains the dominant general step.
- **Redundant friendship:** Equal roots cause no component decrement, preventing a false early answer.
- **Unique timestamps:** Returning an event timestamp is unambiguous. If timestamps tied, all simultaneous events might need batch processing depending on semantics.
- **Disconnected final graph:** The component count remains above one and the result is `-1`.
- **Connection on the last log:** The post-union check returns that final timestamp.
- **Long acquaintance chain:** DSU connectivity naturally handles transitive friendship even when two people never share a direct edge.
- **Variable reuse:** After parent initialization, local `n` is intentionally a component counter. Code changes must not later treat it as an immutable population length.
- **Recursive find depth:** Union by rank would also protect against tall intermediate trees and recursion concerns.
