## General

**Reduce “at least two” to rectangle pairs**

Any eligible square is contained in at least two input rectangles. Selecting any two of those rectangles shows that the same square is contained in their pairwise intersection. It is therefore sufficient to inspect every unordered pair; a region shared by more than two rectangles is already represented by each pair drawn from that group.

For rectangles $i$ and $j$, the overlap dimensions are

$$
w = \min(c_i, c_j) - \max(a_i, a_j)
$$

and

$$
h = \min(d_i, d_j) - \max(b_i, b_j).
$$

If either value is non-positive, the rectangles have no common region with positive area. This case needs no separate branch: $\min(w,h)$ cannot improve a best side length initialized to zero.

**Extract the best square from one overlap**

When both dimensions are positive, every square inside the overlap has side length at most both $w$ and $h$. Thus its side is at most $\min(w,h)$. A square with exactly that side length does fit by placing it against any corner of the intersection, so this bound is attainable.

Track the largest value of $\min(w,h)$ over all pairs and square it once at the end. The pair reduction proves that every feasible square is considered, while the overlap argument proves that the recorded value for each pair is exactly its best possible side. The final squared maximum is therefore the requested maximum area.

## Complexity detail

There are $\binom{n}{2}$ unordered pairs, and each pair uses a constant number of coordinate operations. The time complexity is $O(n^2)$ and the auxiliary space complexity is $O(1)$.

The side length can be as large as $10^7 - 1$, so its area can approach $10^{14}$. The returned product must use an integer type wide enough for that value.

## Alternatives and edge cases

- **Binary search on the side length:** Feasibility is monotone, but testing a candidate by scanning all pairs adds a logarithmic factor without avoiding the pairwise work.
- **Sweep line or spatial indexing:** These techniques may skip many disjoint pairs on favorable data, but the constraints are small enough for a direct pair scan and dense overlap can still produce quadratically many relevant pairs.
- **Materializing every intersection:** Storing pairwise rectangles makes the same computations while increasing auxiliary space to $O(n^2)$.
- Rectangles that only touch along an edge or at a corner have overlap width or height `0` and cannot contain a positive-area square.
- A long, thin overlap is limited by its shorter dimension, not its area or longer dimension.
- Full containment needs no special handling; the intersection formulas recover the contained rectangle.
- A square lying in three or more rectangles is not missed because it also lies in every pair selected from them.
- Square the side using a 64-bit-capable integer representation so large coordinate differences do not overflow.
