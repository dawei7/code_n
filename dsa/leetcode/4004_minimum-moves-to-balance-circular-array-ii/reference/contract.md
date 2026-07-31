## Function Contract

**Inputs**

- `balance`: An integer array of length $n$ containing the initial net balance of each person in circular order.

Each move transfers exactly one unit across one edge of the circle. Indices are interpreted modulo $n$, so the left neighbor of index `0` is index `n - 1`, and the right neighbor of index `n - 1` is index `0`.

**Return value**

Return the minimum number of unit transfers needed to make every entry non-negative. Return `-1` when no sequence of moves can do so.
