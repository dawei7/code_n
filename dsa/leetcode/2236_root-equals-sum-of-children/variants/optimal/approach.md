## General

**Use the fixed tree shape**

The contract guarantees exactly three nodes, so both `root.left` and
`root.right` exist and there are no other values to inspect. Add the two child
values and compare that sum directly with the root value.

The method returns `true` exactly when `root.val == root.left.val +
root.right.val`. This is the condition in the problem definition, so the
comparison accepts every qualifying tree and rejects every other legal tree.

## Complexity detail

The algorithm reads three node values, performs one addition, and performs one
comparison. Its time and auxiliary space are therefore both $O(1)$.

The tree always has exactly three nodes and each value comes from a fixed set
of 201 integers. The bounded-domain certificate records why no growing input
size exists under the legal contract and replaces scaling with broad property
checks across all child-value pairs.

## Alternatives and edge cases

- **General tree traversal:** Breadth-first or depth-first traversal would work but is unnecessary for a tree whose complete shape is fixed by the contract.
- **Recursive subtree sums:** Computing arbitrary subtree totals solves a broader problem and adds recursion without changing this three-node comparison.
- **Negative values:** Ordinary signed addition applies; a negative root may equal the sum of two negative or mixed-sign children.
- **Cancellation:** Children such as `-8` and `8` sum to zero.
- **Guaranteed children:** No null check is required because both children always exist.
- **Value boundaries:** The child sum can range from $-200$ through $200$, even though each individual node value is between $-100$ and $100$.
