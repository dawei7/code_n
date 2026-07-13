# Robot Bounded In Circle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1041 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, String, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [robot-bounded-in-circle](https://leetcode.com/problems/robot-bounded-in-circle/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/robot-bounded-in-circle/).

### Goal
A robot starts at the origin facing north and repeatedly executes the same instruction string forever. Each instruction is `G` for move forward, `L` for turn left, or `R` for turn right. Determine whether the robot's path stays inside some circle.

### Function Contract
**Inputs**

- `instructions`: String of `G`, `L`, and `R` commands.

**Return value**

Boolean indicating whether repeating the commands forever keeps the robot bounded.

### Examples
**Example 1**

- Input: `instructions = "GGLLGG"`
- Output: `true`

**Example 2**

- Input: `instructions = "GG"`
- Output: `false`

**Example 3**

- Input: `instructions = "GL"`
- Output: `true`

---

## Solution
### Approach
Simulate one execution of the instruction string. After one cycle, the path is bounded if either the robot returns to the origin or it faces a direction other than north.

If it returns to the origin, each cycle repeats the same loop. If it changes direction, then after at most four cycles the heading rotates back to north and the net movement cancels. If it is away from the origin and still facing north, every cycle moves it farther in the same direction.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of `instructions`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
