# Delete Duplicate Folders in System

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1948 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Depth-First Search, Trie, Sorting, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [delete-duplicate-folders-in-system](https://leetcode.com/problems/delete-duplicate-folders-in-system/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/delete-duplicate-folders-in-system/).

### Goal
Given folder paths, remove every folder whose entire subtree structure is identical to another folder's subtree. Return the remaining folder paths after all duplicate subtrees are deleted together.

### Function Contract
**Inputs**

- `paths`: a list of folder paths, each represented as folder-name components.

**Return value**

Return the paths that remain, in any valid order.

### Examples
**Example 1**

- Input: `paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]`
- Output: `[["d"],["d","a"]]`

**Example 2**

- Input: `paths = [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["c","b","x"]]`
- Output: `[]`

**Example 3**

- Input: `paths = [["a"],["a","x"],["a","x","y"],["a","z"],["b"],["b","x"],["b","x","y"],["b","z"]]`
- Output: `[]`

---

## Solution
### Approach
Build a trie of folders. Serialize each node by its sorted child names and child serializations; equal non-empty serializations identify duplicate subtrees. A final DFS emits only paths whose node serialization is not duplicated.

### Complexity Analysis
- **Time Complexity**: `O(total path length log d)`, with sorting by child names.
- **Space Complexity**: `O(total path length)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
