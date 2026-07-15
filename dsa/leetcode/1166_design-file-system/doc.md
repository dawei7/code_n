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

### Required Complexity

- **Time:** $O(S)$
- **Space:** $O(S)$

<details>
<summary>Approach</summary>

#### General

**Store complete paths as keys.** Maintain a hash map from each successfully created path string to its integer value. Full paths are already unique identifiers, so a separate tree node is unnecessary for the required operations.

**Validate only the immediate parent.** For `createPath(path, value)`, first reject `path` when it is already a key. Locate its final `/`; the prefix before that slash is the immediate parent. An empty prefix means the parent is the implicit root, so a one-component path is allowed. A non-empty parent must already be in the map. Only after both checks pass should `paths[path] = value` be performed, which prevents failed creations from changing state.

**Use the same map for lookup.** `get(path)` returns the mapped value when present and `-1` otherwise. Because creation requires the immediate parent, every stored nested path has a complete chain of previously created ancestors. Existing keys are never reassigned, so their associated values remain stable.

#### Complexity detail

Hashing a path and finding its final separator cost time proportional to that path's length. Summed over all method calls, the expected total time is $O(S)$. The map stores at most one copy of every successfully created path, whose combined length is at most $S$, so its space use is $O(S)$.

#### Alternatives and edge cases

- **Trie by components:** A trie naturally represents the hierarchy and also achieves linear work in the path text, but it needs node and child-map machinery that the two requested operations do not require.
- **Linear list of paths:** Searching every previously created path is correct but can take quadratic time across many operations.
- **Missing parent:** Creating a nested path fails even if all components are syntactically valid; no intermediate directory is created automatically.
- **Duplicate path:** A second creation fails and must not replace the original value.
- **One-component path:** Its parent prefix is empty, representing the implicit root, so it can be created in an empty system.
- **Missing lookup:** `get` returns `-1` and does not create the requested path.

</details>
