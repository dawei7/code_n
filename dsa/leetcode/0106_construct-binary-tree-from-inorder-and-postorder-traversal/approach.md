## General

Inorder and postorder supply complementary facts:

- inorder is `left subtree, root, right subtree`, so the root position separates the child value sets;
- postorder is `left subtree, right subtree, root`, so the final value of a subtree's postorder block is its root.

Unique values allow a dictionary `d` to map every value to one inorder index. The selected recursion passes array indices and sizes instead of copying subarrays.

**Meaning of `dfs(i, j, n)`**

The state reconstructs a subtree with exactly $n$ nodes. Its inorder block starts at $i$, and its postorder block starts at $j$. Both implicit blocks describe the same values.

If $n\le0$, the block is empty and returns `None`.

For a nonempty block, the postorder root is the final element:

$$
v=\texttt{postorder}[j+n-1].
$$

The dictionary gives its absolute inorder index $k$.

**Deriving subtree sizes**

Within the current inorder block, values from $i$ through $k-1$ form the left subtree. Its size is:

$$
L=k-i.
$$

After excluding those nodes and the root, the right size is:

$$
R=n-L-1=n-k+i-1.
$$

The guarantees ensure these values are nonnegative and that $k$ lies inside the current block.

**Deriving child block starts**

Postorder places the complete left block first, so the left child uses inorder start $i$, postorder start $j$, and size $L$:

`dfs(i, j, k - i)`.

The right postorder block begins after those $L$ left values, at:

$$
j+L=j+k-i.
$$

Its inorder start is after the root at $k+1$, and its size is $R$. Those facts produce the exact right call.

The root value itself remains at postorder index $j+n-1$, after both child blocks, and is not included in either recursive state.

**Trace through the Reference example**

For inorder `[9,3,15,20,7]` and postorder `[9,15,7,20,3]`, the initial root is the final postorder value three. Its inorder index is one, so the left size is one and the right size is three.

The left call uses postorder start zero and selects nine. The right call starts postorder at one. Its three-value block is `[15,7,20]`, whose final value twenty is the root.

Within that state, twenty's inorder index divides fifteen to the left and seven to the right. The resulting structure is `[3,9,20,null,null,15,7]`.

**Why child construction order is safe**

The source computes `l` before `r`. Some postorder solutions consume one global index backward and must construct right before left, because reversed postorder is `root, right, left`.

This implementation does not share a moving cursor. Each child receives an independently calculated postorder block, so building left first cannot consume the right root or alter the right indices.


The final postorder element forces each nonempty subtree's root. Its unique inorder position forces left and right membership and sizes. Those sizes force the two postorder blocks because postorder stores left before right.

Assuming recursive calls reconstruct their smaller matching blocks correctly, attaching them beneath `v` yields exactly the supplied traversals. Empty blocks form missing children. Induction on $n$ proves correctness.

Every choice is forced, so no distinct tree can satisfy both traversals when values are unique.

The state also maintains a block-consistency invariant: the $n$ values in `inorder[i:i+n]` are exactly the values in `postorder[j:j+n]`. It is true initially by the contract. Splitting at $k$ gives $L$ and $R$ values. Postorder's first $L$ entries must describe the left inorder group, its next $R$ entries the right group, and its last entry the root. Therefore both child calls inherit matching blocks. This invariant explains why the globally looked-up index $k$ is always inside the current inorder range for valid input.

## Complexity detail

Building `d` costs $O(n)$ expected time and space. Each node causes one state, constant arithmetic, one expected dictionary lookup, and one allocation, so construction time is $O(n)$.

The map uses $O(n)$ auxiliary space. Recursion uses $O(h)$ frames, at most $O(n)$, and the returned tree has $n$ nodes. Thus auxiliary and total memory are $O(n)$, matching the manifest.

Passing indices avoids slice copying that could make skewed cases quadratic.

## Alternatives and edge cases

- **Backward postorder iterator:** Pop roots from the end and recurse right before left. It is concise but child order becomes mandatory.
- **Half-open interval state:** Carry an exclusive postorder end and inorder bounds instead of starts plus size.
- **Iterative stack:** Reconstruct using postorder in reverse with an inorder pointer, avoiding recursion limits.
- **Repeated inorder search:** Removes the map but can cost $O(n^2)$.
- **Single node:** Both child sizes are zero and one leaf is returned.
- **Skewed tree:** Recursion depth may reach 3000 and exceed Python's default limit.
- **Unique values:** Required for deterministic lookup and reconstruction.
- **No input mutation:** Arrays are read by index only; unlike editorial `pop()` variants, postorder is preserved.
- **Not a BST problem:** Splits use traversal positions, not numerical comparisons.
- **Absolute and local indices:** $k$ is absolute in the complete inorder array; subtracting $i$ converts it into the current block's left size.
- **Invalid arrays outside the contract:** A missing value or inconsistent block could make $k$ fall outside the range. The selected source relies on the guarantees instead of validating this.
