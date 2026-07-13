# Design Skiplist

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1206 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Linked List, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [design-skiplist](https://leetcode.com/problems/design-skiplist/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/design-skiplist/).

### Goal
Design a skiplist supporting search, insertion, and deletion. Duplicate values may exist, and deletion removes one occurrence.

### Design Contract
**Operations**

- `Skiplist()`: Initialize the data structure.
- `search(target)`: Return whether `target` exists.
- `add(num)`: Insert `num`.
- `erase(num)`: Remove one occurrence of `num` and return whether removal succeeded.

**Return value**

Operation-specific return values as described above.

### Examples
**Example 1**

- Input: `["Skiplist","add","add","add","search","add","search","erase","erase","search"]`, `[[],[1],[2],[3],[0],[4],[1],[0],[1],[1]]`
- Output: `[null,null,null,null,false,null,true,false,true,false]`

**Example 2**

- Input: `["Skiplist","add","add","search","erase","search"]`, `[[],[5],[5],[5],[5],[5]]`
- Output: `[null,null,null,true,true,true]`

**Example 3**

- Input: `["Skiplist","search","erase"]`, `[[],[10],[10]]`
- Output: `[null,false,false]`

---

## Solution
### Approach
A skiplist stores sorted linked lists at multiple levels. Higher levels skip over many values, while level `0` contains all values. Search walks right while the next value is smaller than the target, then drops down a level.

Insertion records the predecessor at each level, randomly chooses a height for the new node, and splices it into those levels. Erase finds predecessors and unlinks one matching node wherever it appears.

### Complexity Analysis
- **Time Complexity**: Expected `O(log n)` per operation.
- **Space Complexity**: Expected `O(n)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
