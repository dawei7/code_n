# Replace Elements in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2295 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [replace-elements-in-an-array](https://leetcode.com/problems/replace-elements-in-an-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/replace-elements-in-an-array/).

### Goal
Apply replacement operations to an array of distinct values. Each operation replaces the existing value `old` with a new value `new` that is not currently present.

### Function Contract
**Inputs**

- `nums`: an array of distinct integers.
- `operations`: ordered pairs `[old, new]`.

**Return value**

The array after all operations, preserving element positions.

### Examples
**Example 1**

- Input: `nums = [1, 2, 4, 6]`, `operations = [[1, 3], [4, 7], [6, 1]]`
- Output: `[3, 2, 7, 1]`

**Example 2**

- Input: `nums = [1]`, `operations = [[1, 2], [2, 3]]`
- Output: `[3]`

**Example 3**

- Input: `nums = [5, 9]`, `operations = [[9, 4]]`
- Output: `[5, 4]`

---

## Solution
### Approach
Map each current value to its array index. For operation `[old, new]`, remove `old` from the map, assign `new` to the same index, update the array at that index, and store the new mapping. Distinctness guarantees one position per value.

### Complexity Analysis
- **Time Complexity**: `O(n + q)` expected
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
