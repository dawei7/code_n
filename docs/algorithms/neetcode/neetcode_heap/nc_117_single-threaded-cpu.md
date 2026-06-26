## Problem Description & Examples
### Goal
Given `n` tasks `[enqueueTime, processingTime]` and a CPU that picks the available task with shortest processing time (ties broken by task index), return the order tasks are processed.

### Function Contract
**Inputs**

- `tasks`: List[List[int]] - [enqueueTime, processingTime]

**Return value**

List[int] - task indices in processing order

### Examples
**Example 1**

- Input: `tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]`
- Output: `[0, 2, 3, 1]`

**Example 2**

- Input: `tasks = [[7, 4], [1, 3]]`
- Output: `[1, 0]`

**Example 3**

- Input: `tasks = [[3, 5], [2, 3]]`
- Output: `[1, 0]`

---

## Underlying Base Algorithm(s)
- [Kth largest with heap](heap_02_kth-largest-element.md)
- [Top-K frequent elements](heap_03_top-k-frequent-elements.md)
- [Median in a stream](heap_04_median-in-a-stream.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
