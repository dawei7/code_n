## General

**Sort points by distance**

The exact solution assigns every point a Euclidean-distance key, sorts all points by that key, and returns the first `k`.

For `(x, y)`, `hypot(x, y)` computes `sqrt(x^2 + y^2)`. A smaller key means a closer point.

**Why sorting solves selection**

After ascending sort, every point before position `k` has distance no greater than every point after it.

Therefore, `points[:k]` contains exactly a valid set of the `k` closest points.

The answer is guaranteed unique except for order, so no ambiguous tie crosses the selection boundary in a way that creates different valid sets.

**The key function**

`points.sort(key=lambda p: hypot(p[0], p[1]))` computes one key per point under Python's decorate-sort-undecorate behavior.

The original point lists are rearranged rather than copied. The lambda reads coordinates but does not alter them.

**Why coordinate signs do not matter**

Coordinates may be negative. Squaring makes sign-reflected points with the same magnitudes equally distant.

`hypot` handles signs directly; explicit absolute values are unnecessary.

**Squared distance would give the same order**

Square root is strictly increasing for nonnegative inputs. Thus comparing `x^2 + y^2` gives exactly the same ordering as comparing its square root.

Sorting by squared distance avoids floating arithmetic. The checked-in code uses `hypot`, which is correct for the bounded coordinates.

**Trace**

For `[[1, 3], [-2, 2]]`, distances are `sqrt(10)` and `sqrt(8)`. The second point sorts first, and `k = 1` returns it.

For `[[3, 3], [5, -1], [-2, 4]]`, squared distances are eighteen, twenty-six, and twenty. The first and third points become the answer for `k = 2`.

**Why the slice has the right size**

The contract guarantees `1 <= k <= len(points)`. Python slicing returns exactly `k` references in this range.

When `k` equals the number of points, the slice returns every point.


The key equals geometric distance from the origin. Ascending key order is therefore ascending closeness.

The first `k` entries are no farther than every remaining point, precisely defining a valid closest set. Their internal order is accepted.

**Input mutation and returned objects**

`sort` changes the order of the input outer list. The returned slice is a new outer list, but its entries reference the original inner coordinate lists.

If the caller needs original order preserved, use `sorted` instead.

**Why full sorting does more work than necessary**

The problem needs only a partition between the closest `k` and the rest. Full sorting also orders every point inside both groups.

That extra work is why this implementation is `O(N log N)` instead of the linear quickselect bound claimed by the manifest. It remains simple and correct.

**Why no explicit tie-breaker is needed**

Equal-distance points inside the same side of the selection boundary may appear in either order. The unique-answer guarantee prevents a boundary tie from producing multiple possible sets.

Python's stable sort preserves input order among equal keys, but correctness does not depend on that order.

**Numerical behavior**

`hypot` computes Euclidean norm robustly. Bounded integer coordinates are far within floating range. Squared integer distance is an exact alternative with identical ordering.

Using Manhattan distance would be wrong because it represents different geometry and can rank points differently.

**Formal boundary argument**

Let sorted distances be `d0 <= d1 <= ...`. Every returned distance is at most `d(k-1)`, and every omitted distance is at least `dk`.

No omitted point can be strictly closer than a returned point without contradicting sorted order.

**Slice allocation**

The slice copies `k` references, not coordinate values. It is a new outer list whose inner point objects are shared with `points`.

This explains its `O(k)` time and output storage.

**Why all points need not be distinct**

The logic sorts entries, not coordinate identities. If duplicate coordinate points were present, each occurrence would receive the same distance and still count as one array entry toward `k`.

The stated uniqueness of the answer set controls boundary ambiguity, while the sorting mechanics themselves remain valid for repeated coordinates.

**Comparison with a radius test**

Guessing a distance radius would still require determining how many points lie inside and resolving the exact boundary. Sorting directly establishes the complete order and avoids numeric binary-search termination concerns.

## Complexity detail

Let `N` be point count.

Computing keys is `O(N)`, sorting `O(N log N)`, and slicing `O(k)`. Total time is `O(N log N)`.

Python sorting may use `O(N)` temporary storage, and the output slice uses `O(k)` references. These exact bounds differ from the manifest's quickselect claims.

## Alternatives and edge cases

- **Quickselect:** Expected `O(N)` time and in-place partitioning, matching the intended manifest.
- **Max-heap of size `k`:** `O(N log k)` time and `O(k)` space.
- **Squared-distance sort:** Same asymptotic time with integer keys.
- **`k = 1`:** Return one closest point.
- **`k = N`:** Return all points.
- **Negative coordinates:** Handled naturally.
- **Origin:** Distance zero sorts first.
- **Equal distances:** Relative order is irrelevant away from the unique boundary.
- **Input mutation:** Original point order is lost.
- **Output order:** Sorted-by-distance order is allowed.
