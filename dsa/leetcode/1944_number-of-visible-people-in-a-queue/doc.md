# Number of Visible People in a Queue

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1944 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-visible-people-in-a-queue](https://leetcode.com/problems/number-of-visible-people-in-a-queue/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-visible-people-in-a-queue/).

### Goal
For each person in a queue, count how many people to their right they can see before the view is blocked by someone at least as tall.

### Function Contract
**Inputs**

- `heights`: distinct person heights in queue order.

**Return value**

Return an array where each entry is the number of visible people to the right of that position.

### Examples
**Example 1**

- Input: `heights = [10,6,8,5,11,9]`
- Output: `[3,1,2,1,1,0]`

**Example 2**

- Input: `heights = [5,1,2,3,10]`
- Output: `[4,1,1,1,0]`

**Example 3**

- Input: `heights = [3,2,1]`
- Output: `[1,1,0]`

---

## Solution
### Approach
Scan from right to left with a decreasing stack. A person sees every shorter height popped from the stack, and if one taller height remains, they see that blocker too.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
