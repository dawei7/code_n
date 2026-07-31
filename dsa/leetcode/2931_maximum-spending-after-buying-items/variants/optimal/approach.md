## General

**Larger values belong on later days.** Suppose values $x<y$ are both
available on day $d$, and a feasible schedule buys $y$ then but leaves $x$
until a later day $e$. The item $x$ remains at its shop's available end during
that interval, while $y$ would also remain available if postponed. Swapping
their purchase days therefore preserves every shop's right-to-left order. The
spending changes from $dy+ex$ to $dx+ey$, an increase of

$$
(e-d)(y-x)\ge0.
$$

Repeatedly removing such inversions shows that some optimal schedule always
buys the smallest currently available value.

**Merge the shops from right to left.** Each row is non-increasing from left
to right, so its right-to-left purchase sequence is non-decreasing. Keep the
current rightmost value from every nonempty shop in a min-heap. The heap root
is the smallest item available across all shops. After buying it, expose the
item immediately to its left from the same row and insert that value.

This is a multiway merge of $m$ sorted purchase sequences. The exchange
argument proves each greedy choice can begin an optimal schedule; induction
over the remaining suffixes therefore proves that the complete heap order is
optimal. Multiplying successive popped values by days $1$ through $mn$ gives
the maximum spending.

## Complexity detail

The heap contains at most one item per shop. Each of the $mn$ items causes one
heap removal and at most one insertion, each costing $O(\log m)$ time. Total
time is $O(mn\log m)$ and the heap uses $O(m)$ auxiliary space.

## Alternatives and edge cases

- **Flatten and sort:** Sorting all $mn$ values in ascending order is valid because each row's order is compatible with that ordering, but it takes $O(mn\log(mn))$ time and $O(mn)$ space.
- **Repeated global minimum scan:** Search all remaining values for the next minimum and remove it; this is correct but quadratic in the item count.
- **Linear shop scan:** Checking the current end of all $m$ shops each day takes $O(m^2n)$ time, which is avoidable with the heap.
- **One shop:** Its purchase order is forced from right to left, and the heap naturally follows it.
- **Equal values:** Their relative order does not change the total; heap tie fields only provide deterministic ordering.
- **Wide total:** Up to $10^5$ items of value $10^6$ receive day multipliers, so fixed-width implementations need 64-bit arithmetic.
