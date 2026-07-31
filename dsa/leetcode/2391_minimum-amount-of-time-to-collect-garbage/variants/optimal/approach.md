## General

All pickup work is unavoidable and serial, so begin with the total number of characters across `garbage`. For each type, only its farthest occurrence determines driving: its truck must cross every road before that house, and traveling farther would be unnecessary.

Scan the houses to record the final index containing `'M'`, `'P'`, and `'G'`. Separately build prefix travel times, where prefix index `i` is the time needed to drive from house zero to house `i`. Add the three prefix values at the recorded final indices to the pickup count.

This total is a lower bound because every unit must be collected and every truck must reach its farthest required house. It is achievable by sending each truck exactly through that house and stopping, so it is the minimum. The no-concurrency rule means these independently minimal durations are added.

## Complexity detail

Let $n$ be the number of houses and let
$$
S = \sum_{g \in \texttt{garbage}} \lvert g \rvert.
$$
Scanning all units and building travel prefixes takes $O(n+S)$ time. The prefix array uses $O(n)$ space.

## Alternatives and edge cases

- **Running distance only:** Record the current cumulative travel distance whenever a type appears, reducing auxiliary space to $O(1)$.
- **Repeated prefix sums:** Recomputing `sum(travel[:i])` for every house is correct but can take $O(n^2)$ time.
- **Type absent after house zero:** Its travel contribution is zero.
- **Several types at one house:** Each truck pays the route independently because operation is serial.
- **Many units of one type:** Each character adds one pickup minute, but travel to that house is paid once by its truck.
- **Final house:** A type present there forces its truck to traverse every road segment.
