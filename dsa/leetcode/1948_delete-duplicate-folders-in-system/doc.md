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

### Required Complexity
- **Time:** $O(F\log F)$
- **Space:** $O(F)$

<details>
<summary>Approach</summary>

#### General

**Build the folder trie**

Insert every path into a trie whose edges are folder names. Each trie node is
one folder, and its child-name map exactly describes its immediate
subfolders.

**Intern subtree shapes from the bottom up**

Process children before parents. A folder's structural signature is the sorted
tuple of pairs `(child name, child signature ID)`. Sorting makes the signature
independent of dictionary traversal order, while including each child name
distinguishes equally shaped subtrees with different folder names.

Intern each distinct nonempty signature to one integer ID and count how many
non-root folders receive that ID. Leaves receive ID zero and are not counted:
an empty child set does not qualify as a duplicate structure. The artificial
root is also excluded because it is not an input folder.

Two folders receive the same nonzero ID exactly when their named child sets
and all descendant structures agree recursively. Thus IDs with frequency at
least two identify precisely the folders that must be marked in the original
tree.

**Collect only unmarked subtrees**

Traverse the original trie a second time. When a child's nonzero signature ID
is duplicated, skip that child and its entire subtree. Otherwise append its
path and continue below it. All duplicate decisions come from the unchanged
original trie, so this collection performs the required single simultaneous
deletion rather than discovering new duplicates afterward.

#### Complexity detail

Every folder is created and visited a constant number of times. Across all
nodes, sorting child entries costs at most $O(F\log F)$, and hashing interned
signatures covers $O(F)$ child pairs. The trie, signature table, frequency
map, traversal paths, and output use $O(F)$ structural storage, excluding the
characters already present in the input and output.

#### Alternatives and edge cases

- **Full serialization strings:** Serialize each subtree recursively and count
  equal strings. This is conceptually direct but can repeatedly copy long
  descendant descriptions; interning integer IDs keeps signatures compact.
- **Pairwise subtree comparison:** Compare every folder with every other
  folder recursively. It avoids hashing but can require $O(F^2)$ or more work.
- Empty leaf folders are not duplicates because identical folders must have a
  nonempty subfolder set.
- Duplicate folders need not share a parent or depth.
- When a folder is marked, all descendants disappear even if a descendant's
  own signature is unique.
- The artificial trie root must never participate in duplicate counts.
- Equal structures created only after marked folders vanish are retained
  because deletion runs once.
- If no nonempty signature repeats, every input path remains.

</details>
