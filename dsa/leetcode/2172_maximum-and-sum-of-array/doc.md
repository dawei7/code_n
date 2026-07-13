# Maximum AND Sum of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2172 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-and-sum-of-array](https://leetcode.com/problems/maximum-and-sum-of-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-and-sum-of-array/).

### Goal
Place every number into one of the slots numbered `1` through `numSlots`, with at most two numbers per slot. Maximize the sum of each number bitwise-ANDed with its assigned slot number.

### Function Contract
**Inputs**

- `nums`: the values to assign; its length is at most twice the slot count.
- `numSlots`: the number of numbered slots.

**Return value**

The maximum achievable AND sum.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4, 5, 6]`, `numSlots = 3`
- Output: `9`

**Example 2**

- Input: `nums = [1, 3, 10, 4, 7, 1]`, `numSlots = 9`
- Output: `24`

**Example 3**

- Input: `nums = [1]`, `numSlots = 1`
- Output: `1`

---

## Solution
### Approach
Use dynamic programming over slot occupancy encoded as a base-three mask: each trit is `0`, `1`, or `2` according to how many numbers occupy that slot. The number of filled positions determines which `nums` value to assign next. For every slot with occupancy below two, transition by increasing its trit and adding `nums[i] & slot_number`.

### Complexity Analysis
- **Time Complexity**: `O(numSlots * 3^numSlots)`
- **Space Complexity**: `O(3^numSlots)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
