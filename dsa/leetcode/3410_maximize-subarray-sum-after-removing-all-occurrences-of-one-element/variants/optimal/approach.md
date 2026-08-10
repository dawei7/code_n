## General

**Deleting values changes adjacency.** If every occurrence of a chosen value is removed, the remaining elements close their gaps. A maximum subarray in the resulting array may therefore join pieces that were separated by removed occurrences in the original array. Running Kadane's algorithm independently after every possible deletion would be too slow, so the source maintains maximum-subarray information in a segment tree while temporarily turning selected leaves into empty positions.

**What each segment-tree node means.** For the sequence of currently present elements inside a tree interval, a node stores four values:

- `total`: the sum of all present elements in the interval;
- `prefix`: the greatest sum of a non-empty prefix of the present sequence;
- `suffix`: the greatest sum of a non-empty suffix;
- `best`: the greatest sum of any non-empty subarray.

A normal leaf holding value $x$ is `(x, x, x, x)`. Two adjacent nodes combine with the standard maximum-subarray formulas:

$$
\begin{aligned}
\text{total} &= L_{\text{total}}+R_{\text{total}},\\
\text{prefix} &= \max(L_{\text{prefix}},L_{\text{total}}+R_{\text{prefix}}),\\
\text{suffix} &= \max(R_{\text{suffix}},R_{\text{total}}+L_{\text{suffix}}),\\
\text{best} &= \max(L_{\text{best}},R_{\text{best}},L_{\text{suffix}}+R_{\text{prefix}}).
\end{aligned}
$$

The last choice for `best` represents a subarray crossing the boundary between the children.

**Represent a removed element as an empty sequence.** A removed leaf is

`(0, negative_infinity, negative_infinity, negative_infinity)`.

Its total is zero because it contributes no value. Its prefix, suffix, and best are negative infinity because the problem's subarray must be non-empty; an empty leaf must never win as a standalone subarray. When merged with real nodes, the zero total makes the real sequences on its two sides become adjacent. Thus, a crossing suffix-plus-prefix sum models exactly the gap-closing effect of deleting the element.

The same empty node initializes padding leaves beyond $n$, because the iterative tree uses a power-of-two leaf count. Padding then has no effect on the represented array.

The source uses `-(10**30)` as negative infinity. The smallest possible real sum has magnitude at most $10^5\cdot10^6=10^{11}$, so this sentinel is safely below every valid non-empty subarray sum and cannot accidentally win a maximum.

**Build once, then try each deletion value.** The initial tree contains every array element, and `tree[1][3]` is the maximum subarray sum with no operation. Storing that value first is essential because removal is optional.

The dictionary `positions` groups indices only for negative values. For each distinct negative value $x$, the algorithm:

1. updates every occurrence of $x$ to the removed-node state;
2. reads `tree[1][3]` as the best subarray after removing all occurrences of $x$;
3. restores every affected leaf to value $x$ before trying another value.

Each point update replaces one leaf and recomputes the four fields along its path to the root. Restoration ensures trials are independent: the tree never represents removal of two different values simultaneously.

**Why nonnegative values need not be tried.** Removing a positive or zero value cannot improve the optimum over keeping the original array. Consider any subarray selected after such a value is removed. It may join several original runs separated by removed occurrences. Put those nonnegative occurrences back between the first and last selected elements. They turn the joined result into a contiguous original subarray and do not decrease its sum. Therefore, the original array already has a subarray with sum at least as large. Since “at most once” permits no deletion, only negative values can possibly improve the answer.

If a negative value is the only distinct value and removing it empties the array, all leaves become empty and the root's `best` is negative infinity. That invalid trial cannot improve `answer`, so the source respects the non-empty-result rule without a separate condition.

For the first example, temporarily removing all `-2` leaves the compacted sequence `[-3,2,-1,3,3]`. The segment tree connects the two `3` values across the removed positions and reports the subarray `[2,-1,3,3]` with sum $7$. Restoring the `-2` leaves returns the tree to the original array before the next candidate value.

Correctness follows from the node invariant. The leaf states exactly represent present or removed elements; the merge formulas produce correct totals and maximum non-empty prefix, suffix, and subarray values for every parent. Hence the root reports the correct maximum for each tested resulting array. The no-deletion case plus every potentially useful negative deletion covers an optimal allowed choice.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$ and let `size` be the smallest power of two at least $n$, so `size = O(n)`. Building all leaves and internal nodes takes $O(n)$ time.

A point update changes one leaf and $O(\log n)$ ancestors. Across all distinct negative values, each negative index is removed once and restored once. There are at most $n$ such indices, so all trials perform at most $2n$ point updates and cost $O(n\log n)$ total time. Reading the root after one value's removals is $O(1)$. The total time is $O(n\log n)$.

The tree contains $2\cdot\texttt{size}=O(n)$ four-tuples. `positions` stores each negative index exactly once, also $O(n)$ space. Recursion is not used. Total auxiliary space is $O(n)$, matching the manifest.

## Alternatives and edge cases

- **Rerun Kadane for every distinct value:** Constructing or scanning a resulting array for each candidate can require $O(n^2)$ time when many negative values are distinct.
- **Specialized dynamic programming:** More intricate maps of best prefixes by deleted value can reach linear or near-linear time, but the segment tree gives a direct, verifiable representation of the actual deletion semantics.
- **Remove only one occurrence:** The operation removes every occurrence of the chosen integer. Grouping indices by value and updating the entire group is mandatory.
- **No deletion:** Initializing `answer` from the original root handles arrays where every deletion is unhelpful, including all-positive input.
- **Deleting zero:** It may connect equal-sum runs but cannot beat the original span that includes the zero. Skipping it is safe.
- **All values negative:** The maximum subarray is the greatest single remaining element. Trials that remove some negative value are handled, while a trial that removes the entire array yields only the sentinel and is ignored.
- **Duplicate negative values:** All matching leaves are removed before the root is queried. Querying after each individual removal would evaluate illegal partial deletions.
- **Tree padding:** Leaves beyond $n$ must be empty nodes, not zero-valued real nodes, because a real zero could be chosen as a non-empty subarray.
- **Sentinel size:** The chosen negative infinity must lie below every legal sum. The constraints make `-10**30` comfortably safe.
- **Restoration:** Every group is restored before testing the next value. Omitting restoration would simulate deleting multiple distinct integers, which the operation forbids.
