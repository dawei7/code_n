## General
**Summarize each subtree after its children**

For every node, a postorder traversal returns two values: the height of that node's subtree and the root of the smallest subtree containing all deepest nodes within it. A missing child has height zero and no answer node; a leaf consequently receives height one and selects itself.

Suppose the left summary has height $L$ and the right summary has height $R$. If $L>R$, every deepest descendant of the current subtree lies on the left, so the left answer remains the smallest valid root. The right case is symmetric. The returned height is one plus the larger child height.

**Equal heights meet at the current node**

When $L=R$, both child sides reach the same deepest level. If the height is positive, deepest descendants occur in both branches and no proper descendant can contain them all; the current node is their lowest common ancestor. For a leaf, both missing-child heights are zero and selecting the current node gives the same rule.

Inductively, each child summary is correct for its subtree. The height comparison either preserves the only side containing deepest descendants or chooses the first node joining equally deep sides. Therefore the root returned for the whole tree is exactly the smallest subtree containing every globally deepest node.

## Complexity detail
Postorder visits each of the $n$ nodes once and performs constant work per node, so time is $O(n)$. The recursive call stack holds at most one frame per node on a root-to-leaf path, using $O(h)$ auxiliary space.

## Alternatives and edge cases
- **Compute subtree heights repeatedly:** Descending toward the deeper side is correct, but recomputing both heights at every level takes $O(n^2)$ time on a skewed tree.
- **Collect deepest nodes and find their lowest common ancestor:** This is correct, but it needs extra depth, parent, or ancestor structures and multiple passes.
- **Breadth-first search plus parent climbing:** The last level identifies deepest nodes, after which their ancestor sets can be intersected; it uses $O(n)$ additional storage.
- **Single node:** Both child heights tie at zero, so the root itself is returned.
- **One deepest node:** Every height comparison follows its branch until that node is selected.
- **Deepest nodes in both root branches:** Equal heights select the original root and therefore the whole tree.
- **Deepest nodes share a lower ancestor:** Equal heights first occur at that lower node, preventing an unnecessarily large subtree.
