## General

**Why postfix notation makes tree construction stack-based**

In postfix notation, operands appear before the operator that uses them. When the scan reaches a number, that number already represents a complete one-node expression tree. When it reaches an operator, the two complete operand expressions immediately before it are available and can become its children.

The source stores these not-yet-combined trees in `stk`. Every token first becomes a `MyNode`. If the token is numeric, the node is simply pushed as a leaf. If the token is an operator, the source pops two existing roots, attaches them to the operator node, and pushes the newly combined tree back.

This process reduces two completed expressions to one after every operator. Because the postfix input is guaranteed valid, two roots are always available when an operator appears, and exactly one root remains after the last token. `stk[-1]` is therefore the root of the whole expression.

**Operand order is essential**

The first item popped is assigned to `node.right`, and the second is assigned to `node.left`. A stack removes the most recently completed expression first. For postfix sequence `["5", "2", "-"]`, the 2 is popped first and must be the right operand, while 5 is popped second and must be the left operand. The resulting tree evaluates $5-2$, not $2-5$.

Addition and multiplication would hide an accidental reversal because they are commutative. Subtraction and division expose it. Always attaching the first pop on the right is what preserves the original postfix meaning for every operator.

For a longer example such as `["3", "4", "+", "2", "*"]`, the first operator combines 3 and 4 and pushes the subtree representing $3+4$. The next number pushes a leaf for 2. Finally, `*` pops 2 as its right subtree and $3+4$ as its left subtree, producing $(3+4)\times2$.

**The node interface and concrete representation**

`Node` inherits from `ABC` and declares `evaluate` with `@abstractmethod`. This defines the platform-facing promise: every concrete expression node must know how to evaluate itself.

`MyNode` is the concrete implementation. It stores the original token in `val` and initializes `left` and `right` to `None`. A numeric token remains a leaf with no children. An operator token receives exactly two children during construction.

The single concrete node type handles both roles. `x.isdigit()` distinguishes an operand from an operator. Under the stated token contract, numeric operands have non-negative decimal representations, so `isdigit` is the appropriate test.

**Recursive evaluation mirrors the tree**

When `evaluate` reaches a numeric node, it converts the token to an integer and returns it. This is the recursion base case.

For an operator, it first evaluates the left and right subtrees:

`left, right = self.left.evaluate(), self.right.evaluate()`.

Those recursive calls calculate the complete operand values before the current operation is applied. The method then dispatches on `val`:

- `+` returns `left + right`.
- `-` returns `left - right`.
- `*` returns `left * right`.
- `/` returns `left // right` in this exact Python source.

The input guarantees valid operator tokens and no division by zero, so one of the four branches handles every internal node safely.

The use of `//` is an exact implementation detail: Python floor division rounds a non-integral negative quotient downward, rather than truncating it toward zero. The local contract does not separately specify a negative-division rounding rule, so the explanation records what the source actually executes. Positive divisions behave in the familiar integer-quotient way.

**Why construction produces the unique postfix tree**

Maintain this invariant while scanning: each stack entry is the root of a complete expression tree for one contiguous, fully processed postfix expression, and the stack entries appear in the same left-to-right order as those expressions.

A numeric token creates a valid one-token expression and preserves the invariant when pushed. For an operator, postfix grammar says the last two completed expressions are its left and right operands. Popping right, then left, and joining them below the operator creates exactly their combined expression. Pushing that root restores the invariant.

A valid complete postfix expression consumes all of its component expressions, leaving one stack entry. By the invariant, that entry represents all tokens in their required structure. This establishes construction correctness.

**Why evaluation returns the expression value**

Use structural induction on the constructed tree. A leaf contains a numeric token, and converting it to `int` gives that operand's value. For an internal node, assume each child recursively returns the value of its represented subexpression. Applying the node's stored operator to the left and right results, in that order, gives the value of the combined expression. Thus every subtree evaluates correctly, including the returned root.

The design also separates building from using: `TreeBuilder` knows postfix stack rules, while `MyNode.evaluate` knows recursive expression semantics. The caller receives only the abstract `Node` interface and can evaluate without knowing how the tree was assembled.

## Complexity detail

Let $t$ be the number of postfix tokens. `buildTree` visits each token once. Every node is pushed once, and every non-root node is eventually popped once. Stack operations and token tests are constant time, so construction takes $O(t)$ time.

The tree contains one node per token and the stack can hold $O(t)$ partial roots in the worst case, so construction and returned-tree storage are $O(t)$.

Evaluating the finished tree visits each node exactly once and performs constant work at that node, so evaluation is another $O(t)$ operation. Its recursive call stack is $O(h)$, where $h$ is the tree height. A highly skewed valid expression can have $h=O(t)$; a balanced tree has $h=O(\log t)$. Combining stored nodes and worst-case recursion gives $O(t)$ space, matching the manifest.

No subtree value exceeds the stated numeric bound, and the algorithm does not allocate strings or arrays during evaluation proportional to subtree size.

## Alternatives and edge cases

- **Separate number and operator subclasses:** A `NumberNode` can return its value, while one subclass per operator implements combination behavior. This is more modular for the follow-up because adding an operator need not edit one long conditional method.
- **Operator-function dictionary:** Map each operator token to a callable and let an operator node invoke that callable. Adding operators then changes the mapping rather than evaluation control flow.
- **Evaluate postfix directly:** A value stack can compute the final integer without constructing nodes. That is simpler when only the result is wanted, but it fails the requirement to return an expression tree through the `Node` interface.
- **Recursive parsing from the end:** Walking postfix tokens backward can build the right subtree and then the left subtree recursively. It is valid but needs shared index state and can reach linear recursion depth during construction.
- **Single numeric token:** It becomes one leaf, the stack contains exactly that node, and evaluation returns its integer value.
- **Subtraction and division:** Child order must be preserved. The first popped subtree is the right operand, not the left.
- **Valid postfix guarantee:** The code does not defend against stack underflow or leftover roots because malformed expressions are outside the contract.
- **Division by zero:** The source has no explicit check; the input guarantee makes every division valid.
- **Negative intermediate division:** The exact source uses Python `//`, whose negative non-integral behavior is floor division. A truncation-toward-zero contract would require a different implementation.
- **No explicit final operator fallback:** Valid tokens are limited to the four handled operators, so reaching the end of `evaluate` without returning is impossible for conforming input.
- **Tree height:** A chain-like expression can make recursive evaluation depth linear even though total work remains linear.
- **Additional operators:** The current conditional method must be edited to add one. Subclass or function-table designs satisfy the modularity follow-up more cleanly.
