# Print in Order

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1114 |
| Difficulty | Easy |
| Category | Concurrency |
| Topics | Concurrency |
| Supported Languages | Tracked only |
| Official Link | [print-in-order](https://leetcode.com/problems/print-in-order/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/print-in-order/).

### Goal
Three methods may be called by separate threads in any arrival order. Ensure their side effects always happen in the logical order `first`, then `second`, then `third`.

### Function Contract
**Inputs**

- `printFirst`: callable side effect for the first step
- `printSecond`: callable side effect for the second step
- `printThird`: callable side effect for the third step

**Return value**

None - synchronization controls the order of side effects

### Examples
**Example 1**

- Input: `arrival = [1, 2, 3]`
- Output: `"firstsecondthird"`

**Example 2**

- Input: `arrival = [1, 3, 2]`
- Output: `"firstsecondthird"`

**Example 3**

- Input: `arrival = [3, 2, 1]`
- Output: `"firstsecondthird"`

---

## Solution
### Approach
One-way synchronization gates between ordered phases.

### Complexity Analysis
- **Time Complexity**: `O(1)` synchronization work per method call
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
