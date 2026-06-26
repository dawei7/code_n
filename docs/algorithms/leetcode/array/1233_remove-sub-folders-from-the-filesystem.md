# Remove Sub-Folders from the Filesystem

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1233 |
| Difficulty | Medium |
| Topics | Array, String, Depth-First Search, Trie |
| Official Link | [remove-sub-folders-from-the-filesystem](https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/) |

## Problem Description & Examples
### Goal
Given absolute folder paths, remove every path that is nested inside another listed path. Return only the top-level remaining folders.

### Function Contract
**Inputs**

- `folder`: list of unique folder paths such as `"/a/b"`.

**Return value**

The folder paths that are not subfolders of any other listed path.

### Examples
**Example 1**

- Input: `folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]`
- Output: `["/a","/c/d","/c/f"]`

**Example 2**

- Input: `folder = ["/a","/a/b/c","/a/b/d"]`
- Output: `["/a"]`

**Example 3**

- Input: `folder = ["/a/b/c","/a/b/ca","/a/b/d"]`
- Output: `["/a/b/c","/a/b/ca","/a/b/d"]`

---

## Underlying Base Algorithm(s)
Lexicographic sorting with prefix boundary checks.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n + total_path_length)`
- **Space Complexity**: `O(n)` for the returned paths.
