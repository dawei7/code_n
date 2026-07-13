# Dinner Plate Stacks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1172 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, Stack, Design, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [dinner-plate-stacks](https://leetcode.com/problems/dinner-plate-stacks/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/dinner-plate-stacks/).

### Goal
Design a row of stacks, all with the same capacity. Pushes go to the leftmost stack with free space, while pops come from the rightmost non-empty stack. The API also supports popping from a specific stack index.

### Design Contract
**Operations**

- `DinnerPlates(capacity)`: Initialize the stack row.
- `push(val)`: Push `val` into the leftmost stack that is not full.
- `pop()`: Remove and return the top of the rightmost non-empty stack, or `-1`.
- `popAtStack(index)`: Remove and return the top of stack `index`, or `-1`.

**Return value**

Operation-specific return values as described above.

### Examples
**Example 1**

- Input: `["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]`, `[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]`
- Output: `[null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]`

**Example 2**

- Input: `["DinnerPlates","pop"]`, `[[1],[]]`
- Output: `[null,-1]`

**Example 3**

- Input: `["DinnerPlates","push","popAtStack","pop"]`, `[[1],[7],[3],[]]`
- Output: `[null,null,-1,7]`

---

## Solution
### Approach
Maintain the stacks in an array. A min-heap stores indices of stacks that currently have free space, letting `push` find the leftmost available stack. Before using a heap index, discard stale entries that point past the current stack list or to a stack that is already full.

For `pop`, remove empty stacks from the right end, then pop from the last remaining stack. For `popAtStack`, pop directly if the index is valid and non-empty, then add that index back to the available heap.

### Complexity Analysis
- **Time Complexity**: `O(log s)` for `push` and `popAtStack`, with `s` stacks; `pop` is amortized efficient while trimming empty stacks.
- **Space Complexity**: `O(n)`, where `n` is the number of stored values plus stack metadata.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
