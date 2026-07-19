## General
**Restrict the search to the tower bounding box.** Let `maximum_x` and `maximum_y` be the greatest tower coordinates. Consider an integral point beyond either upper bound. Projecting that coordinate back to the corresponding boundary cannot increase its distance to any tower, so no tower contribution decreases. Repeating for both axes gives a point inside `[0, maximum_x] × [0, maximum_y]` with at least as much quality and a lexicographically no-larger coordinate. Thus an optimal answer exists inside this box.

**Evaluate every legal candidate exactly.** Scan `x` from 0 through `maximum_x`, and for each `x`, scan `y` from 0 through `maximum_y`. For every tower, compute the squared distance first. If it exceeds `radius * radius`, skip the tower; otherwise take the square root, apply the floor formula, and add the contribution.

**Let scan order enforce the tie rule.** The nested increasing loops visit coordinates in lexicographic order. Replace the saved coordinate only when the new quality is strictly greater. The first coordinate attaining any quality is therefore retained across ties. Since every coordinate in the sufficient bounding box is evaluated and its quality is exact, the final saved point is the required lexicographically smallest maximizer.

## Complexity detail
The source contract fixes both coordinates to 0 through 50, so at most $51^2=2601$ candidates exist. Each candidate inspects all $T$ towers, for at most $2601T$ contribution checks, which is $O(T)$ under the fixed legal coordinate domain. Only scalar accumulators and the two-coordinate answer are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Accumulate around each tower:** Visit every grid point within each tower's radius and add its contribution to a table. This is also bounded but uses $O(51^2)$ storage.
- **Scan the full 51×51 grid:** This avoids the bounding-box proof and has the same contract-level asymptotic bound, but performs unnecessary work when towers occupy a small region.
- A tower exactly `radius` units away is reachable because the distance boundary is inclusive.
- A zero-quality tower never increases any coordinate's total, but it still satisfies the input contract.
- When every total is zero, increasing scan order correctly returns `[0,0]`.
- Flooring is applied to each tower contribution before the contributions are summed.
- Multiple towers may share a coordinate; each contributes independently.
