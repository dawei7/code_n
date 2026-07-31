## General

**Summarize whether a range can help.** A segment tree stores the maximum available basket capacity in every interval. If an interval maximum is smaller than the current fruit quantity, no basket in that interval can qualify. If the root maximum is too small, the fruit is immediately known to be unplaceable.

**Descend left before right.** When the root can accommodate the fruit, start at the root. At each internal node, inspect the left child's maximum. Descend left whenever that maximum is sufficient; otherwise the entire left interval is impossible, so descend right. Repeating this choice reaches the smallest index whose available capacity is at least the fruit quantity. This is the required leftmost basket, not merely any feasible basket.

After choosing a leaf, set its value to zero. All legal fruits are positive, so zero safely marks that basket unavailable. Recompute maxima on the path to the root, restoring the range summaries for the next fruit. The implementation pads the leaf layer to a power of two with zeros; padded positions can never qualify and therefore do not affect the answer.

The tree invariant is that every node equals the maximum currently available capacity among its real descendant baskets, with used and padded leaves contributing zero. Construction establishes it, and each leaf-to-root update restores it after one basket is consumed. Thus the root feasibility test is exact, and left-first descent returns precisely the contract-mandated basket.

## Complexity detail

Let $n$ be the common array length. Building the segment tree costs $O(n)$. Each placeable fruit performs one root-to-leaf search and one leaf-to-root update, both $O(\log n)$; an unplaceable fruit stops at the root. Across all fruits, the worst-case time is $O(n\log n)$.

The power-of-two tree has fewer than $4n$ entries, so auxiliary space is $O(n)$. The input arrays are not reordered, and recursion-stack space is avoided by the iterative representation.

## Alternatives and edge cases

- **Direct simulation:** Scanning baskets from the beginning for every fruit is simple but takes $O(n^2)$ time, which is too slow for $n=10^5$.
- **Recursive segment tree:** The same interval maxima and left-first search can be implemented recursively with identical asymptotic bounds, plus $O(\log n)$ call-stack depth.
- **Sorted capacities alone:** Sorting loses original basket positions; the answer requires the leftmost sufficient available basket.
- **Ordered capacity/index pairs:** A more involved ordered-set structure can query capacities and original indices, but it must still preserve the minimum eligible position under deletions.
- **Best-fit basket:** Choosing the smallest sufficient capacity violates the leftmost rule.
- **Exact capacity:** Equality qualifies because the basket condition is greater than or equal.
- **Used basket:** Zeroing a leaf and updating its ancestors prevents the same basket from being selected twice.
- **Non-power-of-two length:** Zero-padded leaves are safe because every valid fruit quantity is positive.
- **No qualifying basket:** Increment the unplaced count without modifying the tree.
- **All baskets consumed:** The root becomes zero, so every later positive fruit is rejected immediately.
- **Large capacities:** Values up to $10^9$ fit in the stored maxima; only comparisons are required.
