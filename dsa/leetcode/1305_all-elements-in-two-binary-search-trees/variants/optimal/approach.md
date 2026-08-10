## General

The two inputs are binary search trees, not arbitrary binary trees. Their ordering property gives a valuable shortcut: an inorder traversal visits each tree's values in ascending order. The exact Optimal solution turns each tree into its own sorted list and then merges those two lists, just like the merge step of merge sort.

This avoids collecting every value and sorting the combined result from scratch. Each tree supplies order for free through its structure.

**Why inorder traversal is sorted**

For every node in a binary search tree, all values in its left subtree are no greater than or ordered before the node according to the BST rule, and all values in its right subtree come after it. Inorder traversal follows:

$$
\text{left subtree} \rightarrow \text{current node} \rightarrow \text{right subtree}.
$$

The helper `dfs(root, nums)` implements exactly that sequence:

1. if `root is None`, return because the empty subtree contributes nothing;
2. recursively traverse `root.left`;
3. append `root.val`; and
4. recursively traverse `root.right`.

Assume recursively that the left and right subtree traversals are sorted. Every left value appears before the current value, and every right value appears after it, so concatenating those three pieces remains sorted. Applying this reasoning from leaves upward proves that the full traversal is sorted.

The method calls `dfs(root1, a)` and `dfs(root2, b)`. Afterward, `a` contains every value from the first tree in ascending order, and `b` contains every value from the second tree in ascending order. Duplicate values are preserved because each node causes one append.

The helper's annotation says it returns `int`, but it actually returns no value and is used only for its append side effects. That annotation does not affect runtime behavior; conceptually, the helper's result type is `None`.

**Merging the two sorted traversals**

`i` is the next unread index in `a`, and `j` is the next unread index in `b`. Initially both are zero. While neither list is exhausted, the code compares `a[i]` and `b[j]`.

If `a[i] <= b[j]`, `a[i]` is appended and `i` advances. Otherwise, `b[j]` is appended and `j` advances.

Why is the smaller front value safe to output? Each list is sorted, so every unread element after `a[i]` is at least `a[i]`, and every unread element after `b[j]` is at least `b[j]`. The smaller of the two fronts is therefore the smallest value remaining anywhere. Appending it cannot violate ascending order.

The equality branch chooses the value from `a` first. This does not discard the equal value from `b`; `j` stays in place, so that occurrence is appended on a later iteration. The final output correctly retains duplicates from one tree or across both trees.

**Finishing after one list is exhausted**

The main merge loop ends when `i == m` or `j == n`. At that point, at least one traversal has no unread values. All remaining values come from the other list, and that suffix is already sorted.

The two following loops append the unread suffix of `a` and then the unread suffix of `b`. Only one can perform meaningful work, although writing both keeps the code symmetric.

No further comparisons are necessary. Every leftover value is at least the last value already appended; otherwise, it would have been the smaller front during the main merge.

**A complete example**

Suppose the first tree yields `a = [1,2,4]` and the second yields `b = [0,1,3]`.

- Compare $1$ and $0$, append $0$ from `b`.
- Compare $1$ and $1$, append the first tree's $1$ because of `<=`.
- Compare $2$ and the still-unread $1$, append that second $1$.
- Compare $2$ and $3$, append $2$.
- Compare $4$ and $3$, append $3$.
- The second list is exhausted, so append the remaining $4$.

The result is `[0,1,1,2,3,4]`.

**Why the final list is complete and sorted**

Each recursive traversal visits every node in its tree exactly once and appends exactly one value for that node. Thus, `a` and `b` together contain every required occurrence and nothing else.

During merging, each step appends the smallest unread value and advances exactly one pointer. Therefore, the output stays sorted and no list element is used more than once. The suffix loops consume everything that remains. At termination, `i == m` and `j == n`, so every node value from both trees appears exactly once in `ans`.

Completeness and sortedness together establish the required result.

## Complexity detail

Let $m$ and $n$ be the numbers of nodes in the two trees, and let $N=m+n$.

The two traversals visit every node once, taking $O(m+n)=O(N)$ time. The merge advances either `i` or `j` on every append, so it also takes $O(N)$ time. Total time is $O(N)$.

The lists `a` and `b` store $N$ values in total. `ans` stores the required $N$-value output. The recursive call stack reaches the height of the currently traversed tree, at most $O(m)$ or $O(n)$ in a skewed case. Overall storage is $O(N)$, matching the manifest.

If required output is excluded from auxiliary space, `a` and `b` still use $O(N)$ extra memory. The exact source is therefore not a height-only-space merge despite its linear time.

Python recursion depth is a practical concern for a highly skewed tree with thousands of nodes. The asymptotic stack bound is valid, but the interpreter may raise a recursion-depth error before reaching the stated maximum unless traversal is made iterative.

## Alternatives and edge cases

- **Parallel iterative inorder traversals:** Maintain one stack per tree and repeatedly emit the smaller available node. This avoids materializing `a` and `b` and uses $O(h_1+h_2)$ auxiliary stack space beyond the output.
- **Collect and globally sort:** Concatenating all values and applying a sort is simpler but costs $O(N\log N)$ time, ignoring the order already supplied by each BST.
- **Morris traversal:** Threaded traversal can generate inorder values with constant traversal storage, but merging two streams and temporarily modifying trees makes the implementation substantially more delicate.
- **Both roots null:** Both traversals stay empty, merge loops do nothing, and the result is an empty list.
- **One root null:** One traversal is empty, and the corresponding suffix loop copies the other tree's sorted values.
- **Duplicate values:** Each node is an occurrence. The `<=` branch chooses an order between equals but preserves both.
- **Negative values:** Comparisons work normally; no nonnegative assumption is used.
- **Highly unbalanced sizes:** If one tree has many nodes and the other has few, the main loop ends early and a suffix loop copies the remainder in linear time.
- **Skewed tree recursion:** An iterative traversal avoids Python recursion-limit failures while preserving the same inorder order.
- **Helper return annotation:** The exact `dfs` is annotated with `-> int` but returns `None`. Correcting it to `-> None` would improve type accuracy without changing the algorithm.
- **Input trees remain unchanged:** Recursive inorder traversal only reads node links and values; all newly allocated data are lists.
