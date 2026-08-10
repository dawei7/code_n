## General

**Visit the most rightward possibilities first**

The selected competitive `Solution` uses depth-first search rather than a
level-order queue. At every node it recursively explores the right child before
the left child. This ordering ensures that the first node reached at any depth
is the rightmost existing node on that level.

The method stores one result value per depth. Later nodes at the same depth are
farther left and cannot replace the first visible choice.

**Start depth numbering at one**

`rightSideView` creates an empty `result` list and calls
`rightSideViewDFS(root, 1, result)`. Root depth is one, so when the root exists,
condition `depth > len(result)` is `1 > 0` and its value is appended.

After values for depths one through $d$ have been recorded, the list length is
$d$. Reaching depth $d+1$ makes the condition true and appends the first node
for that new level. Reaching another node at any already-recorded depth makes
the condition false.

Using zero-based depth with `depth == len(result)` would be an equivalent
convention. The exact code consistently uses one-based depth and a strict
greater-than comparison.

**Return immediately for missing nodes**

The recursive helper begins with `if not node: return`. Missing child pointers
do not add a value and do not recurse further. An empty root therefore returns
the initially empty list naturally.

This guard also lets the caller invoke both child branches without separate
existence tests. Each null branch ends at once.

**Record only the first visit to a depth**

When `depth > len(result)`, no node at that level has been seen before. Because
traversal always prefers right subtrees, the current node is the rightmost
existing node at that depth and its value is appended.

Once the list already contains an entry for that depth, every later visit comes
from a path that is left of an earlier explored path. The algorithm still walks
those nodes because they may contain the first node of a deeper level, but it
does not modify the existing shallower view entry.

**Why right-first preorder identifies geometric rightmost nodes**

At a parent, every position in its right subtree lies to the right of positions
at the corresponding depth in its left subtree. Exploring the entire right
subtree first therefore reaches any existing right-subtree node at a target
depth before a left-subtree competitor.

Within that right subtree, the same rule is applied recursively. If no node
exists at the target depth there, traversal eventually enters the left subtree,
where the first available node is then genuinely the rightmost existing node
for that depth. Missing branches are thus handled correctly without requiring a
complete tree.

**Trace a sparse example**

For `[1,2,3,4,null,null,null,5]`, DFS records root 1 at depth one, then enters
right node 3 and records it at depth two. Node 3 has no descendants, so the
search returns to left node 2, but depth two is already recorded.

From node 2 it enters left node 4, the first encountered node at depth three,
and records 4. Node 4's left child 5 becomes the first node at depth four and
is recorded. The result is `[1,3,4,5]`, showing that a node in a left subtree
can be visible when no more-right node exists at its depth.

**Why the result is exact**

For each occupied depth, DFS eventually visits at least one node there. The
right-before-left ordering ensures the first such visit is the geometrically
rightmost existing node, so the appended value is sound. The length condition
allows exactly one append for that depth, preventing duplicates.

Depth increases by one along every edge, and append order follows first visits
to depths one, two, three, and so on. The result is therefore ordered top to
bottom as required.

**Understand the top-level `TreeNode` definition**

The competitive file includes its own simple `TreeNode` class before
`Solution`. In the platform environment, a tree-node structure is normally
provided as harness code. The helper class is not part of the traversal logic;
`rightSideView` only requires objects exposing `val`, `left`, and `right`.

Its constructor accepts only `x`, unlike some modern templates that accept
children as optional arguments. That interface difference matters when using
the file standalone to construct test trees but not when the runner supplies
compatible nodes.

**Inactive BFS alternative**

`Solution2` is not the selected entry point. It stores one list per level,
iterates it left to right, appends children left before right, and after the
loop uses variable `node`, which remains bound to that level's final node. That
final node is the rightmost one and is appended to the answer.

The source comments correctly distinguish selected DFS stack space $O(h)$ from
the BFS alternative's possible $O(n)$ level storage. The manifest's $O(n)$
space is a valid worst-case upper bound for DFS because a skewed tree can have
$h=n$.

## Complexity detail

Every one of the $n$ nodes is visited once and performs constant work, so time
is $O(n)$.

The recursion stack has depth equal to tree height $h$, giving $O(h)$ auxiliary
space, plus an output list of $O(h)$ values. In the worst-case skewed tree,
$h=n$, so the manifest's $O(n)$ bound is correct. A balanced tree uses only
$O(\log n)$ stack depth, which can be smaller than BFS's maximum width.

## Alternatives and edge cases

- **Right-to-left BFS:** The optimal variant records the first queued node of each level and avoids recursion.
- **Left-to-right BFS:** Record the last node after processing a frozen level.
- **Sentinel BFS:** Delimit levels with a marker, though size measurement is usually simpler.
- **Empty root:** Null guard returns an empty result.
- **Single node:** First depth visit records only the root.
- **Left-only tree:** With no right alternative, each left node is first at its depth and visible.
- **Deep skewed tree:** DFS uses $O(n)$ stack and may hit recursion limits in a larger generalized domain.
- **Duplicate values:** One value per level is returned even if several levels share the same number.
- **Missing branches:** Right-first traversal falls back to the left subtree only when necessary.
- **Platform node class:** Only `val`, `left`, and `right` compatibility is required by the algorithm.
