## General

Preorder visits a subtree as root, then left subtree, then right subtree. Postorder visits it as left subtree, then right subtree, then root. The recursive solution uses these fixed boundary facts to determine the root and the size of the first child subtree.

The helper `dfs(a, b, c, d)` reconstructs one subtree from:

- preorder indices `a` through `b`;
- postorder indices `c` through `d`.

These two slices describe the same set of nodes in different traversal orders.

**Empty and one-node ranges.** If `a > b`, the preorder range is empty and the helper returns `None`. Otherwise `preorder[a]` is the subtree root because preorder always starts with the root. If `a == b`, the range contains only that root, so it is returned as a leaf.

**Identify the first child subtree.** For a nonleaf subtree, `preorder[a + 1]` is the root of the first subtree visited after the root. The construction treats this as the left child subtree. The values are distinct, so its position in postorder is unique.

The dictionary `pos` maps every postorder value to its index. If

```text
i = pos[preorder[a + 1]]
```

then postorder segment `c..i` contains exactly the nodes of that first child subtree, because postorder finishes a subtree at its root. Its size is

$$
m=i-c+1.
$$

The next $m$ preorder values, indices `a + 1` through `a + m`, must describe the same subtree. Those paired ranges form the recursive left call.

Everything remaining before the root belongs to the right subtree:

- preorder `a + m + 1 .. b`;
- postorder `i + 1 .. d - 1`.

The `d - 1` excludes the current root, which is the final postorder value for this subtree.

**Why ambiguity is acceptable.** Preorder and postorder alone do not always uniquely determine a binary tree. If a node has exactly one child, the traversals cannot reveal whether that child was left or right: both placements produce the same orders. The problem allows any valid reconstruction. This algorithm consistently treats the first child as the left subtree and may leave the right subtree empty.

**Why the recursive ranges remain consistent.** The first child root's postorder position determines exactly $m$ nodes. Preorder lists those same subtree nodes contiguously immediately after the current root. Removing the current root and those $m$ nodes leaves identical node sets for the right ranges. Distinct values prevent a boundary from matching the wrong occurrence.
A zero-node range returns an empty tree and a one-node range returns the only possible root. For a larger range, preorder identifies the correct root. The next preorder value identifies the root of the first child subtree, and its unique postorder position gives that subtree's exact size. By the induction assumption, the recursive calls construct trees matching their respective traversal segments. Attaching them left then right makes the overall preorder root-left-right and postorder left-right-root exactly equal to the supplied ranges. Therefore the top-level tree has both requested traversals.

For preorder `[1,2,4,5,3,6,7]` and postorder `[4,5,2,6,7,3,1]`, root 1 is immediate. The next preorder value 2 appears at postorder index 2, so the first subtree has three nodes: `[2,4,5]`. The other three nonroot nodes form the subtree rooted at 3. Recursion repeats the same split inside each part.

The position map avoids a linear scan in every recursive call. Each node becomes a root once, so reconstruction is linear.

## Complexity detail

Let $n$ be the number of nodes. Building `pos` takes $O(n)$ time and space. Each recursive call creates one node and performs constant-time boundary arithmetic and one dictionary lookup.

- **Time complexity:** $O(n)$.
- **Space complexity:** $O(n)$ for the postorder index map, constructed tree, and up to $O(n)$ recursion depth in a skewed reconstruction.

If output-tree storage is excluded, the auxiliary map and recursion stack still require $O(n)$ in the worst case.

## Alternatives and edge cases

- **Search postorder linearly in each call:** This preserves the logic but can cost $O(n^2)$ on skewed splits. The index map makes lookup constant-time.
- **Iterative stack construction:** One can advance through preorder and close nodes according to postorder. It also reaches $O(n)$ time but has a subtler invariant.
- **Require a unique tree:** That is impossible from these traversals when unary nodes exist. The contract deliberately accepts any valid answer.
- **Single node:** Both traversals contain that value; the leaf base returns it directly.
- **Only one child:** The algorithm attaches it on the left. A right-only version could have the same traversals, but either is valid.
- **Full binary tree:** When every internal node has two children, the traversals determine the structure uniquely.
- **Distinct values:** The `pos` dictionary relies on uniqueness. Duplicate values would make child-root positions ambiguous beyond the allowed structural ambiguity.
- **Empty right range:** The right recursive call receives `a > b` and returns `None`.
- **Exclude postorder root:** Using `d - 1` is necessary because `postorder[d]` is the current root, not part of either child.
- **Range length consistency:** Each left preorder range contains exactly the $m$ nodes counted in left postorder.
- **Input guarantee:** Both arrays are valid traversals of the same tree, so boundary calculations do not encounter missing values or inconsistent sizes.
- **Return node objects:** The algorithm constructs and links `TreeNode` instances; it does not return traversal arrays.
