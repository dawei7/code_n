# Design File System

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1166 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Design, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [design-file-system](https://leetcode.com/problems/design-file-system/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/design-file-system/).

### Goal
Design a file-system-like key-value store for absolute paths. A path can be created only if it does not already exist and its parent path already exists. Values are integers.

### Design Contract
**Operations**

- `FileSystem()`: Create an empty file system.
- `createPath(path, value)`: Create `path` with `value` and return whether creation succeeded.
- `get(path)`: Return the value for `path`, or `-1` if the path does not exist.

**Return value**

Operation-specific return values as described above.

### Examples
**Example 1**

- Input: `["FileSystem", "createPath", "get"]`, `[[], ["/a", 1], ["/a"]]`
- Output: `[null, true, 1]`

**Example 2**

- Input: `["FileSystem", "createPath", "createPath", "get"]`, `[[], ["/leet", 1], ["/leet/code", 2], ["/leet/code"]]`
- Output: `[null, true, true, 2]`

**Example 3**

- Input: `["FileSystem", "createPath", "get"]`, `[[], ["/c/d", 1], ["/c"]]`
- Output: `[null, false, -1]`

---

## Solution
### Approach
Store created paths in a hash map from full path string to value. To create a path, reject empty/root paths and existing paths, then extract the parent prefix before the final slash. The parent is valid if it is root or already exists in the map.

A trie is also natural, but a hash map keeps each operation direct and compact.

### Complexity Analysis
- **Time Complexity**: `O(L)` per operation, where `L` is the path length.
- **Space Complexity**: `O(T)`, where `T` is the total length of stored paths.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
