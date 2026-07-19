# Remove Sub-Folders from the Filesystem

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1233 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Depth-First Search, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/) |

## Problem Description

### Goal

You are given a list `folder` of unique absolute folder paths. A listed path is a sub-folder of another listed path when it starts with that complete parent path followed immediately by `"/"`. Thus `"/a/b"` is a sub-folder of `"/a"`, while a path that merely shares characters, such as `"/ab"`, is not.

Every valid path contains one or more components, each written as `"/"` followed by one or more lowercase English letters; neither an empty string nor `"/"` alone occurs. Remove every listed path that is a sub-folder of another listed path, then return the remaining folders in any order.

### Function Contract

**Inputs**

- `folder`: A list of $n$ unique valid paths, where $1\le n\le4\cdot10^4$ and each path has length from $2$ through $100$.

Let $L$ be the maximum length of any path in `folder`.

**Return value**

- All paths that are not sub-folders of another listed path; the result may be in any order.

### Examples

**Example 1**

- Input: `folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]`
- Output: `["/a","/c/d","/c/f"]`

`"/a/b"` is removed under `"/a"`, and `"/c/d/e"` is removed under `"/c/d"`.

**Example 2**

- Input: `folder = ["/a","/a/b/c","/a/b/d"]`
- Output: `["/a"]`

Both longer paths are sub-folders of the listed folder `"/a"`.

**Example 3**

- Input: `folder = ["/a/b/c","/a/b/ca","/a/b/d"]`
- Output: `["/a/b/c","/a/b/ca","/a/b/d"]`

None of these paths is a complete parent followed by `"/"` for another one.
