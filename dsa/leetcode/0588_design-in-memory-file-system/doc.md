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

### Required Complexity

- **Time:** $O(P + k \log k + C)$
- **Space:** $O(S)$

<details>
<summary>Approach</summary>

#### General

**Represent path components as trie edges**

Use one node for the root. Each directory node stores a hash map from an immediate child name to its child node. Splitting an absolute path on `/` yields the sequence of edges to follow, so path traversal depends on depth rather than the total number of stored entries.

**Distinguish files from directories**

A node whose content field is `None` is a directory. A file node holds a list of appended text fragments. Keeping fragments avoids repeatedly copying all earlier content on every append; reading joins them in write order.

**Share one path walker**

A helper starts at root and follows every nonempty path component. In creation mode it inserts missing nodes, which gives `mkdir` its recursive behavior and creates a file node's path before content is attached.

**Implement listing according to node type**

When the target is a file, return only the path's final component. When it is a directory, sort and return its immediate child names. Descendants are not included in a directory listing.

**Why operations preserve filesystem semantics**

Each absolute component sequence maps to exactly one trie route, so distinct sibling names cannot collide and repeated traversal reaches the same node. Directory creation adds only missing edges, file appends preserve fragment order at the terminal node, and reads concatenate precisely those fragments. Listing consults exactly the terminal node's type and children, producing the required file or directory behavior.

#### Complexity detail

Let `P` be the number of path components traversed, `k` the number of immediate children returned by a directory listing, and `C` the content length read or appended. Hash-map traversal is $O(P)$ expected time; directory listing costs $O(k \log k)$; content work costs $O(C)$. Total stored nodes, names, and content occupy $O(S)$ space.

#### Alternatives and edge cases

- **Flat maps keyed by full paths:** can support direct file lookup, but directory listing needs either a separate child index or a scan of stored paths.
- **Sorted child arrays:** make listing immediate but insertion and lookup among many siblings can take $O(k)$ per component.
- **Single growing content string:** is simple, but repeated appends can repeatedly copy existing content and become quadratic in total written length.
- **Root path:** has no components and lists root's immediate children.
- **Recursive directory creation:** one `mkdir` call may create several missing ancestors.
- **Listing a file:** returns a one-element list containing its basename.
- **Repeated append:** preserves all content in call order.
- **Empty directory:** returns an empty list.
- **Lexicographic listing:** sort names only when a directory is listed; insertion order is irrelevant.
- **Shared prefixes:** paths reuse the same ancestor nodes and diverge only at the first different component.

</details>
