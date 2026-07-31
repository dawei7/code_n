## General

A preorder traversal always keeps one current root-to-node path. Store that path in a stack of node identifiers. The first entry must be the root, so its parent identifier must be $-1$; initialize the stack with its node identifier.

For each later pair `[id, parentId]`, remove stack entries while the top is not `parentId`. Each removed node belongs to a subtree that the traversal has finished. If the stack becomes empty, the claimed parent is no longer on the active path, so returning to it would violate preorder and the answer is `false`. Otherwise, the top is exactly the new node's parent, and pushing `id` extends the active path.

This invariant matches preorder precisely: before processing an entry, the stack contains exactly the ancestors whose subtrees may still receive the next node. Popping models finishing one or more nested subtrees, and a successful parent match attaches the next node at the only legal active location. Therefore every accepted order admits a preorder traversal, while every rejected order tries to attach a node beneath a subtree that has already closed.

## Complexity detail

Each of the $n$ identifiers is pushed once and popped at most once. The total running time is $O(n)$, including all iterations of the inner popping loop. The stack can hold an entire root-to-leaf path, so the auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Rebuild the tree and traverse it:** Constructing explicit child lists and comparing a generated traversal can also be linear, but the children have no fixed left-versus-right labels, so the implementation must preserve the candidate order carefully.
- **Search the ancestor list first:** Checking whether every parent occurs anywhere in the stack before popping is correct, but linear membership searches make a deep chain take $O(n^2)$ time.
- **Single root:** A one-node tree is always a valid preorder when that entry has parent identifier $-1$.
- **Deep unwinding:** Moving from a leaf to an uncle is valid because the stack may pop several completed ancestors before finding the uncle's parent.
- **Closed subtree:** Once a node is popped, no later entry may name it as a parent.
