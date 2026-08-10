## General

**Use the geometry forced by ninety-degree turns.**

Every segment is horizontal or vertical, and directions repeat north, west, south, east. Segment `i` is perpendicular to segments `i - 1`, `i - 3`, and `i - 5`, while it is parallel to segments `i - 2` and `i - 4`. The path's rigid turning pattern severely limits how the first self-intersection can occur.

Adjacent segments always share their ordinary endpoint; that required connection is not the self-crossing being tested. Segment `i - 2` is parallel to the current segment and separated by the positive-length intervening move, so it cannot be the first new intersection. For the first self-crossing, only three local configurations remain:

1. the current segment crosses or touches segment `i - 3`;
2. the current segment overlaps or touches segment `i - 4` after the path folds exactly onto the same line;
3. the current segment crosses or touches segment `i - 5` during the transition from an outward spiral to an inward spiral.

The source checks exactly these three cases for every `i` starting at `3`. No crossing is possible with fewer than four segments.

**Normalize the current direction.**

The inequalities are easier to understand if the picture is rotated so that the current segment `i` points north. Rotation does not change whether segments intersect. In that orientation, the recent directions are:

- segment `i`: north;
- segment `i - 1`: east;
- segment `i - 2`: south;
- segment `i - 3`: west;
- segment `i - 4`: north;
- segment `i - 5`: east.

Write $d_t=\text{distance}[t]$. All lengths are positive, so the orientation and relative placement are unambiguous.

**Case one: cross the segment three moves back.**

Place the start of segment `i - 3` at coordinate $(0,0)$. After moving west by $d_{i-3}$, south by $d_{i-2}$, and east by $d_{i-1}$, the current northward segment begins at

$$
(-d_{i-3}+d_{i-1},-d_{i-2}).
$$

Segment `i - 3` lies horizontally at height zero from $x=-d_{i-3}$ through $x=0$. The current vertical segment's $x$ coordinate lies on that horizontal range exactly when

$$
d_{i-1}\le d_{i-3}.
$$

The current segment begins $d_{i-2}$ below the horizontal line, so it reaches that line exactly when

$$
d_i\ge d_{i-2}.
$$

These are the source's first two-part condition:

`d[i] >= d[i - 2] and d[i - 1] <= d[i - 3]`.

Equality is intentional. It includes touching at an endpoint, which counts as the path crossing itself. For `[2,1,1,2]` at `i = 3`, `2 >= 1` and `1 <= 2`, so the eastward fourth segment reaches the first northward segment.

**Case two: overlap the segment four moves back.**

Now include segment `i - 4`, which is parallel to the current northward segment. Put its end at $(0,0)$ and let it begin at $(0,-d_{i-4})$. After the west, south, and east moves, the current segment has horizontal coordinate

$$
-d_{i-3}+d_{i-1}.
$$

It lies on the same vertical line as segment `i - 4` only when

$$
d_{i-1}=d_{i-3}.
$$

The current segment starts at height $-d_{i-2}$ and extends upward by $d_i$. It reaches the lower endpoint $-d_{i-4}$ of the old vertical segment when

$$
d_i+d_{i-4}\ge d_{i-2}.
$$

Together, these give the second source condition. This configuration includes a single touching point or a positive-length overlap.

For `[1,1,2,1,1]`, no earlier case fires. At `i = 4`, the two intervening horizontal lengths are equal, $d_3=d_1=1$, and $d_4+d_0=2\ge d_2=2$. The current segment returns to the line of segment zero and touches it.

**Case three: cross the segment five moves back.**

This is the transition configuration that requires four inequalities. Keep the same normalized orientation and place segment `i - 4` from $(0,-d_{i-4})$ to $(0,0)$. Then segment `i - 5` is horizontal at height $-d_{i-4}$ and ends at $(0,-d_{i-4})$; its left endpoint is $(-d_{i-5},-d_{i-4})$.

The current segment is vertical at

$$
x=-d_{i-3}+d_{i-1},
$$

starting at height $-d_{i-2}$ and ending at $-d_{i-2}+d_i$.

