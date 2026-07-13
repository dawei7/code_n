# Button with Longest Push Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3386 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [button-with-longest-push-time](https://leetcode.com/problems/button-with-longest-push-time/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/button-with-longest-push-time/).

### Goal
Given a sequence of button presses represented as a list of events, where each event contains the button index and the timestamp at which the press ended, determine which button took the longest time to press. If multiple buttons share the same maximum duration, return the one with the smallest index.

### Function Contract
**Inputs**

- `events`: A list of lists, where each `events[i]` is `[index, time]`, representing the button ID and the absolute time the press concluded.

**Return value**

- An integer representing the index of the button that required the longest duration to press.

### Examples
**Example 1**

- Input: `events = [[1, 2], [2, 5], [3, 9], [1, 15]]`
- Output: `1`
- Explanation: Durations are: Button 1 (2-0=2), Button 2 (5-2=3), Button 3 (9-5=4), Button 1 (15-9=6). Max duration is 6 for button 1.

**Example 2**

- Input: `events = [[10, 5], [1, 7]]`
- Output: `10`
- Explanation: Durations are: Button 10 (5-0=5), Button 1 (7-5=2). Max duration is 5 for button 10.

**Example 3**

- Input: `events = [[9, 4], [19, 5]]`
- Output: `9`

---

## Solution
### Approach
Linear scan (Single pass iteration). We maintain the current maximum duration and the corresponding button index, updating them whenever a strictly greater duration is found or a tie occurs with a smaller index.

### Complexity Analysis
- **Time Complexity**: O(n), where n is the number of events, as we iterate through the list exactly once.
- **Space Complexity**: O(1), as we only store a few variables to track the maximum duration and the best button index.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(events: list[list[int]]) -> int:
    max_duration = -1
    result_index = -1
    prev_time = 0

    for index, time in events:
        duration = time - prev_time

        if duration > max_duration:
            max_duration = duration
            result_index = index
        elif duration == max_duration:
            if index < result_index:
                result_index = index

        prev_time = time

    return result_index
```
</details>
