## General

**Only the leaf-to-root path must change**

Rerooting does not require rebuilding the entire tree. The new root is the supplied `leaf`, and the only edges whose direction changes are those on the parent chain from that leaf to the old `root`. Every subtree hanging off that path remains attached to the same path node, although one left child may need to move to the right to free the left pointer for the reversed parent edge.

The implementation walks upward with constant state:

- `cur` is the current path node whose original parent edge will be reversed;
- `p` is `cur`’s original parent;
- `gp` temporarily saves `p`’s original parent before any pointer changes.

Initially `cur = leaf` and `p = leaf.parent`.

**Save the grandparent before changing parent links**

At the top of each iteration, `gp = p.parent` records the next node above `p`. This assignment must occur before `p.parent = cur`. Once `p`’s parent pointer is reversed, following it would lead back down to `cur` instead of continuing toward the old root. Saving `gp` preserves the traversal route.

This is the same principle used when reversing a linked list: retain the next original link before overwriting it.

**Make room for the reversed edge**

The required new structure makes the original parent `p` become `cur.left`. If `cur` already has a left child, overwriting that field would lose an entire off-path subtree. The source first performs

`cur.right = cur.left`

when `cur.left` exists.

Why is it safe to write into `cur.right`? At the initial iteration, `cur` is the supplied leaf and has no children. At later iterations, `cur` was the previous iteration’s parent. Its child pointer toward the path node below has just been cleared. If that path child was its right child, the right slot is empty and a remaining left off-path child must move there. If the path child was its left child, the left slot is already empty, so the conditional move does not run and any ordinary right child stays in place.

The moved child’s `parent` pointer needs no update because it remains a child of the same node `cur`; only its left-versus-right side changes.

**Reverse one path edge and remove the old direction**

After making the left slot available, the source assigns `cur.left = p`. This makes the original parent a child of the current node. It also updates the reverse metadata with `p.parent = cur`, so the downward child pointer and upward parent pointer agree.

The old parent `p` still has a child pointer to `cur`. Leaving that pointer would create a two-node cycle. The implementation checks which side held `cur`:

- if `p.left == cur`, set `p.left = None`;
- otherwise, if `p.right == cur`, set `p.right = None`.

Exactly one comparison is true in a valid tree. Clearing that pointer completes the edge reversal: `cur` now points down to `p`, `p` points up to `cur`, and `p` no longer points back down to `cur`.

The variables then advance upward with `cur = p` and `p = gp`. All pointer decisions for that iteration used the old values before these assignments.

**Why the loop excludes the old root**

The loop runs while `cur != root`. It processes every path node from the leaf through the child immediately below the old root. In the final iteration, `p` is the old root. That iteration attaches the old root as the current node’s left child, updates `root.parent` to point downward toward the new root, and removes the old root’s pointer back to that child.

After advancing, `cur` becomes the old root and the loop stops. There is no edge above the old root to reverse, so processing it again would be meaningless and `p` would be `None`.

Finally, `leaf.parent = None` removes the new root’s old upward link. No iteration changes that field because `leaf` is always `cur` in the first reversal, while the code changes `p.parent`. Explicitly clearing it establishes the defining root property.

**A path-level invariant and correctness**

After each iteration, the portion from the original leaf down through the just-processed original parent has the required reversed orientation. Every processed node’s child and parent pointers agree, and no old forward pointer creates a cycle. The saved `gp` still identifies the unprocessed continuation toward the old root.

Off-path subtrees remain attached to their original path nodes. If such a subtree occupied a left slot needed for the new parent edge, it moved to the right of the same node; otherwise it was untouched. No node is allocated, copied, or discarded.

The loop eventually reverses every original edge on the unique leaf-to-root path. Clearing `leaf.parent` makes the leaf the only top node, and the returned object is that same supplied leaf. Therefore all nodes remain in one correctly rerooted tree with parent pointers consistent with the new child directions.

## Complexity detail

Let `h` be the number of edges on the path from `leaf` to the original `root`. The loop executes once per path edge. Each iteration performs a constant number of pointer reads, comparisons, and assignments, so running time is $O(h)$.

The method stores only `cur`, `p`, and `gp` plus existing node references. It allocates no collection and uses no recursion, so auxiliary space is $O(1)$.

Nodes outside the path are not traversed. Even if they contain most of the tree, their cost does not appear beyond the constant-time pointer preservation at their attachment point.

## Alternatives and edge cases

- **Recursive upward rerooting:** Recursion can reverse the same parent chain with $O(h)$ time, but it uses $O(h)$ call-stack space and must still save original links before mutation.
- **Store the complete path first:** Collect leaf-to-root nodes in an array, then reconnect them in a second pass. This can simplify reasoning but uses $O(h)$ extra space that the parent pointers make unnecessary.
- **Forget to clear `p`’s old child pointer:** This creates a cycle in which `cur` points to `p` and `p` still points to `cur`.
- **Forget to save `gp`:** After `p.parent = cur`, the original upward path is lost and following `p.parent` moves in the wrong direction.
- **Existing left off-path subtree:** It must move to `cur.right` before `cur.left` is overwritten, or that subtree becomes unreachable.
- **Existing right off-path subtree:** It remains in place when the original path child was on the left; the code moves a child only when `cur.left` is occupied.
- **Two-node tree:** The loop runs once, makes the old root the leaf’s left child, clears the old root’s child link, and makes the leaf’s parent null.
- **Leaf is genuinely childless:** The first iteration never needs to preserve a left subtree, matching the supplied-node guarantee.
- **Old root’s parent:** It begins as `None` but is correctly changed during the final edge reversal because the old root is no longer the root.
- **New root’s parent:** The explicit final assignment to `None` is required; child pointers alone are not enough for this custom node structure.
- **Unique values:** The algorithm does not rely on values at all. It compares node objects and follows structural pointers, so uniqueness is irrelevant to its mechanics.
- **In-place behavior:** All changes affect the supplied nodes directly. Any external references to those nodes observe the rerooted relationships.
