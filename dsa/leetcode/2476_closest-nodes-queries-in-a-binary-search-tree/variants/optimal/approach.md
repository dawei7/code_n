## General

**Expose the BST's sorted order once.** An in-order traversal visits every binary search tree value in ascending order. Store that sequence in `values`. Use an explicit stack rather than recursion so a tree with up to $2 \cdot 10^5$ nodes remains safe even when it degenerates into a chain.

**Locate the insertion boundary.** For each query `x`, binary search for the first index whose value is at least `x`. If that position contains `x`, the query has an exact match and both answers are `x`. Otherwise, the value immediately before the insertion point is the greatest value below `x`, and the value at the insertion point is the smallest value above `x`.

When the insertion point is zero, no lower value exists; when it equals the sequence length, no upper value exists. Substituting `-1` at those boundaries gives the required result without special tree searches. Because every query uses the same sorted sequence, the traversal cost is paid only once.

## Complexity detail

Let $n$ be the number of tree nodes and $q = \lvert\texttt{queries}\rvert$. Iterative in-order traversal takes $O(n)$ time. Each query performs an $O(\log n)$ binary search, for total time $O(n + q\log n)$. The sorted values occupy $O(n)$ space; the traversal stack uses $O(h)$ space for tree height $h \le n$, so total auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Search the BST independently per query:** Each query can track predecessor and successor while descending, but costs $O(qh)$ and becomes quadratic when both the tree and query set are large and the tree is skewed.
- **Sort the queries and sweep:** Sorting queries and merging them with the in-order values costs $O(n + q\log q)$ and is useful when queries greatly outnumber nodes, but requires restoring original query order.
- **Recursive traversal:** It is concise, but a degenerate legal tree can exceed Python's recursion limit.
- **Exact match:** The same node value is both the greatest value at most the query and the smallest value at least it.
- **Outside the value range:** A query below the minimum has lower bound `-1`; a query above the maximum has upper bound `-1`.
- **Repeated queries:** Answer each occurrence independently and preserve the input order.
