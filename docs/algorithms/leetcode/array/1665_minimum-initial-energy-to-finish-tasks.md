# Minimum Initial Energy to Finish Tasks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1665 |
| Difficulty | Hard |
| Topics | Array, Greedy, Sorting |
| Official Link | [minimum-initial-energy-to-finish-tasks](https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/) |

## Problem Description & Examples
### Goal
Each task has an actual energy cost and a minimum energy required before starting it. Choose an order and find the smallest initial energy that allows all tasks to be completed.

### Function Contract
**Inputs**

- `tasks`: a list where each entry is `[actual, minimum]`.

**Return value**

Return the minimum starting energy needed to finish every task.

### Examples
**Example 1**

- Input: `tasks = [[1,2],[2,4],[4,8]]`
- Output: `8`

**Example 2**

- Input: `tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]`
- Output: `32`

**Example 3**

- Input: `tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]`
- Output: `27`

---

## Underlying Base Algorithm(s)
Use a greedy ordering. Tasks with larger `minimum - actual` are more restrictive because they require keeping more unused energy available before execution, so perform them earlier. After sorting by that gap descending, simulate the schedule and raise the starting energy whenever the current available energy would be below the next task's minimum.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` besides the sort storage
