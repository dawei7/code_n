## General
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

## Complexity detail
Every folder is created and visited a constant number of times. Across all
nodes, sorting child entries costs at most $O(F\log F)$, and hashing interned
signatures covers $O(F)$ child pairs. The trie, signature table, frequency
map, traversal paths, and output use $O(F)$ structural storage, excluding the
characters already present in the input and output.

## Alternatives and edge cases
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
