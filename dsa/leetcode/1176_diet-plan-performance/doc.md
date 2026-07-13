# Diet Plan Performance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1176 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [diet-plan-performance](https://leetcode.com/problems/diet-plan-performance/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/diet-plan-performance/).

### Goal
Evaluate every consecutive `k`-day calorie window. A window below `lower` loses one point, a window above `upper` gains one point, and a window inside the range changes nothing.

### Function Contract
**Inputs**

- `calories`: Calories consumed per day.
- `k`: Window length.
- `lower`: Lower threshold.
- `upper`: Upper threshold.

**Return value**

Final performance score.

### Examples
**Example 1**

- Input: `calories = [1,2,3,4,5]`, `k = 1`, `lower = 3`, `upper = 3`
- Output: `0`

**Example 2**

- Input: `calories = [3,2]`, `k = 2`, `lower = 0`, `upper = 1`
- Output: `1`

**Example 3**

- Input: `calories = [6,5,0,0]`, `k = 2`, `lower = 1`, `upper = 5`
- Output: `0`

---

## Solution
### Approach
Maintain the sum of a sliding window of length `k`. After each complete window, compare its sum with `lower` and `upper` and update the score accordingly.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of days.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