For its horizontal coordinate to lie within segment `i - 5`, both of these must hold:

$$
d_{i-1}\le d_{i-3}
$$

and

$$
d_{i-1}+d_{i-5}\ge d_{i-3}.
$$

The first prevents the current segment from lying to the right of the old segment's endpoint. The second prevents it from lying to the left of the old segment's start.

For the old segment's height to lie within the current segment, both of these must hold:

$$
d_{i-2}\ge d_{i-4}
$$

and

$$
d_i+d_{i-4}\ge d_{i-2}.
$$

The first says the current segment starts at or below the old horizontal line. The second says it ends at or above that line. The source writes the last inequality equivalently as

$$
d_i\ge d_{i-2}-d_{i-4}.
$$

All four conditions are required because two axis-aligned segments intersect only when the vertical segment spans the horizontal segment's height and the horizontal segment spans the vertical segment's $x$ coordinate.

For `[1,1,2,2,1,1]`, the earlier configurations do not apply. At `i = 5`, all four third-case inequalities hold, so the sixth segment reaches the segment five moves back.

**Why these local cases are exhaustive.**

Before the first crossing, the counter-clockwise path behaves as a nonintersecting spiral. While opposite-direction lengths expand far enough, each new segment lies outside the boundary made by earlier segments. If expansion stops, the path begins folding inward.

At that transition, the current segment can meet the boundary three moves back directly, align with the parallel boundary four moves back, or pass through the older perpendicular boundary five moves back. Those are the three cases above. Once the path is inward, the nearer recent segments shield all more distant segments: reaching a segment earlier than `i - 5` would require crossing one of the intervening boundaries first. That nearer intersection would already have been detected at an earlier or current iteration.

Thus, assuming no previous crossing, the first crossing must be one of these local configurations. The loop checks them in a constant amount of work and returns immediately when any appears.

**Why false is correct after the loop.**

Each iteration tests every geometrically possible first intersection involving the new segment. If none succeeds, the new segment does not create the first crossing. By induction over segment index, the processed prefix remains non-self-crossing. If all segments are processed without a match, the complete path does not cross itself.

## Complexity detail

Let $n$ be the number of distances. The loop visits indices `3` through `n - 1` once. Each iteration performs a fixed number of arithmetic comparisons involving at most the previous five lengths. Total time complexity is $O(n)$.

The source aliases the input as `d` and uses only the loop index and temporary arithmetic results. It does not store coordinates, segments, or a visited-point set, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Construct every segment and compare with all earlier segments:** General axis-aligned intersection checks are straightforward, but comparing each new segment against the whole prefix takes $O(n^2)$ time. The turning pattern makes only three local configurations necessary.

- **Store every visited lattice point:** Distances can be as large as `100000`, so expanding moves into unit steps can require enormous time and memory. Crossings can also occur along segment interiors, which geometric inequalities handle directly.

- **Track full coordinates with a sweep-line structure:** This solves a more general segment-intersection problem in roughly $O(n\log n)$ time, but is unnecessary for the fixed counter-clockwise direction cycle.

- **Fewer than four moves:** No non-adjacent perpendicular segment exists yet, so the loop has no iterations and correctly returns `False`.

- **Endpoint touching:** All relevant comparisons use `>=`, `<=`, or equality. Touching an earlier segment at one point counts as self-crossing and must return true.

- **Collinear overlap:** The second configuration explicitly detects the current segment lying on segment `i - 4` and reaching it. Overlap is a crossing, not a harmless parallel move.

- **Positive distances:** The contract excludes zero-length moves. The geometric derivation and the claim that segment `i - 2` is separated rely on that positivity.

- **Rotation of directions:** The proof imagines the current move pointing north, but every other `i` is just a rotation of the same shape. Length inequalities are invariant under rotation.

- **Large coordinate totals:** The source never forms absolute coordinates, so accumulated position magnitude is irrelevant. Its additions involve only two bounded distances and are safe in Python; fixed-width implementations should still choose a type that safely holds such sums.
