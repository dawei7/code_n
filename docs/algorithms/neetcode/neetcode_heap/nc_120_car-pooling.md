## Problem Description & Examples
### Goal
A vehicle can carry at most `capacity` passengers. Given `trips = [[numPassengers, from, to], ...]`, return `True` if all trips can be completed without exceeding capacity.

### Function Contract
**Inputs**

- `trips`: List[List[int]] - [passengers, from, to]
- `capacity`: int

**Return value**

bool - True if all trips can be completed

### Examples
**Example 1**

- Input: `trips = [[2, 1, 5], [3, 3, 7]], capacity = 4`
- Output: `False`

**Example 2**

- Input: `trips = [[5, 16, 20]], capacity = 8`
- Output: `True`

**Example 3**

- Input: `trips = [[3, 18, 30]], capacity = 9`
- Output: `True`

---

## Underlying Base Algorithm(s)
- [Kth largest with heap](heap_02_kth-largest-element.md)
- [Top-K frequent elements](heap_03_top-k-frequent-elements.md)
- [Median in a stream](heap_04_median-in-a-stream.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
