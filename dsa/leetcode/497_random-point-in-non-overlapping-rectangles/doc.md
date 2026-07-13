# Random Point in Non-overlapping Rectangles

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 497 |
| Difficulty | Medium |
| Topics | Array, Math, Binary Search, Reservoir Sampling, Prefix Sum, Ordered Set, Randomized |
| Official Link | [LeetCode](https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/) |

## Problem Description
### Goal
Construct a random-point picker from non-overlapping axis-aligned rectangles described by inclusive corners `[a, b, x, y]`. Each rectangle contains every integer-coordinate point whose horizontal coordinate lies from `a` through `x` and whose vertical coordinate lies from `b` through `y`, including its boundary.

Each `pick()` call must return one integer point chosen uniformly from the union: every covered lattice point has the same probability, regardless of which rectangle contains it or how large that rectangle is. Weight rectangles by their number of integer points rather than choosing rectangles equally, never return a point outside the union, and make a fresh random selection on every call.

### Function Contract
**Inputs**

- `rects`: rectangles `[x1, y1, x2, y2]` with inclusive integer boundaries and no overlapping lattice points
- `random_values`: a deterministic stream of values in `[0, 1)` used by the local adapter
- `draws`: the number of points to generate

**Return value**

- The generated `[x, y]` points in draw order

### Examples
**Example 1**

- Input: `rects = [[1,1,1,1]], random_values = [0], draws = 2`
- Output: `[[1,1],[1,1]]`

**Example 2**

- Input: `rects = [[-2,-2,-1,-1]], random_values = [0,0.25,0.5,0.75], draws = 4`
- Output: `[[-2,-2],[-1,-2],[-2,-1],[-1,-1]]`

**Example 3**

- Input: `rects = [[0,0,0,0],[2,3,3,3]], random_values = [0,0.5,0.9], draws = 3`
- Output: `[[0,0],[2,3],[3,3]]`

### Required Complexity

- **Time:** $O(r + d \log r)$
- **Space:** $O(r + d)$

<details>
<summary>Approach</summary>

#### General

**Weight rectangles by lattice-point count**

An inclusive rectangle contains $(x2 - x1 + 1) \cdot (y2 - y1 + 1)$ integer points. Choosing rectangles with equal probability would bias small rectangles, so build cumulative totals of these weights.

**Choose one global point ticket**

A uniform value selects one integer ticket from zero through `total_points - 1`. Binary search finds the first cumulative total greater than that ticket, identifying the rectangle that owns it. Every lattice point in the entire union corresponds to exactly one ticket, so all points have equal probability.

**Decode the ticket inside its rectangle**

Subtract the preceding prefix total to obtain a zero-based local offset. With the rectangle's inclusive width, `offset % width` is the x displacement and `floor(offset / width)` is the y displacement.

**Why non-overlap matters**

Since rectangles share no lattice point, their ticket ranges form a disjoint partition of the union. Prefix weighting counts every valid point once, and binary search selects precisely one owning rectangle.

#### Complexity detail

For `r` rectangles and `d` draws, prefix construction takes $O(r)$ time and space. Each binary search costs $O(\log r)$, and storing the returned points costs $O(d)$, for $O(r + d \log r)$ time and $O(r + d)$ space. The native `pick()` operation itself uses $O(\log r)$ time after construction.

#### Alternatives and edge cases

- **Linear rectangle selection per draw:** is correct but takes $O(r)$ per point instead of binary search.
- **Choose a rectangle uniformly:** is biased unless every rectangle contains the same number of lattice points.
- **Expand all points:** gives constant-time draws but may require space proportional to the entire coordinate area.
- **Single-point rectangle:** has weight one and always decodes to its only coordinate.
- **Negative coordinates:** do not affect widths or local offset decoding.
- **Inclusive boundaries:** both dimensions require the `+1` term.
- **Zero draws:** returns an empty list after harmless preprocessing.
- **Deterministic stream:** the local adapter cycles authored values; the native artifact uses platform randomness.

</details>
