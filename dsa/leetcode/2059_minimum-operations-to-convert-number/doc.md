# Minimum Operations to Convert Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2059 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-operations-to-convert-number](https://leetcode.com/problems/minimum-operations-to-convert-number/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-operations-to-convert-number/).

### Goal
Starting from `start`, repeatedly choose a number from `nums` and apply addition, subtraction, or xor. Find the fewest operations needed to reach `goal`.

### Function Contract
**Inputs**

- `nums`: operation operands.
- `start`: starting value.
- `goal`: target value.

**Return value**

Return the minimum operation count, or `-1` if unreachable under the allowed search rule.

### Examples
**Example 1**

- Input: `nums = [2,4,12], start = 2, goal = 12`
- Output: `2`

**Example 2**

- Input: `nums = [3,5,7], start = 0, goal = -4`
- Output: `2`

**Example 3**

- Input: `nums = [2,8,16], start = 0, goal = 1`
- Output: `-1`

---

## Solution
### Approach
Use BFS over values in the allowed intermediate range `0..1000`. From each value, generate `x + num`, `x - num`, and `x ^ num`. Values outside the range are not expanded, but if one equals `goal`, the search can stop.

### Complexity Analysis
- **Time Complexity**: `O(1001 * len(nums))`
- **Space Complexity**: `O(1001)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
