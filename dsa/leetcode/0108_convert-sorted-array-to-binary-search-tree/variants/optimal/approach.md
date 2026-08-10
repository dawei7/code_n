## General

The input already gives one of the most useful views of a binary search tree: its inorder traversal. Inorder traversal visits the left subtree, then the root, then the right subtree. Because every value in a binary search tree's left subtree is smaller than the root and every value in its right subtree is larger, a tree containing distinct values produces those values in ascending order.

That observation solves the ordering requirement, but not yet the balance requirement. Choosing an endpoint as the root would leave almost every value on one side and could create a chain. Choosing a middle element instead divides the remaining values into two groups whose sizes differ by at most one. Repeating that choice inside every group keeps the resulting tree height-balanced.

**What one recursive call promises**

The nested `dfs(l, r)` function uses an inclusive index interval. Its promise is:

- construct a height-balanced binary search tree containing exactly `nums[l]` through `nums[r]`; and
- return `None` when the interval is empty.

The empty interval is represented by `l > r`. This condition arises naturally after choosing a leaf: its left call receives an interval ending before it begins, and its right call does too. Returning `None` connects the absence of a child directly to that exhausted interval.

For a nonempty interval, `mid = (l + r) >> 1` computes the floor of $(l+r)/2$. For nonnegative indices, shifting right by one bit has the same result as integer division by two. Thus an odd-length interval has its unique middle selected, while an even-length interval selects the left of its two middle positions.

The solution constructs `TreeNode(nums[mid], dfs(l, mid - 1), dfs(mid + 1, r))`. The left call receives every index strictly below `mid`; the right call receives every index strictly above it. The middle index itself belongs only to the new root.

**Why the search-tree ordering is guaranteed**

The array is strictly increasing. Consequently, if $i < \texttt{mid}$, then `nums[i] < nums[mid]`, and if $i > \texttt{mid}$, then `nums[i] > nums[mid]`.

The recursive partition puts exactly the first group into the left subtree and exactly the second group into the right subtree. If recursive calls obey the same rule internally, all nodes satisfy the binary-search-tree condition. No comparisons, insertions, or later repairs are needed: the sorted positions establish the ordering before any node is created.

Every index is also used exactly once. A call removes its middle index and splits the rest into two disjoint intervals. Those intervals neither overlap nor omit an index. Repeating the partition eventually reaches one-element intervals and then empty intervals, so the returned tree contains all and only the input values.

**Why choosing the middle produces balance**

Suppose a call owns $m$ elements. After removing the selected middle, the left and right recursive intervals contain $\lfloor(m-1)/2\rfloor$ and $\lceil(m-1)/2\rceil$ elements, possibly in the opposite verbal order depending on the midpoint convention. Their sizes differ by at most one.

Each child repeats the same near-halving construction. Therefore both child trees have the minimum or near-minimum height possible for their number of nodes, and their heights differ by at most one. The same statement holds at every recursively created node, which is exactly the definition of a height-balanced binary tree.

For even interval lengths, choosing the lower middle makes the right side one element larger. Choosing the upper middle would make the left side one element larger and would be equally valid. The problem asks for any valid height-balanced tree, so the shape need not match the displayed example exactly.

**Concrete construction**

For `[-10, -3, 0, 5, 9]`, the initial interval is `[0, 4]`, so index two becomes root value zero. The left interval `[0, 1]` chooses index zero, producing `-10` with right child `-3`. The right interval `[3, 4]` chooses index three, producing `5` with right child `9`.

An inorder traversal of that result returns `[-10, -3, 0, 5, 9]`, confirming the search-tree ordering. Its two root subtrees have equal height, and the one-sided children below them differ from empty children by only one level, confirming balance. This is the alternative tree mentioned in the Reference, even though its level-order serialization differs from the first displayed output.

**Source-level assumptions**

The selected source relies on the platform to provide `List`, `Optional`, and `TreeNode`; their imports and definition are commented out or absent in this file. That matches a judge environment that supplies its tree model and typing names. In a standalone Python module, the corresponding imports and `TreeNode` definition must exist before the annotated method is defined.

## Complexity detail

Let $n$ be `len(nums)`. Each nonempty recursive call creates exactly one node for one unique array index. Apart from its two recursive calls, it performs constant work: a midpoint calculation, one array access, and one node construction. Across all calls, this gives $O(n)$ time.

The recursion follows one of the nearly equal halves at each step. Its maximum depth is $O(\log n)$, so the active call stack uses $O(\log n)$ auxiliary space. Calls that have already returned do not remain on the stack.

The returned tree contains $n$ newly allocated nodes and therefore needs $O(n)$ output space. Complexity conventions normally exclude required output storage from auxiliary space, which is why the manifest reports $O(\log n)$ space rather than $O(n)$. If total allocated memory including the returned tree is requested, the answer is $O(n)$.

The algorithm passes index boundaries rather than array slices. A slicing implementation could copy elements at every recursion level, adding $O(n\log n)$ aggregate copying in Python and increasing peak memory. The selected source avoids that cost.

## Alternatives and edge cases

- **Upper-middle recursion:** Use the right middle for even-length intervals. It produces a different but equally valid height-balanced binary search tree with the same complexity.
- **Random middle tie-breaking:** Randomly select either middle when an interval length is even. Correctness and balance remain unchanged, but nondeterminism makes testing and debugging less predictable.
- **Inorder simulation with an iterator:** Recursively create the left shape, consume the next sorted value for the root, and then create the right shape. This can avoid repeated random array access, though the direct index method is simpler here.
- **Repeated BST insertion:** Inserting values in their original ascending order creates a maximally skewed tree and violates the balance requirement. Even reordering insertions adds machinery that direct construction does not need.
- **Array slicing:** Passing `nums[:mid]` and `nums[mid + 1:]` is visually simple but copies subarrays and weakens the space and aggregate-time bounds in Python.
- **One input value:** The initial midpoint is that value, and both child intervals are empty, so the result is a single balanced node.
- **Two input values:** The lower middle becomes the root and the larger value becomes its right child. Their subtree heights differ by one, so the result is balanced.
- **Strictly increasing values:** Distinctness makes every left value strictly smaller and every right value strictly larger. Duplicate-handling rules are unnecessary because the contract excludes duplicates.
- **Negative and positive values:** Only ordering matters; signs and magnitudes do not affect the construction.
- **Maximum input length:** The balanced recursion depth is logarithmic, so an input of $10^4$ elements does not create the linear call depth that a skewed insertion process would.
- **Empty array outside the stated constraints:** Although the Reference requires at least one element, `dfs(0, -1)` would return `None` safely.
- **Exact output shape:** A test must validate the returned tree's contents, BST property, and balance rather than demand one particular level-order serialization when multiple valid trees exist.
