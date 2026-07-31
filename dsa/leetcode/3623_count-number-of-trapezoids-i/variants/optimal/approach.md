## General

**Characterize a valid selection by height.** A horizontal side requires two points with the same y-coordinate. A convex quadrilateral cannot contain three collinear vertices, so a valid four-point selection must take exactly two points from one height and exactly two from another height. Conversely, any two distinct point pairs on different horizontal lines form the two parallel opposite sides of a convex trapezoid when their endpoints are connected in x-order.

**Count sides before combining levels.** Group the points by y-coordinate. If a level contains $c$ points, it supplies $\binom{c}{2}=c(c-1)/2$ possible horizontal sides. Choosing one side from each of two different levels uniquely chooses four points and therefore one trapezoid.

Maintain the total number of sides supplied by already processed heights. For a new height with `sides` choices, `sides * earlier_sides` counts every trapezoid whose second height is the current one. Add that product to the answer, then add the current side count to the running total. Each unordered pair of heights is considered exactly once, without a nested loop over levels. Apply the modulus during accumulation.

## Complexity detail

Let $n$ be the number of points and $h$ the number of distinct y-coordinates. Counting heights takes $O(n)$ expected time, and combining the $h\le n$ groups takes $O(h)$ time, for $O(n)$ expected time overall under standard hash-table behavior. The height table holds $O(h)$ entries, bounded by $O(n)$ auxiliary space.

The benchmark uses $n/2$ distinct heights with exactly two points at each, so every height contributes one side and the answer is $\binom{n/2}{2}$. The linear method scans the points and groups once; a correct alternative that explicitly pairs all height groups takes $O(n^2)$ time on this workload.

## Alternatives and edge cases

- **Pair every pair of heights:** Multiplying their side counts is correct, but the nested level loops take $O(h^2)$ time.
- **Enumerate four-point subsets:** Testing all selections takes $O(n^4)$ time and ignores the decisive horizontal-level structure.
- **One populated height:** Even many horizontal segments cannot form a convex quadrilateral without a second height, so the result is zero.
- **Singleton heights:** They provide no horizontal side and contribute zero automatically.
- **Unequal group sizes:** A height with $c$ points contributes every one of its $\binom{c}{2}$ endpoint choices.
- **Horizontal rectangles and parallelograms:** They have horizontal parallel sides and are included because the definition requires at least one such pair.
- **X-coordinates:** Once points are distinct, the count depends only on how many occupy each height; negative, overlapping, or widely separated x-ranges do not change it.
- **Large answer:** Reduce accumulated products modulo $10^9+7$.
