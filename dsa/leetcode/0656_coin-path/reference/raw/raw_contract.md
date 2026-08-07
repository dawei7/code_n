## Function Contract

`solve(coins: list[int], maxJump: int) -> list[int]`

**Inputs**

- `coins`: visit costs in source position order; `coins[0]` represents source index `1`, and `-1` marks a position that cannot be visited.
- `maxJump`: the inclusive maximum number of positions one forward jump may cross.

The path starts at source index `1` and must end at source index `n`. Each jump advances by at least one and at most `maxJump`. The total cost includes every visited position, including the start and destination. The first position is guaranteed to be valid, but the destination may be blocked or otherwise unreachable.

**Return value**

Return the one-based indices of the lexicographically smallest minimum-cost path. Return `[]` when no valid path reaches index `n`.
