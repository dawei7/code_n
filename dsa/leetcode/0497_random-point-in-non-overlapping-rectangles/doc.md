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
