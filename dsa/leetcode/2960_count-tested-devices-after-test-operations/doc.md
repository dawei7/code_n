# Count Tested Devices After Test Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2960 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-tested-devices-after-test-operations/) |

## Problem Description
### Goal
You are given a 0-indexed array `batteryPercentages`, where position `i` holds
the battery percentage of device `i`. Process the devices once in increasing
index order.

When the current device has battery greater than zero, test it and increase the
tested-device count. That successful test decreases every later device's
battery by one, with each value clamped at zero. If the current battery is
already zero, skip the device and do not change later batteries. Continue to
the next index in either case.

Return the number of devices tested after the ordered process finishes.

### Function Contract
**Inputs**

- `batteryPercentages`: the devices' initial battery percentages in processing order

Let $N=\lvert\texttt{batteryPercentages}\rvert$. The contract guarantees
$1\le N\le100$ and $0\le\texttt{batteryPercentages[i]}\le100$.

**Return value**

The number of devices whose battery is positive when their turn is reached
after all decrements caused by earlier successful tests.

### Examples
**Example 1**

- Input: `batteryPercentages = [1,1,2,1,3]`
- Output: `3`
- Explanation: Devices `0`, `2`, and `4` remain positive when processed; their successful tests produce the intermediate batteries described by the operations.

**Example 2**

- Input: `batteryPercentages = [0,1,2]`
- Output: `2`
- Explanation: Device `0` is skipped, device `1` is tested and decreases the final battery to one, and device `2` is then tested.
