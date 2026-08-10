## General

A horizontal side must connect two points with the same y-coordinate. A horizontal trapezoid therefore requires:

- two distinct points at one height;
- two distinct points at another height.

The x-coordinates determine which segment is chosen at a height, but they do not affect whether that segment is horizontal.

**Count points by height**

`Counter(p[1] for p in points)` maps each y-coordinate to the number of input points lying on that horizontal line.

All points are distinct. At one height, distinct points cannot share both x and y, so any pair has different x-coordinates and forms a nonzero horizontal segment.

**Count horizontal segments at one height**

If a height contains `v` points, the number of unordered endpoint pairs is:

$$
\binom{v}{2}=\frac{v(v-1)}2.
$$

The source stores this count in `t`. Heights containing zero or one point produce `t=0` and cannot supply a trapezoid side.

**Combine sides from different heights**

Choosing one horizontal segment at height `y_1` and another at different height `y_2` determines four distinct points. Ordering the lower segment's endpoints and upper segment's endpoints around their boundary forms a convex quadrilateral with those two horizontal sides parallel.

Thus every pair of segments from two different height groups creates one horizontal trapezoid.

The source avoids a quadratic loop over all pairs of heights. `s` stores the total number of horizontal segments seen at earlier heights. For the current height with `t` segments:

`s * t`

counts every choice of one earlier segment and one current segment.

After adding that contribution, `s += t` makes the current segments available to later heights.

**Why each trapezoid is counted exactly once**

Any valid horizontal trapezoid has exactly two vertices on one horizontal supporting line and two on another. Those lines have distinct y-coordinates because the quadrilateral has nonzero area.

When the loop reaches the later-iterated of those two height groups, its segment is current and the other segment is included in `s`. The four-point choice is counted once there.

It cannot be counted at any other pair of heights because its vertices determine their two y-values uniquely. The arbitrary iteration order of `Counter.values()` does not matter; each unordered pair of height groups still has exactly one earlier and one current member.

**Why x-overlap is not required**

The two horizontal segments do not need to overlap in their x-ranges. Connecting opposite endpoints in boundary order still produces a convex trapezoid. The definition requires at least one pair of parallel sides, not a particular orientation of the nonparallel sides.

The counting formula therefore depends only on the number of possible segments per height.

**Following the first example**

Height 0 has three points, producing:

$$
\binom32=3
$$

horizontal segments. Height 2 has two points, producing one segment.

Choosing that one upper segment with any of the three lower segments yields `3*1=3` trapezoids.

**Streaming combination invariant**

Before processing a height, `s` equals the total number of segments across all previously processed heights, and `ans` equals the number of trapezoids whose two heights are both in that processed set.

The current `s*t` adds exactly the trapezoids pairing the new height with one old height. No trapezoid entirely among old heights changes, and none using a future height is ready. Updating `s` restores the invariant for the enlarged processed set.

Induction over all height groups proves the final answer.

**Modulo handling**

The answer may be large, so each update applies modulo `10^9+7`:

`ans = (ans + s*t) % mod`.

`s` itself is not reduced modulo the constant. This is still correct because Python integers do not overflow, and reducing only the accumulated answer preserves the final remainder.

Reducing `s` as well would also be valid for modular multiplication, but the source retains the exact segment count.

**Environment dependencies**

The exact file uses `Counter` and `List` without showing imports. A normal standalone module must import `Counter` from `collections` and `List` from `typing` unless the execution harness supplies them.

## Complexity detail

Let `n` be the number of points and `h` the number of distinct y-coordinates.

Building the counter visits every point once and uses expected `O(n)` time. Iterating its `h <= n` values is `O(h)`. Total expected time is `O(n)`.

The counter stores one entry per distinct height, so auxiliary space is `O(h)` and therefore `O(n)` in the worst case. No segments or quadrilaterals are materialized.

Arithmetic uses Python integers; combination counts and `s` can exceed fixed-width ranges without overflow.

## Alternatives and edge cases

- **Double loop over heights:** Compute each segment count, then multiply every pair. It is correct but can take `O(h^2)` time.
- **Prefix sum of segment counts:** This is exactly the role of scalar `s`; no prefix array is necessary.
- **Enumerate all four-point subsets:** It costs `O(n^4)` and repeats geometry checks.
- **One point at a height:** It creates no horizontal side and contributes zero.
- **Two points at a height:** They create exactly one possible side.
- **All points at one height:** There is no second parallel supporting line, so the answer is zero.
- **Every point at a distinct height:** Every `t` is zero and the answer is zero.
- **Negative y-coordinates:** Counter keys handle them exactly like positive heights.
- **Negative or unordered x-coordinates:** Only equality of y matters for choosing a horizontal segment.
- **Parallelogram:** It is a trapezoid under “at least one pair” and is counted once by its two horizontal sides.
- **Modulo:** Only the returned count is reduced; geometric uniqueness is counted over ordinary integers first.
- **Counter iteration order:** It affects which height is “earlier” but not the total over unordered height pairs.
- **Input preservation:** The source reads coordinates and never sorts or mutates `points`.
- **Missing imports:** Standalone use must provide `Counter` and `List`.
