# Reschedule Meetings for Maximum Free Time II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3440 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [reschedule-meetings-for-maximum-free-time-ii](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/).

### Goal
Given the total time available in a day and a list of scheduled meetings, determine the maximum possible duration of a single continuous block of free time that can be achieved by moving exactly one meeting to a different position. The moved meeting must not overlap with any other existing meetings.

### Function Contract
**Inputs**

- `eventTime` (int): The total duration of the day (from time 0 to `eventTime`).
- `startTime` (List[int]): A list of start times for each meeting.
- `endTime` (List[int]): A list of end times for each meeting.

**Return value**

- `int`: The maximum length of a continuous free time interval achievable after relocating one meeting.

### Examples
**Example 1**

- Input: `eventTime = 5, startTime = [1, 3], endTime = [2, 4]`
- Output: `3`
- Explanation: Moving the meeting [1, 2] to [4, 5] creates a free block from 0 to 3.

**Example 2**

- Input: `eventTime = 10, startTime = [0, 7, 9], endTime = [1, 8, 10]`
- Output: `5`

**Example 3**

- Input: `eventTime = 5, startTime = [0, 1, 2, 3, 4], endTime = [1, 2, 3, 4, 5]`
- Output: `0`

---

## Solution
### Approach
The problem is solved using a greedy approach combined with prefix/suffix maximums. We first identify all existing gaps between meetings. To determine if a meeting can be moved into a gap, we check if the gap size is at least the duration of the meeting. We use a prefix maximum array to track the largest gaps to the left of a meeting and a suffix maximum array for gaps to the right, allowing us to efficiently calculate the potential free time created by shifting a meeting.

### Complexity Analysis
- **Time Complexity**: O(N log N) due to sorting the meetings by start time, where N is the number of meetings. The subsequent linear scans are O(N).
- **Space Complexity**: O(N) to store the gaps and the prefix/suffix maximum arrays.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(eventTime: int, startTime: list[int], endTime: list[int]) -> int:
    n = len(startTime)
    meetings = sorted(zip(startTime, endTime))

    # Calculate gaps between meetings
    # gaps[i] is the gap between meeting i-1 and meeting i
    # gaps[0] is before the first meeting, gaps[n] is after the last
    gaps = [0] * (n + 1)
    gaps[0] = meetings[0][0]
    for i in range(1, n):
        gaps[i] = meetings[i][0] - meetings[i-1][1]
    gaps[n] = eventTime - meetings[n-1][1]

    # Precompute prefix and suffix max gaps
    pref_max = [0] * (n + 1)
    suff_max = [0] * (n + 1)
    for i in range(n + 1):
        pref_max[i] = gaps[i]
        if i > 0:
            pref_max[i] = max(pref_max[i], pref_max[i-1])

    for i in range(n, -1, -1):
        suff_max[i] = gaps[i]
        if i < n:
            suff_max[i] = max(suff_max[i], suff_max[i+1])

    # To efficiently check if a gap exists elsewhere,
    # we need to know the second largest gap.
    # We use a sorted list of all gaps to query this.
    import bisect
    sorted_gaps = sorted(gaps)

    def get_max_gap_excluding(val):
        # Find index of val and return the max of the remaining
        idx = bisect.bisect_left(sorted_gaps, val)
        # Remove one instance of val
        temp = sorted_gaps[:idx] + sorted_gaps[idx+1:]
        return temp[-1] if temp else 0

    ans = 0
    for i in range(n):
        duration = meetings[i][1] - meetings[i][0]

        # Can we move meeting i into a gap?
        # The gap created by removing meeting i is gaps[i] + gaps[i+1] + duration
        # We check if we can fit this meeting into any other gap

        # Max gap available excluding the current surrounding gaps
        # We need the largest gap in the array that is not gaps[i] or gaps[i+1]
        # Actually, we just need the largest gap available in the whole set
        # excluding the ones we are merging.

        # Optimization: check if the largest gap (excluding current) >= duration
        # We use the precomputed sorted_gaps
        best_other = 0
        # If we remove gaps[i] and gaps[i+1], the largest remaining is:
        # We can use a frequency map or just check the two largest
        # For simplicity, check the max of (pref_max[i-1], suff_max[i+2])
        if i > 0:
            best_other = max(best_other, pref_max[i-1])
        if i + 2 <= n:
            best_other = max(best_other, suff_max[i+2])

        if best_other >= duration:
            ans = max(ans, gaps[i] + gaps[i+1] + duration)
        else:
            ans = max(ans, gaps[i] + gaps[i+1])

    return ans
```
</details>
