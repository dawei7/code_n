# Design File System

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1166 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Design, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/design-file-system/) |

## Problem Description

### Goal

Design a file system that creates new absolute paths and associates an integer value with each one. A valid path consists of one or more components, where every component begins with `/` and then contains one or more lowercase English letters. Thus `"/leetcode"` and `"/leetcode/problems"` are valid, while `""` and `"/"` are not.

The system begins without any created paths. A new path may be created only when it does not already exist and its immediate parent already exists; a one-component path has the implicit root as its parent and may be created directly. Existing values cannot be overwritten. A lookup returns the stored value for an existing path and `-1` for a missing path.

### Function Contract

**Operations**

- `FileSystem()`: Initialize an empty file system.
- `createPath(path, value)`: If `path` is new and its parent exists, associate it with `value` and return `true`; otherwise return `false` without changing the system.
- `get(path)`: Return the value associated with `path`, or `-1` when it has not been created.
- Every `path` has length from $2$ through $100$, every value is from $1$ through $10^9$, and at most $10^4$ method calls are made.
- Define

$$
S = \sum_{o \in \text{operations}} \lvert \operatorname{path}(o) \rvert.
$$

**Return value**

- Each operation returns its method-specific result described above.

### Examples

**Example 1**

- Input: `operations = [["createPath", ["/a", 1]], ["get", ["/a"]]]`
- Output: `[true, 1]`

**Example 2**

- Input: `operations = [["createPath", ["/leet", 1]], ["createPath", ["/leet/code", 2]], ["get", ["/leet/code"]], ["createPath", ["/c/d", 1]], ["get", ["/c"]]]`
- Output: `[true, true, 2, false, -1]`

The nested path `"/leet/code"` succeeds after its parent is present. Creating `"/c/d"` fails because `"/c"` does not exist.
