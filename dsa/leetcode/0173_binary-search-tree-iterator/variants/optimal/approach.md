## General

**Flatten inorder values during construction**

The selected class does not maintain a paused tree traversal. Its constructor
performs a complete recursive inorder traversal and stores every node value in
`self.vals`.

For a binary search tree, inorder means:

1. visit the left subtree;
2. process the current node;
3. visit the right subtree.

The BST ordering property places every left-subtree value before the current
value and every right-subtree value after it. Therefore the resulting list is
in non-decreasing order and represents the exact iterator sequence.

`self.cur` begins at zero, so it identifies the first value that has not yet
been returned.

**Understand the nested traversal helper**

`inorder` is defined inside `__init__` and closes over `self`. For a null node,
it does nothing. For a real node, it recursively completes the left subtree,
appends `root.val`, and then completes the right subtree.

Appending only after the left recursive call is what places the smallest
reachable value first. Appending before that call would be preorder and would
not satisfy this iterator.

The complete traversal occurs before construction returns. Subsequent calls no
longer access the tree and depend only on the flat array.

**Serve `next` with one array access**

`next()` reads `self.vals[self.cur]`, saves it as `res`, increments `self.cur`,
and returns the value.

The Reference guarantees every `next()` call is valid, so the source does not
check the array boundary first. If a caller violates the guarantee after all
values have been consumed, Python raises `IndexError`.

Advancing after the read matches the conceptual pointer that begins before the
smallest element: the first call returns index zero and leaves the cursor at
index one.

**Answer `hasNext` from cursor position**

`hasNext()` returns whether `self.cur < len(self.vals)`. Equality means every
stored traversal value has been returned. A smaller cursor means its indexed
value is the next one.

This returns an actual Python Boolean and does not change iterator state.
Calling it repeatedly between `next()` operations is harmless.

**Trace the example tree**

For the BST rooted at seven with left child three and right subtree
`15 <- 9, 20`, inorder traversal builds:

`[3, 7, 9, 15, 20]`.

The first two `next()` calls return three and seven, moving `cur` to two.
`hasNext()` compares two with five and returns true. Later calls return nine,
15, and 20 in order. Once `cur` reaches five, `hasNext()` returns false.

The iterator stores values rather than nodes. Since the interface returns
integers, node identity is not needed after construction.

**Why flattening is correct**

By induction on a subtree, the recursive helper appends exactly that subtree's
values in sorted inorder. The empty subtree contributes an empty sequence.
For a real root, the correct left sequence is appended first, then the root,
then the correct right sequence. BST ordering makes the concatenation sorted.

After construction, the invariant is that `vals[0:cur]` contains exactly the
values already returned and `vals[cur:]` contains exactly those still pending.
`next` transfers the first pending value across that boundary, and `hasNext`
tests whether the pending suffix is nonempty.

**Recognize the eager design tradeoff**

Flattening makes each public query extremely simple and worst-case constant
time. The cost is paid up front even if a caller asks for only the smallest
one or two values.

It also stores all $n$ values, which does not satisfy the follow-up's $O(h)$
memory goal on a balanced tree. The manifest's space declaration describes the
lazy controlled-traversal design, not this exact selected source.

**Harness and recursion details**

`TreeNode` is commented as a platform-provided type. A standalone environment
must supply it for the annotation and tree fields.

The recursive call depth equals tree height $h$. A highly skewed tree with up
to $10^5$ nodes can exceed Python's default recursion limit, even though the
algorithm is mathematically correct.

## Complexity detail

Let $n$ be the node count and $h$ the tree height. Construction visits every
node once, taking $O(n)$ time. Each `next()` and `hasNext()` call is worst-case
$O(1)$ time.

`self.vals` stores $n$ values, and recursion uses $O(h)$ call-stack space.
Total auxiliary space is $O(n+h)=O(n)$. This contradicts the manifest's
$O(h)$ claim for the exact source, except in a fully skewed tree where
$h=O(n)$.

## Alternatives and edge cases

- **Lazy explicit stack:** Push the current left spine, pop one node per `next`, then push its right child's left spine. It uses $O(h)$ memory and amortized $O(1)$ per `next`.
- **Generator recursion:** Expresses inorder naturally but still uses call-stack depth and requires careful iterator state.
- **Morris traversal:** Can use $O(1)$ auxiliary space by temporary threading, but it mutates links during traversal and complicates an interruptible iterator.
- **Single-node tree:** Construction stores one value; one `next` consumes it.
- **Empty tree outside the stated node lower bound:** The list remains empty and `hasNext` is false.
- **Repeated `hasNext`:** It reads state without advancing.
- **Invalid `next`:** The contract forbids it; otherwise indexing raises an exception.
- **Skewed tree:** Recursive construction risks Python recursion overflow.
- **Eager work:** The whole tree is visited even if only one result is requested.
- **Manifest mismatch:** The flat list requires $O(n)$ rather than follow-up $O(h)$ space.
