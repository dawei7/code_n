# Video Stitching

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1024 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [video-stitching](https://leetcode.com/problems/video-stitching/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/video-stitching/).

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

## Solution
### Approach
Greedy interval coverage.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` auxiliary space if sorting in place

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1024: Video Stitching."""


def solve(clips: list[list[int]], time: int) -> int:
    clips.sort()
    answer = 0
    current_end = 0
    farthest = 0
    i = 0

    while current_end < time:
        while i < len(clips) and clips[i][0] <= current_end:
            farthest = max(farthest, clips[i][1])
            i += 1
        if farthest == current_end:
            return -1
        answer += 1
        current_end = farthest
    return answer
```
</details>
