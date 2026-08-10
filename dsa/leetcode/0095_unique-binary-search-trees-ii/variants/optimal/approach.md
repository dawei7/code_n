## General

A binary search tree is determined recursively. Once a value $v$ is chosen as the root, every smaller value must appear in its left subtree and every larger value must appear in its right subtree. Because the required values are exactly the consecutive integers from `1` through `n`, choosing the root divides the problem into two independent consecutive ranges:

$$
[i,v-1]\quad\text{and}\quad[v+1,j].
$$

The selected solution uses this fact directly. The helper `dfs(i, j)` returns a list containing the root of every structurally unique BST that uses each value in the inclusive range `[i, j]` exactly once.

**Why every possible root must be tried**

For an interval `[i, j]`, any value `v` from `i` through `j` can legally be its root. Once `v` is fixed, the BST ordering rule leaves no freedom about which values belong on each side: `[i, v - 1]` must go left, and `[v + 1, j]` must go right.

There may still be many possible shapes for each side. The recursive calls return all of them as `left` and `right`. The nested loops form the Cartesian product: for every left tree `l` and every right tree `r`, create `TreeNode(v, l, r)`. Each pair represents one complete tree whose root is `v`.

Trying only matching list indices would be wrong. If there are two possible left shapes and three possible right shapes, the root has $2\cdot3=6$ combinations, not merely two or three.

**Why an empty interval returns `[None]`**

When `i > j`, no value is available. There is one valid tree for that range in the combinatorial sense: the empty tree. The helper represents that single possibility as a list containing `None`.

Returning an empty list would say there are zero possible attachments. The Cartesian-product loops would then run zero times whenever a root had no left or right values. That would incorrectly eliminate every leaf and every node with one missing child.

For example, while building the one-value interval `[2, 2]`, root `2` has empty ranges on both sides. The recursive results are `[None]` and `[None]`; their one pair creates `TreeNode(2, None, None)`. Thus `[None]` acts as the multiplicative identity for combining subtree choices.

**Trace for `n = 3`**

The initial state is `dfs(1, 3)`.

- If `v = 1`, the left side is empty. The right range `[2, 3]` has two trees: one rooted at `2` with right child `3`, and one rooted at `3` with left child `2`. Pairing each with the empty left side creates two full trees.
- If `v = 2`, both ranges contain one value. There is one left tree containing `1` and one right tree containing `3`, creating one full tree.
- If `v = 3`, the right side is empty. Range `[1, 2]` has two possible trees, creating two more full trees.

The total is five, the five structures shown by the Reference.

**Why all returned trees are valid**

Assume recursively that every tree in `left` contains exactly the values `[i, v - 1]` and satisfies BST ordering, and every tree in `right` does the same for `[v + 1, j]`. All left values are smaller than `v`; all right values are larger. Connecting one tree from each list beneath a new node valued `v` therefore produces a BST containing every value in `[i, j]` exactly once.

The empty-range base case is valid, so this induction applies from leaves up to `dfs(1, n)`.

**Why no structure is missed or duplicated**

Take any valid BST on `[i, j]`. Its root has one definite value `v`, and the outer loop considers it. Its left subtree must be one of the trees returned for `[i, v - 1]`, while its right subtree must be one returned for `[v + 1, j]`. The nested loops eventually choose exactly that pair, so the tree is generated.

Two trees built under different root values are immediately distinct. Under the same root, two different left/right pairs differ structurally on at least one side. Assuming recursive lists contain no duplicate structures, the Cartesian product introduces none. This proves uniqueness recursively.

**The selected source is recursive but not memoized**

Although the local editorial describes recursive dynamic programming with a memo, this exact `solution.py` does not cache `(i, j)` results. If the same interval is requested from different ancestors, its list is rebuilt. The explanation must follow that selected source, so no hash map or memo lookup should be claimed.

The solution also attaches returned subtree objects directly. Within one call, a left subtree object can be paired with multiple right subtrees and therefore shared by several returned roots. This is safe for the challenge because the generated trees are only returned and not subsequently mutated by the method. If a caller requires every returned tree to own disjoint node objects, each attached subtree must be cloned, increasing actual allocation work.

## Complexity detail

Let $C_n$ be the $n$th Catalan number, the number of structurally unique BSTs on $n$ ordered values:

$$
C_n=\frac{1}{n+1}\binom{2n}{n}.
$$

There are $C_n$ returned roots. Conceptually, each result contains $n$ nodes, so explicitly materializing or serializing all trees requires $\Theta(nC_n)$ output work and storage. This is the manifest's stated $O(nC_n)$ time and space bound. Since

$$
C_n=\Theta\left(\frac{4^n}{n^{3/2}}\right),
$$

the bound may also be written as $O(4^n/\sqrt n)$.

The exact implementation shares some subtree node objects rather than deep-cloning them for every output tree, so its number of physical node allocations can be smaller than the conceptual $nC_n$ forest size. On the other hand, the absence of memoization causes interval lists to be recomputed. The manifest's $O(nC_n)$ is a safe conventional output-sensitive upper bound and describes the size required when outputs are treated as independent trees.

Recursion depth is at most $n$. Temporary lists, returned tree roots, and the conceptual output dominate the stack. Under the manifest convention that includes the generated forest, space is $O(nC_n)$. If only auxiliary stack space were counted while allowing shared returned objects, it would be described separately as $O(n)$ plus transient recursive results.

For the constraint $n\le8$, the Catalan growth is still manageable; $C_8=1430$.

## Alternatives and edge cases

- **Top-down memoization by interval:** Cache each `(i, j)` result so repeated interval requests reuse one list. It avoids recomputation but deliberately increases shared-subtree reuse unless results are cloned.
- **Bottom-up interval DP:** Build all trees for shorter consecutive ranges before longer ranges. It removes recursion and exposes dependencies clearly, but stores many interval result lists.
- **Size-based DP with value offsets:** Store shapes for sizes starting at value one, then clone right subtrees with an offset. It can reduce the number of interval states, but cloning and value translation make it more complex.
- **Generate shapes, then label inorder:** First enumerate unlabeled binary-tree shapes and assign `1..n` in inorder. This separates structure from BST labeling but still must produce Catalan-many outputs.
- **Do not return `[]` for an empty side:** A missing child is one valid option, represented by `[None]`; zero options would erase legitimate combinations.
- **Single node:** Both child intervals are empty, so the sole result is a root valued `1` with two `None` children.
- **Extreme root values:** Choosing the smallest value produces an empty left side; choosing the largest produces an empty right side. Both are ordinary cases handled by the same base result.
- **Shared subtree references:** The returned forest may not consist of fully disjoint objects. Do not mutate one generated tree unless the API guarantees or the implementation creates independent clones.
- **Output order:** Root values are tried ascending, then left and right lists in their recursive order. The contract accepts any order.
