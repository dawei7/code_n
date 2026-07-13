# Single-Threaded CPU

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1834 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [single-threaded-cpu](https://leetcode.com/problems/single-threaded-cpu/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/single-threaded-cpu/).

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

## Solution
### Approach
- [Kth largest with heap](heap_02_kth-largest-element.md)
- [Top-K frequent elements](heap_03_top-k-frequent-elements.md)
- [Median in a stream](heap_04_median-in-a-stream.md)

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
