## General
**Treat every non-root subtree as one possible cut**

Removing the edge above a node separates that node's complete subtree from the rest of the tree. If its sum is $s$ and the total tree sum is $S$, the product for that edge is $s(S-s)$. Thus every candidate can be evaluated once all subtree sums and $S$ are known.

Perform an iterative postorder traversal. Push each node first as unprocessed; when it is popped in that state, schedule it as processed after its children. When the processed entry is reached, both child sums are already available, so store their sum plus the node value. This avoids recursion depth failures on a legal 50,000-node chain.

The root is processed last, yielding $S$. Evaluate $s(S-s)$ for every stored non-root subtree sum and keep the largest full integer product. Each removable edge corresponds to exactly one non-root node, so this checks every legal split exactly once. Apply the modulus only to the final maximum.

## Complexity detail
Each node is pushed and processed a constant number of times, giving $O(n)$ time. The traversal stack, subtree-sum map, and collected sums use $O(n)$ space.

## Alternatives and edge cases
- **Two recursive traversals:** One traversal can compute $S$ and another can find the best subtree product, but a skewed legal tree may exceed Python's recursion limit.
- **Repeated subtree summation:** Recomputing all descendants for every candidate edge is correct but takes $O(n^2)$ time on a chain.
- **Two nodes:** There is only one legal edge to remove.
- **Skewed tree:** Iterative postorder handles maximum depth without call-stack growth.
- **Equal products:** Only the product value matters; the particular edge need not be returned.
- **Modulo timing:** Choose the maximum using unreduced products and take modulo afterward.
- **Positive values:** Every component sum is positive, so every legal cut has a positive product.
