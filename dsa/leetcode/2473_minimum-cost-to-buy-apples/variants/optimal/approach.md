## General

**Turn a round trip into one weighted distance.** In an undirected graph, the cheapest route from a start $u$ to a purchase city $v$ has the same distance in either direction. If that distance is $d(u,v)$, outward travel costs $d(u,v)$ and the return costs $k d(u,v)$. Buying in $v$ therefore costs

$$
\texttt{appleCost}[v] + (k + 1)d(u,v).
$$

The answer for $u$ is the minimum of this expression over every possible purchase city $v$.

**Make every city a Dijkstra source.** Multiply every road weight by `k + 1`, initialize city $v$ with tentative distance `appleCost[v]`, and put all cities in one min-heap. This is equivalent to adding a virtual source with an edge of weight `appleCost[v]` to every city $v$, then running a single Dijkstra search. A path from the virtual source through $v$ to $u$ represents buying in $v$ and paying the combined outward-and-return travel cost to start $u$.

All edge weights are positive, so when a city is removed from the heap with its current best value, that value is final. Relaxing each road in both directions propagates the best purchase choice across the graph. Disconnected components need no special treatment because every city begins as a source and each component independently retains at least its local apple prices.

## Complexity detail

Let $m = \lvert\texttt{roads}\rvert$. Building the adjacency list takes $O(n + m)$ space and time. Multi-source Dijkstra processes $O(n)$ heap states and $O(m)$ edge relaxations, each with an $O(\log n)$ heap operation, for $O((n + m)\log n)$ time and $O(n + m)$ auxiliary space.

## Alternatives and edge cases

- **Dijkstra from every starting city:** Computing all distances independently and then choosing an apple source is correct but costs $O(n(n + m)\log n)$ time.
- **Floyd-Warshall:** All-pairs shortest paths make the final minimization easy, but $O(n^3)$ time and $O(n^2)$ space are excessive for $n = 1000$.
- **Buying locally:** Each city is initialized with its own apple price, so the zero-travel choice is always considered.
- **Disconnected roads:** A start can only benefit from apple sources in its own connected component; multi-source relaxation respects that automatically.
- **Return multiplier:** The transformed road factor is `k + 1`, not `k`, because the normal-cost outward trip must also be paid.
