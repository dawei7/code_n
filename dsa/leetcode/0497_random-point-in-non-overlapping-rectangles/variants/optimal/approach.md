## General
**Weight rectangles by lattice-point count**

An inclusive rectangle contains $(x2 - x1 + 1) \cdot (y2 - y1 + 1)$ integer points. Choosing rectangles with equal probability would bias small rectangles, so build cumulative totals of these weights.

**Choose one global point ticket**

A uniform value selects one integer ticket from zero through `total_points - 1`. Binary search finds the first cumulative total greater than that ticket, identifying the rectangle that owns it. Every lattice point in the entire union corresponds to exactly one ticket, so all points have equal probability.

**Decode the ticket inside its rectangle**

Subtract the preceding prefix total to obtain a zero-based local offset. With the rectangle's inclusive width, `offset % width` is the x displacement and `floor(offset / width)` is the y displacement.

**Why non-overlap matters**

Since rectangles share no lattice point, their ticket ranges form a disjoint partition of the union. Prefix weighting counts every valid point once, and binary search selects precisely one owning rectangle.

## Complexity detail
For `r` rectangles and `d` draws, prefix construction takes $O(r)$ time and space. Each binary search costs $O(\log r)$, and storing the returned points costs $O(d)$, for $O(r + d \log r)$ time and $O(r + d)$ space. The native `pick()` operation itself uses $O(\log r)$ time after construction.

## Alternatives and edge cases
- **Linear rectangle selection per draw:** is correct but takes $O(r)$ per point instead of binary search.
- **Choose a rectangle uniformly:** is biased unless every rectangle contains the same number of lattice points.
- **Expand all points:** gives constant-time draws but may require space proportional to the entire coordinate area.
- **Single-point rectangle:** has weight one and always decodes to its only coordinate.
- **Negative coordinates:** do not affect widths or local offset decoding.
- **Inclusive boundaries:** both dimensions require the `+1` term.
- **Zero draws:** returns an empty list after harmless preprocessing.
- **Deterministic stream:** the local adapter cycles authored values; the native artifact uses platform randomness.
