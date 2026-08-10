## General

**Only horizontal position affects a vertical strip**

A vertical area extends infinitely along the $y$-axis. Its width is determined solely by two vertical boundary lines, so point $y$-coordinates cannot change whether a point lies horizontally inside the strip.

Project every point onto its $x$-coordinate. The problem becomes finding the largest open interval between occupied $x$ positions that contains no occupied position. Points may lie on either boundary because boundary points are explicitly allowed.

**Sort points by x-coordinate**

`points.sort()` applies Python's lexicographic list ordering. It compares each point's first entry, $x$, first and uses $y$ only to order points whose $x$ values tie. Thus, after sorting, the sequence of $x$-coordinates is non-decreasing.

The call sorts the input list in place. The method does not create a separate coordinate list.

`pairwise(points)` then yields every adjacent pair `(a,b)` in that sorted order. For each pair, the generator computes `b[0] - a[0]`, the horizontal gap between their $x$ positions. `max` returns the largest such gap.

The constraint of at least two points guarantees that `pairwise` yields at least one pair, so `max` never receives an empty generator.

**Why only adjacent sorted positions matter**

Suppose two boundary points have $x$-coordinates $x_L<x_R$. If some point has $x$ strictly between them, that point lies inside the infinite vertical strip regardless of its $y$-coordinate, so the area is invalid.

After sorting by $x$, an interval contains no occupied $x$ strictly inside it exactly when its endpoints are consecutive in the sorted sequence of occupied positions. Therefore every valid candidate width appears among adjacent differences.

Conversely, between two adjacent sorted points there is no point whose $x$ lies strictly between their $x$ values. The open vertical strip between those boundary lines contains no point, while any points on the boundary lines are allowed. Every adjacent gap is therefore a valid candidate.

Taking their maximum produces the widest valid vertical area.

**Repeated x-coordinates**

Several points can share the same vertical line. They appear consecutively after sorting, with gaps of zero between them. Those zero-width candidates do not harm the maximum.

More importantly, the transition from the last point at one distinct $x$ to the first point at the next distinct $x$ still appears as an adjacent pair. Its difference is the full gap between the occupied vertical lines. Therefore there is no need to deduplicate $x$ values first.

For example, sorted $x$ positions `[7,8,9,9]` produce gaps 1, 1, and 0. The maximum is 1, which is correct.

**Why y tie ordering is harmless**

Python sorts equal-$x$ points by $y$, but all gaps within that group remain zero. The group still occupies one contiguous part of the sorted list. Whichever equal-$x$ point is last, its next neighbor has the next larger $x$, so the useful gap is unchanged.

The geometry is completely captured by `a[0]` and `b[0]` in the generator.


Let $W$ be the maximum adjacent $x$ gap computed by the source. The two points defining that gap have no sorted point with an intermediate $x$, so the open strip between their vertical lines contains no point. Hence a valid area of width $W$ exists.

Now take any valid vertical area bounded by point $x$ positions $L<R$. If its boundary positions were not consecutive among sorted occupied $x$ values, another point would have $x$ strictly between them and would lie inside the area, contradicting validity. Thus its width $R-L$ is one of the adjacent differences and cannot exceed $W$.

The computed value is both achievable and at least as large as every valid width, so it is exactly the answer.

## Complexity detail

Let $n$ be the number of points. In-place sorting costs $O(n\log n)$ time. `pairwise` and the maximum generator then traverse $n-1$ adjacent pairs in $O(n)$ time. Total time is $O(n\log n)$.

Python's Timsort may use $O(n)$ auxiliary memory in the worst case. The `pairwise` iterator, generator, and current maximum use constant additional state. The manifest's $O(n)$ space bound therefore accurately covers sorting workspace.

The input list itself is mutated into sorted order. No $O(n)$ list of x-coordinates or gaps is allocated by the source, because differences are generated lazily.

## Alternatives and edge cases

- **Extract and sort only x-coordinates:** `xs = sorted(x for x, _ in points)` makes the relevant dimension explicit but allocates another $O(n)$ list rather than sorting the supplied points.
- **Deduplicate x-coordinates first:** Sorting a set can reduce repeated zeros, but building the set uses extra storage and is not necessary for correctness.
- **Bucket or counting sort:** Coordinates range up to $10^9$, so a direct coordinate-sized bucket array is impractical.
- **Maximum-gap linear algorithms:** With numeric bucketing, the maximum adjacent sorted gap can be found in linear expected time, but the implementation is much more complex and ordinary sorting fits $n\le10^5$.
- **Two points:** Their horizontal difference is the only adjacent gap and therefore the answer.
- **All points share one x-coordinate:** Every gap is zero, so the widest valid area has width zero.
- **Duplicate points:** They contribute zero gaps and do not alter gaps between distinct x positions.
- **Boundary points:** Points at the chosen left or right x-coordinate are allowed, so only strict interior positions invalidate a strip.
- **Arbitrary y-coordinates:** They never influence an infinitely tall vertical area's width or emptiness.
- **Input mutation:** `points.sort()` changes the original ordering. Use `sorted(points)` if caller-visible preservation were required.
- **At least two points guarantee:** Without it, `max` over `pairwise` would be empty and raise an error; the stated constraints rule that out.
