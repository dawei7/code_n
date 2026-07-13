# Maximum Consecutive Floors Without Special Floors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2274 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-consecutive-floors-without-special-floors](https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/).

### Goal
Within an inclusive floor range, find the longest consecutive run containing no special floor.

### Function Contract
**Inputs**

- `bottom`, `top`: the lowest and highest floors in the building section.
- `special`: distinct special floor numbers within that range.

**Return value**

The maximum number of consecutive non-special floors.

### Examples
**Example 1**

- Input: `bottom = 2`, `top = 9`, `special = [4, 6]`
- Output: `3`

**Example 2**

- Input: `bottom = 6`, `top = 8`, `special = []`
- Output: `3`

**Example 3**

- Input: `bottom = 2`, `top = 3`, `special = [2]`
- Output: `1`

---

## Solution
### Approach
Sort special floors. Compare the gap below the first special floor, every gap between consecutive special floors, and the gap above the last one. Sentinel boundaries at `bottom - 1` and `top + 1` make every run equal to the difference between adjacent boundaries minus one.

### Complexity Analysis
- **Time Complexity**: `O(s log s)`
- **Space Complexity**: `O(1)` auxiliary space when sorting in place

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
