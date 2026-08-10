## General

**View favorites as a functional directed graph**

Each employee has exactly one outgoing edge to their favorite. Every connected component of such a graph contains exactly one directed cycle, with directed trees feeding into its cycle vertices.

The circular seating constraint produces two fundamentally different usable structures:

- one directed cycle of length at least three;
- any number of mutual-favorite cycles of length two, each extended by incoming chains.

The source computes the best value for both categories and returns their maximum.

**Find the longest directed cycle**

`max_cycle` uses a global `vis` array. From each unvisited employee `i`, it follows favorite edges and records the newly visited path in `cycle` until it reaches a globally visited vertex `j`.

If `j` occurs inside the current `cycle` list, the suffix beginning at that occurrence is the new directed cycle. The loop over `cycle` finds `j` and updates with `len(cycle) - k`.

If `j` belongs to an earlier traversal, it does not occur in the current list. No new cycle is counted because the current path merely feeds into a component whose cycle was already handled.

Taking the maximum gives the largest cycle length.

**Why a long cycle cannot accept an incoming chain**

For a directed cycle of length at least three, every invited cycle employee needs their favorite, the next cycle vertex, adjacent. Arranging all directed favorite edges around the circular table consumes the cycle's seating adjacencies.

Inserting a chain employee between two cycle members would separate at least one employee from their favorite. Therefore, the usable invitation based on such a component is exactly the cycle itself.

Only one such long cycle can form the table arrangement, so the relevant value is the maximum cycle length rather than a sum over long cycles.

**Why a two-cycle is special**

If employees `a` and `b` favor each other, seating them together satisfies both using their shared adjacency. Each still has one free side on the circular arrangement.

One longest incoming chain ending at `a` can attach on `a`'s outer side, and one longest chain ending at `b` can attach on `b`'s outer side.

Extended two-cycle segments can be concatenated around the table, so contributions from all disjoint mutual-favorite pairs may be summed.

**Prune trees and propagate longest chain lengths**

`topological_sort` computes indegrees and initializes `dist[i] = 1`, representing a chain containing employee `i` alone.

Employees with indegree zero cannot lie on cycles, so they enter a queue. When pruned employee `i` points to `favorite[i]`, the source updates

`dist[favorite[i]] = max(dist[favorite[i]], dist[i] + 1)`.

This records the longest pruned chain ending at the favorite. It then reduces that favorite's indegree and queues it if it becomes zero.

After pruning stops, only cycle vertices retain positive indegree. Importantly, a two-cycle endpoint is never removed, so its partner's cycle edge is not propagated into its `dist`. Each `dist` contains the endpoint plus only the best external chain feeding it.

**Recognize and sum mutual pairs**

The condition

`i == favorite[favorite[i]]`

means following two favorite edges returns to `i`. Since self-favorites are forbidden, this identifies exactly a two-cycle.

The sum includes both endpoints. For pair `a,b`, it adds `dist[a] + dist[b]`, which is the pair plus the best incoming chain on each side.

Every two-cycle endpoint satisfies the condition, so no extra division is needed: both endpoint chain lengths are intentionally part of the contribution.

**Why the final maximum is correct**

Any valid circular invitation in a functional graph must be based either on one directed cycle of length at least three or on mutual pairs extended by chains.

The first helper finds the best cycle category. The second helper finds the total size attainable by joining every extended two-cycle segment. These categories cannot be combined into one larger circular arrangement without breaking cycle adjacencies.

Taking `max` returns the global optimum.

## Complexity detail

Let $n$ be the number of employees.

Cycle traversal visits each employee once. Topological pruning processes each vertex and its single outgoing edge once. The final pair scan is linear. Total time is $O(n)$.

Visited, indegree, distance, queue, and temporary traversal lists use $O(n)$ space.

## Alternatives and edge cases

- **Brute-force seating subsets:** Exponential and unnecessary once functional-graph structure is recognized.
- **Count only the longest cycle:** This misses the ability to combine multiple extended two-cycles.
- **Sum all cycles:** Long cycles cannot be concatenated while preserving every directed favorite adjacency.
- **Use every incoming branch:** Only one chain can attach to each free side of a two-cycle endpoint; `max` propagation keeps the longest.
- **Pure cycle of length three or more:** Its cycle length is the full contribution.
- **Single mutual pair:** Contribution is at least two and may include two chains.
- **Several mutual pairs:** Their extended segments are summed.
- **Path entering an old component:** `max_cycle` does not recount its already discovered cycle.
- **Self-favorites absent:** Makes the two-step return test identify only genuine pairs.
- **Distance initialization:** One counts the endpoint employee itself.
- **Topological leftovers:** They are exactly cycle vertices in a functional graph.
- **Input preservation:** Favorite edges are read but not changed.
