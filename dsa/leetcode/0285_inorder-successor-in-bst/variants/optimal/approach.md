## General

**Translate “inorder successor” into a value search**

An inorder traversal of a binary search tree visits node values in increasing order. Because all node values are unique, the node immediately after `p` in that traversal is exactly the node with the smallest value strictly greater than `p.val`.

The exact solution searches for this upper bound directly. It does not perform an inorder traversal, does not need parent pointers, and does not separately inspect whether `p` has a right child. The BST ordering lets one root-to-leaf path find the smallest value above the target.

The search maintains `ans`, the best successor candidate seen so far. Initially it is `None` because no greater value has yet been found.

**When the current value is not greater, discard the left side**

Suppose the current node satisfies

$$
\texttt{root.val}\le\texttt{p.val}.
$$

The current node cannot be the successor because a successor must be strictly greater than `p.val`. Every value in the current node's left subtree is even smaller than `root.val`, so none of those nodes can qualify either.

The only place in this subtree that might contain a greater value is the right subtree. The source therefore assigns `root = root.right` and does not change `ans`.

This same branch handles the moment the search reaches `p` itself. Since `root.val == p.val`, the algorithm moves right. If `p` has a right subtree, its smallest value will be discovered by later leftward moves; if it has no right subtree, the previously saved ancestor candidate may be the answer.

**When the current value is greater, save it and search left**

Suppose instead that

$$
\texttt{root.val}>\texttt{p.val}.
$$

The current node is a valid successor candidate, so the source stores it in `ans`. However, it may not be the smallest qualifying value. The current node's left subtree can contain values that are still greater than `p.val` but smaller than the current node.

The algorithm consequently moves left to search for a tighter candidate.

The right subtree can be discarded. Every value there is greater than `root.val`, and `root` is already a qualifying candidate. No right-subtree node can be smaller than that candidate, so none can improve the answer.

**Why replacing `ans` always improves it**

Every assignment to `ans` happens at a node greater than `p.val`, so the candidate is always valid. After saving such a node, the search moves into its left subtree. Any later qualifying node encountered there must be smaller than the saved node. Therefore, later assignments make `ans` strictly closer from above to `p.val`.

If the left search reaches a value at or below `p.val`, the algorithm moves right within that smaller subtree, looking for the boundary again. This is ordinary BST lower-bound search: greater values pull the search left, while values that are too small pull it right.

**A search-interval argument**

At every iteration, all discarded nodes are unable to improve `ans`:

- after a node at or below `p.val`, its node and left subtree are not strictly greater;
- after a node above `p.val`, its right subtree is no smaller than the valid candidate just saved.

Only the chosen child can contain a better answer. When the chosen path reaches `None`, every unvisited region has been discarded for one of those two reasons. If `ans` is a node, it is the smallest value greater than `p.val`; if `ans` is still `None`, no greater value exists anywhere in the tree.

That precisely matches the successor contract.

**How the two familiar successor cases appear automatically**

If `p` has a right child, its inorder successor is the leftmost node of `p.right`. When this search reaches `p`, it moves right. Every greater node encountered becomes a candidate and causes a left move, so it naturally reaches that right subtree's leftmost node without special-case code.

If `p` has no right child, the successor—if one exists—is the lowest ancestor for which `p` lies in the ancestor's left-side search region. Such an ancestor was saved when the algorithm moved left from it. Later descent toward `p` cannot replace it with a larger value, and a smaller qualifying ancestor or descendant would replace it only if truly closer.

If `p` is the maximum value, the search never encounters a greater node after any needed moves. `ans` remains `None`, correctly representing the absence of a successor.

**Trace the first example**

For `root = [2,1,3]` and `p = 1`:

| Current value | Comparison with 1 | `ans` afterward | Next direction |
|---:|---|---:|---|
| 2 | greater | 2 | left |
| 1 | equal | 2 | right |

The right child of 1 is absent, so the loop ends and returns node 2. In sorted inorder sequence `[1,2,3]`, 2 immediately follows 1.

For `root = [5,3,6,2,4,null,null,1]` and `p = 6`, the search compares 5 with 6 and moves right, then compares 6 and moves right again. It never sees a value greater than 6, so it returns `None`.

As a right-subtree illustration, if `p = 3` in the same tree, the root 5 is first saved as a candidate. The search moves left to 3, then right to 4. Node 4 is greater and replaces 5 before the search moves left to `None`. The returned successor is 4.

**Why node identity is not needed during the search**

The source compares only values, even though the input supplies the actual node `p`. Unique BST values make the successor depend completely on `p.val`. There is only one node with that key, so searching for the smallest greater key identifies the correct successor node object.

The guarantee that `p` belongs to the tree supports the problem's meaning, but the lower-bound search would also return the smallest tree value greater than `p.val` for an external probe node. What matters to this implementation is the target value and uniqueness ordering.

## Complexity detail

Let $h$ be the tree height and $n$ the number of nodes. The loop visits one node per level along a single search path, so time is $O(h)$. In a balanced BST, $h=O(\log n)$; in a completely skewed tree, $h=O(n)$.

The implementation is iterative and stores only the current node, target reference, and one candidate reference. Auxiliary space is $O(1)$. It does not allocate a traversal list or recursion stack.

The returned `TreeNode` already belongs to the input tree, so no output node is created. Returning `None` also uses constant space.

## Alternatives and edge cases

- **Full inorder traversal:** Visit all nodes in sorted order and return the node after `p`. This works for any binary tree but costs $O(n)$ time and up to $O(h)$ recursion or stack space, ignoring the BST search property.
- **Right-subtree plus parent-pointer cases:** If `p.right` exists, find its leftmost node; otherwise climb ancestors until moving up from a left child. This is efficient when parent pointers are available, but the provided `TreeNode` has no parent field.
- **Recursive lower-bound search:** The same comparisons can be expressed recursively in $O(h)$ time, but recursion uses $O(h)$ call-stack space instead of the exact loop's $O(1)$.
- **`p` has a right subtree:** The search moves right at `p` and then tightens candidates leftward, returning the right subtree's minimum.
- **`p` has no right subtree:** A previously saved greater ancestor is returned if one exists.
- **`p` is the maximum node:** No greater candidate is ever saved, so the answer is `None`.
- **`p` is the minimum node:** The method still searches by comparisons and returns the next-smallest value, which may be an ancestor or a right-subtree descendant.
- **Root is the target:** If the root has a right side, search continues there; otherwise `None` is returned. No parent information is needed.
- **Single-node tree:** The sole node equals `p`, the search moves to its missing right child, and `ans` remains `None`.
- **Unique values:** Strict comparison is sufficient because duplicates are forbidden. With duplicate keys, “successor” would need a node-identity and duplicate-placement policy that this value-only search does not define.
- **Negative values:** BST comparisons work unchanged across the allowed negative and positive range.
- **Returned type:** The method returns the candidate node itself, not merely its integer value, matching the native interface.
