## General
**Generate the reverse of postorder**

Ordinary postorder is `children from left to right, then node`. Its reversal is `node, then children from right to left`. That reversed sequence is easy to produce with one stack.

**Let stack order visit right children first**

Pop a node, append its value, and push its children from left to right. Because a stack removes the last child first, the temporary sequence visits the node before its child subtrees from right to left.

**Reverse the temporary sequence once**

After every node has been emitted in root-right-left order, reverse the complete list. This moves each parent behind all descendants and changes right-to-left sibling order back to left-to-right.

**Why the final list is postorder**

For every subtree, the temporary traversal places its root before the reversed ordering of all child subtrees. Reversing the complete sequence reverses both relationships: each child subtree precedes its parent, and child subtrees appear in their original left-to-right order. Induction over subtrees therefore yields exact N-ary postorder.

## Complexity detail
Every one of the `n` nodes is pushed, popped, and appended once, and the final reversal is linear, so time is $O(n)$. The stack and output can each hold $O(n)$ values, giving $O(n)$ total space.

## Alternatives and edge cases
- **Recursive traversal with one shared output list:** directly processes children then appends the parent in $O(n)$ time, but deep trees can exceed recursion limits.
- **Stack of node/visited pairs:** simulates recursive entry and exit explicitly in $O(n)$ time without the final reversal.
- **Recursive list concatenation:** is correct, yet repeatedly copying the growing child result can take $O(n^2)$ time.
- **Preorder push direction:** pushing children in reverse and then reversing the result produces the wrong sibling order.
- **Empty tree:** returns an empty list.
- **Leaf node:** is appended immediately as the only result.
- **Wide root:** all children must remain left to right before the root.
- **Deep chain:** an explicit stack avoids call-stack overflow.
- **Repeated values:** visit every node occurrence independently.
