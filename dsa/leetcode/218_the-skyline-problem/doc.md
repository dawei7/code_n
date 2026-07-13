# The Skyline Problem

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 218 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Divide and Conquer, Binary Indexed Tree, Segment Tree, Sweep Line, Sorting, Heap (Priority Queue), Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/the-skyline-problem/) |

## Problem Description
### Goal
Each building is an axis-aligned rectangle described by `[left, right, height]`, occupying the half-open horizontal interval from `left` up to `right` at a positive height. The buildings are given in non-decreasing order by `left`. Buildings may overlap or hide one another. Viewed from far away, the skyline follows the maximum building height present at each horizontal coordinate.

Return the skyline as left-to-right key points `[x, height]` marking every change in visible height. Combine simultaneous starts and ends into the correct height at that coordinate, omit redundant adjacent points with equal heights, and include the final drop to ground level `0`. The result describes only the outer silhouette, not individual building edges concealed beneath taller rectangles.

### Function Contract
**Inputs**

- `buildings`: left-sorted triples `[left, right, height]`

**Return value**

Left-to-right key points `[x, height]`, including the final ground-level drop and no adjacent equal heights.

### Examples
**Example 1**

- Input: `[[2,9,10],[3,7,15],[5,12,12]]`
- Output begins: `[[2,10],[3,15],[7,12],[12,0]]`

**Example 2**

- Touching equal-height buildings merge into one plateau
- Output: one start and one final drop

**Example 3**

- A taller building is nested inside another
- Output rises and falls back to the outer height

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

The visible height changes only at a building's left or right boundary. Collect and sort all distinct boundary coordinates, then sweep them from left to right. Between two consecutive boundaries, the set of covering half-open intervals is unchanged, so no key point can occur in the interior.

Maintain a max-heap of candidate buildings as pairs `(-height, right)`, plus a permanent ground entry `(0, infinity)`. At coordinate `x`:

1. Push every building whose left boundary is `x`.
2. While the heap leader has `right <= x`, pop it because half-open interval `[left, right)` no longer covers `x`.
3. The negated height at the heap top is the current skyline height.
4. Emit `[x, height]` only if that height differs from the last emitted height.

Lazy expiration is subtle. An ended building may remain buried below a taller active building. That is safe: it cannot affect the maximum while buried. If it later reaches the heap top, the expiry loop removes it before its height is observed. Thus the heap may contain stale entries, but its post-cleanup leader is always active.

Processing all starts at the same coordinate before reading the height ensures shared starts produce one rise directly to the tallest building rather than several key points with the same `x`. Processing expirations at `right <= x` handles touching intervals correctly under half-open coverage. Equal-height touching buildings cause no emitted change and merge into one plateau.

For a tall building nested inside a shorter one, the heap first reports the outer height, then the inner height. When the inner interval expires, it is popped and the still-active outer building becomes visible again, producing the correct downward key point rather than dropping to zero.

All possible height changes occur at swept boundaries. After starts are inserted and every expired heap leader is removed, the heap top is the tallest building covering the current coordinate: any taller active building would be above it, while a stale top would have been removed. Therefore the sampled height at each boundary equals the true skyline. Emitting exactly when this height differs records every rise or fall and omits redundant adjacent equal segments. The ground sentinel guarantees the final building end emits height zero.

#### Complexity detail

There are at most `2n` distinct boundaries. Sorting them costs $O(n \log n)$. Each building is pushed once and popped at most once, with $O(\log n)$ heap operations, for total $O(n \log n)$ time. Boundary storage and the heap use $O(n)$ space.

#### Alternatives and edge cases

- Divide and conquer recursively builds and merges skylines in $O(n \log n)$ time and can be elegant but has more involved merge logic.
- Sampling every integer coordinate is infeasible when coordinates are large or sparse.
- Eagerly deleting an arbitrary ended heap entry requires an indexed heap or multiset; lazy deletion keeps the ordinary heap simple.
- Shared starts and ends must produce at most one key point per coordinate. Touching equal-height buildings form one plateau.
- The result must end with a ground-level point and must not contain adjacent equal heights.

</details>
