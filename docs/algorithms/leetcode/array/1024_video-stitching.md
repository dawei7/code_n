# Video Stitching

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1024 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Greedy |
| Official Link | [video-stitching](https://leetcode.com/problems/video-stitching/) |

## Problem Description & Examples
### Goal
Given video clips as time intervals and a target time `time`, choose the fewest clips needed to cover the whole interval `[0, time]`. Return `-1` if full coverage is impossible.

### Function Contract
**Inputs**

- `clips`: List[List[int]] intervals `[start, end]`
- `time`: int target end time

**Return value**

int - minimum number of clips, or `-1`

### Examples
**Example 1**

- Input: `clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10`
- Output: `3`

**Example 2**

- Input: `clips = [[0,1],[1,2]], time = 5`
- Output: `-1`

**Example 3**

- Input: `clips = [[0,4],[2,8]], time = 5`
- Output: `2`

---

## Underlying Base Algorithm(s)
Greedy interval coverage.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` auxiliary space if sorting in place
