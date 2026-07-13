# Count Tested Devices After Test Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2960 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-tested-devices-after-test-operations](https://leetcode.com/problems/count-tested-devices-after-test-operations/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-tested-devices-after-test-operations/).

### Goal
Given an array of integers representing the battery percentages of a sequence of devices, simulate a testing process. For each device, if its battery percentage is greater than the number of devices already tested, it is considered "tested" and the count of tested devices increases. Crucially, every time a device is successfully tested, the battery percentage of all subsequent, untested devices is reduced by 1. Determine the total number of devices that pass the test.

### Function Contract
**Inputs**

- `batteryPercentages`: A list of integers where `batteryPercentages[i]` represents the initial battery level of the i-th device.

**Return value**

- An integer representing the total count of devices that were successfully tested.

### Examples
**Example 1**

- Input: `batteryPercentages = [1, 1, 2, 1, 3]`
- Output: `3`

**Example 2**

- Input: `batteryPercentages = [0, 1, 2]`
- Output: `2`

**Example 3**

- Input: `batteryPercentages = [0, 0, 0]`
- Output: `0`

---

## Solution
### Approach
The problem can be solved using a **Greedy Simulation** approach. By maintaining a running counter of how many devices have been successfully tested, we can determine if the current device's effective battery level (initial level minus the number of previously tested devices) is greater than zero.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the list exactly once.
- **Space Complexity**: `O(1)`, as we only use a single integer variable to track the number of tested devices.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(batteryPercentages: list[int]) -> int:
    """
    Calculates the number of tested devices by tracking the number of
    successful tests performed so far.
    """
    tested_count = 0

    for battery in batteryPercentages:
        # The effective battery is the original battery minus the number
        # of devices already tested.
        if battery - tested_count > 0:
            tested_count += 1

    return tested_count
```
</details>
