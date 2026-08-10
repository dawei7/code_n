## General

The competitive source performs the same postorder dynamic programming without Python recursion. It stores explicit stack frames for entering a node and for finishing that node after both children have produced their return gains.

`result` is the best complete path sum seen anywhere. Each simulated recursive call returns one extendable downward gain through a mutable one-element list.

**Why there are two frame steps**

A recursive function naturally pauses after calling its children and resumes with their results. An explicit stack must represent that pause.

A step-one frame means “enter this node.” It allocates separate holders `ret1` and `ret2` for the left and right child return values. It then pushes:

1. a step-two frame for the current node;
2. a step-one frame for the right child; and
3. a step-one frame for the left child.

Because the stack is last-in, first-out, execution enters the left child, then the right child, then resumes the current node. That is postorder.

**How mutable holders simulate returns**

Each child receives a distinct list such as `[0]` as its `ret` destination. When the child finishes, its step-two frame writes the extendable gain into `ret[0]`.

The parent's saved step-two frame references the same lists. By the time it is popped, both child calls have updated their holders, so `ret1[0]` and `ret2[0]` are available.

Plain integer arguments would not work this way because rebinding an integer inside a child frame would not update the parent's stored value. The one-element lists provide reference-based return slots.

The outer `max_sum = [0]` name is misleading: it is merely the return holder for the root call. The final global maximum is the separate scalar `result`, and the root's extendable return is not used by a parent.

**Null-child behavior**

When a step-one frame receives a null node, it executes `continue` without writing its holder. Every new holder starts as zero, so a missing child contributes zero.

No step-two frame is pushed for a null node. This exactly matches a recursive base case returning zero.

**Finishing a real node**

At step two, the child holders contain their raw extendable gains. The complete path through the current node uses each child only when its gain is positive:

`node.val + max(ret1[0], 0) + max(ret2[0], 0)`.

This candidate may use both sides because it ends somewhere in the left branch and somewhere in the right branch, meeting at the current node. `result` keeps the maximum such candidate over all nodes.

The value written to the parent holder is:

`node.val + max(ret1[0], ret2[0], 0)`.

It chooses at most one child. A path extended into the parent cannot already use both child branches, or it would fork at the current node.

**Why negative subtrees are treated correctly**

A negative child gain is replaced by zero when attaching it, because omitting that side improves the current path. The child's internal complete paths are not lost; its own step-two frame already compared them with `result`.

`result` begins at negative infinity, not zero. Every real node produces a candidate containing at least itself, so an all-negative tree returns its largest node value instead of the invalid empty-path sum zero.

**Why every possible path is covered**

Any valid simple path has a unique node closest to the original root. At that highest node, the path may descend into at most one branch on each side and cannot go farther upward.

The step-two complete candidate considers the best nonnegative downward gain from both sides at every potential highest node. It therefore dominates every valid path with that highest node.

Every constructed candidate is valid because the two child paths are disjoint except at the current node. Maximizing all candidates yields the global optimum.

**Tracing the iterative control flow**

For a leaf, entry pushes its finish frame plus two null entries. The null entries leave child holders at zero. The finish frame updates `result` with the leaf value and writes the leaf value into its parent's holder.

At node twenty in the Reference example, holders eventually contain fifteen and seven. Its finish frame records forty-two as a complete candidate and returns thirty-five as its extendable gain.

The root's finish frame may calculate another candidate, but `result` remains forty-two. The explicit stack has reproduced the same information flow as recursive postorder.

**Input contract and active class**

The tree is guaranteed nonempty. If `root` were `None` outside the contract, no finish frame would run and the source would return negative infinity.

The file also defines recursive `Solution2`, but the selected entry point is the first `Solution`. Its iterative stack avoids recursion depth failures. The source-defined `TreeNode` provides the expected fields.

## Complexity detail

Each real node creates one enter frame and one finish frame. Null-child frames also occur only a constant number per node. Total time is $O(n)$.

The explicit DFS stack holds suspended ancestor finish frames and pending sibling work. Its maximum size is $O(h)$, where $h$ is tree height. Separate one-element holders are referenced by those frames, so their number alive at once is also $O(h)$.

For a balanced tree, $h=O(\log n)$; for a chain, $h=O(n)$. Unlike recursive Python, the explicit heap-backed list is not constrained by the interpreter's recursion limit.

The returned integer uses constant output space, and the input tree is not mutated.

## Alternatives and edge cases

- **Recursive postorder with global answer:** Much shorter and expresses the two quantities naturally, but may overflow Python's call stack.
- **Recursive pair return:** Return both best complete path and extendable gain, avoiding shared global state.
- **Explicit dictionary of gains:** Traverse postorder and map every node to its gain. It is simpler than holders but uses $O(n)$ memory rather than $O(h)$.
- **Enter/exit frames:** The selected approach uses them to preserve child results without a node map.
- **Single node:** Its finish frame makes `result` equal its value.
- **All-negative values:** Negative-infinity initialization preserves the least negative node.
- **Null children:** Their preinitialized holders remain zero.
- **Positive gains on both sides:** Both contribute to the complete candidate but only one is returned.
- **Negative gain on one side:** It is omitted at the parent.
- **Path below the root:** `result` updates at every finish frame, so it is retained.
- **Nonempty requirement:** An empty tree would return negative infinity in this exact source.
- **Distinct holders:** Left and right need separate lists; sharing one would overwrite a child result.
- **Push order:** Finish must be pushed before children, and right before left, to execute left-right-current.
- **No mutation:** Stack frames and holders contain references, but tree pointers and values remain unchanged.
- **Alternative class:** `Solution2` is not executed by the active `Solution`.
