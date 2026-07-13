# Count Days Without Meetings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3169 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-days-without-meetings](https://leetcode.com/problems/count-days-without-meetings/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-days-without-meetings/).

### Goal
Given a total number of days in a period (labeled 1 to `days`) and a list of scheduled meeting intervals, calculate the number of days within that period where no meetings are scheduled.

### Function Contract
**Inputs**

- `days`: An integer representing the total number of days in the period.
- `meetings`: A list of lists, where each inner list `[start, end]` represents a meeting spanning from day `start` to day `end` inclusive.

**Return value**

- An integer representing the count of days that are not covered by any meeting interval.

### Examples
**Example 1**

- Input: `days = 10, meetings = [[5,7],[1,3],[9,10]]`
- Output: `2`

**Example 2**

- Input: `days = 5, meetings = [[2,4]]`
- Output: `3`

**Example 3**

- Input: `days = 6, meetings = [[1,6]]`
- Output: `0`

---

## Solution
### Approach
The problem is solved using the **Interval Merging** technique. By sorting the meeting intervals by their start times, we can iterate through them to merge overlapping or contiguous intervals. Once merged, the total number of days occupied by meetings is the sum of the lengths of these disjoint intervals. Subtracting this sum from the total `days` yields the result.

### Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the number of meetings, due to the sorting step. The subsequent linear scan takes `O(N)`.
- **Space Complexity**: `O(1)` or `O(N)` depending on the sorting implementation's space requirements, as we only store a few variables to track the current merged interval.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(days: int, meetings: list[list[int]]) -> int:
    if not meetings:
        return days

    # Sort a local copy by start time.
    meetings = sorted(meetings)

    merged_days = 0
    # Initialize with the first meeting
    curr_start, curr_end = meetings[0]

    for i in range(1, len(meetings)):
        next_start, next_end = meetings[i]

        if next_start <= curr_end + 1:
            # Overlapping or contiguous, extend the current interval
            curr_end = max(curr_end, next_end)
        else:
            # Gap found, add the duration of the previous interval
            merged_days += (curr_end - curr_start + 1)
            curr_start, curr_end = next_start, next_end

    # Add the last interval
    merged_days += (curr_end - curr_start + 1)

    return days - merged_days
```
</details>
