## General

A polygon is convex when walking around its boundary never requires switching from a left turn to a right turn or vice versa. The polygon may be listed clockwise or counterclockwise; either direction is valid. What matters is consistency.

The exact solution examines every three consecutive vertices, computes the signed two-dimensional cross product for that turn, and verifies that every nonzero cross product has the same sign.

**Turn orientation from a cross product**

For consecutive boundary points

$$
A=P_i,\qquad B=P_{i+1},\qquad C=P_{i+2},
$$

the code forms vectors from `A`:

$$
\overrightarrow{AB}=(x_1,y_1),\qquad
\overrightarrow{AC}=(x_2,y_2).
$$

Their scalar two-dimensional cross product is

$$
\operatorname{cross}(\overrightarrow{AB},\overrightarrow{AC})
=x_1y_2-x_2y_1.
$$

- A positive result means the direction from `AB` toward `AC` is counterclockwise.
- A negative result means it is clockwise.
- Zero means `A`, `B`, and `C` are collinear, so this step makes no left or right turn.

It is also common to cross `AB` with `BC`. The code's `AC` formulation has the same result because `AC = AB + BC`, and crossing a vector with itself contributes zero:

$$
AB\times AC=AB\times(AB+BC)=AB\times BC.
$$

**Remember the last genuine turn**

`pre` stores the most recent nonzero cross product. It begins at zero because no orientation has yet been established.

For each `cur`:

- If `cur == 0`, ignore it. A collinear boundary point does not contradict either clockwise or counterclockwise travel.
- If `cur != 0` and `cur * pre < 0`, the signs are opposite, so the polygon contains both turn directions and is not convex.
- Otherwise, store `cur` in `pre` as the current established direction.

When `pre` is still zero, `cur * pre` is zero rather than negative, so the first noncollinear turn simply establishes the sign.

**Why modulo indexing closes the polygon**

The input lists each vertex once but the polygon also has an edge from the final point back to the first. Indices `(i + 1) % n` and `(i + 2) % n` wrap around automatically.

For `i = n - 2`, the triple is the second-last point, last point, and first point. For `i = n - 1`, it is the last point, first point, and second point. Thus turns at the closing boundary are checked just like interior list positions. Omitting them could miss a concave corner near the list boundary.

**Why consistent turns imply convexity here**

In a simple polygon whose vertices are in boundary order, a concave or reflex vertex turns in the direction opposite to the polygon's overall orientation. Therefore any concavity creates a sign reversal among noncollinear cross products.

Conversely, if all nonzero turns share one orientation, every interior angle is at most 180 degrees in the allowed weak-convex sense. No boundary indentation exists. The simple-polygon guarantee rules out self-intersections, which could otherwise make local turn consistency insufficient for the usual polygon interpretation.

The method is independent of whether input order is clockwise. A clockwise convex polygon produces all negative turns; a counterclockwise one produces all positive turns. Neither sign is preferred.

**Trace the examples**

For the square `[[0,0],[0,5],[5,5],[5,0]]`, each consecutive triple turns in the same clockwise direction. Every nonzero cross product has the same negative sign, so the method returns `True`.

For `[[0,0],[0,10],[10,10],[10,0],[5,5]]`, the point `[5,5]` creates an inward notch. Turns around the outer corners have one sign, while a turn around the notch has the opposite sign. Their product becomes negative, so the algorithm returns `False` immediately.

**Collinear boundary vertices**

A convex polygon may include an extra point lying along a straight boundary edge. The corresponding cross product is zero and is ignored, while turns on either side still establish the common orientation. This implements non-strict convexity, where 180-degree boundary angles are allowed.

If every triple were collinear, the exact code would return true because it never observes a sign reversal. The source promises a simple polygon, which conventionally excludes a degenerate all-collinear boundary; that contract is what makes the behavior appropriate.

## Complexity detail

Let $n$ be the number of vertices. The loop processes exactly $n$ triples. Each iteration performs a constant number of indexed reads, subtractions, multiplications, and comparisons, so time complexity is $O(n)$.

Only `n`, `pre`, `cur`, loop indices, and four vector components are stored. The input is not copied or modified, so auxiliary space is $O(1)$.

Coordinate differences have bounded magnitude, and Python integer arithmetic cannot overflow. In a fixed-width implementation, the coordinate limits also keep these cross products within a standard signed 32-bit range, though using a wider type is a common safety habit.

## Alternatives and edge cases

- **Compute a convex hull:** Compare the hull with all input vertices. This costs $O(n\log n)$ and is unnecessary because vertices already arrive in boundary order.
- **Check every diagonal:** Verifying that all other vertices lie on one side of every edge can take $O(n^2)$ time; consecutive-turn signs capture the same property for a simple ordered polygon.
- **Use dot products:** Dot products measure angles and lengths but do not directly encode clockwise versus counterclockwise orientation.
- **Clockwise input:** All nonzero cross products are negative and the polygon is still accepted.
- **Counterclockwise input:** All nonzero cross products are positive and accepted.
- **Collinear consecutive points:** Zero turns are ignored, allowing points along a straight convex edge.
- **Closing corners:** Modulo indices ensure the last-to-first transitions are checked.
- **Self-intersection outside the contract:** Local turn checks alone should not replace a simplicity test for arbitrary vertex lists.
- **Three vertices:** Any valid nondegenerate simple triangle has one consistent orientation and is convex.
- **Repeated points:** The source guarantees uniqueness; duplicates could create zero-length edges and would require separate validation.
