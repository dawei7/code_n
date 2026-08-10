## General

The competitive solution recursively carries the decimal number formed by ancestors. It returns a completed value at a leaf and adds the results from left and right subtrees at every internal node.

`sumNumbersRecu(root, num)` treats `num` as the number formed before including `root`.

**Base case for an absent node**

If `root is None`, the helper returns zero. An absent child contains no leaf and therefore contributes nothing to the total.

This zero is an additive identity. It does not mean an empty child forms the number zero, because it is never appended as a separate output path; it merely leaves the real sibling's total unchanged.

**Completing a number at a leaf**

When both child pointers are null, the current node is a leaf. The complete path number is:

`num * 10 + root.val`.

The helper returns that number immediately. No null-child recursive calls are needed for a leaf.

Equality with a target is not involved; every leaf number contributes to the requested sum.

**Extending through an internal node**

For a non-leaf, the same expression `num * 10 + root.val` is passed to both child calls.

This updated value includes the current digit. Each child then appends its own digit, so the decimal position grows correctly one level at a time.

The expression is written twice in the return statement, once for each branch. That duplicates a constant amount of arithmetic but does not change the asymptotic bound.

**Why branch state is independent**

Integers are immutable. The left call receives one integer value, and the right call receives an equal integer value; neither can modify the other's state.

Consequently, there is no shared mutable path and no need to remove a digit after one branch finishes. Recursive return naturally restores the parent's local `num`.

**Why adding branches is correct**

Every complete path below an internal node next enters either the left child or the right child. No leaf belongs to both subtrees.

The left recursive result is the sum of all completed numbers in the left subtree with the current prefix. The right result is the analogous sum for the right subtree. Adding them covers the union exactly once.

At a one-child node, the missing call returns zero, so only the real branch contributes.

**Decimal-prefix invariant**

Suppose `num` represents ancestor digits $d_1d_2\ldots d_k$. Multiplication by ten shifts those digits left, and adding `root.val` places the current digit at the end.

Thus every recursive edge preserves the invariant that the parameter represents exactly the nodes above the callee. At a leaf, applying the formula one final time produces the full root-to-leaf number.

Starting with zero at the public call establishes the invariant before the root.

**Why no path is missing or duplicated**

A tree gives each leaf exactly one root path. Recursive branching reaches every real child and therefore every leaf.

Each leaf returns once. Internal additions combine nonoverlapping leaf sets, while null returns contribute nothing. The public result is therefore the sum over all and only root-to-leaf numbers.

**Example walkthrough**

For `[1,2,3]`, the root passes prefix one to both children. Leaf two returns twelve and leaf three returns thirteen, producing twenty-five.

For the route `4 -> 9 -> 5`, successive prefix values are zero before the root, four before node nine, forty-nine before leaf five, and 495 as the completed return.

The other leaves similarly return 491 and 40; recursive sums produce 1,026.

**Source and input behavior**

The active file defines its own `TreeNode`. The public method would also return zero for an empty root, although the contract guarantees a nonempty tree.

Node values are assumed to be single decimal digits. The source does not validate that precondition and does not mutate any node.

## Complexity detail

Every one of the $n$ nodes is entered once, with constant local arithmetic and checks. Total time is $O(n)$.

The call stack depth is the tree height $h$, so auxiliary space is $O(h)$. The stated depth limit of ten makes the practical stack bound small.

No explicit path collection is retained. The integer result is constant-size under the problem's bounded-answer model.

Both child calls are evaluated for an internal node because every leaf number must be included; there is no short-circuit opportunity analogous to an existence query.

## Alternatives and edge cases

- **Nested closure with accumulated prefix:** Same recurrence without a separate instance helper method.
- **Iterative stack:** Pair each pending node with its prefix, add at leaves, and avoid recursive calls.
- **Morris traversal:** Achieves constant auxiliary space by temporary threading, but must undo decimal digits when returning through threads.
- **Return a list of numbers:** Unnecessary because the contract requests only their sum.
- **Empty root outside constraints:** Returns zero.
- **One digit:** Returns that digit directly.
- **Zero leaf:** Appending it shifts the prefix by one decimal place.
- **Leading zero:** Does not create a separate decimal place in integer display but arithmetic remains correct.
- **Only left or right child:** Null contributes zero; the existing route continues.
- **Internal node:** Its prefix is never added directly because it is not a complete path.
- **All leaves:** Every one contributes, so branch results must be added.
- **Depth ten:** Recursion is safe and numbers remain short.
- **Digit-domain assumption:** Values outside zero through nine would no longer represent single appended decimal digits.
- **No mutation:** The input tree can be reused after the call.
- **Locally defined node type:** Compatible objects need only `val`, `left`, and `right`.
