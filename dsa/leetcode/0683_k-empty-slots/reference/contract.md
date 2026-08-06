## Function Contract

`solve(bulbs: list[int], k: int) -> int`

**Inputs**

- `bulbs`: a permutation of the one-based bulb positions. At zero-based index `i`, `bulbs[i]` is the position switched on during day `i + 1`.
- `k`: the exact number of bulbs that must remain off strictly between two bulbs that are on.

**Return value**

Return the earliest one-based day when such a pair of lit endpoints exists. Return `-1` when no day satisfies the condition.
