## General

The choice made inside one subtree affects its parent only through two facts: the Boolean value produced and the number of flipped leaves. Therefore, each node needs a pair of costs rather than one locally preferred evaluation.

For every node $u$, store the minimum flips that make its subtree false and the minimum flips that make it true. A leaf already produces its stored bit for cost zero and produces the opposite bit for cost one. A NOT node swaps its child's two costs.

For an OR, AND, or XOR node, try the four pairs of child outcomes. Apply the node's operator to determine the resulting Boolean value, add the two child costs, and retain the smaller sum for that result. These four combinations include every way the node can obtain either outcome, while the child entries are already optimal by postorder induction. The resulting pair is therefore optimal for the whole subtree.

An explicit visited-state stack performs postorder traversal without recursion. This matters because the tree may contain $10^5$ nodes and can be deep enough to exceed Python's call-stack limit. Once the root pair is known, select the entry indexed by the requested result.

## Complexity detail

Let $n$ be the number of tree nodes. Each node is pushed a constant number of times and each operator examines at most four child-outcome pairs, giving $O(n)$ time. The postorder stack and the two-cost table can each contain $O(n)$ entries, so auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Recursive tree DP:** The same two-state recurrence is mathematically sufficient, but a skewed tree near the maximum size can overflow Python's recursion stack.
- **Evaluate first, then repair:** Choosing flips only after following the current Boolean evaluation can miss a cheaper combination in a subtree; both possible outcomes must be retained.
- **Leaf root:** Its answer is zero when its value matches `result` and one otherwise.
- **Unary child side:** A NOT node may use either its left or right child, so the implementation selects whichever child exists.
- **XOR semantics:** Equal child outcomes produce false and different outcomes produce true; it cannot use the shortcuts for OR or AND.
