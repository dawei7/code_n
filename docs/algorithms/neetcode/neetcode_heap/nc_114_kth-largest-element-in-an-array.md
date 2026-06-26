## Problem Description & Examples
### Goal
Given an integer array `nums` and integer `k`, return the k-th largest element in the array (not distinct).

### Function Contract
**Inputs**

- `nums`: List[int]
- `k`: int

**Return value**

int - k-th largest element

### Examples
**Example 1**

- Input: `nums = [3, 2, 1, 5, 6, 4], k = 2`
- Output: `5`

**Example 2**

- Input: `nums = [-2, 94], k = 2`
- Output: `-2`

**Example 3**

- Input: `nums = [-66, 45], k = 1`
- Output: `45`

---

## Underlying Base Algorithm(s)
- [Kth largest with heap](heap_02_kth-largest-element.md)
- [Top-K frequent elements](heap_03_top-k-frequent-elements.md)
- [Median in a stream](heap_04_median-in-a-stream.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
