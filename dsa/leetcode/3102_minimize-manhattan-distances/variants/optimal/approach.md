## General

**Transform Manhattan distance into one-dimensional spreads.** For point $(x,y)$ define:

$$
u=x+y
\qquad\text{and}\qquad
v=x-y.
$$

For any two points, their Manhattan distance satisfies:

$$
\lvert x_1-x_2\rvert+\lvert y_1-y_2\rvert
=
\max\left(
\lvert u_1-u_2\rvert,
\lvert v_1-v_2\rvert
\right).
$$

One way to see this is to let $a=x_1-x_2$ and $b=y_1-y_2$. The transformed differences are $a+b$ and $a-b$. The larger of their absolute values equals $\lvert a\rvert+\lvert b\rvert$, depending on whether $a$ and $b$ have the same or opposite signs.

**Maximum pair distance becomes a range calculation.** Among a set of scalar values, the maximum absolute difference is maximum minus minimum. Therefore, for any remaining point set, the maximum Manhattan distance between any pair is:

$$
\max\left(
\max(u)-\min(u),
\max(v)-\min(v)
\right).
$$

This identity removes the need to examine every pair. It is enough to know the smallest and largest transformed coordinates.

**Why ordered multisets are used.** The source creates two `SortedList` instances:

- `sl1` stores every `x + y` value;
- `sl2` stores every `x - y` value.

They are multisets rather than ordinary sets. Different points can have the same transformed value, and removing one candidate point must remove only one occurrence. `SortedList.remove(value)` has exactly that multiplicity-aware behavior.

After the initial loop, both structures describe all points. Their first and last elements are the current minima and maxima.

**Evaluate each possible removal literally.** The problem requires removing exactly one point. For candidate $(x,y)$, the source temporarily removes one `x+y` from `sl1` and one `x-y` from `sl2`. Because the same original point produced those two values, the two multisets now represent precisely the remaining points.

It computes:

`max(sl1[-1] - sl1[0], sl2[-1] - sl2[0])`.

By the transformed-distance identity, this is exactly the largest Manhattan distance among every pair left after that removal. `ans` retains the smallest candidate value across all removed points.

The source then adds both transformed values back before moving to the next point. Restoring them is essential: every candidate removal must be evaluated against the full original collection, not against a collection that accumulates deletions.

**A point need not itself be on every extreme.** Removing an interior point leaves both transformed ranges unchanged, so its candidate value equals the original maximum distance. Removing a point responsible for a unique minimum or maximum can expose the second extreme and reduce the answer. Trying all points lets the ordered multisets handle both situations uniformly without separately identifying special candidates.

**Duplicates are safe.** Suppose two points both produce the current largest `u`. Removing one leaves the other identical maximum in `sl1`, so the range does not falsely shrink. A plain set would lose the value entirely and be incorrect. The multiset is therefore part of correctness, not just a convenience.

**A correctness argument.** Fix any point index $r$. After its two transformed values are removed, `sl1` and `sl2` contain one value per remaining point. The endpoint differences equal the maximum pairwise differences in the transformed coordinates. Their maximum equals the maximum Manhattan distance by the identity above. Thus the candidate computed for $r$ is exact.

The loop considers every legal choice of the one removed point. Taking the minimum of all exact candidate maxima is exactly the requested minimum possible maximum distance.

**A small geometric intuition.** Lines of constant $x+y$ slope downward, while lines of constant $x-y$ slope upward. The two transformed ranges measure the spread of the point cloud along these diagonal axes. A pair's Manhattan distance is governed by the larger diagonal separation. Removing a point can shrink one or both diagonal spans, and the algorithm measures both.

**Why endpoints remain available.** The contract has at least three points. Removing one leaves at least two, so both sorted lists remain nonempty. Accesses `[0]` and `[-1]` are always valid; no special empty or singleton case is needed.

## Complexity detail

Building the two sorted multisets performs $2n$ insertions. Each `SortedList.add` costs $O(\log n)$ amortized for its ordered structure, so initialization is $O(n\log n)$.

For every point, the source performs two removals and two reinsertions, each $O(\log n)$, plus constant-time endpoint reads. The complete exact implementation therefore takes $O(n\log n)$ time.

Both sorted lists store $n$ numbers, so auxiliary space is $O(n)$. This directly contradicts the local Optimal manifest, which claims $O(n)$ time and $O(1)$ space and describes retaining only two indexed minima and maxima. That extrema-only design is a possible different implementation; the checked-in `solution.py` uses full `SortedList` multisets and must receive their actual bounds.

## Alternatives and edge cases

- **Two smallest and two largest values:** For each transform, retain extrema with point indices so deleting one point can expose the next. This achieves $O(n)$ time and $O(1)$ extra space and matches the manifest idea.
- **Recompute all pair distances:** Trying every removal and every remaining pair can take $O(n^3)$.
- **Recompute transformed extrema after each removal:** It avoids an ordered multiset but still takes $O(n^2)$ time.
- **Duplicate points:** Their Manhattan distance is zero, and multiset multiplicity preserves all remaining copies correctly.
- **Duplicate transformed extrema:** Removing one occurrence must not remove the shared extreme value entirely.
- **All points identical:** Every transformed range is zero, so every candidate and the answer are zero.
- **Point interior to both ranges:** Its removal changes neither maximum distance nor either endpoint spread.
- **Point extreme in one transform only:** It can still be the best removal because only the larger of the two post-removal ranges determines the candidate.
- **Exactly three points:** Removing one leaves two; their single Manhattan distance is represented by both range formulas.
- **Exactly one removal:** Values are restored after each trial so candidates are independent.
- **Large coordinates:** `x+y` and `x-y` fit safely in Python integers; fixed-width languages should use a type covering roughly twice the coordinate range.
- **Negative transformed values:** `x-y` may be negative, but sorted ordering and max-minus-min work unchanged.
- **Why two transforms:** Using only `x+y` misses point pairs whose coordinate differences have opposite signs.
- **Why no square root:** Manhattan distance is not Euclidean distance; the diagonal transform gives an exact max identity.
- **Source/manifest discrepancy:** The exact multiset solution is correct but has $O(n\log n)$ time and $O(n)$ space, not the advertised extrema-only bounds.
