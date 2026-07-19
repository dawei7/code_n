# Rectangle Area II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 850 |
| Difficulty | Hard |
| Topics | Array, Segment Tree, Sweep Line, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/rectangle-area-ii/) |

## Problem Description
### Goal
Each entry `[x1, y1, x2, y2]` in `rectangles` describes a nonzero-area, axis-aligned rectangle. The point `(x1, y1)` is its bottom-left corner and `(x2, y2)` is its top-right corner, with all coordinates between $0$ and $10^9$.

Compute the total area covered by at least one rectangle. Regions where rectangles overlap must be counted once rather than once per covering rectangle. Because the union area may be very large, return it modulo

$$
M = 10^9 + 7.
$$

### Function Contract
**Inputs**

- `rectangles`: an array of $n$ four-integer rectangle descriptions, where $1 \leq n \leq 200$, $0 \leq x_1 < x_2 \leq 10^9$, and $0 \leq y_1 < y_2 \leq 10^9$.

**Return value**

Return the area of the union of all rectangles, reduced modulo $M$.

### Examples
**Example 1**

- Input: `rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]`
- Output: `6`

Overlapping portions of the three rectangles contribute only once.

**Example 2**

- Input: `rectangles = [[0,0,1000000000,1000000000]]`
- Output: `49`

The rectangle has area $10^{18}$, whose remainder modulo $M$ is $49$.

**Example 3**

- Input: `rectangles = [[0,0,2,2],[2,0,4,2]]`
- Output: `8`

Sharing a boundary does not create positive-area overlap.
