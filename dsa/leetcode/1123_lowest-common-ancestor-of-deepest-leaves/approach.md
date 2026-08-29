## General

**Return both depth information and an ancestor candidate**

At each node, the algorithm needs to know which child side contains the deepest leaves. It also needs the lowest node covering all deepest leaves on that side.

`dfs(root)` therefore returns a pair:

- a node that is the LCA of the deepest leaves in this subtree, and
- the height of this subtree measured as the number of nodes from this root level through its deepest leaf.

The public method needs only the candidate node, but the height guides every recursive decision.

**Base case for an empty child**

For `None`, the helper returns `(None, 0)`. An empty subtree has height zero and no ancestor candidate.

A leaf has two empty children. Their heights tie at zero, so the leaf returns itself with height one. This correctly treats a lone leaf as the LCA of the deepest-leaf set containing only itself.

**Compare left and right heights**

After recursively obtaining `l, d1` and `r, d2`:

- If `d1 > d2`, every deepest leaf below the current node lies in the left subtree. The correct LCA is already `l`, and the current subtree height is `d1 + 1`.
- If `d1 < d2`, the symmetric result `r, d2 + 1` is returned.
- If `d1 == d2`, deepest leaves occur at the same depth on both sides. Any node covering all of them must cover both child subtrees, so the current node is their lowest common ancestor. It returns `root, d1 + 1`.

The addition of one accounts for the edge level from the current node to either child summary.

**Why the equal-height case includes leaf nodes**

When both children are absent, equal zero heights make the leaf return itself. When both are nonempty with equal greatest heights, each side contributes at least one globally deepest leaf and the current node is the first place those groups meet.

The same single rule therefore handles both a leaf base and a genuine merge of deepest leaves.

**Why a taller side can discard the other candidate**

Suppose the left height is greater. Every leaf in the right subtree is closer to the current node than at least one leaf in the left subtree. The problem cares only about leaves at maximum global depth within this subtree, so no right-side leaf belongs to that set.

The LCA of the relevant deepest leaves was already computed inside the left subtree as `l`. Returning the current node would be a higher, non-lowest ancestor, so propagating `l` is necessary.

**Complete inductive argument**

For an empty subtree, the returned summary is correct. Assume both child summaries correctly identify their deepest-leaf LCA and height.

Height comparison identifies exactly which child subtrees contain leaves at the current subtree’s maximum depth. One taller child means its candidate remains correct; equal heights mean both sets must be joined at the current root. The returned height is also exact.

By induction, the pair returned for the original root contains the LCA of all deepest leaves in the whole tree. `dfs(root)[0]` returns that node.

The height is relative to the current subtree rather than an absolute root depth. Relative heights are sufficient because the two child roots are one level below the same parent, so comparing them preserves the comparison of their deepest leaves’ absolute depths.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height. Each node is visited exactly once and performs constant work after its children, so time is $O(n)$.

The recursion stack contains at most one call per level, giving $O(h)$ auxiliary space. This is $O(\log n)$ for a balanced tree and $O(n)$ for a skewed tree.

No parent map, depth list, or collection of leaves is stored. Returned pairs use constant space per active call.

## Alternatives and edge cases

- **Two-pass depth method:** First find maximum depth, then recursively find the LCA of leaves at that depth. It is correct but traverses nodes twice.
- **Parent pointers plus deepest leaf list:** BFS can collect deepest leaves, then move ancestors upward. It uses $O(n)$ extra mappings.
- **Return height only:** Insufficient because a second traversal would be needed to recover the LCA candidate.
- **Single node:** Both child heights tie at zero, so the root returns itself.
- **One deepest leaf:** Its candidate propagates through every taller-side comparison and the result is the leaf itself.
- **Deepest leaves on both root sides:** Equal child heights make the root the answer.
- **Unequal subtree heights:** Shallower leaves are irrelevant to the deepest set.
- **Several deepest leaves within one child:** That child’s recursively computed LCA propagates upward.
- **Unique values:** Values are not used by the algorithm; node identity and structure determine the answer.
- **Nonempty root:** The contract ensures the returned candidate is a real node.
- **Skewed tree:** Time remains linear, but recursion space becomes $O(n)$.
- **No tree mutation:** The method reads child links and returns an existing node without changing structure.
