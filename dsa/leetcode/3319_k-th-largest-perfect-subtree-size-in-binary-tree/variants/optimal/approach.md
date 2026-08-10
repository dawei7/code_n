## General

**A subtree is perfect exactly when both children are perfect and equally large.** The recursive helper returns a positive subtree size when its argument roots a perfect binary tree and returns `-1` otherwise. An empty child returns zero, which serves as the size of a perfect empty subtree for the recurrence.

At a real node, the source first obtains `l` and `r` from its children. If the left result is negative, the left subtree is imperfect. If `l != r`, then either the right subtree is imperfect or the two perfect child subtrees have different sizes. In either situation, the current subtree cannot be perfect and returns `-1`.

The condition only explicitly tests `l < 0`, not `r < 0`, but inequality catches every case where only `r` is negative, and when both are negative they are equal. That last case is subtle: if both children return `-1`, then `l < 0` is true, so the current node still returns `-1`. The combined condition is safe.

**Why equal perfect sizes imply equal heights.** A perfect binary tree of height $h$ has $2^h-1$ nodes under the convention that a leaf has height one. This size uniquely determines $h$. Therefore two child subtrees that are independently perfect and have equal sizes also have equal heights and leaves on the same level. Adding their parent produces another perfect tree.

When valid, the current size is `l + r + 1`. The helper appends it to `nums` and returns it upward. A leaf has two empty children, so $l=r=0$, is appended with size one, and correctly counts as a perfect subtree.

**Postorder is necessary.** The current node's status depends on completed results from both children. Recursion naturally visits left and right subtrees before processing the node, which is postorder. The manifest calls the method iterative and height-based, but the exact source is recursive and returns sizes.

**Collect every perfect subtree, including nested ones.** A perfect tree contains smaller perfect subtrees rooted at its descendants. Each root corresponds to a distinct subtree and must participate in the ranking. Appending at every valid node records all of them, not just maximal perfect regions.

After traversal, if fewer than $k$ sizes were collected, the source returns `-1`. Otherwise it sorts `nums` in descending order and returns zero-based index `k - 1`. Duplicate sizes remain separate because different subtree roots are different perfect subtrees. Thus two size-three subtrees occupy two ranking positions.
The empty tree returns zero and is a valid neutral child. Assume child returns are exact. The source rejects precisely when a child is imperfect or perfect child sizes differ, both of which violate the perfect-tree definition. Otherwise both children are perfect at equal height, so the parent is perfect and its returned size is exact. This induction proves `nums` contains exactly every perfect-subtree size. Sorting then makes its $k$-th entry the required order statistic.

**Recursion depth caveat.** The tree can contain 2000 nodes in a chain. Standard CPython's default recursion limit is around 1000, so the exact implementation can raise `RecursionError` on a legal skewed tree. An explicit postorder stack would match the manifest's iterative wording and eliminate this failure mode.

## Complexity detail

DFS visits each of the $n$ nodes once and performs constant work, so collection takes $O(n)$ time. If $p\le n$ perfect subtrees are found, sorting costs $O(p\log p)$, bounded by $O(n\log n)$. Total time is $O(n\log n)$.

`nums` stores at most $n$ sizes. The recursion stack can reach $O(n)$ in a skewed tree, and sorting uses implementation-dependent temporary memory within $O(n)$. Total auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Iterative postorder:** Store nodes with a processed flag and map child results to parents. It avoids recursion limits and matches the manifest summary.
- **Min-heap of size $k$:** Keep only the $k$ largest perfect sizes during traversal, reducing ranking storage to $O(k)$ and sorting work to $O(n\log k)$.
- **Count by perfect height:** Sizes are of form $2^h-1$, so a frequency array by height can answer rankings without a full sort.
- **Leaf node:** Both child sizes are zero, so every leaf contributes a perfect subtree of size one.
- **One missing child:** Results zero and positive differ, so the parent is correctly rejected.
- **Both children imperfect:** Both may return `-1`, but `l < 0` prevents their equality from falsely validating the parent.
- **Equal-size perfect children:** Equal size uniquely implies equal perfect height, making the parent perfect.
- **Duplicate subtree sizes:** They represent different roots and must remain duplicate entries in the sorted ranking.
- **Fewer than $k$ perfect roots:** The explicit length check returns `-1`.
- **Entire tree perfect:** Its root contributes the largest size, while every perfect descendant is also collected.
- **Node values:** They never affect structural perfection and are intentionally ignored.
- **Deep skew:** The abstract linear traversal is sound, but recursive Python may fail beyond its recursion limit.
- **Manifest discrepancy:** The code performs recursive size-returning postorder, not iterative height computation.
