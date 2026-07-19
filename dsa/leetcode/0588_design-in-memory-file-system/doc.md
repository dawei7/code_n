# Design In-Memory File System

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 588 |
| Difficulty | Hard |
| Topics | Hash Table, String, Design, Trie, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/design-in-memory-file-system/) |

## Problem Description
### Goal
Design an in-memory file system with absolute paths beginning at `/`. It must support `ls(path)`, which returns a directory's immediate files and directories in lexicographic order or the file's own name when `path` names a file, and `mkdir(path)`, which creates every missing directory along the requested path.

It must also support `addContentToFile(filePath, content)`, creating the file if necessary and appending rather than replacing its text, and `readContentFromFile(filePath)`, which returns the file's complete accumulated content. State must persist across calls, shared path prefixes must refer to the same directory nodes, and listings must not recursively include deeper descendants.

### Function Contract
**Inputs**

- `operations: list[list]`: an app-local sequence of method calls
- `["ls", path]`: list a directory's immediate entries in lexicographic order, or return the file's own name when `path` names a file
- `["mkdir", path]`: create every missing directory component
- `["addContentToFile", filePath, content]`: create a file when absent and append `content`
- `["readContentFromFile", filePath]`: return all content written to the file

**Return value**

- A list containing the results of `ls` and `readContentFromFile` operations in execution order
- Mutating operations do not add result entries

### Examples
**Example 1**

- Input: list root, create `/a/b/c`, write `"hello"` to `/a/b/c/d`, list root, then read the file
- Output: `[[], ["a"], "hello"]`

**Example 2**

- Input: append `"ab"` and then `"cd"` to `/x/file`
- Output of reading the file: `"abcd"`

**Example 3**

- Input: create root entries `b`, `a`, and `c`, then list root
- Output: `["a", "b", "c"]`
