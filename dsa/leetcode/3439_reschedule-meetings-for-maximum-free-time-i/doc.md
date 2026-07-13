# Reschedule Meetings for Maximum Free Time I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3439 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [reschedule-meetings-for-maximum-free-time-i](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/).

### Goal
Given a total time duration `eventTime` and a list of existing meetings defined by their start and end times, you are allowed to reschedule at most `k` meetings. The goal is to find the maximum possible duration of a single continuous block of free time after optimally shifting the chosen meetings.

### Function Contract
**Inputs**

- `eventTime` (int): The total duration of the day (from time 0 to `eventTime`).
- `k` (int): The maximum number of meetings you are permitted to reschedule.
- `startTime` (List[int]): A list of start times for the existing meetings.
- `endTime` (List[int]): A list of end times for the existing meetings.

**Return value**

- `int`: The maximum length of a continuous free time interval achievable.

### Examples
**Example 1**

- Input: `eventTime = 5, k = 1, startTime = [1, 3], endTime = [2, 4]`
- Output: `3`

**Example 2**

- Input: `eventTime = 10, k = 1, startTime = [0, 5, 7], endTime = [5, 8, 9]`
- Output: `6`

**Example 3**

- Input: `eventTime = 10, k = 2, startTime = [0, 2, 5], endTime = [1, 3, 7]`
- Output: `7`

---

## Solution
### Approach
The problem is solved using a **Sliding Window** approach on the gaps between meetings. First, calculate the durations of all gaps between consecutive meetings (including the gaps before the first meeting and after the last). By rescheduling `k` meetings, we can effectively merge `k+1` adjacent gaps into one large free block. We maintain a sliding window of size `k+1` over the array of gap durations to find the maximum sum.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of meetings. We iterate through the meetings once to calculate gaps and once through the gaps to find the maximum window sum.
- **Space Complexity**: `O(n)` to store the calculated gap durations.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
    # Calculate the gaps between meetings
    # Gaps: [0 to start[0]], [end[0] to start[1]], ..., [end[n-1] to eventTime]
    gaps = []

    # Gap before the first meeting
    gaps.append(startTime[0])

    # Gaps between meetings
    for i in range(len(startTime) - 1):
        gaps.append(startTime[i+1] - endTime[i])

    # Gap after the last meeting
    gaps.append(eventTime - endTime[-1])

    # We can merge k meetings, which means we can combine k+1 gaps
    window_size = k + 1

    # Use sliding window to find the maximum sum of k+1 consecutive gaps
    current_gap_sum = sum(gaps[:window_size])
    max_free_time = current_gap_sum

    for i in range(window_size, len(gaps)):
        current_gap_sum += gaps[i] - gaps[i - window_size]
        if current_gap_sum > max_free_time:
            max_free_time = current_gap_sum

    return max_free_time
```
</details>
