## General

**Flatten the BST into sorted order**

For every binary search tree node, all values in its left subtree come before the node, and all values in its right subtree come after it. An inorder traversal therefore produces a non-decreasing list of tree values.

The nested `dfs` recursively visits left child, appends `root.val`, and visits right child. `None` returns immediately. The resulting `nums` list supports binary search for every query.

The manifest calls this traversal iterative, but the protected source is recursive. That distinction matters for a skewed tree with up to $10^5$ nodes because Python recursion can overflow.

**Find the floor value**

For query `x`, the required minimum-side answer is actually the floor: the largest tree value no greater than `x`.

The expression

`bisect_left(nums,x+1)-1`

finds the first index whose value is at least `x+1`, then steps back. Because values and queries are integers, values smaller than `x+1` are exactly values at most `x`.

If every tree value is greater than `x`, the resulting index is -1 and the bounds check returns -1. Otherwise `nums[i]` is the rightmost value no greater than the query.

Using `bisect_right(nums,x)-1` would be an equivalent and perhaps more direct expression.

**Find the ceiling value**

`j = bisect_left(nums,x)` finds the first value at least `x`, exactly the requested ceiling.

If `j==len(nums)`, every tree value is smaller and no ceiling exists. The bounds check then returns -1.

When `x` itself appears in the BST, the floor and ceiling searches both select `x`, producing `[x,x]`.

The two searches deliberately use inclusive comparisons on opposite sides. A predecessor search using strictly less than `x` would mishandle an exact match, as would a successor search using strictly greater. The transformed upper boundary `x+1` and the lower-bound search at `x` encode “less than or equal” and “greater than or equal” precisely.

**Preserve query order**

The loop processes queries in their supplied order and appends one pair per query. Duplicate queries simply repeat the same two binary searches and produce duplicate answer pairs, as required.

For sorted values `[1,2,4,6,9,13,14,15]`:

- Query 5 has floor index at value 4 and ceiling index at value 6.
- Query 16 has floor 15, while the ceiling insertion index is past the list and becomes -1.
- Query 2 selects 2 on both sides.

**Why the searches are correct**

Inorder traversal includes every node once and respects BST ordering, so `nums` contains precisely the searchable value multiset in sorted order.

The floor index is the last position in the prefix of values `<=x`. The ceiling index is the first position in the suffix of values `>=x`. Binary search returns these boundary positions by definition. Bounds checks convert empty prefix or suffix cases to the required sentinel.

Applying this independently to every query proves the complete answer.

The method does not need to retain node references after traversal. Once values are in sorted order, tree shape is irrelevant to the floor and ceiling questions. This is why one preprocessing pass can serve all queries even when the original tree is highly unbalanced.

**Why preprocess rather than search the tree per query**

A balanced BST path search would take $O(\log n)$ per query and use no full sorted list, but the input tree is not guaranteed balanced. A skewed tree could require $O(n)$ per query. Inorder preprocessing makes later searches predictably logarithmic regardless of shape.

## Complexity detail

Let $N$ be the number of tree nodes and $Q$ the number of queries. Inorder traversal visits each node once, taking $O(N)$ time. Each pair of binary searches costs $O(\log N)$, so total time is $O(N+Q\log N)$.

The sorted list uses $O(N)$ space. Recursive traversal uses $O(h)$ stack frames for tree height $h$, up to $O(N)$. The returned result uses $O(Q)$ space. Auxiliary preprocessing space is $O(N)$.

At maximum skew, recursive `dfs` may raise `RecursionError`. An explicit stack would retain the same asymptotic bounds and match the manifest wording.

## Alternatives and edge cases

- **Iterative inorder:** Use an explicit node stack to build the sorted list without recursion risk.
- **Direct BST search per query:** Track floor and ceiling while descending. It uses $O(h)$ time per query and can become $O(NQ)$ on a skewed tree.
- **Offline merged scan:** Sort queries with original indices and sweep them alongside inorder values, achieving $O(N+Q\log Q)$ time.
- **Query below every value:** Floor index is invalid and returns -1; ceiling is the smallest tree value.
- **Query above every value:** Floor is the largest tree value and ceiling returns -1.
- **Exact match:** Both results equal the query value.
- **Duplicate queries:** They remain separate output entries in original order.
- **Skewed tree:** Sorted-list logic remains correct, but recursive traversal is operationally unsafe.
- **Integer query property:** `x+1` makes `bisect_left` behave as an inclusive upper-bound search.
- **Metadata mismatch:** The exact traversal is recursive, not iterative, even though time and total space bounds remain the same.
