## General

Let $q$ be the number of road-addition queries.

**Maintain the cumulative directed graph**

Create an adjacency list containing every initial road $i \to i+1$. For each query `[u, v]`, append `v` to the outgoing roads of `u`. No road is removed, so this one graph exactly represents all additions processed so far.

**Recompute the shortest path with BFS**

Every road has length one. Breadth-first search from city $0$ therefore visits cities in nondecreasing path length. Initialize its distance to zero, mark all other cities unvisited, and assign a neighbor the current distance plus one the first time it is reached. The first assigned distance of every city is minimal in an unweighted directed graph.

After the queue is exhausted, the stored distance of city $n-1$ is the answer for the current query. The original chain is always present, so that destination remains reachable. Repeating this traversal after each cumulative addition produces the requested sequence; a newly added road may reduce the distance or leave it unchanged, but can never increase it.

## Complexity detail

After $k$ additions, the graph has $n-1+k$ roads, and BFS takes $O(n+k)$ time. Summing over all $q$ queries gives

$$
O\left(\sum_{k=1}^{q}(n+k)\right)=O(q(n+q)).
$$

The adjacency list holds $O(n+q)$ roads and the BFS queue and distance array hold $O(n)$ entries, for $O(n+q)$ space.

## Alternatives and edge cases

- **Recompute all-pairs shortest paths:** Floyd-Warshall after every addition is correct but spends $O(qn^3)$ time on distances unrelated to the required source and destination.
- **Enumerate directed paths:** The graph is acyclic because every road points forward, but the number of distinct paths can still grow exponentially.
- **Incremental distance propagation:** Relaxing only nodes affected by the new road can avoid some repeated work, but requires more careful update bookkeeping; the stated limits make full BFS direct and reliable.
- A road may not improve the current shortest path because its source is expensive to reach or an even shorter route already exists.
- Once a direct road `0 -> n - 1` is added, every later answer remains one.
- The output sequence is nonincreasing because roads are only added.
- Direction matters: an added road can be used only from `u` to `v`.
- A query skips at least one city, so it never duplicates an initial chain road.
- Overlapping and nested shortcuts are allowed and may combine into a route shorter than either shortcut alone.
