## General

Inorder traversal has a precise recursive definition: completely traverse a node's left subtree, then visit the node itself, then completely traverse its right subtree. The selected solution translates that definition directly into a helper function. Its brevity is not a shortcut around the reasoning; the binary tree's recursive structure and the requested order match exactly.

**What one call promises**

For any node passed as `dfs(root)`, the helper appends to `ans` every value in that node's subtree, exactly once and in left-subtree, node, right-subtree order. It does not return a separate list. Instead, all calls share `ans` from the enclosing function.

If `root is None`, the subtree is empty and contributes no values. Returning immediately is both the recursion base case and the correct traversal of an absent child.

For a real node, the operations occur in the required order:

1. `dfs(root.left)` finishes the entire left subtree.
2. `ans.append(root.val)` visits the current node.
3. `dfs(root.right)` finishes the entire right subtree.

Changing those lines changes the traversal. Appending before both calls would be preorder; appending after both would be postorder. Inorder is determined by the position of the append between the recursive calls.

**A small trace**

For the tree encoded as `[1,null,2,3]`, node `1` has no left child and has node `2` on the right; node `2` has node `3` on the left.

- The call for node `1` first calls its empty left child, which contributes nothing.
- It appends `1`.
- It enters node `2`, but cannot append `2` yet because its left subtree must come first.
- The call for node `3` appends `3` after its empty left side.
- Control returns to node `2`, which appends `2`.

The result is `[1, 3, 2]`, matching the Reference.

**Why every node is visited exactly once**

Consider any nonempty subtree rooted at node $v$. Assume recursively that the call on its left child emits exactly that left subtree in inorder, and the call on its right child does the same for the right subtree. The current call appends $v$ exactly once between those two completed sequences. A binary tree's left subtree, root, and right subtree are disjoint and together contain the entire subtree rooted at $v$. Thus the call emits every node in that subtree once and in the required order.

The empty-subtree base case begins this structural induction. Applying the argument to the original root proves correctness for the entire tree. If the original root is `None`, no value is appended and the correct answer is the empty list.

**How recursive control replaces an explicit stack**

When the helper descends left, Python retains the suspended call for each ancestor, including the fact that it still needs to append that ancestor and then explore its right child. When an empty left pointer is reached, returns unwind to the nearest suspended node. This call stack is the mechanism that remembers where traversal should resume.

For a binary search tree, inorder values happen to be nondecreasing, but this problem accepts any binary tree. The algorithm does not compare values and does not rely on the search-tree ordering property. “Inorder” describes structural visitation order, not numerical sorting.

**Why sharing one answer list is safe**

Each call only appends; no call removes or reorders earlier entries. A left-subtree call completes before the current value is added, and the right-subtree call begins only afterward. Therefore mutations to the shared list occur in the same total sequence as recursive visitation. Building and concatenating a new list at every node would be correct but could copy accumulated values repeatedly and use more temporary memory.

The `TreeNode` structure is platform-provided, as shown by the commented definition. The user's method only reads `left`, `right`, and `val`; it does not modify the tree.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height, measured as the maximum number of real nodes on a root-to-leaf path. Each real node causes one append and two child-call attempts. Empty-child calls return immediately. The total number of calls and constant-time operations is proportional to the tree size, so time is $O(n)$.

At any instant, the recursion stack contains at most one root-to-current path, so it uses $O(h)$ auxiliary space. For a balanced tree, $h=O(\log n)$; for a completely skewed tree, $h=O(n)$. This is why the manifest uses $O(h)$ rather than claiming that recursion is always logarithmic.

The returned `ans` list occupies $O(n)$ space because it must contain every value. As usual, the manifest's auxiliary-space bound excludes mandatory output. Including the output, total memory is $O(n+h)=O(n)$.

## Alternatives and edge cases

- **Explicit stack:** Repeatedly push the current node and move left; when no left child remains, pop, visit, and move right. This satisfies the iterative follow-up with $O(h)$ auxiliary space and simulates the same suspended-call state.
- **Visited-flag stack:** Push tuples indicating whether a node should be expanded or visited. It generalizes cleanly to preorder and postorder but stores more stack entries and flags.
- **Morris traversal:** Temporarily thread each inorder predecessor back to its ancestor, enabling $O(1)$ auxiliary space. It restores the tree but is more subtle and temporarily mutates links.
- **Do not concatenate recursive result lists mechanically:** Expressions that create `left_result + [value] + right_result` may copy lists repeatedly, reaching quadratic time on skewed trees in languages or implementations where concatenation copies.
- **Empty tree:** The initial helper call receives `None`, returns immediately, and the method returns `[]`.
- **Single node:** Both child calls are empty, so the sole value is appended once.
- **Left-skewed tree:** Recursion reaches the deepest node before appending anything, then emits values while unwinding. Stack depth reaches $n$.
- **Right-skewed tree:** Each node is appended before descending to its right child, but suspended calls still create depth $n$.
- **Duplicate values:** Nodes are distinct even when values match. Each node contributes one entry, so duplicate numbers may correctly appear in the result.
- **Recursion limit:** The challenge has at most 100 nodes, which is safe for ordinary Python recursion limits. For much deeper external trees, prefer an explicit stack or Morris traversal.
