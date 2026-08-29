## General

Preorder and inorder reveal complementary information:

- preorder lists `root, left subtree, right subtree`, so the first value of any subtree's preorder block is its root;
- inorder lists `left subtree, root, right subtree`, so the root's position separates the two child value sets.

The values are unique, making every root position unambiguous. The selected solution stores each inorder value's index in dictionary `d` and recursively reconstructs matching array ranges.

**Meaning of `dfs(i, j, n)`**

The state builds a subtree containing exactly $n$ nodes:

- its preorder block begins at index $i$;
- its inorder block begins at index $j$; and
- both blocks describe the same $n$ values.

The blocks are implicit; no slices are created. Avoiding slices prevents repeated copying and preserves linear time.

If $n\le0$, the interval contains no nodes and returns `None`. This represents a missing child.

**Finding the root and split**

For a nonempty state, `v = preorder[i]` is the root value because preorder visits the root first. `k = d[v]` gives its absolute index in the full inorder array.

The current inorder block begins at $j$. Values from $j$ through $k-1$ belong to the left subtree, so its size is:

$$
L=k-j.
$$

The root occupies one node. The remaining right-subtree size is:

$$
R=n-L-1=n-k+j-1.
$$

These sizes are nonnegative because the traversals are guaranteed consistent.

**Deriving the child calls**

Immediately after the root in preorder comes the complete left subtree. Its preorder start is `i + 1`, its inorder start remains `j`, and its size is $L$. Hence:

`dfs(i + 1, j, k - j)`.

The right subtree starts in preorder after the root and all $L$ left nodes:

$$
i+1+L=i+1+k-j.
$$

Its inorder block starts after the root at $k+1$, and it has $R$ nodes. This gives the exact second call.

The source computes both child roots first and then creates `TreeNode(v, l, r)`. Construction order does not alter tree structure; the saved root value and range formulas already determine parentage.

**Trace through the Reference example**

For preorder `[3,9,20,15,7]` and inorder `[9,3,15,20,7]`, the initial state has `i = 0`, `j = 0`, and `n = 5`. Root value three is at inorder index one.

The left size is one, so the left call uses preorder index one and builds node nine. The right size is three, and its preorder start is `0 + 1 + 1 = 2`, pointing to twenty.

For that right state, twenty's inorder index is three while its inorder start is two. Its left size is one, selecting fifteen; its remaining right size is one, selecting seven. The reconstructed tree matches `[3,9,20,null,null,15,7]`.

**Why reconstruction is unique and correct**

The root of each nonempty preorder block is forced. Its unique inorder position forces exactly which values lie in each child subtree and how many there are. Preorder's root-left-right layout then forces the matching child block starts.

Assuming recursive calls correctly reconstruct those smaller blocks, attaching them beneath the forced root produces a tree with exactly the requested traversals. The empty-size base handles absent children. Induction on $n$ proves correctness.

Because each decision is forced, no second different tree can satisfy both traversals under unique values.

The state invariant also guarantees that `preorder[i]` belongs inside the current inorder block. At the initial call this follows from the input guarantee. After a split, the calculated preorder lengths exactly equal the two inorder interval lengths, so each child receives matching value sets. This prevents the global dictionary index `k` from falling outside the child's intended interval. The code does not check this explicitly because both traversals are guaranteed valid; malformed arrays would require separate validation.

## Complexity detail

Building `d` visits all $n$ inorder values once. Each real node creates one recursive state, performs constant-time expected dictionary lookup and arithmetic, and allocates one node. Total time is $O(n)$.

The dictionary uses $O(n)$ space. Recursion uses $O(h)$ frames, at most $O(n)$, and the returned tree itself has $n$ nodes. Thus auxiliary space is $O(n)$ due to the map, matching the manifest; total space including output is also $O(n)$.

No array slice is allocated, which is essential to the linear bound.

## Alternatives and edge cases

- **Global preorder iterator plus inorder bounds:** Consume one root per call and split using the same index map. It reduces one state parameter.
- **Iterative stack reconstruction:** Compare preorder nodes with the inorder sequence to determine when left chains end. It is linear but less direct to derive.
- **Repeated inorder search:** Avoiding a map makes each root search linear and can degrade total time to $O(n^2)$ on skewed trees.
- **Single value:** Both child sizes are zero, producing one leaf.
- **Skewed tree:** One child size is repeatedly zero; recursion depth can reach $n$.
- **Unique-value guarantee:** Essential for a one-to-one value-index dictionary and unique reconstruction.
- **Valid-traversal guarantee:** The formulas assume both arrays contain the same values and consistent subtree blocks.
- **Python recursion limit:** A 3000-node skewed tree may require an iterative alternative.
- **Negative values:** Dictionary keys and traversal logic handle them normally.
- **No input mutation:** Both traversal arrays are read by index only, so callers retain their original sequences.
- **Absolute versus local indices:** `k` is absolute in the complete inorder array, while `k - j` converts it to a size local to the current block.
