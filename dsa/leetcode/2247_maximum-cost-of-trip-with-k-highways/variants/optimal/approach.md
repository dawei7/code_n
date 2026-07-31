## General

**Reject impossible path lengths**

A trip crossing `k` highways visits `k + 1` distinct cities. If `k >= n`,
that many distinct cities do not exist, so return `-1` immediately.

**Identify equivalent partial trips**

For a feasible length, represent the visited cities by a bitmask and record
the current endpoint. Two partial trips with the same `(mask, city)` state
have exactly the same legal continuations: either may next take an incident
highway to a city whose bit is absent. Only the greater accumulated cost can
matter, so retain that maximum and discard the dominated trip.

Initialize one zero-cost state at every possible starting city. For each of
the `k` required crossings, extend every current state along each incident
highway to an unvisited neighbor. Store the best cost for each resulting state
in a fresh layer. Using separate layers guarantees that every retained state
has crossed exactly the current number of highways.

After `k` extensions, the greatest state value is the best valid trip. If a
layer becomes empty, no exact-length trip exists and the answer is `-1`.
Every constructed state describes a simple path, and every legal trip follows
one sequence of these transitions, so the dynamic program is complete.

## Complexity detail

There are at most $2^n n$ mask-and-endpoint states. A state may inspect
$O(n)$ neighbors, giving $O(2^n n^2)$ worst-case time. At most two layers of
state values and the adjacency lists are stored, bounded by $O(2^n n)$ space.

## Alternatives and edge cases

- **Enumerate every simple path:** Depth-first search is correct but can explore a factorial number of city orders in a dense graph.
- **Track only endpoint and step count:** Different visited sets permit different future cities, so merging them can allow repeats or discard the optimum.
- **Keep the first cost per state:** A later partial trip can reach the same state with a larger toll sum and must replace the earlier value.
- **Use at most `k` highways:** The contract requires exactly `k`; shorter high-cost paths are not candidates.
- **`k >= n`:** A simple path would require more cities than exist, so return `-1`.
- **Disconnected graph:** Starting is allowed in any component, but one component must contain a path of the exact length.
- **Zero tolls:** A valid trip costing `0` is distinct from impossibility and must return `0`, not `-1`.
- **Undirected highways:** Add every highway to both endpoint adjacency lists.
