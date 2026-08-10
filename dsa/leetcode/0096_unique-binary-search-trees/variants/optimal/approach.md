## General

The actual values `1` through `n` are already in sorted order, so the number of possible BSTs depends only on how many values a subtree receives. Choosing a root divides the remaining values into a smaller left group and a larger right group. The selected solution counts all combinations of those two independent groups with bottom-up dynamic programming.

Let $f[i]$ be the number of structurally unique BSTs that can be made from any $i$ consecutive ordered values. Their specific labels do not affect the count: values `[1, 2]` and `[8, 9]` permit the same two shapes.

**Why $f[0]=1$**

The initialization gives the empty value range one possible tree: the empty tree. This does not mean there is a physical node. It means there is one valid way to attach nothing as a child.

This multiplicative base is essential. For a one-node tree, the root has zero nodes on each side, so its number of combinations is

$$
f[0]\cdot f[0]=1.
$$

If $f[0]$ were zero, every root with an empty side would contribute zero, eliminating leaves and therefore every finite tree.

**Deriving one DP entry**

Suppose the total size is $i$. If the chosen root has $j$ nodes on its left, then it has

$$
i-j-1
$$

nodes on its right: subtract the $j$ left nodes and the root itself. The left group has $f[j]$ possible structures, and the right group has $f[i-j-1]$.

Every left structure can be paired with every right structure, so that split contributes their product. The inner loop tries $j=0,1,\ldots,i-1$, covering every possible root rank:

$$
f[i]=\sum_{j=0}^{i-1} f[j]f[i-j-1].
$$

This is the Catalan recurrence.

The outer loop runs from zero through `n`. At `i = 0`, the inner range is empty, preserving the initialized `f[0] = 1`. At `i = 1`, the sole split adds `f[0] * f[0]`, producing one. Every later entry reads only smaller indices, so they are already complete.

**Trace through `n = 3`**

- $f[0]=1$ represents an empty child.
- For one node, the only split is `(0, 0)`, so $f[1]=1$.
- For two nodes, splits `(0, 1)` and `(1, 0)` contribute one each, so $f[2]=2$.
- For three nodes, splits `(0, 2)`, `(1, 1)`, and `(2, 0)` contribute $2$, $1$, and $2$. Therefore $f[3]=5$.

Those three splits correspond to choosing the smallest, middle, or largest value as the root. Their five total structures match the Reference.

**Why multiplication and addition are both required**

For a fixed root rank, left and right choices are independent: selecting one left shape does not restrict which right shape can accompany it. The Cartesian-product rule therefore multiplies their counts.

Different root ranks are disjoint cases because their root values differ. Counts from those cases must be added. Reversing these operations would not describe the construction.

**Why the recurrence is complete and duplicate-free**

Every BST with $i$ nodes has one definite root rank and therefore one definite number $j$ of nodes on its left. Removing the root yields one left BST counted by $f[j]$ and one right BST counted by $f[i-j-1]$. Thus every valid tree belongs to one pair in one summand.

Conversely, any pair counted in a summand becomes a valid BST when joined under the corresponding root: all left labels are smaller and all right labels are larger. Two different root ranks cannot produce the same tree, and two different subtree pairs differ structurally. Every tree is therefore counted exactly once.

The method counts structures only; it does not allocate `TreeNode` objects. This is why it is dramatically cheaper than ID 95, which must return every tree.

## Complexity detail

For each size $i$, the inner loop runs $i$ times. The total iteration count is

$$
\sum_{i=0}^{n}i=\frac{n(n+1)}{2},
$$

so time is $O(n^2)$. Each iteration performs constant-many indexed reads, one multiplication, and one addition under the usual fixed-width arithmetic model. The Reference guarantees the answer fits the expected integer domain for $n\le19$.

The list `f` contains $n+1$ integers, so auxiliary space is $O(n)$, matching the manifest. The returned value itself is one integer.

## Alternatives and edge cases

- **Closed-form Catalan computation:** Use $C_n=\frac{1}{n+1}\binom{2n}{n}$ with careful integer arithmetic. This can run in $O(n)$ time and $O(1)$ extra space.
- **Catalan ratio recurrence:** Starting from $C_0=1$, compute $C_{k+1}=C_k\frac{2(2k+1)}{k+2}$. Exact division order matters in fixed-width languages.
- **Memoized recursion:** Recursively try every root size and cache results by subtree size. It has the same $O(n^2)$ time and $O(n)$ memo plus stack space but more call overhead.
- **Do not enumerate trees:** Constructing all $C_n$ trees solves a harder output problem and is unnecessary when only the count is requested.
- **Empty subtree versus public input:** The contract starts at $n=1$, but internal size zero is fundamental to leaf counting.
- **Single node:** The recurrence derives $f[1]=1$ without a separate hard-coded case.
- **Symmetry:** Splits $j$ and $i-1-j$ contribute equal products, but the source sums both because they represent roots mirrored in rank. An optimized half-sum must double carefully and handle a central split.
- **No overflow in Python:** Python integers grow as needed. Fixed-width implementations should choose a type large enough for the stated maximum.
