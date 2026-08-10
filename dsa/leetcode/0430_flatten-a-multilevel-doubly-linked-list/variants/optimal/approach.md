## General

**The required order is preorder over two kinds of links**

At a node `cur`, the flattened order must be:

1. `cur` itself;
2. every node reachable through `cur.child`, recursively flattened; and
3. the nodes that originally followed through `cur.next`.

This is preorder depth-first traversal if `child` is treated like a first branch and `next` like a second branch. The recursive helper `preorder(pre, cur)` links the flattened structure beginning at `cur` immediately after node `pre` and returns the tail of everything it flattened.

Returning the tail is crucial. After inserting a child list, the original next node must be connected after the deepest final node of that child structure, not merely after the child's head.

**Link the current node first**

If `cur is None`, there is nothing to append, so the helper returns `pre`. This base case is especially useful when a node has no child: flattening that absent child returns the node itself as the correct tail.

For a real current node, the assignments

`cur.prev = pre` and `pre.next = cur`

create reciprocal links between the already flattened prefix and `cur`. This happens before recursion because `cur` precedes both its child list and its original next list in the required order.

**Save the original next pointer before flattening the child**

The statement `t = cur.next` preserves the original continuation. This must occur before the child recursion. If a child exists, `preorder(cur, cur.child)` executes `cur.next = cur.child`, deliberately overwriting the pointer that formerly led to the next node on the parent level.

Without `t`, that original continuation would be lost and all nodes after `cur` on its level could become unreachable.

The call

`tail = preorder(cur, cur.child)`

inserts and recursively flattens the entire child hierarchy immediately after `cur`. It returns the final node of that inserted block. If there is no child, the base case returns `cur`, which is exactly the correct insertion tail.

The child pointer has now served its purpose and is cleared with `cur.child = None`, satisfying the output requirement that no child links remain.

Finally,

`preorder(tail, t)`

attaches the saved original continuation after the child block and recursively handles any children encountered there. Its returned value becomes the tail for the entire structure starting at `cur`.

**A pointer-level example**

Suppose `1.next` is `2`, while `1.child` begins `3 -> 4`. At node `1`, the code saves `t = 2`. Child recursion rewires `1.next = 3`, sets `3.prev = 1`, then links `3 <-> 4` and returns tail `4`. The final recursive call links `4.next = 2` and `2.prev = 4`.

The result is `1 <-> 3 <-> 4 <-> 2`, exactly placing the child list before the old next node. Nested children follow the same rule recursively, producing full depth-first order.

**Why the dummy node simplifies the head case**

For a nonempty input, the solution creates `dummy = Node(0, None, head, None)` and calls `preorder(dummy, head)`. The helper can now assume `pre` is always a real node and use the same two linking assignments even for the first actual node.

That temporarily makes `head.prev = dummy`. After traversal, `dummy.next` is still the first real node. The line `dummy.next.prev = None` detaches the sentinel from the result, and `dummy.next` is returned.

The dummy is not inserted into any later position and is not part of the returned list.

**Why every node is visited exactly once**

The original structure gives every non-head node one ownership path: either it is reached through a level's `next` chain or from exactly one `child` pointer. At each node, the helper recursively visits the child branch before the saved next branch. Saving `t` preserves both branches even as pointers are rewritten.

No recursive call follows a newly created link as if it were an unvisited original branch; calls use the explicit original `child` and saved original `next` references. Therefore each node is processed once, no node is lost, and no node is duplicated.

**List invariants after flattening**

Every link is established in both directions at the same moment: `pre.next = cur` and `cur.prev = pre`. Every processed `child` is set to `None`. The original final node of the depth-first traversal already has no unvisited continuation, so it remains the tail with `next = None`. Detaching the dummy gives the real head `prev = None`.

Thus the output is a single-level, well-formed doubly linked list in the required order.

## Complexity detail

Let $n$ be the total number of nodes across every level. Each node enters `preorder` once and undergoes constant pointer work, so time complexity is $O(n)$.

The implementation is recursive. In the worst case, nodes form a deeply nested chain through child/next recursion, producing $O(n)$ active calls. Auxiliary-space complexity is therefore $O(n)$. No new result nodes are allocated; the dummy is one constant extra node, and the original nodes are rewired in place.

## Alternatives and edge cases

- **Iterative preorder with a stack:** Push an original `next` node before the child so the child is popped first. It also takes $O(n)$ time and $O(n)$ worst-case space while avoiding recursion depth limits.
- **Find each child-list tail by walking:** Splice the child after its parent, then scan to its tail before reconnecting the old next. Repeated tail scans can revisit nodes and degrade toward $O(n^2)$.
- **Collect nodes before relinking:** A DFS array makes rewiring simple but uses $O(n)$ explicit storage in addition to recursion/iteration state.
- **Forget to save `cur.next`:** Child insertion overwrites it, losing the remainder of the parent level.
- **Forget to clear `child`:** The visible next/prev chain might look correct, but the result would still violate the single-level contract.
- **Empty input:** The early return gives `None` and avoids constructing/dereferencing a dummy result.
- **No child pointers anywhere:** The recursion relinks the existing sequence consistently and returns the original head.
- **Child on the final node:** Its flattened block simply becomes the new tail.
- **Nested children:** Returning the deepest tail ensures each saved continuation is attached after the entire nested block.
- **Head predecessor:** The final detachment is necessary; otherwise the returned head would incorrectly point back to the dummy.
