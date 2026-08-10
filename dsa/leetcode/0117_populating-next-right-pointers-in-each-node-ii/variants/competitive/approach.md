## General

The competitive source uses each completed level as a linked list and constructs the next level as another linked list. It works for arbitrary binary trees: parents may have two children, one child, or no children.

A dummy node named `pre` stands just before the first child discovered on the next level. `cur` is the tail of that growing child chain. This is the same dummy-head technique often used to build an ordinary linked list without special-casing its first element.

**Preserving the original answer object**

The source saves `head = root` before traversal. The local variable `root` will later move horizontally and downward, eventually becoming `None`. Saving `head` preserves the original root reference so it can be returned after all links are populated.

For an empty input, both variables are `None`, the loops are skipped, and returning `head` correctly returns the empty root.

**The invariant at the start of a level**

At the beginning of an outer `while root` iteration:

- `root` is the leftmost real node on the current level;
- all `next` pointers across the current level are already correct;
- `pre.next` is empty; and
- `cur` points to the dummy `pre`, ready to build the next level.

This is initially true for the one-node root level because its `next` pointer starts null. The inner loop follows `root = root.next` across the current level while appending children to the next-level chain.

**Appending children without assuming tree shape**

For each current parent, the source checks the left child and then the right child independently.

When a child exists, `cur.next = child` attaches it after the last child previously discovered, and `cur = cur.next` advances the tail. If this is the first discovered child, `cur` is still the dummy, so `pre.next` automatically becomes the next level's head.

If a child is absent, nothing is appended. If a parent has no children, the tail remains unchanged. Because parents are traversed left to right and each parent's left child is considered before its right child, the resulting chain contains every real child in correct horizontal order.

There is no separate cross-parent case. The same tail append that connects siblings also connects the previous parent's last child to the next parent's first child.

**Moving to the newly built level**

After the inner loop, `pre.next` points to the first child on the next level, or `None` if no child was found. The tuple assignment

`root, cur = pre.next, pre`

evaluates its right-hand side before either left-hand assignment. Thus `root` safely receives the next-level head, and `cur` is reset to the dummy.

The following `cur.next = None` now means `pre.next = None`. It clears the dummy's link so the same dummy node can build another level.

This assignment does not disconnect the real child chain. The new `root` variable already holds a reference to its first node, and the children remain linked to one another through their own `next` fields.

**A subtle distinction about the last child**

After the tuple assignment, the old real tail is no longer stored in `cur`; `cur` has become the dummy. Therefore `cur.next = None` does not explicitly clear the last real child's `next`.

The algorithm relies on the contract that all node `next` fields initially equal null. Each level's final child is never assigned a successor, so its initial null value remains correct. If arbitrary stale links were allowed, the real tail would need to be saved and cleared explicitly.

**Tracing the sparse Reference example**

At root one, the builder appends children two and three, producing `2 -> 3`. The dummy is reset and traversal moves to node two.

Across the second level, node two contributes four and five. Node three has no left child but contributes right child seven. The common tail operation produces `4 -> 5 -> 7` without any placeholder for the missing child.

The third level has no children, so `pre.next` remains `None`. The outer update makes `root = None`, ending the process. The saved `head` still points to node one and is returned.

**Why the construction is complete and ordered**

Assume the current level's links are correct. Following them visits every real parent exactly once from left to right. Appending each parent's real children left then right enumerates precisely all real nodes of the next level in left-to-right order.

The dummy's first link identifies that level's leftmost node, and the tail links every adjacent pair. Hence the next level is correctly formed, reestablishing the outer invariant. Starting from the root proves the result for all depths.

The method only changes `next`. Original tree edges and values remain untouched. One constant-size dummy `Node` is allocated; it is not returned or inserted into any actual level.

## Complexity detail

Let $n$ be the number of nodes. Each real node is visited once as a current-level parent. Each real child is appended once to a next-level chain. All checks and assignments are constant time, so total time is $O(n)$.

The algorithm stores `head`, `root`, `pre`, and `cur`, plus one dummy node. Their number does not depend on input size, giving $O(1)$ auxiliary space.

Using existing `next` fields for traversal does not count as an extra data structure; those fields are the required output. The dummy is a fixed single object, so it remains constant space.

Unlike queue BFS, memory does not grow with maximum width. A level containing thousands of nodes is traversed through its own links one node at a time.

## Alternatives and edge cases

- **Queue breadth-first search:** Simple and robust, but uses $O(w)$ auxiliary memory and does not meet the constant-space follow-up.
- **Helper function for child append:** Encapsulate the dummy/tail update and return the new tail. It can improve readability while preserving the same state.
- **Separate first-child special case:** Track the next level's head without a dummy. This avoids one allocation but adds branching each time the first child is found.
- **Perfect-tree direct formulas:** Not valid for arbitrary sparse trees because a neighboring parent may lack the expected child.
- **Explicit real-tail reset:** Preserve the final child tail and set its `next = None` if inputs may have stale links.
- **Empty tree:** Returns the saved `None` head.
- **Single node:** Builds no next level and returns the same node.
- **Parent with only a right child:** The right child is appended as the next real node with no artificial gap.
- **Parent with only a left child:** The left child is appended normally.
- **Parent with no children:** It contributes nothing and does not disturb the tail.
- **Gap across parents:** The last child of one parent connects directly to the first real child of a later parent.
- **Child order:** Left must be considered before right to preserve horizontal order.
- **Dummy reset:** It must occur after saving `pre.next` into `root`; clearing first would lose access to the next level.
- **Tuple assignment semantics:** Python reads both old right-hand values before rebinding `root` and `cur`, which makes the reset sequence safe.
- **Initial null links:** Required for real level tails because only the dummy link is explicitly cleared.
- **Return identity:** `head` preserves and returns the original root even though the working `root` cursor ends as `None`.
- **Locally defined `Node`:** The constant dummy uses the source's compatible node class; it carries no meaningful tree value.
