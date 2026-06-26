## Problem Description & Examples
### Goal
You have a collection of `stones` with various weights. On each turn, take the two heaviest stones and smash them together. If equal, both are destroyed; otherwise the smaller is destroyed and the larger is reduced by the smaller weight. Return the weight of the last stone (or 0 if none remain).

### Function Contract
**Inputs**

- `stones`: List[int]

**Return value**

int - weight of last stone or 0

### Examples
**Example 1**

- Input: `stones = [2, 7, 4, 1, 8, 1]`
- Output: `1`

**Example 2**

- Input: `stones = [50, 98]`
- Output: `48`

**Example 3**

- Input: `stones = [18, 73]`
- Output: `55`

---

## Underlying Base Algorithm(s)
- [Kth largest with heap](heap_02_kth-largest-element.md)
- [Top-K frequent elements](heap_03_top-k-frequent-elements.md)
- [Median in a stream](heap_04_median-in-a-stream.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
