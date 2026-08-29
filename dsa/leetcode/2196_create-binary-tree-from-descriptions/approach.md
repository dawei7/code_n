## General

Descriptions may arrive in any order. A child can be mentioned before the row where that same value acts as a parent, so the construction needs one shared `TreeNode` object per unique value.

The exact solution interns nodes in a mapping, connects left and right references immediately, records every value used as a child, and identifies the root as the only created value never used as a child.

**Intern one node object per value**

Dictionary `nodes` maps integer values to `TreeNode` instances.

For each description, the code checks whether `parent` and `child` already exist. If not, it creates `TreeNode(parent)` or `TreeNode(child)`.

Reusing mapped objects is essential. If the child in one description later becomes a parent in another, both descriptions must refer to the same node object. Creating a fresh object on every row would split one logical node into disconnected copies.

Although `nodes` is declared as `defaultdict(TreeNode)`, the exact code explicitly checks membership and supplies the correct value to each constructor. The default factory is not relied on for normal creation.

**Attach the described edge**

When `isLeft` is truthy, `nodes[parent].left` receives `nodes[child]`. Otherwise the right pointer receives it.

The validity guarantee ensures these assignments do not conflict: a parent is not given two different left children, a child does not acquire multiple parents, and the relationships form one binary tree.

Description order does not matter. Both endpoint objects exist before attachment, and later rows reuse them.

**Record which values have parents**

Every `child` value is added to set `children`. A node's presence in this set means some description gives it an incoming parent edge.

Parent values are not separately collected because `nodes.keys()` already contains every value seen as either an endpoint.

In a valid nonempty tree, exactly one node has no parent: the root.

**Find the unique non-child**

`set(nodes.keys()) - children` removes every value that appears as a child. The validity guarantee makes the difference a one-element set.

Calling `pop()` obtains that sole root value. The method returns `nodes[root]`, the already-connected object at the top of the structure.

No traversal is needed after linking. Every child reference was installed while reading descriptions, so returning the root exposes the complete reachable tree.

**Why every described relationship appears**

Each input triple is processed once. Before the iteration ends, the exact shared parent object has the exact shared child object assigned to the specified side.

No later valid description overwrites that side with a conflicting child. Therefore every required edge remains in the final object graph with correct orientation.

**Why no extra relationship appears**

The only assignments to `left` or `right` occur in response to a description. Fresh nodes begin with null children. Thus every non-null edge in the result was explicitly requested.

The mapping itself does not create tree edges; it only makes node identity reusable.

**Why the selected node is the root**

Every non-root node in a tree has exactly one parent and consequently appears in `children`. The root has no parent and never appears there, though it appears in `nodes` as a parent endpoint.

Set difference therefore selects exactly the root. Since all descriptions form one valid tree, all other node objects are reachable below it through installed links.

For the first example, values 15, 17, 20, 80, and 19 appear as children, while 50 does not. The difference selects 50, whose pointers already lead through the constructed tree.

## Complexity detail

Let $m$ be the number of descriptions. A valid tree with $m$ edges has $m+1$ nodes. Each description performs expected constant-time dictionary and set operations, giving $O(m)$ construction time.

Creating the key set and subtracting `children` also takes $O(m)$ expected time. Total time is $O(m)$.

The mapping, child set, and newly created tree nodes each contain $O(m)$ entries or objects. Total storage is $O(m)$, including the returned tree structure, matching the manifest.

## Alternatives and edge cases

- **Parent-to-child graph then DFS:** Store value relationships first, find the root, and recursively create nodes. It works but requires a second construction traversal.
- **BFS construction:** Similarly builds nodes level by level after root discovery, adding queue machinery unnecessary for direct interning.
- **Track indegrees:** An integer indegree map also identifies the unique zero-indegree node; a child set is simpler because valid tree indegrees are zero or one.
- **Description order arbitrary:** Interning ensures a child object can later receive its own children.
- **One description:** Two nodes are created, the parent is the sole non-child, and the edge is returned correctly.
- **Parent with two children:** Separate left and right descriptions assign the two distinct fields.
- **Node is both child and parent:** It stays one object in `nodes` and appears below its parent while owning its own subtree.
- **Unique values:** Dictionary keys unambiguously identify logical nodes.
- **Valid-tree guarantee:** It ensures one root, no cycles, no conflicting parent assignments, and no disconnected components.
- **Set `pop` order:** Nondeterminism is irrelevant because the set has exactly one element.
- **Defaultdict factory:** Explicit membership checks prevent accidental zero-valued placeholder nodes.
- **No post-build traversal:** All pointers are already linked when the root is identified.
- **Input preservation:** Description rows are only read.
