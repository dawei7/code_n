## General

The competitive source constructs a binary search tree directly from the sorted positions, but it does more than choose the ordinary midpoint. Its primary `Solution` class computes a pivot that gives the tree the shape of a complete binary tree: every level except possibly the last is full, and nodes on the last level are packed from left to right.

A complete shape is automatically height-balanced. Assigning sorted values according to their inorder positions then makes that shape a binary search tree.

The file also contains a separate `Solution2` iterator construction. The public class selected by the usual `Solution` contract is the first one, so the complete-tree pivot is the main algorithm explained here; the iterator version is a useful alternative, not a step performed by `Solution`.

**The half-open interval contract**

`sortedArrayToBSTRecu(nums, start, end)` owns the half-open interval `[start, end)`. It contains `end - start` values. The public call supplies `[0, len(nums))`, covering the complete array.

If `start == end`, the interval contains no values and the method returns `None`. Otherwise it asks `perfect_tree_pivot(end - start)` how many positions should lie to the root's left. If that returned offset is $k$, then `mid = start + k`.

The root receives `nums[mid]`. Its left child is built from `[start, mid)`, containing exactly $k$ values, and its right child from `[mid + 1, end)`, containing the remaining values. These intervals are disjoint and exclude only the chosen root.

Because the input is strictly increasing, every value in the left interval is smaller than `nums[mid]`, and every value in the right interval is larger. Applying the same partition recursively proves the binary-search-tree ordering at every node. It also proves that every input index appears exactly once.

**Deriving the complete-tree pivot**

Let $n=\texttt{end}-\texttt{start}$ for one nonempty call. The expression `1 << (n.bit_length() - 1)` computes the largest power of two not exceeding $n$; call it $x$. Thus $x=2^h$ for some $h$, with

$$
x \le n < 2x.
$$

A perfect tree with $h$ fully populated levels above a possible last level contains $x-1$ nodes. The remaining $n-(x-1)$ nodes belong on the lowest level. In a complete tree, those lowest-level nodes fill the left subtree before they spill into the right subtree.

Each child subtree has a perfect upper portion containing $x/2-1$ nodes. If enough lowest-level nodes exist to fill the left child's final level, the entire left subtree contains $x-1$ nodes. The condition

$$
x/2-1 \le n-x
$$

detects that case in the source, and `perfect_tree_pivot` returns `x - 1`.

Otherwise, all lowest-level nodes still fit inside the left subtree. Its node count is the perfect upper portion plus those remaining nodes. Algebraically that count becomes $n-x/2$, which is the second return expression. In both branches, the returned number is precisely the number of array values assigned to the left subtree.

For example, take $n=8$. Then $x=8$, and the second branch returns $8-4=4$. The root is placed after four values; the left subtree gets four nodes and the right gets three. For $n=11$, $x=8$ and the first branch returns seven, so the left subtree is perfect with seven nodes while the right gets three. Both choices describe a complete eight-node or eleven-node tree, respectively.

**Why the result is height-balanced**

The pivot formula distributes nodes exactly as a complete tree of size $n$ distributes them. Its left and right subtree heights can therefore differ by at most one. Each recursive call repeats the same complete-shape calculation for its own size, so the property holds at every node, not merely at the root.

Completeness is stronger than this problem requires. A height-balanced tree may have more than one permissible arrangement, but the deterministic formula selects one particular well-packed arrangement. The displayed level order may consequently differ from another accepted midpoint construction while satisfying the same contract.

**Tracing a small size**

For five sorted values, $x=4$. The condition `x // 2 - 1 <= n - x` becomes `1 <= 1`, so the pivot offset is three. The root uses the fourth value, the left interval contains three values, and the right interval contains one.

The three-node left interval chooses its middle value and forms a perfect subtree. The one-node right interval becomes a leaf. The root's subtree heights are two and one when measured in nodes, a difference of one. Inorder traversal still visits the original five values in their ascending order.

**Implementation details that matter**

The bit operation is only evaluated for nonempty intervals, so `n.bit_length() - 1` is never negative. The recursive base condition is `start == end`, not `start > end`, because all generated half-open intervals are valid and never cross.

This source declares its own module-level `TreeNode` and returns instances with the conventional `val`, `left`, and `right` attributes. Those structural attributes are what the surrounding tree serializer needs. The secondary `Solution2` stores an iterator on `self`, so one instance should not interleave two calls; the primary `Solution` has no such mutable per-call state.

## Complexity detail

Every nonempty recursive call selects one unique array element and creates one tree node. The two child intervals partition the remaining indices, so there are exactly $n$ node-creating calls. The pivot calculation uses integer arithmetic and `bit_length`; under the usual fixed-word model for indices bounded by the input size, that is constant work. Total time is $O(n)$.

Because every constructed subtree is complete, following any single recursive branch reduces the problem height by one. The maximum active recursion depth is $O(\log n)$, which gives $O(\log n)$ auxiliary stack space.

The created tree itself contains $n$ nodes and occupies $O(n)$ output space. As usual, the manifest's $O(\log n)$ space bound excludes the returned structure and counts only working memory. Including output, total allocated memory is $O(n)$.

No array slices are created. Each call carries only boundaries, a few integer locals, and one node reference. That preserves the linear-time and logarithmic-auxiliary-space bounds even though the pivot arithmetic is more elaborate than a simple midpoint.

## Alternatives and edge cases

- **Ordinary lower-middle recursion:** Choose `(start + end - 1) // 2` and recursively split around it. This is much simpler and still guarantees height balance, although it does not deliberately produce the complete left-packed shape.
- **Upper-middle recursion:** Choosing the other middle on even lengths is also valid and merely changes which balanced tree is returned.
- **The file's `Solution2` inorder iterator:** First construct a left subtree of the required size, consume the next sorted value as the root, and then construct the right subtree. It runs in $O(n)$ time and $O(\log n)$ stack space but relies on mutable iterator state stored on the object.
- **Random tie-breaking:** Randomly choosing between two middle positions retains balance but gives no correctness or complexity advantage over deterministic selection.
- **Repeated insertion:** Ascending insertion into an ordinary unbalanced BST creates a chain, causing $O(n^2)$ time and violating the height requirement.
- **One value:** Here $x=1$; the first branch returns zero, so the only value is the root and both half-open child intervals are empty.
- **Power-of-two sizes:** The complete-tree pivot gives the left subtree one more lowest-level node than a symmetric midpoint might, ensuring last-level nodes remain packed to the left.
- **Sizes one below a power of two:** The result is a perfect tree, and both child subtrees receive the same number of nodes.
- **Strict input ordering:** It supplies strict BST inequalities automatically; the source does not contain duplicate-placement logic.
- **Negative values:** Pivot calculations use indices and sizes, not stored values, so negative numbers have no special effect.
- **Recursion safety:** The call depth is logarithmic rather than proportional to $n$, which is essential for the upper constraint of $10^4$.
- **Tree shape in tests:** Multiple height-balanced BSTs can be correct. Validation should not reject this complete-tree layout merely because it differs from a reference serialization.
- **Nonempty precondition inside `perfect_tree_pivot`:** Calling the helper directly with zero would make the shift count invalid. The recursive method's base case prevents that state.
