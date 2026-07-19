## General
**Compress clips by start time:** Build `farthest_from_start`, where each integer start stores the greatest endpoint among clips beginning there. Shorter clips with the same start can never improve a minimum solution.

**Treat coverage like minimum jumps:** Scan integer positions from `0` toward `T`. Maintain `farthest`, the greatest endpoint offered by any clip whose start has been scanned, and `current_end`, the endpoint reachable with the clips already committed.

**Commit only when existing coverage ends:** When the scan reaches `current_end`, choose one clip implicitly by extending `current_end` to `farthest`. This is the clip among all currently available choices that reaches farthest. If `farthest` does not pass the current position, a coverage gap makes the task impossible.

Choosing a shorter reachable endpoint can never expose a clip earlier than choosing the farthest endpoint, so the greedy extension cannot use more future clips than another feasible choice. Repeating this exchange argument at each committed boundary yields the minimum clip count.

## Complexity detail
Compressing the $N$ clips costs $O(N)$, and scanning the $T$ integer positions costs $O(T)$, for $O(N+T)$ time. The farthest-end array has $T+1$ entries and uses $O(T)$ space.

## Alternatives and edge cases
- **Sort intervals:** Sorting by start and greedily extending coverage takes $O(N\log N)$ time and is useful without bounded integer endpoints.
- **Dynamic programming:** Computing the minimum clips for every time from every interval costs $O(NT)$ time.
- **Gap at zero:** If no clip starting at zero extends coverage, return `-1`.
- **One covering clip:** A clip spanning `[0, T]` gives answer one even when many redundant clips exist.
- **Clips beyond time:** Endpoints past `T` are useful and may finish coverage immediately.
