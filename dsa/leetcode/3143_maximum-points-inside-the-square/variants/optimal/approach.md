## General

For a point `(x, y)`, the smallest axis-aligned square centered at the origin that contains it has half-side length

$$
r = \max(\lvert x\rvert, \lvert y\rvert).
$$

Thus, choosing a square is equivalent to choosing a radius: it contains exactly the points whose values of $r$ do not exceed that radius.

**Locate the first unavoidable duplicate**

For each lowercase tag, keep the smallest radius at which that tag appears. When another occurrence arrives, the larger of the tag's two smallest radii is the first radius at which both occurrences would be contained. The update can be performed online: if the new radius is smaller than the stored nearest radius, the old nearest becomes a duplicate threshold; otherwise the new radius is a duplicate threshold.

Maintain `conflict_radius` as the minimum such threshold over all tags. Any square with radius at least `conflict_radius` is invalid, because it contains the corresponding duplicate-tag pair. Every point strictly closer than that threshold is safe: if two of those points shared a tag, their second-smallest radius would make the global threshold smaller.

There can be at most one safe point per tag. Count the stored nearest radii that are strictly less than `conflict_radius`. The strict comparison is essential because boundary points are included; all points at the first conflicting radius enter together, so none at that radius can be part of the best valid square.

## Complexity detail

Let $n$ be the number of points. Each point is processed once and the final scan covers the fixed 26-letter alphabet, so the running time is $O(n)$.

The nearest-radius array has 26 entries. Since the tag alphabet is fixed by the contract, the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Sort by radius:** Processing equal-radius groups in sorted order is correct and makes the boundary behavior explicit, but sorting increases the running time to $O(n \log n)$.
- **Try every candidate square:** Rechecking all points for every distinct radius is correct but can require $O(n^2)$ time; it is the principal slower benchmark comparison.
- **Binary search the radius:** A validity check is monotone, but repeated $O(n)$ checks add logarithmic work and are unnecessary once the first two radii per tag are tracked directly.
- Points at the same radius enter simultaneously. If two share a tag, a smaller square must exclude every point on that boundary.
- A point at the origin can be included by a zero-side-length square unless another point with the same tag also lies at radius zero; coordinates themselves remain distinct.
- If every tag is unique, `conflict_radius` remains infinite and all points are counted.
- Repeated tags farther than the earliest conflict cannot change the answer, although they are still handled by the same minimum update.
