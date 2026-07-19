## General
**Bound the capacity answer:** The ship must hold the heaviest individual package, so `max(weights)` is the smallest candidate. Capacity $S$ ships everything in one day and is always feasible, giving an inclusive search interval containing the optimum.

**Test one capacity greedily:** Scan packages in order, adding each weight to the current day's load. If the next package would exceed `capacity`, begin a new day with that package. This greedy choice packs every day as fully as the fixed order permits, so no other schedule with the same capacity can use fewer days.

**Binary-search the feasibility transition:** If a capacity succeeds, every larger capacity also succeeds; if it fails, every smaller capacity fails. Test the midpoint, retaining the lower half when feasible and the upper half otherwise. When the bounds meet, that value is the least feasible capacity.

The greedy test exactly determines whether a candidate can meet the deadline, and feasibility is monotone in capacity. Binary search therefore discards only values that cannot be the minimum and terminates at the requested optimum.

## Complexity detail
Computing the bounds costs $O(N)$. Each feasibility test scans at most $N$ weights, and binary search performs $O(\log S)$ tests, for $O(N\log S)$ total time. The bounds, counters, and current load use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Try every capacity:** Testing integers from `max(weights)` upward is correct but can require $O(NS)$ time.
- **Dynamic programming over day boundaries:** It can represent all partitions but uses substantially more time and space than monotone answer search.
- **One day:** The capacity must equal $S$.
- **One day per package:** The minimum capacity is `max(weights)`.
- **Order constraint:** A feasible schedule partitions the array into contiguous groups; arbitrary redistribution between days is invalid.
