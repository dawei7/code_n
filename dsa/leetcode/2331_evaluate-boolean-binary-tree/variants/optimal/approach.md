## General

**A parent can be evaluated only after its children**

Every leaf already stores a Boolean value. Every internal node stores an operation whose operands are the evaluations of its left and right subtrees. This recursive definition maps directly to postorder evaluation: recursively obtain both child results, apply the current operator, and return the result to the parent.

The tree is full, so every node has either zero children or two. The exact solution uses `root.left is None` to recognize a leaf. Under the full-tree guarantee, a missing left child also means the right child is missing.

**Convert a leaf's encoded integer to Boolean**

Leaf values are zero or one. `bool(root.val)` converts zero to `False` and one to `True`, exactly matching the encoding.

This base case stops recursion. It does not inspect an operator or recurse into missing child pointers.

**Select the operation encoded by an internal node**

For a non-leaf:

- value `2` represents OR, so `op` becomes `or_`;
- otherwise `op` becomes `and_`.

The valid internal values are only two and three, so the `else` case means AND. Correctness relies on that contract; an unexpected internal value would also be treated as AND by the exact code.

The return expression recursively evaluates the left and right children and calls `op` with the two Boolean results.

For OR, the result is true when at least one child result is true. For AND, it is true only when both are true. This is precisely the node-evaluation rule.

**The function calls evaluate both subtrees**

Although the logical operations OR and AND are often short-circuiting language operators, `or_` and `and_` here are ordinary functions. Python evaluates both function arguments before calling `op`. Consequently, both recursive subtree calls occur even when the left result alone would determine the Boolean answer.

That behavior does not hurt correctness. Every subtree is valid and has a well-defined result. It also makes the time analysis straightforward: every node is visited exactly once in the evaluation tree.

The helper functions conventionally come from Python's `operator` module. Applied to Boolean operands, they compute bitwise OR or AND, whose results agree exactly with logical OR and AND for `False` and `True`.

**Why the recursion returns the correct value**

Use structural induction. For a leaf, `bool(root.val)` is its definition, so the base result is correct.

Assume recursive evaluation is correct for both children of an internal node. If the node value is two, the method applies OR to exactly those correct results. If it is three, it applies AND. In either case, the returned value is the evaluation defined for the current subtree.

By induction, this holds at every node, including the root. Therefore the final return is the Boolean evaluation of the whole tree.

**A small trace**

Suppose the root is OR, its left child is leaf one, and its right child is an AND node with leaves zero and one. The left recursive call returns true. The AND subtree evaluates both leaves, obtains false and true, and returns false. The root applies OR to true and false and returns true.

This mirrors the conceptual bottom-up evaluation even though the code is written top-down as recursive calls.

**The input tree is not rewritten**

Some iterative approaches store evaluated values back into nodes. This source leaves every `val` and child pointer unchanged. Results exist only as return values on the recursion stack.

## Complexity detail

Let `n` be the number of nodes and `h` the tree height. Every node causes one function call. Leaves do constant conversion work, and internal nodes do constant operator selection and application after two child calls. Total time is `O(n)`.

At any moment, recursion stores frames along active root-to-node paths. Peak stack space is `O(h)`. A balanced full tree has `h = O(\log n)`, while a highly unbalanced full tree can have linear height in the number of internal levels, so worst-case space is `O(n)`.

No map, explicit stack, or per-node result array is allocated. The exact source evaluates both children eagerly, so there is no best-case subtree skipping in the operation count.

With up to 1000 nodes, a maximally deep valid full tree can approach Python recursion limits depending on the environment. An iterative postorder traversal would eliminate that runtime concern.

## Alternatives and edge cases

- **Iterative postorder traversal:** Use a stack with visited markers and store each node's evaluated result. This avoids recursion limits but uses `O(n)` explicit storage.
- **Use Python's short-circuit `or` and `and`:** This could skip a right subtree when the left result determines the answer. It remains semantically correct because skipped subtrees have no side effects, but it differs from the exact eager `or_` and `and_` calls.
- **Breadth-first traversal:** Level order visits parents before their child results are ready. It would need extra storage and a reverse-processing phase, making postorder more natural.
- **Mutate internal node values:** Replacing operator codes with evaluated results can support iterative reduction but changes the input tree. The recursive return-value method preserves it.
- **Single-node tree:** The root is a leaf and `bool(0)` or `bool(1)` is returned immediately.
- **OR with two false children:** Both recursive results are false, so `or_` returns false.
- **OR with either true child:** The result is true, although the exact function still evaluates both children.
- **AND with two true children:** Both must be true for `and_` to return true.
- **AND with either false child:** The result is false, again after eager evaluation of both.
- **Full-tree guarantee:** Checking only `left is None` is safe because a valid node cannot have only a right child.
- **Invalid unary node:** The source contract excludes it. If left were present and right missing, recursion on `None` would fail.
- **Invalid internal value:** Any non-two value is treated as AND. Correctness depends on the guarantee that the only alternative is three.
- **Leaf value encoding:** `bool` would treat any nonzero integer as true, but valid leaves are exactly zero or one.
- **Deep tree:** Mathematical space is `O(h)`, but Python's recursion limit can be a practical boundary.
- **Helper availability:** The exact code relies on `or_` and `and_` being available, conventionally from the `operator` module.
