# Number of Valid Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1063 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-valid-subarrays](https://leetcode.com/problems/number-of-valid-subarrays/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-valid-subarrays/).

### Goal
Count subarrays where the first element is less than or equal to every other element in that subarray.

### Function Contract
**Inputs**

- `nums`: List of integers.

**Return value**

Number of valid subarrays.

### Examples
**Example 1**

- Input: `nums = [1, 4, 2, 5, 3]`
- Output: `11`

**Example 2**

- Input: `nums = [3, 2, 1]`
- Output: `3`

**Example 3**

- Input: `nums = [2, 2, 2]`
- Output: `6`

---

## Solution
### Approach
For each index, the valid subarrays starting there continue until the first strictly smaller element to its right. A monotonic increasing stack can find and count these ranges in one pass.

Scan left to right while keeping indices whose values are nondecreasing. When a smaller value appears, pop larger values; each popped index can no longer extend past the current position, so add its contribution. A sentinel or final cleanup accounts for ranges that reach the end.

### Complexity Analysis
- **Time Complexity**: `O(n)`, because each index is pushed and popped at most once.
- **Space Complexity**: `O(n)` for the monotonic stack.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
