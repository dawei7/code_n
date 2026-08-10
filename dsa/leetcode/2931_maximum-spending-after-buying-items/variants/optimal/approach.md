## General

The multiplier grows with the day number, so expensive items should be delayed and cheap items bought early. For two values $a>b$ assigned to days $d<e$, buying the smaller one first produces

$$
bd+ae
$$

instead of $ad+be$. The improvement is

$$
(bd+ae)-(ad+be)=(a-b)(e-d)>0.
$$

Thus any schedule containing a larger value before a smaller value can be improved by swapping them, provided the shop-access rules still allow the order. The ideal global purchase order is non-decreasing by value.

**Each shop exposes an ascending sequence from the right**

Every row is non-increasing from left to right. The rightmost item is therefore that shop's smallest remaining value and is the only currently buyable item. After it is removed, the item immediately to its left becomes available and is at least as large.

Viewed in purchase order from right to left, each shop is a sorted non-decreasing sequence. The task becomes merging $m$ sorted sequences into one global non-decreasing sequence.

**Heap contains one available item per shop**

The initial heap contains tuples `(row[-1], i, n - 1)` for every shop $i$: value, shop index, and column index. `heapify` turns these $m$ current frontiers into a min-heap.

On each iteration, `heappop` returns the smallest currently available value. If it came from column $j>0$, the source pushes `values[i][j - 1]`, the next rightmost item of that same shop. At all times, the heap contains exactly one entry for each nonempty shop.

Tuple fields `i` and `j` also break value ties deterministically, but tied values produce the same spending regardless of order.

**Why the smallest remaining item is always available**

Consider the globally smallest item not yet bought. If it is not currently rightmost in its shop, some unbought item lies to its right. Because the row is non-increasing, that right-side item has value no greater than the hidden one. Therefore a global minimum can always be found among the currently exposed rightmost items.

The heap selects such a minimum. Repeating this argument proves the popped sequence is a globally sorted order of all $mn$ values while respecting every shop's required right-to-left order.

**Why sorted purchase order maximizes spending**

The day multipliers $1,2,\ldots,mn$ are increasing. The exchange calculation shows that whenever a larger value is assigned an earlier day than a smaller value, swapping them cannot decrease spending and strictly increases it when values differ.

Therefore pairing values in non-decreasing order with days in increasing order is optimal. The heap constructs exactly that feasible order, so adding `v * d` on every pop yields the maximum.

The source starts `ans = d = 0` and increments `d` before charging the popped item. The first purchase is multiplied by one, not zero. The loop ends only after all heap entries and all revealed predecessors are consumed, so every item is bought exactly once.

For rows `[8,5,2]` and `[6,4,1]`, the initial heap exposes $2$ and $1$. It pops $1$, reveals $4$, then pops $2$, reveals $5$, and continues merging. Hidden $8$ and $6$ cannot incorrectly appear early.

## Complexity detail

Let $m$ be number of shops, $n$ items per shop, and $N=mn$ total items. Each item is pushed and popped once. The heap contains at most $m$ entries, so each operation costs $O(\log m)$. Total time is $O(mn\log m)$.

The heap holds one tuple per nonempty shop, requiring $O(m)$ auxiliary space. The input rows are read but not modified.

Building the initial list and heap takes $O(m)$ time, dominated by processing all items.

## Alternatives and edge cases

- **Flatten and sort all values:** Global ascending order is feasible here and sorting gives $O(mn\log(mn))$ time plus $O(mn)$ storage. The heap exploits already sorted rows.
- **Choose the largest available item:** That puts expensive values on small multipliers and minimizes rather than maximizes the rearrangement objective.
- **Dynamic programming over shop positions:** The state space across $m$ shops is enormous and unnecessary because the exchange argument determines the order.
- **One shop:** The heap simply buys its row from right to left, pairing ascending values with increasing days.
- **One item per shop:** All items are initially available, and the method becomes an ordinary heap sort of $m$ values.
- **Equal values:** Any order among them has identical contribution; tuple tie-breaking does not affect optimality.
- **Day numbering:** Increment before multiplication is essential because days begin at one.
- **Large total:** Products and their sum can be large; Python integers avoid overflow.
- **Row ordering guarantee:** If rows were not non-increasing, the current-frontier heap would not necessarily expose a global minimum and the proof would fail.
- **Pairwise different note:** The algorithm does not rely on global uniqueness and remains correct with equal values.
- **Heap invariant:** Immediately before every pop, each heap entry is the rightmost unbought item of its shop; pushing only `j - 1` preserves this fact inductively.
