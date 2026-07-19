## General
**Model the required order as iterative depth-first traversal**

The flattened order visits a node, then its entire child sequence, then its original next node. Use a stack of pending nodes. After popping the current node, push its original `next` first and its `child` second, so last-in-first-out order processes the child before returning to the sibling.

**Link each visited node to the previous output node**

Keep `previous`, the tail of the flattened prefix. Connect `previous.next` to the popped node and set the node's `prev` back to `previous`. Clear the node's `child` after saving it on the stack. The original head remains the first node and must keep `prev = None`.

**Why each pointer is rewritten exactly as required**

The stack order is precisely preorder over the multilevel structure. Every original node is pushed once from either a `next` or `child` link and popped once. Linking consecutive pops creates the exact flattened adjacency in both directions, while clearing every popped node's child removes all remaining levels. The final node has no pending successor, so the chain terminates normally.

## Complexity detail
Each of the `n` nodes is pushed, popped, and linked once, giving $O(n)$ time. In the worst case the stack holds $O(n)$ pending siblings; the transformation itself reuses all original nodes.

## Alternatives and edge cases
- **Recursive splice returning the tail:** flatten a child and return its tail to reconnect the saved sibling; this takes $O(n)$ time and $O(d)$ call-stack space.
- **Walk from every child head to rediscover its tail:** produces the same order but can revisit long flattened children and take $O(n^2)$ time.
- **Empty input:** return `None`.
- **No child links:** preserve the existing order while ensuring reciprocal pointers remain valid.
- **Nested children:** a descendant is completed before any saved sibling resumes.
- **Head predecessor:** the returned head's `prev` must remain `None`.
