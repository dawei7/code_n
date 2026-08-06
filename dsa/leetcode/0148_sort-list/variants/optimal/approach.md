## General
**Bottom-up run doubling avoids recursive stack space**

Count the nodes, then regard each node as a sorted run of width one. For each `width`, scan the list from left to right, merge adjacent runs of at most that width, and double the width after the complete pass. Once `width >= length`, the list is one sorted run.

**Cut each pair of runs before merging it**

`_split` advances through at most `width` nodes, null-terminates that run, and returns the first node after it. Split `left`, then `right`, and save the returned remainder as `current` before merging. These cuts keep a merge from consuming nodes that belong to the next pair.

`_merge` repeatedly appends the smaller run head, choosing `left` on equality so equal nodes remain stable. It attaches the nonempty remainder and returns both the merged head and tail, allowing the pass to connect the next merged run without rescanning the accumulated output.

At the start of a width-$w$ pass, the list consists of sorted adjacent runs of length at most $w$. Merging each neighboring pair preserves all nodes and produces sorted runs of length at most $2w$, which establishes the invariant for the doubled width. Eventually one run spans the list, proving the returned chain is fully sorted.

## Complexity detail
Every merge pass processes all $n$ nodes a constant number of times, and there are $\lceil\log_2 n\rceil$ passes, giving $O(n \log n)$ time. The iterative method retains only dummy nodes, counters, and a constant number of references, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Top-down merge sort:** has the same time bound but consumes $O(\log n)$ recursion-stack space.
- **Insertion sort:** relinks nodes in place but takes $O(n^2)$ time on an already ordered list with a forward insertion scan.
- **Array sorting:** is concise but stores $O(n)$ node references or values.
- Empty and one-node lists return immediately.
- A final run may be shorter than `width` or have no right partner; `_split` and `_merge` handle both cases.
- Null-terminating every split is essential to prevent a merge from crossing into later runs.
