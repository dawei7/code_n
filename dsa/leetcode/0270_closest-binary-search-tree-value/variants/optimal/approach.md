## General
**Update the best value along one search path**

Keep the closest value seen so far. At each node, update it if the node is nearer, using the smaller value to break a tie, then move left when the target is smaller and right otherwise.

Before leaving a node, `closest` is optimal among the visited path. The discarded subtree lies entirely on the opposite side of the current value from the target and therefore cannot improve over the current node.

**The opposite subtree cannot beat the current node**

If the target is below the current value, every value in the right subtree is at least the current value and therefore no closer than the current node; only the left subtree can improve the answer. The symmetric argument holds when the target is larger. Updating before following that sole promising child preserves the best candidate until the search path ends.

## Complexity detail
One node per tree level is examined, for $O(h)$ time. Iteration stores only the current node and best value.

## Alternatives and edge cases
- **Traverse the whole tree:** is correct but takes $O(n)$ instead of exploiting BST order.
- Exact matches may return immediately; targets outside the value range converge to an extreme node.
