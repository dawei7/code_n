## General

**Pause an inorder traversal with an explicit stack**

The competitive iterator does not flatten the tree. Instead, `self.__stk`
stores the chain of nodes whose left subtrees have been handled but whose own
values are still pending.

The helper `__traversalLeft(node)` pushes `node` and repeatedly follows
`.left`. After it stops, the stack top is the leftmost node of that subtree and
therefore the next inorder value.

The constructor calls this helper on the root, preparing the smallest tree
value before any public operation.

**Maintain the next node at the stack top**

The central invariant is that, whenever pending nodes exist, the top of the
stack is the next node in inorder.

Nodes below it are ancestors whose left side has already been represented in
the traversal but whose own turn comes later. Unvisited right subtrees are not
placed on the stack early; they become relevant only after their parent is
returned.

This is equivalent to pausing recursive inorder just before it processes a
node. The explicit list preserves the recursion state across separate method
calls.

**Advance one inorder position**

`next()` pops the stack top into `node`. That node is the next smallest value
by the invariant.

After visiting a node in inorder, traversal proceeds to its right subtree. The
smallest value in that subtree is its leftmost node, so the source calls
`__traversalLeft(node.right)`. If there is no right child, the helper performs
no work and the next pending ancestor is already exposed on the stack.

Finally, the method returns `node.val`.

**Trace the sample**

For the root seven, construction pushes seven and then three. The top is three,
so the first `next()` pops and returns it. Three has no right subtree, exposing
seven.

The second `next()` pops seven, then descends through its right child 15 and
that node's left child nine. The stack top becomes nine. Later, popping nine
exposes 15; popping 15 pushes 20; and popping 20 empties the stack.

The resulting sequence is `3, 7, 9, 15, 20`, exactly the BST's inorder order.

**Why each node appears once**

A node is pushed only when the helper follows a left edge from a subtree root.
It remains pending until popped by `next`. After being popped, the algorithm
visits its right subtree but never pushes that same node again.

Every tree node is either on the initial left spine or belongs to the right
subtree of some node eventually popped. Therefore every node is eventually
pushed and returned exactly once.

The stack-top invariant holds after construction. Popping returns the correct
node, and pushing the right subtree's full left spine prepares its smallest
pending successor. Induction over calls proves sorted output.

**Amortized time rather than worst-case time**

One `next()` call can descend a long left chain in a right subtree, taking
$O(h)$ time in that call. However, every node is pushed once and popped once
across the iterator's entire lifetime.

For $q$ successful `next()` calls, the total stack work is $O(q+h)$, and over
all $n$ nodes it is $O(n)$. The average, or amortized, cost per `next()` is
$O(1)$. This is the follow-up guarantee; it is not a promise that every
individual call is worst-case constant.

**Return-type defect in `hasNext`**

The selected `hasNext()` returns `self.__stk` directly. An empty list is falsy
and a nonempty list is truthy, so the method works in a Boolean condition such
as `while iterator.hasNext():`.

However, the contract explicitly requires a Boolean result. The exact source
returns either the mutable list object or an empty list, not `True` or `False`.
A serializer or strict equality check can observe this mismatch. The conforming
implementation is `return bool(self.__stk)`.

**Harness node definition**

The file includes a top-level `TreeNode` class. In the native platform, the
tree node is normally harness-provided. The iterator itself allocates no new
tree nodes and only reads their links.

## Complexity detail

Construction follows at most one root-to-leaf path, taking $O(h)$ time.
`hasNext()` is conceptually $O(1)$. Each `next()` is $O(1)$ amortized and
$O(h)$ worst case for one call.

The stack holds at most one path of height $h$, so auxiliary space is $O(h)$.
These intended bounds match the manifest. The list-valued `hasNext` remains a
type-contract issue, not an asymptotic one.

## Alternatives and edge cases

- **Eager inorder array:** Gives worst-case $O(1)$ public methods but uses $O(n)$ storage and $O(n)$ construction time.
- **Recursive generator:** Naturally pauses traversal but relies on generator and recursion-stack machinery.
- **Morris threading:** Uses constant extra space but temporarily changes tree links and is more difficult to pause safely.
- **One node:** Construction pushes it, one `next` returns it, and the stack becomes empty.
- **Repeated `hasNext`:** It does not mutate stack state, though it returns the stack object rather than a Boolean.
- **Valid-next guarantee:** The source calls `pop()` without checking; an invalid call would raise `IndexError`.
- **Deep skew:** The explicit stack handles height $n$ without Python recursion overflow.
- **Right subtree:** Its entire left spine must be pushed after returning the parent.
- **Tree preservation:** The iterator never writes node links.
- **Boolean contract:** Wrap the stack with `bool(...)` for an actual `True` or `False` result.
