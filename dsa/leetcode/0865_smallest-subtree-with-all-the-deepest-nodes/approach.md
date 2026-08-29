## General

**The answer is the lowest common ancestor of all deepest nodes**

A subtree contains all deepest nodes exactly when its root is an ancestor of every deepest node. The smallest such subtree begins at their lowest common ancestor.

The postorder recursion finds that node without first building a separate deepest-node list. Each call returns:

- the smallest subtree root containing all deepest nodes within the current subtree;
- the height of the current subtree.

Combining these two pieces tells a parent which side contains the globally deepest descendants below it.

**Height definition**

For a null node, DFS returns `(None,0)`.

A leaf receives height zero from both null children and returns height one. In general, returned height is the number of nodes on a longest downward path beginning at the current node.

Absolute depth from the original tree root is not needed. Comparing left and right subtree heights is enough to locate which side contains deeper nodes relative to the current node.

**Process children first**

For current `root`:

- `(l,ld)` describes the left subtree;
- `(r,rd)` describes the right subtree.

The candidates `l` and `r` are already the smallest subtrees containing the deepest nodes within their respective sides.

Postorder timing ensures this information is complete before choosing a result for `root`.

**Left subtree is deeper**

If `ld > rd`, every deepest node of the current subtree lies in the left side. Nodes in the right side stop at a smaller height and cannot tie for deepest.

The smallest subtree covering the current subtree's deepest nodes is therefore exactly `l`, the answer already computed for the left child.

The current call returns `(l,ld+1)`. Adding one accounts for the edge/node level from current root down into that child height.

**Right subtree is deeper**

The symmetric case `ld < rd` returns `(r,rd+1)`.

All deepest descendants lie in the right subtree, so including the current root or left side would make the result larger than necessary.

**Equal subtree heights**

If `ld == rd`, the deepest downward level occurs on both sides.

Any subtree containing every deepest node must contain at least one deepest node from the left and one from the right. Their paths first meet at current `root`, so current root is their lowest common ancestor and the smallest valid subtree root.

The call returns `(root,ld+1)`.

This case also handles a leaf: both child heights are zero, and the leaf itself is the only deepest node in its subtree.

**Trace the main example**

In the subtree rooted at node 2, leaves 7 and 4 have equal depths in its left and right sides. The recursive heights tie, so node 2 becomes the candidate.

At ancestor 5, the side containing node 2 is deeper than leaf 6, so candidate 2 propagates upward unchanged.

At root 3, its left subtree is deeper than its right subtree, so candidate 2 again propagates. The function returns node 2, the smallest subtree containing both globally deepest nodes.

**One deepest node**

If only one node attains maximum depth, every ancestor on its path sees one child side strictly deeper. The candidate propagates from the deepest leaf itself all the way upward.

The returned subtree root is that leaf, which is the smallest subtree containing it.

**Why local heights solve a global question**

Within a subtree, nodes at its maximum local height are exactly the descendants that can become globally deepest if this subtree lies on a deepest root path. The recursive candidate summarizes their lowest common ancestor.

At each parent, comparing heights discards any shallower side or joins tied sides at the current root. This is precisely the LCA decision needed for deepest descendants.

**Why the recurrence is correct**

Induct on subtree size. Null and leaf cases follow directly.

Assume child results are correct. If one height is greater, only that child contains deepest nodes, so its minimal candidate remains minimal. If heights tie, deepest nodes occur in both sides and no proper descendant of current root can contain both; current root is necessary and sufficient.

Thus, every call returns the stated candidate and correct height. Applying it at the original root yields the requested subtree.

## Complexity detail

Let `n` be node count and `h` tree height.

Each node is visited once and performs constant comparisons, so time is `O(n)`.

The recursion stack holds at most one root-to-leaf path, using `O(h)` space. Returned tuples are constant-size and no per-node collection is stored.

For a balanced tree, `h=O(\log n)`; for a skewed tree, `h=O(n)`.

## Alternatives and edge cases

- **Find maximum depth, collect deepest nodes, then compute LCA:** It works but needs multiple passes or parent/depth storage.

- **Parent pointers and upward intersection:** Collect ancestors of deepest nodes and find the lowest common one. More storage is required.

- **Single-node tree:** Equal null heights return the root.

- **Only one deepest leaf:** Its candidate propagates through strictly deeper child choices.

- **Deepest nodes in both root subtrees:** The root itself is returned.

- **Tied heights below an internal node:** That internal node becomes the local candidate.

- **Shallower sibling subtree:** It is excluded when the other height is greater.

- **Unique node values:** Not required by the algorithm because it returns object references.

- **Null child:** It contributes height zero and candidate `None`.

- **Input immutability:** Tree pointers are only read.
