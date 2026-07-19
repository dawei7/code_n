## General
**Store one total per active player.** A hash map from player ID to accumulated score makes `addScore` a direct addition and `reset` a direct deletion. Resetting truly removes the entry, so a later addition naturally begins from zero.

**Select only the requested leaders.** For `top(K)`, use a size-$K$ selection heap through `nlargest` rather than sorting all scores. The heap retains the best $K$ values seen so far; summing those values gives exactly the requested total. Equal scores occupy separate heap entries because they belong to separate players.

**Replay the app operation trace.** Construct one leaderboard and invoke each method in order, appending its result. This preserves state across calls while keeping the native class interface intact beside the app-local `solve(operations)` adapter.

## Complexity detail
`addScore` and `reset` take expected $O(1)$ time. With $p$ active players, `top(K)` examines all scores and maintains a heap of at most $K$, taking $O(p\log K)$ time. The score map plus selection heap use $O(p)$ space overall.

## Alternatives and edge cases
- **Sort every score for each `top`:** It is correct but takes $O(p\log p)$ even when $K$ is small.
- **Repeated linear maximum selection:** Selecting one unused leader at a time takes $O(Kp)$ time.
- **Always-sorted score list:** `top` becomes fast, but every score addition or reset requires locating and updating an ordered entry.
- **Score buckets:** Bounded scores can support frequency trees, but accumulated totals and implementation complexity make a heap selection simpler here.
- **Repeated addition:** Add to the current total rather than replacing it.
- **Tied scores:** Each tied active player counts separately toward $K$.
- **Reset then add:** The new total contains only scores added after the reset.
