## General
**Reuse the consumed prefix as the ancestor stack**

Maintain `top`, the last occupied position of a decreasing stack stored inside the already consumed prefix of `preorder`. A new value greater than the stack top closes left subtrees; pop until the active ancestor path can accept it, and let the last popped value become the strict lower bound for all later values.

After each value, `preorder[0:top + 1]` represents the unfinished root-to-current path, and every future value must exceed `lower_bound` because traversal has already entered that ancestor's right subtree.

**Entering a right subtree creates a permanent lower bound**

Whenever `x` exceeds an ancestor on the stack, preorder has finished that ancestor's left subtree and entered its right subtree. Any later value below the last popped ancestor would violate BST ordering. Otherwise, popping exactly the smaller ancestors identifies the valid active path, and writing `x` at the next stack position preserves the decreasing-stack invariant.

Each input position is read before that position can be overwritten. Stack writes affect only the consumed prefix, so reusing the array does not change any future value that remains to be validated.

## Complexity detail
Each value is pushed once and popped at most once, giving $O(n)$ time. The input array itself stores the monotonic stack, while `top` and `lower_bound` use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Separate monotonic stack:** preserves the input and uses the same recurrence, but requires $O(n)$ auxiliary space in the worst case.
- **Recursively partition each range:** mirrors the tree definition but repeatedly scans skewed ranges and can take $O(n^2)$.
- **Input mutation:** is the tradeoff that achieves the source follow-up's constant-extra-space target.
- **Singleton sequence:** is always a valid preorder under the minimum legal input size.
