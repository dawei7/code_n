# Minimum Time to Build Blocks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1199 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-time-to-build-blocks](https://leetcode.com/problems/minimum-time-to-build-blocks/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-time-to-build-blocks/).

### Goal
Workers must build all blocks. A worker can either build one block, taking that block's time, or split into two workers, taking `split` time. Return the minimum time needed to finish every block starting with one worker.

### Function Contract
**Inputs**

- `blocks`: Build times for each block.
- `split`: Time needed for one worker to split into two workers.

**Return value**

Minimum completion time.

### Examples
**Example 1**

- Input: `blocks = [1]`, `split = 1`
- Output: `1`

**Example 2**

- Input: `blocks = [1,2]`, `split = 5`
- Output: `7`

**Example 3**

- Input: `blocks = [1,2,3]`, `split = 1`
- Output: `4`

---

## Solution
### Approach
Use the greedy merging view. If two subplans finish in times `a <= b`, creating enough workers to run them in parallel costs `split + b`. Therefore, repeatedly combine the two smallest available completion times into `split + max(a, b)`.

A min-heap implements this directly; the final remaining time is the answer.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`.
- **Space Complexity**: `O(n)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
