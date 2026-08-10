## General

**Recognize the defect through traversal order**

The corrupted node is not identified by a value passed to the function. The only observable defect is structural: its `right` pointer refers to another node at the same depth that lies to its right. A normal tree edge points downward to an unvisited child, while the bad edge points sideways to a node that already belongs elsewhere in the tree.

This distinction becomes detectable if nodes on the right are visited before nodes on the left. By the time traversal reaches the invalid node, the same-level node to which its corrupted `right` pointer leads has already been seen. The exact implementation performs a depth-first traversal in this order:

1. process the current node;
2. recursively process its right subtree;
3. recursively process its left subtree.

This is often called root-right-left traversal or reverse preorder. The global set `vis` stores the actual node objects already processed.

**Why checking the right pointer identifies the invalid node**

At the start of `dfs(root)`, the condition

`root is None or root.right in vis`

handles both stopping cases. A missing child returns `None` naturally. If `root.right` already belongs to `vis`, the current node is the unique corrupted node and must also be replaced by `None`.

For the promised defect, the target of the bad pointer lies at the same depth and to the current node’s right. A right-first traversal has processed that rightward portion before arriving at the corrupted node, so the target object is in `vis`.

For an ordinary node, a legitimate right child cannot already be visited. Tree traversal reaches a parent before descending to that child, and a valid tree node has only its one structural parent. Therefore the test does not remove an ordinary node. In a completely valid portion of the tree, an already-visited child reference would itself imply sharing or a cycle, neither of which occurs under the contract.

The set contains node objects, not node values. The description guarantees unique values, so values could also identify nodes, but object identity directly matches what the pointer stores and requires no extraction of `val`.

**Rebuild the tree in place while unwinding**

If the current node is neither missing nor invalid, it is added to `vis`. The recursive calls then repair its two child subtrees:

`root.right = dfs(root.right)`

`root.left = dfs(root.left)`

The right call must come first. Reversing those lines would visit a defective node before the same-level node to its right, so the bad target might not yet be in `vis` and the defining check would fail.

Each recursive call returns the root of the corrected version of that child subtree. Normally it returns the original child object after recursively fixing descendants. When it encounters the invalid node, however, it returns `None` immediately. The parent assignment then disconnects the entire invalid subtree with one pointer update. There is no need to traverse or delete every descendant individually: once the parent no longer references that subtree, none of those nodes belong to the returned tree.

The qualification in the statement about excluding the node incorrectly pointed to is handled automatically. That target node lives in a separate legitimate portion of the tree and was visited earlier. The algorithm returns `None` before following the corrupted pointer, so it removes the invalid node’s original subtree without removing the already-existing target.

**A small trace**

Suppose the root has left child `2` and right child `3`, and node `2.right` has been corrupted to point at node `3`. The traversal first records the root, then visits node `3` and records it. It then enters the left side at node `2`. Before adding `2`, it observes that `2.right` is the exact node object already present in `vis`. The call for the root’s left child returns `None`, so the root’s `left` field becomes empty while node `3` remains untouched.

In the larger example, the traversal similarly visits the legitimate node `4` in the right portion of its level before reaching invalid node `7`. Returning `None` for `7` also detaches its legitimate descendant `2`, exactly as requested.

**Why the whole corrected tree is returned**

For any ordinary node, assume recursively that each child call returns the correctly repaired version of its subtree. Assigning those results to `right` and `left` makes the current node’s subtree correct, and returning the current node preserves it. For the unique invalid node, returning `None` is exactly the required replacement and prevents traversal through its corrupt link.

The right-first order guarantees that the unique invalid node is recognized. All nodes outside its subtree return normally and keep their original relationships, except for the one parent pointer changed to `None`. Applying this reasoning from the leaves back to the initial call proves that `dfs(root)` returns the original root with precisely the invalid node and its descendants removed.

The root itself cannot be the invalid node under the valid-input guarantees: there is no other node at the root’s depth to its right. Thus returning `None` for the initial call is not a valid-case concern.

## Complexity detail

Let `N` be the number of nodes in the original tree. Every node that remains reachable during the right-first traversal is entered at most once, and each entry performs expected constant-time set operations plus two pointer assignments. The algorithm may stop before traversing descendants of the invalid node, but the worst case still visits $O(N)$ nodes. Expected running time is $O(N)$.

The visited set can hold $O(N)$ node references. The recursive call stack has depth equal to the tree height `H`, which is $O(N)$ in the worst-case skewed tree. Total auxiliary space is therefore $O(N)$.

The implementation mutates existing child pointers and does not allocate a replacement tree. That saves a second $O(N)$ node structure, but it does not remove the set and recursion-stack costs. Python recursion depth can also be a practical concern for a highly skewed tree near the $10^4$-node limit even though the asymptotic bound is correct.

## Alternatives and edge cases

- **Right-to-left breadth-first search:** Process one level at a time, store visited nodes from that level, and carry parent references in the queue. The bad pointer targets a node already processed in the same layer, so its parent can be detached in $O(N)$ time and $O(N)$ space without recursion-depth risk.
- **Left-to-right BFS with a complete level set:** One may first collect all nodes of a level, then test whether a node’s right pointer targets another member. This works but needs separate parent tracking and careful exclusion of normal next-level children.
- **Ordinary left-first DFS:** This is incorrect for the chosen detection rule because the bad target lies to the right and may not have been visited when the invalid node is checked.
- **Search by node value alone:** Unique values make this possible, but no `fromNode` or `toNode` value is provided to the function; traversal order is still needed to discover the defect.
- **Invalid node with descendants:** Returning `None` at that node intentionally skips and disconnects its entire subtree in one step.
- **Corrupted pointer target preservation:** The target was reached through its genuine place in the tree. The invalid call returns before recursing through the bad edge, so that legitimate target stays present.
- **A missing ordinary child:** `dfs(None)` returns `None` and leaves that field empty without adding anything to `vis`.
- **Very skewed tree:** The $O(N)$ recursion stack may exceed Python’s runtime recursion limit; an explicit-stack right-first traversal with parent information is the robust alternative.
- **Object hashing:** Standard `TreeNode` instances are identity-hashable in the expected harness. If a custom node type disabled hashing, the set could instead store unique `node.val` values.
- **Mutation semantics:** The returned root is not a deep copy. The source repairs the supplied tree in place, which is exactly sufficient for the required returned structure.
