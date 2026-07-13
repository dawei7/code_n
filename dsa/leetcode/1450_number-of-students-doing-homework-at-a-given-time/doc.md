# Number of Students Doing Homework at a Given Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1450 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-students-doing-homework-at-a-given-time](https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/).

### Goal
Count students whose homework interval includes the given query time.

### Function Contract
**Inputs**

- `startTime`: start times for each student.
- `endTime`: end times for each student.
- `queryTime`: the time to check.

**Return value**

The number of intervals `[startTime[i], endTime[i]]` containing `queryTime`.

### Examples
**Example 1**

- Input: `startTime = [1,2,3], endTime = [3,2,7], queryTime = 4`
- Output: `1`

**Example 2**

- Input: `startTime = [4], endTime = [4], queryTime = 4`
- Output: `1`

**Example 3**

- Input: `startTime = [9,8,7], endTime = [10,9,8], queryTime = 6`
- Output: `0`

---

## Solution
### Approach
Direct interval counting.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(start_time, end_time, query_time):
    return sum(start <= query_time <= end for start, end in zip(start_time, end_time))
```
</details>
