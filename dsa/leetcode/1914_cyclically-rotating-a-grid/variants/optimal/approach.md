## General
**Describe one layer in movement order**

For layer `d`, its boundaries are `top = left = d`, `bottom = R - 1 - d`, and `right = C - 1 - d`. Enumerate its coordinates in the direction a value moves under a counter-clockwise rotation:

1. down the left edge, including both corners;
2. right across the bottom edge, excluding the repeated left corner;
3. up the right edge, excluding the repeated bottom corner;
4. left across the top edge, excluding both repeated corners.

Every border cell appears exactly once. Because both dimensions are even, there are $\min(R,C)/2$ complete rectangular layers and no unlayered center row or column.

**Map directly to the final position**

If a layer contains $P$ coordinates, only `k % P` matters. A value at coordinate-list index `i` moves to index `(i + k) % P`, since the list follows the counter-clockwise movement direction. Write each source value directly into that target coordinate of a copied result matrix.

Each layer is disjoint, so these writes cannot conflict. Within a layer, adding a fixed offset modulo $P$ is a permutation: every source reaches one target and every target receives one source. It therefore produces exactly the same arrangement as applying the one-step cyclic move `k` times.

## Complexity detail
Across all layers, the coordinate lists contain exactly the $RC$ matrix cells. Building the lists and writing the shifted values takes $O(RC)$ time, independent of the magnitude of `k`. The copied result and layer coordinates use $O(RC)$ auxiliary space in the worst case.

## Alternatives and edge cases
- **Simulate one rotation at a time:** Moving every perimeter once for each of `k` steps is direct but can take $O(kRC)$ time and is infeasible when $k$ is large.
- **In-place cycle decomposition:** Following permutation cycles can reduce auxiliary storage, but careful visited-state and corner handling make it more error-prone.
- **Perimeter multiple:** If `k % P == 0`, that layer remains unchanged even though other layers may move.
- **Two-row or two-column grid:** The grid has one thin layer; corner exclusion is essential to avoid duplicate coordinates.
- **Different layer perimeters:** Reduce `k` separately for every layer.
- **Repeated values:** Equal values do not change the coordinate mapping and may make a rotation visually indistinguishable.
