## General
**The smallest remaining card fixes a group start**

Count the available copies of every value and process distinct values in ascending order. If the smallest value still present is $x$, it cannot be placed after a smaller card: no smaller remaining value exists to begin that group. Therefore every remaining copy of $x$ must start a group containing $x,x+1,\ldots,x+\texttt{group\_size}-1$.

Let `copies = counts[start]`. For each value in that consecutive interval, require at least `copies` available cards and subtract that many. If any count is smaller, those unavoidable groups cannot be completed, so no partition exists. Otherwise, all copies of the current start are consumed and the scan continues to the next sorted value with a positive count.

This greedy choice is forced rather than merely convenient. Any valid arrangement must place the smallest remaining cards at the beginnings of their groups, and consuming their required successors leaves exactly the residual instance that later starts must solve. Repeating the argument either constructs a partition of every card or identifies the first impossible successor.

Before processing counts, reject when `len(hand) % group_size != 0`, because complete equal-sized groups cannot cover a non-divisible number of cards.

## Complexity detail
Building the frequency map takes $O(n)$ time, and sorting at most $n$ distinct values takes $O(n\log n)$. Across all successful starts, each loop operation removes at least one card, so the consecutive-range work totals $O(n)$. The overall time is $O(n\log n)$ and the counts plus sorted keys use $O(n)$ space.

## Alternatives and edge cases
- **Min-heap of distinct values:** Repeatedly taking the smallest live value also implements the forced greedy choice in $O(n\log n)$ time, but stale heap entries and synchronized counts add bookkeeping.
- **Repeated minimum search:** Calling `min(counts)` after deleting every exhausted key is correct, but rescans the remaining keys and can take $O(n^2)$ time.
- **Sorted card list with open groups:** Tracking how many groups expect each next value can remain $O(n\log n)$, though its state is less direct than subtracting forced batches.
- **Non-divisible hand size:** If $n$ is not a multiple of `group_size`, a complete partition is impossible immediately.
- **Group size one:** Every card forms its own valid group, including duplicate and widely separated values.
- **Duplicate cards:** Multiple copies of a start force the same number of parallel consecutive groups.
- **Large gaps:** A gap is harmless only after all groups below it have already closed; otherwise the first missing successor causes failure.
- **Zero-valued cards:** Zero is an ordinary possible start because card values are nonnegative.
