## General

The four input points arrive in arbitrary order, so the solution cannot assume which pairs are sides and which are diagonals. Instead of sorting points or trying every cyclic ordering, it tests a property that is independent of order:

> Every choice of three vertices from a square forms a nondegenerate right isosceles triangle.

There are exactly four triples among four points—one triple obtained by omitting each point. The outer return calls `check` on all four.

**Squared distances avoid square roots**

For three points $a$, $b$, and $c$, the helper computes:

$$
d_1=\lVert a-b\rVert^2,\qquad
d_2=\lVert a-c\rVert^2,\qquad
d_3=\lVert b-c\rVert^2.
$$

For coordinates, squared distance is

$$
(x_1-x_2)^2+(y_1-y_2)^2.
$$

Taking square roots is unnecessary. Equal lengths have equal squared lengths, and the Pythagorean relation for a right triangle is already written in squared form. Integer arithmetic is exact and avoids floating-point rounding.

**Recognizing a right isosceles triangle without knowing the right vertex**

In a right isosceles triangle, the two legs have equal positive length, and the hypotenuse’s squared length is the sum of the two squared leg lengths. The right angle could be at any of the three input points, so `check` considers three cases:

- `d1 == d2 and d1 + d2 == d3`: edges from $a$ to $b$ and $a$ to $c$ are equal legs;
- `d2 == d3 and d2 + d3 == d1`: edges meeting at $c$ are equal legs;
- `d1 == d3 and d1 + d3 == d2`: edges meeting at $b$ are equal legs.

Each case also ends with the common squared leg value, such as `and d1`. In Python, zero is false and a positive integer is true. This rejects coincident points and zero-length “sides.” `any(...)` converts the truthiness of the three candidate expressions into one Boolean result.

For ordinary clarity, `and d1 != 0` would express the same nondegeneracy condition more explicitly. The exact code’s shorter form is valid.

**Why a square makes every check pass**

Choose any three vertices of a square. One of them is the corner where two square sides meet; those two sides have equal positive length and form a right angle. The remaining connection joins opposite corners of that three-vertex selection and is a square diagonal. Its squared length is twice a side’s squared length. Thus, one of `check`’s three arrangements succeeds.

Omitting each of the square’s four vertices still leaves such a triangle, so all four helper calls return true.

**Why requiring all four triples rules out other shapes**

A single right isosceles triangle is not enough; many possible fourth points would not form a square. The conjunction forces the fourth point to complete the same distance pattern consistently.

Take any passing triple and scale/rotate coordinates conceptually so its right-angle vertex is at $(0,0)$ and its two equal-leg vertices are at $(s,0)$ and $(0,s)$ for nonzero $s$. For each of the three triples involving the fourth point to also be right isosceles, the fourth point must lie at $(s,s)$; other candidates either make unequal legs, violate the Pythagorean equality, or duplicate a point. These four coordinates are exactly a square.

Equivalently, across all six pairwise distances, the conditions force four equal positive smaller squared distances (the sides) and two equal squared distances twice as large (the diagonals). That is the complete distance signature of a square.

**Tracing the first example**

The points `[0,0]`, `[1,1]`, `[1,0]`, and `[0,1]` are not supplied around the perimeter. Consider the first three. Their squared distances are 2, 1, and 1. The helper recognizes the two ones as equal legs and $1+1=2$ as the diagonal relation. Every other triple has the same multiset `{1,1,2}`, so all checks pass.

For `[0,12]` replacing `[0,1]`, triples involving that point have incompatible distances, so at least one helper returns false and the conjunction rejects the shape.

**Why the algorithm is correct**

If the input forms a square, every three-vertex subset is a nondegenerate right isosceles triangle, so all four checks pass. Conversely, if all checks pass, any first passing triple establishes two perpendicular equal-length directions. The requirements on all remaining triples force the fourth point to be the opposite corner along those directions. Therefore, the points form a square. The helper’s positive-leg test also ensures the square has nonzero area.

The argument is invariant under translation, rotation, reflection, and input order because it uses only pairwise squared distances.

## Complexity detail

There are always exactly four points, four helper calls, three distance calculations per call, and a fixed number of comparisons. Therefore, time is $O(1)$.

The helper stores a fixed number of coordinate components and squared distances. There are no input-sized collections, recursion, or sorting, so auxiliary space is $O(1)$.

Coordinate differences are at most 20000, so squared sums fit comfortably within typical 32-bit signed range up to $8\cdot10^8$. Python integers would remain exact even beyond that.

## Alternatives and edge cases

- **Sort the four points:** Lexicographic order gives a known side/diagonal arrangement that can be checked. Sorting four items is still $O(1)$, but the geometric indexing proof is less immediately obvious.
- **Six-distance multiset:** Compute all pairwise squared distances. A square has four equal positive small values and two equal values twice as large. This is often the simplest order-independent alternative.
- **Three possible vertex cycles:** Fix one point and explicitly test the three ways to pair the remaining points as adjacent/opposite. Constant work, but more arrangement-oriented.
- **Vector dot products:** Choose a candidate corner and require two equal nonzero adjacent vectors with dot product zero, then verify the fourth point. Requires testing possible corners.
- **Rhombus:** Four equal sides alone are insufficient; unequal diagonals or non-right angles must cause rejection.
- **Rectangle:** Equal diagonals alone are insufficient; unequal side lengths must cause rejection.
- **Duplicate points:** A zero squared leg makes the relevant triple fail, so no zero-area square is accepted.
- **Rotated square:** Distance relations do not depend on axis alignment, so diamonds are accepted.
- **Negative coordinates:** Differences and squares work identically.
- **Arbitrary input order:** Every triple and every possible right-angle position is checked, so ordering is irrelevant.
- **Truthy distance idiom:** `and d1` rejects zero but returns an integer within the list expression; `any` intentionally interprets it as Boolean.
- **Avoid square roots:** Squared distances preserve all equalities and Pythagorean relations exactly.
