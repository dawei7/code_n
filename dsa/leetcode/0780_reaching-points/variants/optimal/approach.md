## General
**Reverse the forced last move**

Forward moves only increase coordinates, so searching outward branches rapidly. In reverse, when `tx > ty`, the last forward move must have increased `tx`; its predecessor is `(tx - ty, ty)`. The symmetric rule applies when `ty > tx`. Thus the reverse path is forced until a source coordinate is reached or a target coordinate drops below it.

**Batch identical subtractions with modulo**

Repeatedly subtracting the smaller coordinate is exactly a Euclidean-algorithm step. While both target coordinates remain strictly above their source bounds, replace the larger one by its remainder modulo the smaller one. This skips all predecessors that differ only by repeated additions of the unchanged coordinate.

**Finish at a source boundary**

If `tx = sx`, no further reverse step may reduce `tx`. The remaining difference `ty - sy` must therefore be a nonnegative multiple of `sx`. The same divisibility test applies when `ty = sy`. If neither coordinate reaches its source value, or a coordinate falls below its source bound, the target is unreachable.

Each reverse step is forced by the larger coordinate, and modulo merely batches consecutive applications of that same forced subtraction. The final divisibility test exactly characterizes the only moves still possible once one coordinate is fixed. Therefore the method accepts precisely the targets having a valid forward sequence.

## Complexity detail
The modulo reductions follow the Euclidean algorithm and take $O(\log(\max(tx, ty)))$ iterations. Only four coordinates are maintained, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **One subtraction per reverse move:** This follows the same forced path but can take linear time in a large coordinate quotient.
- **Forward breadth-first search:** Generating both successors is useful only for tiny bounds because the number and magnitude of points grow quickly.
- **Recursive modulo reduction:** The mathematics is identical, but recursion uses $O(\log(\max(tx, ty)))$ stack space.
- **Target equals source:** Return true immediately.
- **One coordinate already matches:** Use the nonnegative divisibility test instead of applying modulo past the source boundary.
- **Target below source:** Forward moves never decrease a coordinate, so such a target is impossible.
- **Equal target coordinates:** If they are not already the source point, neither could have been produced as the unique larger coordinate of the last move.
