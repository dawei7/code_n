## Problem Description & Examples
### Goal
Given an array of `points` (each `[x, y]`) and integer `k`, return the `k` points closest to the origin (0,0). Distance = sqrt(x^2 + y^2) but we compare x^2 + y^2.

### Function Contract
**Inputs**

- `points`: List[List[int]] - [x,y] coordinates
- `k`: int

**Return value**

List[List[int]] - k closest points

### Examples
**Example 1**

- Input: `points = [[1, 3], [-2, 2]], k = 1`
- Output: `[[-2, 2]]`

**Example 2**

- Input: `points = [[-2, 94], [7, -90]], k = 1`
- Output: `[[7, -90]]`

**Example 3**

- Input: `points = [[-66, 45], [95, -84]], k = 1`
- Output: `[[-66, 45]]`

---

## Underlying Base Algorithm(s)
- [Kth largest with heap](heap_02_kth-largest-element.md)
- [Top-K frequent elements](heap_03_top-k-frequent-elements.md)
- [Median in a stream](heap_04_median-in-a-stream.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
