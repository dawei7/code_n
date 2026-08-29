## General

**Use the BST ordering to visit values from largest to smallest**

An ordinary in-order traversal visits left subtree, node, then right subtree. In a binary search tree with unique values, that produces values in ascending order.

Reversing the traversal order to right subtree, node, then left subtree produces descending order. When a node is visited, every strictly greater value has already been processed, while every smaller value remains for later.

This is exactly the order needed for a running suffix sum. The new value of a node is its original value plus every greater original value.

**Meaning of the running sum**

The variable `s` begins at zero. During reverse in-order traversal, immediately before processing a node with original value `v`, `s` equals the sum of all original values strictly greater than `v`.

The code performs:

- `s += root.val`, adding the current original value.
- `root.val = s`, storing the required greater-or-equal sum.

Afterward, `s` equals the sum of all original values greater than or equal to `v`. That is exactly the information needed when traversal later reaches smaller nodes.

**Why the right subtree comes first**

BST ordering guarantees every value in `root.right` is greater than `root.val`. The call `dfs(root.right)` processes and accumulates all of them before the current node is changed.

After the current value is added and replaced, `dfs(root.left)` handles smaller values. For each of those nodes, the running sum already includes the current value and the entire right subtree, all of which are greater.

Swapping the recursive calls would accumulate smaller values and solve a different problem.

**Why mutation does not corrupt the sum**

Previously visited nodes are overwritten with their greater sums. However, `s` already captured each node's original value at the moment it was processed. The traversal never reads that node's value again for accumulation.

The current node is also added before it is overwritten. Therefore, every original value contributes to `s` exactly once, and no transformed value is accidentally added.

Tree links are not changed. Only `val` fields mutate, so the recursive route determined by `left` and `right` remains intact even though the transformed numeric values may no longer satisfy the original BST comparisons.

**How `nonlocal s` works**

`s` is created in `bstToGst` and shared by every nested `dfs` call. The declaration `nonlocal s` tells Python that `s += root.val` updates that enclosing variable rather than creating a separate local sum for each call.

Python determines scope for the whole helper function when compiling it, so the declaration is effective even though it appears after `dfs(root.right)` in the source text. Conceptually, all recursive frames cooperate on one descending-order accumulator.

A separate sum per recursive branch would be wrong because values in the right subtree must contribute to the current node and then to nodes in the left subtree.

**Trace a small tree**

Consider a BST with root four, right child six, and six's children five and seven.

Reverse in-order first reaches seven. The sum changes from zero to seven, and node seven remains seven.

Traversal returns to six. The running sum already contains the greater value seven. Adding original six gives thirteen, so six becomes thirteen.

The next visited node is five. The running sum contains original seven plus original six. Adding five gives eighteen, so five becomes eighteen.

Finally, root four is processed after its entire right subtree. The sum of original values five, six, and seven is already eighteen. Adding four makes twenty-two, which is the correct new value for four within this smaller example.

The same pattern continues into the root's left subtree, where every already visited value is greater.

**Trace the two-node example**

For root zero with right child one, DFS reaches one first. `s` becomes one and that node's value is set to one.

Returning to zero, the running sum is one. Adding zero leaves one, so the root becomes one. The result is `[1, null, 1]`.

Even a zero-valued node is processed normally; adding zero simply does not change the accumulated total.

**Why unique values simplify the statement**

The source guarantees all BST values are unique, so “greater than” corresponds exactly to nodes visited earlier in descending order. After adding the current node, `s` represents values greater than or equal to it.

If duplicates were allowed under a particular BST convention, the target definition and traversal ordering among equal values would need careful handling. No such ambiguity exists here.


Before the current node is processed, all nodes with greater values have been visited and no smaller node has been visited. The running sum equals the sum of their original values.

Adding the current original value makes `s` equal to the sum of all original values greater than or equal to the current key. Assigning it therefore writes exactly the required transformed value.

Reverse in-order visits every node once in descending key order, preserving the invariant from one node to the next. Structural induction over the recursive traversal proves that every node receives the correct greater sum.

**Return the same root**

The helper returns nothing because it modifies nodes in place. After `dfs(root)` completes, `root` still points to the same tree object, now containing transformed values. Returning it satisfies the interface without rebuilding any nodes.

The type annotation allows an optional root. If `root` is `None`, the helper returns immediately and the method returns `None`. The source cases contain at least one node, but the implementation is safely general.

## Complexity detail

Let `N` be the number of nodes and `H` the tree height. Every node is visited exactly once and performs constant-time addition and assignment. Calls on missing children add only a linear number of constant operations. Total time is `O(N)`, matching the manifest.

The recursion stack contains at most one frame per node along the active path, so auxiliary space is `O(H)`. A balanced tree has `H = O(\log N)`; a skewed tree has `H = O(N)`. The algorithm allocates no list of values and reuses the input tree as output.

## Alternatives and edge cases

- **Iterative reverse in-order traversal:** Use an explicit stack, repeatedly descend right, process a node, then move left. It has the same `O(N)` time and `O(H)` space while avoiding recursion limits.
- **Collect sorted values first:** Ordinary in-order can create an array, then suffix sums can transform nodes in a second traversal. It is easier to visualize but uses `O(N)` extra storage and two passes.
- **Morris reverse traversal:** Temporary threads can visit nodes in descending order with `O(1)` auxiliary space. It is much more delicate because tree links must be restored correctly.
- **Repeatedly sum greater nodes:** Searching the BST separately for each node can take `O(N^2)` time on an unfavorable tree. The running sum shares work across nodes.
- **Single node:** The right subtree is empty, its value is added to zero, and it remains its own greater sum.
- **Root value zero:** Zero contributes nothing numerically but is still assigned the accumulated sum of greater values.
- **All values unique:** No equal-key ordering issue exists, matching the source guarantee.
- **Right-skewed tree:** Recursion first reaches the maximum at the bottom, then accumulates while unwinding. Stack depth is `O(N)`.
- **Left-skewed tree:** Each node is processed before descending left, and the running sum grows in descending key order. Depth is again `O(N)`.
- **Balanced tree:** Recursion depth is logarithmic even though all `N` nodes are visited.
- **Input mutation:** Node values are overwritten. Callers needing original values must copy the tree or record them before conversion.
- **Structure preservation:** No child pointer changes, so the original shape remains exactly the same.
- **Transformed values and BST order:** The task asks for a Greater Sum Tree, not for subsequent searches under original key comparisons. The numeric transformation may change ordinary BST ordering relationships.
- **Recursive sum sharing:** A nonlocal accumulator is necessary; returning independent subtree sums without carefully passing right-side totals would not update left branches correctly.
