## General

**Use the ordering property of an inorder traversal**

An inorder traversal visits a node's left subtree, then the node, then its right subtree. In a binary search tree, this produces node values in non-decreasing order over the entire tree.

The requested level contains only some of those nodes. If we take a sorted sequence and delete every item not at the desired depth, the remaining subsequence is still sorted. Therefore, an inorder traversal can collect only nodes whose depth equals `level`, and those collected values need no additional sorting.

This is the key source idea. It does not traverse the requested level in arbitrary order and sort afterward. It obtains sorted order for free from the BST property.

**Pass the current depth through recursive DFS**

The helper `dfs(root, i)` receives a node and its zero-based depth `i`.

If the node is `None`, it returns immediately.

Otherwise it recursively processes:

1. `root.left` at depth `i + 1`;
2. the current node;
3. `root.right` at depth `i + 1`.

At the current-node step, it appends `root.val` only when `i == level`.

The initial call `dfs(root, 0)` correctly labels the root as level 0. Every child increments depth by one, which matches edge distance from the root.

Although only one level is collected, the exact source continues traversing below that level. A descendant cannot later return to a smaller depth, so this deeper work is unnecessary, but it does not change the collected values.

**Why the collected level values are sorted**

Suppose two values `u` and `v` are appended in that order. The inorder traversal visited `u` before `v`. Because the input is a BST, every inorder value is no greater than every value that follows it. Hence `u <= v`.

Filtering by the depth condition changes only which visits append; it never changes visit order. The final `nums` list is therefore the requested level's values in non-decreasing order.

This remains true if the BST convention permits duplicate values. Inorder then yields non-decreasing rather than strictly increasing order, which is exactly sufficient for median selection.

For a root 6 with children 3 and 8, inorder visits 3, 6, 8. Filtering to level 1 keeps `[3,8]`, already sorted.

**Select the upper median by index**

Let $K=\lvert\texttt{nums}\rvert$. The contract defines the median as the element at zero-based sorted index

$$
\left\lfloor\frac K2\right\rfloor.
$$

For odd $K=2q+1$, this is index $q$, the unique middle.

For even $K=2q$, the two middle indices are $q-1$ and $q$. Index $q$ is the larger, or upper, median.

The source returns `nums[len(nums) // 2]`, which implements both cases with integer division.

If `nums` is empty, no node exists at the requested level. The conditional expression returns -1 instead of trying to index an empty list.

**Why every requested node appears exactly once**

Recursive traversal reaches every tree node through its unique parent path. The depth parameter starts at zero and increases once per edge, so a node is appended exactly when its actual level equals the requested one.

No node is revisited because a tree has no cycles, and no node at another depth is appended. Thus `nums` contains precisely the level's multiset of values. Its inorder order supplies the sorted sequence, and the selected index supplies the defined median.

**The exact source differs from the manifest summary**

The manifest says the implementation uses “left-to-right level order during breadth-first traversal” and claims $O(W)$ space, where $W$ is maximum width. The exact source uses recursive inorder depth-first traversal and stores all $K$ values at the target level.

It has no queue and is not breadth-first. This changes the faithful auxiliary-space description to recursion depth plus collected values.

There is also a constraint-level robustness defect. A valid BST can be a chain of up to 200,000 nodes. Python's usual recursion limit is around one thousand calls. The recursive `dfs` can raise `RecursionError` on such a valid skewed tree, even when the requested level is shallow, because the exact source continues traversing the entire tree.

An iterative traversal or actual BFS is needed to cover the full constraint safely.

## Complexity detail

The exact source visits all $N$ nodes, including descendants below the requested level, so time is $O(N)$. Appending $K$ target-level values and selecting one index do not exceed that bound.

Let $H$ be tree height. Recursive call frames require $O(H)$ space, and `nums` stores $O(K)$ values. Exact auxiliary space is $O(H+K)$, which can be $O(N)$.

This does not match the manifest's $O(W)$ claim. A BFS that stores one level at a time could use $O(W)$ queue space, but the recursive source uses call-stack depth instead. On a skewed tree, $W=1$ while $H=N$, demonstrating why the two bounds are not interchangeable.

## Alternatives and edge cases

- **Breadth-first search to the requested level:** Process levels with a queue, stop upon reaching `level`, and use the BST's left-to-right level ordering. This matches the manifest description, avoids deep recursion, and uses $O(W)$ space.
- **Iterative inorder traversal:** An explicit stack preserves globally sorted order without interpreter recursion limits. It uses $O(H)$ stack space plus $O(K)$ collected values.
- **Prune below the target level:** Once DFS reaches `i == level`, append the value and return without visiting children. This can save substantial work when the target is shallow, though worst-case time remains $O(N)$.
- **Collect then sort in an arbitrary tree:** Without the BST property, level values would need sorting or selection. Here inorder order eliminates that $O(K\log K)$ step.
- **Level zero:** Only the root is collected, so its value is the median.
- **Nonexistent level:** No value is appended and the function returns -1.
- **Even number of nodes:** Index `K // 2` selects the larger of the two middle sorted values.
- **Duplicate values:** Non-decreasing inorder order still supports the same median index.
- **Skewed BST:** Functional recursion logic is correct, but the exact Python source can exceed the recursion limit well below the allowed 200,000 nodes.
- **Nonempty-root guarantee:** The contract supplies a tree, but the helper also safely handles a `None` node and would return -1 for a missing root.
- **Traversal below the target:** It is unnecessary but present in the exact source, so the faithful time analysis counts all nodes rather than only nodes through the requested depth.
