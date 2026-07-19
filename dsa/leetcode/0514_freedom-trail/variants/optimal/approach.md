## General
**Represent the best cost at every ring position**

Let `cost[position]` be the minimum rotation cost after spelling the processed key prefix and leaving that ring position at the selector. Initially only position `0` is reachable with cost zero. Button presses are identical for every complete solution, so add `abs(key)` once after minimizing rotations.

**Apply a circular distance transform**

For the next key character, every target position needs
`min(source_cost + circular_distance(source, target))` over all current positions. Duplicate the cost array to length `2n`. A left-to-right pass relaxes movement from the left, and a right-to-left pass relaxes movement from the right. Repeated sources in the second copy model crossing the ring boundary, so the minimum of transformed positions `target` and `target + n` is the best circular arrival cost.

**Keep only positions bearing the required character**

After the transform, set every nonmatching position back to infinity. Matching positions become exactly the possible states after selecting the current key character. Repeating this for every character preserves all choices between duplicate letters without enumerating every source-target pair.

**Why the transform is exact**

On a line, the two directional passes compute the minimum initial cost plus absolute distance from any source. In the duplicated ring, a source appears at both `source` and `source + n`; reaching either copy of a target therefore considers both clockwise and counterclockwise wrap distances. Filtering changes no path cost—it only enforces that the selected position contains the required character. Induction over the key prefix gives the minimum rotation cost for every valid ending position.

## Complexity detail
For each of `abs(key)` characters, two passes over `2 * abs(ring)` entries and one filter take $O(|ring|)$ time. The two cost arrays use $O(|ring|)$ space. Adding button presses is constant time.

## Alternatives and edge cases
- **Occurrence-to-occurrence dynamic programming:** is straightforward but can take $O(|key| \cdot |ring|^2)$ time when a character appears everywhere.
- **Memoized depth-first search:** uses states `(key_index, ring_position)` and tries every matching occurrence, with the same quadratic transition factor.
- **Dijkstra on layered ring states:** is correct but introduces heap overhead for a graph whose cycle distances admit linear transforms.
- **One-character ring:** requires no rotation, only one press per key character.
- **Repeated target character:** staying at the current matching position may cost zero rotation.
- **Duplicate letters:** all occurrences must remain candidates because a locally farther choice can help later characters.
- **Wraparound:** distance between indices is $\min(\left\lvert a - b \right\rvert, n - \left\lvert a - b \right\rvert)$.
