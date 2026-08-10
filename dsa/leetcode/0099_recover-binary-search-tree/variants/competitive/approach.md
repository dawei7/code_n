## General

The competitive implementation combines Morris inorder traversal with the same inversion rule used for an almost-sorted sequence. Morris supplies inorder nodes without recursion or an explicit stack by temporarily threading each left subtree's rightmost node back to its ancestor.

The list `broken = [None, None]` stores the two node objects whose values must be exchanged. `pre` is the previously visited inorder node, while `cur` is the node currently reached by traversal.

**Detecting swapped nodes**

The helper `detectBroken` checks whether `pre.val > cur.val`. On the first inversion, it stores `pre` in `broken[0]`. On every inversion, it stores `cur` in `broken[1]`.

If swapped values are adjacent in inorder, there is one inversion and those two nodes are the answer. If they are separated, the first inversion exposes the too-large value on the left, while the second exposes the too-small value on the right. Updating only the second slot at the later inversion gives the correct endpoints.

For example, the corrupted inorder values `[1, 5, 3, 4, 2, 6]` contain descending pairs `5 > 3` and `4 > 2`. The first call records node `5` as `broken[0]` and node `3` provisionally as `broken[1]`. The second call keeps node `5` and replaces the second slot with node `2`. Swapping `5` and `2` restores the sorted inorder sequence. For adjacent corruption such as `[1, 3, 2, 4]`, the sole call immediately records the final pair.

**Morris case with no left child**

When `cur.left is None`, no unvisited left subtree precedes the node. The method calls `detectBroken`, assigns `pre = cur`, and follows `cur.right`. That right link can be an original child or a temporary thread returning to an ancestor.

**Morris case with a left child**

The code finds the rightmost node in `cur.left`, stopping if its right link is empty or already points to `cur`.

- On the first encounter, an empty right link becomes `node.right = cur`, and traversal descends left. The ancestor is not visited yet.
- On the second encounter, the existing thread proves that the left subtree is complete. The current ancestor is now the next inorder node, so inversion detection runs. The thread is removed, `pre` advances, and traversal enters the original right subtree.

Unlike ID 98's selected Morris validator, this method never returns early after finding an inversion. It continues until the traversal is complete, so every installed thread reaches its removal branch. The tree's child pointers are fully restored before values are swapped.

**Why the aggregate work is linear**

The predecessor-search loop may walk several right edges, but each such edge is involved only a constant number of times across thread creation and removal. A tree has linearly many edges, so the nested-looking traversal remains $O(n)$.

**Final repair**

After Morris traversal, the two saved node values are exchanged simultaneously:

`broken[0].val, broken[1].val = broken[1].val, broken[0].val`

Python evaluates the right side first, so neither original value is lost. Only payloads change; the restored structure remains untouched.

The exact-two-swapped-nodes premise guarantees both entries are real nodes. An already valid or differently corrupted tree could leave an entry `None` and fail at this line, but such input is outside the contract.

**Return-value discrepancy**

The public method returns `self.MorrisTraversal(root)`, and the helper returns `root` after mutation. The local Function Contract says this operation should return `None` and rely on the mutated input. LeetCode-style runners generally ignore the return value for this problem, so the tree repair remains correct, but the exact source does not honor the documented return value. Removing `return root` or calling the helper without forwarding its result would match the contract.

The top-level `TreeNode.__repr__` is debugging support and is not used by recovery.

## Complexity detail

Each node is visited in inorder and relevant edges are traversed a constant number of times, giving $O(n)$ time.

The algorithm stores a two-entry list and a constant number of node references. Morris threads reuse existing empty pointers and are removed before completion, so auxiliary space is $O(1)$, matching the manifest and the follow-up. The input tree itself is the output and no node collection is allocated.

## Alternatives and edge cases

- **Recursive inorder detection:** Shorter to write, but uses $O(h)$ call-stack space and may hit recursion limits.
- **Explicit inorder stack:** Avoids temporary tree mutation with $O(h)$ storage.
- **Full inorder array:** Makes the almost-sorted sequence visible but needs $O(n)$ memory and usually a second traversal.
- **One inversion:** Adjacent swapped values fill both `broken` slots during the same call.
- **Two inversions:** The first slot remains fixed while the second is overwritten by the later, truly too-small node.
- **Thread restoration:** Continuing after detection is essential. Early return could leave cycles in the tree.
- **Return contract:** Mutation is correct, but this source returns the root instead of `None`.
- **No swapped nodes:** Not supported by the premise; the unconditional final dereference would fail.
- **Value swap only:** Node identity and all structural links remain unchanged.
- **Why no early stop is used:** Even after two inversion endpoints are known, completing traversal guarantees that every outstanding Morris thread is removed. Restoration is more important than saving a few visits.
- **Unique values:** The detector uses strict `>`. The BST premise excludes duplicates, so equality neither indicates a swapped pair nor needs special handling.
