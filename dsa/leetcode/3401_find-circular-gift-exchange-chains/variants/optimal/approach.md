## General

Treat `SecretSanta` as a directed graph. Under the valid circular-chain input, every employee has one outgoing edge and one incoming edge, so each connected component is a directed cycle. The edge carries `gift_value`.

Seed a recursive CTE with every exchange. A state remembers its original `start_id`, the employee reached by the latest edge as `current_id`, the accumulated gift value, and the number of traversed edges. While `current_id` differs from `start_id`, join the current employee to the row where that employee is the giver and extend the state by one edge.

When `current_id = start_id`, the traversal has closed exactly one cycle. Starting from each employee in that cycle produces the same `chain_length` and `total_gift_value`, so select those two columns with `DISTINCT`. This also matches the verified platform behavior when separate cycles share both statistics: their identical output pair appears once.

Sort the remaining statistic pairs by decreasing length and then decreasing value. `ROW_NUMBER()` over that same order assigns the required one-based `chain_id`; repeating the order in the outer query makes the presentation deterministic.

Each seed follows exactly its own cycle and stops at its first return to the seed. Thus every emitted closed state contains every edge of that cycle once, so both aggregates are exact. Every cycle has at least one seed and therefore contributes its statistic pair before deduplication.

## Complexity detail

Let $e$ be the number of exchanges. There are $e$ starting states, and a state can traverse at most $e$ edges before closing. With indexed lookup by `giver_id`, the recursive stage creates $O(e^2)$ states and takes $O(e^2)$ time. Materializing those states uses $O(e^2)$ working space; deduplication and ordering do not exceed that bound.

The benchmark defines `size` as $e$ and uses one cycle of 8, 32, and 128 exchanges, spanning 16x. The accepted query follows indexed edges while storing constant-size state per recursive row. A correct slower baseline carries a growing delimited path and scans that path for membership at every step, adding one factor of path length and failing only the scaling verdict.

## Alternatives and edge cases

- **Carry a visited path:** A delimited string or JSON array can prevent revisiting arbitrary nodes, but valid input already consists of cycles; scanning that growing path makes the recursion unnecessarily cubic.
- **Start from one guessed employee:** This finds only that employee's cycle and misses every disconnected exchange chain.
- **Emit every starting employee:** Without deduplication, a cycle of length $k$ appears $k$ times because each member can be its seed.
- **Deduplicate by employees:** The requested output has no member-list column. The verified judge identifies output rows by `(chain_length, total_gift_value)`, including its collapse of separate equal-statistic cycles.
- **Stop before adding the closing edge:** The edge returning to `start_id` belongs to the loop and must contribute to both length and total value.
- **Two-person chain:** Each directed gift is a separate edge, so the chain length is two.
- **Equal lengths:** Break ties by `total_gift_value` descending before assigning `chain_id`.
- **Deterministic output:** The window order assigns ids, but the final `ORDER BY` is still required to guarantee row presentation.
