## General
**Sort points into sweep order**

Order coordinates lexicographically by `x` and then `y`. This provides the left-to-right order needed to construct the lower and upper portions of the convex boundary.

**Use cross products to recognize a wrong turn**

For consecutive candidate points `a`, `b`, and new point `c`, the signed cross product $(b - a) \cdot (c - a)$ indicates orientation. While building the lower chain, a negative value is a clockwise turn and proves that `b` lies above the required lower boundary, so remove it. Applying the same rule to the reversed point order constructs the upper chain.

**Preserve collinear boundary trees**

Pop only for a strictly negative cross product. A zero cross product represents collinear points and must remain so every tree lying along a straight fence edge is returned. This strictness is the key difference from a hull that keeps only corner vertices.

**Combine and deduplicate both chains**

The lower and upper sweeps share endpoints, and an all-collinear input places points on both chains. Combine the chains through a set of coordinate pairs, then convert them back to the requested list representation.

**Why the chains form exactly the fence**

After each sweep step, removing clockwise turns leaves a chain that never bends into the interior relative to its side of the hull. Any removed point lies strictly inside the convex region bounded by neighboring candidates and cannot be a boundary point. Non-clockwise turns retain all extreme vertices and collinear edge points. The lower and upper chains together surround every input point, so their union is precisely the complete convex boundary.

## Complexity detail
Sorting `n` points costs $O(n \log n)$ time. Each point is pushed and popped at most once per chain, so both sweeps are linear after sorting. The chains and deduplication set use $O(n)$ space.

## Alternatives and edge cases
- **Graham scan:** also sorts by angle and builds a hull, but collinear-angle handling must deliberately retain every boundary point.
- **Jarvis march:** takes $O(nh)$ time for `h` hull points and can be useful when the hull is very small.
- **Test every supporting line:** is conceptually direct but checking all point pairs against all other points takes $O(n^3)$ time.
- **Pop on a nonpositive cross product:** incorrectly removes collinear trees along fence edges.
- **All points collinear:** every point belongs to the boundary.
- **One or two points:** every input point is on the fence.
- **Repeated chain endpoints:** deduplicate when joining lower and upper chains.
- **Interior points:** are removed by at least one strict turn and do not appear in the result.
- **Output order:** is unrestricted and should be validated by membership.
