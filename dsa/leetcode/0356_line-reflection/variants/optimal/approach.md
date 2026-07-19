## General
**Derive the only possible reflection axis**

If a vertical symmetry line exists, it is forced by the extreme horizontal coordinates. The leftmost and rightmost points must reflect to each other, so the axis is halfway between `min_x` and `max_x`.

**Verify partners without fractional arithmetic**

Avoid storing that midpoint as a possibly fractional number. Let `axis_sum = min_x + max_x`, which equals twice the axis coordinate. Reflecting `(x, y)` produces `(axis_sum - x, y)`. Put all point pairs into a hash set and verify that this reflected pair exists for every input point.

**Why one missing partner disproves symmetry**

The extreme-coordinate argument proves there is no other candidate line to try. If every reflected pair exists under the forced axis, reflection maps the point set onto itself and symmetry holds. If any pair is missing, that point cannot be matched under the only possible axis, so no vertical reflection line exists.

**Trace a point on the axis**

For `[[0,0],[2,0],[1,1]]`, the extreme sum is `2`, representing axis $x = 1$. The first two points exchange, while `(1,1)` maps to itself because it lies on the axis.

## Complexity detail
Finding the extremes, building the set, and checking all reflected points each take $O(n)$ expected time. The point set uses $O(n)$ space. Integer addition and subtraction avoid floating-point precision concerns.

## Alternatives and edge cases
- **Sort each row's points:** can compare outer pairs in $O(n \log n)$ time after grouping by vertical coordinate.
- **Linear partner search:** degrades to $O(n^2)$ when every reflected point is sought in the original list.
- **Validate rows independently:** works only if every row is also required to share the same global reflection axis.
- A point on the reflection line maps to itself.
- Duplicate coordinate entries do not change the geometric point set.
- Negative coordinates and half-integer axes are handled by `axis_sum` without division.
