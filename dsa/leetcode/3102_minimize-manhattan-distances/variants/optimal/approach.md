## General

**Rotate the distance formula.** For two points, write $Delta x = x_i-x_j$ and $Delta y = y_i-y_j$. The Manhattan distance has the identity

$$
lvert Delta x vert + lvert Delta y vert
=
maxleft(
lvert (x_i+y_i)-(x_j+y_j) vert,
lvert (x_i-y_i)-(x_j-y_j) vert
ight).
$$

Thus each point needs only two transformed coordinates: its sum $s=x+y$ and difference $d=x-y$. For any fixed set of points, the maximum Manhattan distance is

$$
maxleft(max s-min s, max d-min dight).
$$

The farthest pair therefore depends only on the extrema of these two one-dimensional projections, not on an explicit comparison of every pair.

**Preserve extrema after one removal.** Removing an indexed point can invalidate at most one current minimum or maximum in each projection. Record the smallest two and largest two values of $s$, each together with its point index, and do the same for $d$. These are occurrences rather than distinct values: if two points share the minimum, both can occupy the first and second positions.

When considering removal of index `r`, use the second minimum only if `r` supplied the first minimum; otherwise the first minimum remains. Select the maximum analogously. This reconstructs the exact remaining range for both projections in constant time. The input has at least three points, so a valid second extreme always exists after one point is removed.

Evaluate those two ranges for every possible removed index and keep their smallest resulting maximum. Every legal removal is examined, and for each one the projection identity gives the exact largest remaining Manhattan distance, so the minimum found is the required optimum.

## Complexity detail

Let $n$ be the number of points defined in the function contract. Two scans collect the constant number of extrema, and one final scan evaluates all removals. The total time is $O(n)$. Only eight indexed extreme pairs and a constant number of scalar variables are stored, so the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Sort both transformed coordinates:** Sorting indexed $x+y$ and $x-y$ values makes the first two and last two occurrences directly available and leads to a simpler $O(n log n)$ implementation using $O(n)$ space.
- **Ordered multisets:** Insert every transformed value, temporarily erase each point, query both ranges, and restore it. This mirrors the hints but also costs $O(n log n)$ time and $O(n)$ space.
- **Rescan after every removal:** Recompute all four extrema among the remaining points for each candidate removal. It is correct and uses constant auxiliary space, but takes $Theta(n^2)$ time.
- **Enumerate remaining pairs:** Trying every removal and every remaining pair directly takes $Theta(n^3)$ time.
- **Duplicate extrema:** Extrema must retain separate point indices. Tracking only distinct values would incorrectly discard a tied minimum or maximum when just one occurrence is removed.
- **Exactly three points:** After a removal, the answer is simply the distance between the two survivors; the second-extreme logic still applies without a special case.
- **Large coordinates:** Differences and sums stay within the stated integer range, but implementations in fixed-width languages should use a type wide enough for transformed values and distances.
