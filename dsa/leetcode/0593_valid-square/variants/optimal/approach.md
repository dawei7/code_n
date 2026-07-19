## General
**Ignore input order by examining every pair**

Four points determine exactly six pairwise distances. Compute squared Euclidean distances so all arithmetic remains integral and no square roots or floating-point comparisons are needed.

**Recognize the square distance pattern**

A nondegenerate square has four equal positive side lengths and two equal diagonals. By the Pythagorean theorem, each squared diagonal equals twice a squared side. Sort the six values and test that the first four are one positive value, the last two are equal, and the diagonal value is twice the side value.

**Why this pattern is sufficient**

The four equal shortest distances give every vertex degree two in the side graph; a triangle among three vertices would force the remaining pair distances to violate the two-equal-diagonals pattern. The four equal edges therefore form a cycle. Equal diagonals whose squared length is twice the edge length make adjacent side vectors perpendicular, so that cycle is a square. A positive shortest distance also rules out coincident points.

## Complexity detail
There are always exactly four points and six distances. Computing and sorting this fixed-size collection takes $O(1)$ time and $O(1)$ space under the standard fixed-width integer model.

## Alternatives and edge cases
- **Choose one vertex and compare vectors:** identify its two nearest points, verify equal lengths and zero dot product, then repeat or confirm the opposite vertex; this is also constant time.
- **Test all point permutations:** checking the side and diagonal pattern for 24 orders is constant but more error-prone.
- **Compute squares by repeated addition:** remains correct for integer coordinates but takes time proportional to coordinate differences instead of constant arithmetic operations.
- **Use square roots:** introduces unnecessary floating-point precision concerns.
- **Coincident points:** create a zero distance and must be rejected.
- **Rectangle that is not a square:** has unequal side lengths.
- **Rhombus that is not a square:** has unequal diagonals.
- **Rotated square:** has the same squared-distance multiset and qualifies.
- **Arbitrary input order:** does not affect the sorted distances.
- **Negative coordinates:** squared differences work unchanged.
