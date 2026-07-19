## General
**Use the postfix stack invariant.** After processing any prefix of `postfix`, keep a stack containing the roots of all complete expressions encoded by that prefix but not yet consumed by a later operator. An operand token creates a leaf and adds one root. An operator consumes exactly two complete expressions: pop the right root first, then the left root, attach both to a new operator node, and push the new root.

**Separate construction from evaluation.** Every concrete node stores its token and optional children. A leaf converts its operand token to an integer. An operator recursively evaluates its left and right subtrees, then applies its stored operation in that order. For division, compute the magnitude quotient and restore the sign so negative results truncate toward zero rather than following floor division.

Because the input is a valid postfix expression, every operator finds two roots and the final stack contains exactly one root. The stack invariant shows that this root represents the entire expression with the correct operand order. Structural recursion then applies each tree operator to exactly the values of its two represented subexpressions, so `evaluate()` returns the postfix expression's value.

## Complexity detail
Each of the $t$ tokens creates one node or combines two existing roots in $O(1)$ stack work, so construction takes $O(t)$ time. Evaluation visits every node once and also takes $O(t)$ time. The tree, construction stack, and worst-case recursive evaluation depth each use $O(t)$ space.

## Alternatives and edge cases
- **Evaluate without retaining a tree:** An integer stack can compute the postfix value in $O(t)$ time, but it does not satisfy the required `Node` and `TreeBuilder` design contract.
- **Recursive parsing from the end:** Reading tokens right-to-left can recursively build the right subtree and then the left subtree in $O(t)$ time, but careful shared-index management is required.
- **Front-based list stack:** Inserting and removing at index zero preserves correctness, but shifting the remaining entries can make construction $O(t^2)$.
- A one-token expression produces a single leaf with no children.
- Subtraction and division require popping the right operand before the left; reversing them changes the result.
- Intermediate values may be negative even when every operand token is nonnegative.
- Division must truncate toward zero, which differs from floor division for negative quotients.
