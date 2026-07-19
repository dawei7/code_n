# Delete Duplicate Folders in System

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1948 |
| Difficulty | Hard |
| Topics | Array, Hash Table, String, Depth-First Search, Trie, Sorting, Hash Function |
| Official Link | [LeetCode](https://leetcode.com/problems/delete-duplicate-folders-in-system/) |

## Problem Description
### Goal
Each entry in `paths` names an absolute folder path as a sequence of
lowercase folder names. All parent folders are included, so the entries
together describe one file-system tree rooted above the first path component.

Two folders are identical when they contain the same nonempty set of named
subfolders and those subfolders have identical recursive structures. The
folders may occur at different depths. Empty folders alone are not considered
duplicates because the required subfolder set must be nonempty.

Mark every folder that has an identical counterpart, together with every
folder below it. Then delete all marked folders simultaneously and return the
paths that remain. Marking happens only once: folders that become identical
because of this deletion are not deleted in a second pass.

### Function Contract
**Inputs**

- `paths`: between 1 and $2\cdot10^4$ distinct folder paths. Each path contains
  1 to 500 names, each name has 1 to 10 lowercase letters, every non-root
  folder's parent path is present, and the total number of name characters is
  at most $2\cdot10^5$.

Let $F$ be the number of distinct folders represented by the trie.

**Return value**

- All paths whose folders remain after the one simultaneous duplicate-subtree
  deletion. The paths may be returned in any order.

### Examples
**Example 1**

- Input:
  `paths = [["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]]`
- Output: `[["d"], ["d", "a"]]`

**Example 2**

- Input:
  `paths = [["a"], ["c"], ["a", "b"], ["c", "b"], ["a", "b", "x"], ["a", "b", "x", "y"], ["w"], ["w", "y"]]`
- Output: `[["a"], ["a", "b"], ["c"], ["c", "b"]]`

**Example 3**

- Input: `paths = [["a", "b"], ["c", "d"], ["c"], ["a"]]`
- Output: `[["a"], ["a", "b"], ["c"], ["c", "d"]]`
