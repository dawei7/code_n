# Maximize the Topmost Element After K Moves

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2202 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximize-the-topmost-element-after-k-moves](https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/).

### Goal
Perform exactly `k` moves on a stack represented from top to bottom. A move either removes the top element or returns one previously removed element to the top. Maximize the final top value, or return `-1` if the stack must be empty.

### Function Contract
**Inputs**

- `nums`: stack values ordered from top to bottom.
- `k`: the exact number of moves.

**Return value**

The maximum possible top value after exactly `k` moves, or `-1` when no element can remain.

### Examples
**Example 1**

- Input: `nums = [5, 2, 2, 4, 0, 6]`, `k = 4`
- Output: `5`

**Example 2**

- Input: `nums = [2]`, `k = 1`
- Output: `-1`

**Example 3**

- Input: `nums = [1, 2, 3]`, `k = 2`
- Output: `3`

---

## Solution
### Approach
Handle the one-element parity case separately. Otherwise, a final top can be either any of the first `k - 1` values, removed and restored on the last move, or `nums[k]`, exposed by making all `k` moves removals when that index exists. Return the maximum among these candidates.

### Complexity Analysis
- **Time Complexity**: `O(min(n, k))`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
