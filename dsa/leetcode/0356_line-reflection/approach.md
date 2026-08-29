## General

A vertical reflection changes only the horizontal coordinate. Reflecting a point $(x,y)$ across the vertical line $x=c$ produces

$$
(2c-x,y).
$$

The height stays exactly the same, while the two horizontal coordinates have average $c$. The task is therefore to find the only possible value of $2c$ and verify that every input point has its required partner.

**Why the extreme horizontal coordinates determine the axis.**

Let `min_x` be the smallest horizontal coordinate in the point set and `max_x` the largest. If a vertical reflection preserves the set, the leftmost point or points must reflect to the rightmost horizontal position. Reflection reverses horizontal order: smaller $x$ values become larger reflected values. Therefore the reflection axis must lie halfway between the two extremes:

$$
c=\frac{\texttt{min\_x}+\texttt{max\_x}}{2}.
$$

There is no need to try multiple candidate lines. Any other axis would send the minimum horizontal coordinate somewhere other than the maximum, so the extreme coordinates could not be preserved.

The exact solution stores `s = min_x + max_x`, which equals $2c$. This avoids floating-point arithmetic. The axis may lie at a half-integer, such as $x=1.5$, but `s` remains an exact integer. A point's reflected horizontal coordinate is simply `s - x`.

**Collecting the facts in one pass.**

The first loop begins with `min_x = inf` and `max_x = -inf`. Every point updates both extremes. At the same time, `(x, y)` is inserted into `point_set`, a hash set used for expected constant-time membership checks.

Tuples are used because Python lists are mutable and cannot be hash-set keys. Converting `[x, y]` to `(x, y)` preserves both coordinate values in an immutable, hashable form.

Repeated input points collapse into one set entry. That is consistent with the problem's set-preservation meaning: repeating the same coordinate does not introduce a new geometric location that needs a different mirror. The second pass still visits repeated entries from the original list, but it asks the same membership question each time.

If the intended object were a multiset whose exact multiplicities had to match across the axis, a plain set would be insufficient. One would need frequencies. The accepted set-based interpretation treats the input as geometric points with duplicates allowed but not multiplicity-significant.

**Verifying every mirror.**

After computing `s`, the generator examines every original point `(x, y)`. Its uniquely required mirror is `(s - x, y)`. The expression

```text
(s - x, y) in point_set
```

checks whether that reflected location exists. `all(...)` returns true only if every point passes. It can stop early at the first missing partner.

For `[[1, 1], [-1, 1]]`, the extremes are `-1` and `1`, so `s = 0` and the axis is $x=0$. Point `(1, 1)` requires `(-1, 1)`, and point `(-1, 1)` requires `(1, 1)`. Both exist.

For `[[1, 1], [-1, -1]]`, the same candidate axis is derived. The mirror of `(1, 1)` would be `(-1, 1)`, not `(-1, -1)`. The missing same-height partner makes the answer false. This demonstrates why comparing only horizontal coordinate counts is not enough; pairing must preserve $y$.

**Why checking one direction proves equality.**

The test explicitly proves that reflecting every original point lands inside the original set. Could the original set contain extra points not reached by reflection? No. Reflection is an involution: applying it twice returns the starting point,

$$
s-(s-x)=x.
$$

It is therefore a one-to-one transformation. On a finite set, if every member maps into the same set under an injective transformation, the image has the same number of distinct points and must equal the set. More concretely, every point's verified partner reflects back to that point. The one-direction membership loop is sufficient.

**Points on the axis.**

When $x=c$, the reflected horizontal coordinate is unchanged. In doubled form, `s - x == x`. Such a point is its own partner, so one set membership succeeds without needing a second distinct coordinate. If every point shares one horizontal coordinate, then `min_x == max_x`, the candidate axis passes through all points, and the answer is true regardless of their vertical coordinates.

**Why the method is complete.**

If the function returns true, every point has exactly the mirror required by the extreme-derived axis, so reflecting the set preserves it. If a valid vertical axis exists, the extreme argument proves that its doubled coordinate is exactly `min_x + max_x`; for every input point, its reflection must be in the set, so every membership check succeeds. The function therefore returns true exactly for reflectable point sets.

## Complexity detail

Let $n$ be the number of entries in `points` and let $u$ be the number of distinct coordinate pairs, where $u\le n$.

The first loop processes all $n$ entries once. Updating extrema is constant time, and set insertion is expected $O(1)$, so this pass takes expected $O(n)$ time. The `all` generator processes at most $n$ entries and performs one expected constant-time set lookup for each, giving another expected $O(n)$ pass. Total expected running time is $O(n)$, strictly better than the follow-up's $O(n^2)$ pairwise search.

The set stores $u$ tuples, so auxiliary space is $O(u)$ and at most $O(n)$. The generator used by `all` is lazy and requires only $O(1)$ temporary state. The input list is not sorted or modified.

Hash-set operations have expected constant cost. With ordinary integer tuple keys, this is the standard analysis. Coordinate sums remain well within Python's arbitrary-precision integer support; even in fixed-width languages, the stated bounds make `min_x + max_x` fit comfortably in a signed 32-bit integer.

## Alternatives and edge cases

- **Group and sort x-coordinates by height:** For every $y$, sort that row's horizontal coordinates and compare pairs from the outside inward against a common sum. This can verify symmetry but costs $O(n\log n)$ time overall.

- **Try every possible partner or axis:** Comparing point pairs can reach $O(n^2)$ time and ignores the fact that the global extremes uniquely determine the candidate axis.

- **Frequency map for multiset symmetry:** Store counts of every coordinate and require equal counts for `(x, y)` and `(s - x, y)`. This is necessary only if duplicate multiplicity is semantically meaningful; the exact source follows set semantics.

- **Floating-point midpoint:** Computing `(min_x + max_x) / 2` works within these bounds but is unnecessary. The doubled-axis sum keeps every mirror calculation exact and generalizes safely.

- **All points on one vertical line:** Each point mirrors to itself, so the result is true.

- **Axis at a half-integer:** An odd `s` represents such an axis exactly. For example, horizontal coordinates `1` and `2` reflect around $x=1.5$ because each maps to `3 - x`.

- **Negative coordinates:** Minimum, maximum, addition, and mirror subtraction work identically across zero. No translation is needed.

- **Same x-values at different heights:** Each point is tested with its own unchanged $y$ coordinate. Vertical arrangement does not matter when all horizontal mirrors exist.

- **Missing one partner:** `all` short-circuits immediately and returns false; it need not inspect the remaining points.

- **Repeated coordinates:** They do not change extrema or the geometric membership set. Repeated checks are harmless and produce the same answer as one copy.

- **Nonempty input:** The constraints guarantee at least one point, so `min_x` and `max_x` are replaced before their sum is computed. No empty-input axis convention is needed.
