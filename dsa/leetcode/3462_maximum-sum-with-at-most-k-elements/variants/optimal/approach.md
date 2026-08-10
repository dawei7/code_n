## General

**Only the largest allowed values from each row can matter.** If at most `limits[i]` elements may be chosen from row $i$, any selected smaller value can be replaced by an unselected larger value from the same row without violating the limit and without decreasing the sum. Therefore, row $i$ contributes a candidate pool consisting only of its largest `limits[i]` entries.

The source sorts each row ascending and removes those candidates from the end with `nums.pop()`.

**Keep the globally largest \(k\) candidates.** `pq` is a min-heap of selected candidate values. For every row candidate:

1. push it into the heap;
2. if heap size exceeds $k$, pop the smallest.

After processing any prefix of candidates, the heap invariant is that it contains the largest at most $k$ values seen so far. A new value either belongs among them, displacing the previous minimum, or is itself immediately removed.

At the end, summing the heap gives the maximum possible total.

For `grid = [[1,2],[3,4]]` with limits $[1,2]$ and $k=2$, the row candidate pools are $\{2\}$ and $\{4,3\}$. Processing all three while retaining two largest leaves $3$ and $4$, sum $7$.

The heap evolution in that example is straightforward. Pushing $2$ gives `[2]`. Pushing $4$ gives a two-element heap containing $2$ and $4$. Pushing $3$ temporarily creates three retained values, so the smallest, $2$, is removed. What matters is the set represented by the heap, not its internal array order. The final set is $\{3,4\}$, exactly the two greatest eligible values.

**Why row filtering before global selection is valid.** Any feasible solution selects no more than the row limit. If it selects a value outside that row's top-limit pool, then fewer than `limit` larger row values can all be selected; at least one larger candidate is available for replacement. Repeating removes every dominated value. Thus an optimum exists entirely within the generated pool.

This replacement argument handles the row and global restrictions separately. Replacing a selected row value with a larger value from the same row does not change how many elements that row contributes, and it does not change the total number selected. Therefore, it preserves both constraints simultaneously. Once every selected value lies in its row's candidate pool, the problem loses its row structure: choosing any $k$ items from the pooled candidates is automatically feasible because no row contributed more than its own limit to that pool.

**Why “at most \(k\)” becomes exactly \(k\) here.** All grid values are nonnegative, and the constraints give `k <= sum(limits)`. When $k>0$, enough allowed candidates exist and adding another nonnegative value never lowers the sum, so retaining exactly $k$ is optimal. When $k=0$, each push is immediately popped and the final empty sum is zero.

**The exact source differs from the manifest summary.** The summary describes a max-heap merge that exposes candidates row by row. The protected code instead iterates through every top-limit candidate and maintains one global size-$k$ min-heap. Both implement the same selection principle, but their operation counts differ.

The method mutates `grid` substantially. Each row is sorted in place, and then its largest `limit` values are popped and removed from the row. Callers do not receive the original matrix contents afterward.
Row dominance proves discarded lower entries are never necessary. The bounded-min-heap invariant proves the final heap contains the $k$ largest values in the complete eligible pool. Those values automatically respect row limits because the pool contains at most the allowed count from each row. Their sum is therefore feasible and at least every other feasible sum.

The heap invariant follows by induction. Before processing anything, the empty heap contains the largest zero seen values. Suppose it is correct before a new candidate arrives. After pushing, if there are at most $k$ values, all seen values fit. If there are $k+1$, removing their smallest leaves precisely the largest $k$ among the old retained values and the newcomer; every previously discarded value was already no larger than an old retained value, so it cannot re-enter contention. The invariant therefore remains true after every candidate.

## Complexity detail

Let the matrix have $n$ rows and $m$ columns, and let

$$
L=\sum_i\texttt{limits}[i].
$$

Sorting all rows costs $O(nm\log m)$. The source processes exactly $L$ candidates, each with a heap push and possibly pop costing $O(\log(k+1))$. Exact total time is

$$
O(nm\log m+L\log(k+1)).
$$

The heap stores at most $k$ values. Python sorting may use $O(m)$ temporary space per row, one row at a time, so auxiliary space is $O(k+m)$. The manifest's stated $O(n+m)$ and `k log n` belong to the different merge implementation and do not precisely describe this source.

Because $L\le nm$, a looser bound is $O(nm\log m+nm\log(k+1))$. Keeping $L$ in the formula is more informative when row limits are small: the rows must still be sorted in full, but only the permitted suffixes generate heap operations. The final `sum(pq)` costs $O(k)$, which is absorbed by the heap-processing term for positive $k$.

## Alternatives and edge cases

- **Flatten every row completely:** Values below a row's top limit can never be selected and only increase work.
- **Sort all eligible candidates globally:** This is correct but stores $O(L)$ candidates; the bounded heap stores only $k$.
- **Max-heap row merge:** Push each row's largest available candidate and expose the next after selection. It can process only $k$ heap removals but needs row cursors; that is not the protected implementation.
- **\(k=0\):** Every pushed value is removed, and `sum([])` returns zero.
- **Zero values:** Selecting them may tie with using fewer than $k$, so exactly-$k$ retention remains optimal.
- **Zero row limit:** The pop loop performs no work for that row.
- **Limit equal to row length:** Every row value enters the candidate stream.
- **Duplicate values:** Heap identity is irrelevant; equal copies from valid row slots can all be selected.
- **Input mutation:** Sorting and popping alter every processed row.
- **Complexity fidelity:** The number of heap operations is $L$, not merely $k$, in this exact implementation.
