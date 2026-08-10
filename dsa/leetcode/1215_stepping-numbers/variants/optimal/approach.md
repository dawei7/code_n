## General

Every positive stepping number can be built digit by digit. If its last digit is $x$, the only legal next digits are $x-1$ and $x+1$ when they remain between zero and nine. The exact solution performs a breadth-first generation starting from the one-digit numbers one through nine.

Zero is handled separately because extending a leading zero would create ordinary shorter numbers rather than new decimal representations.

**Seed every positive one-digit stepping number**

Every one-digit number is stepping because it has no adjacent digit pair that could violate the rule. The queue begins with `1` through `9` in increasing order.

If `low == 0`, the method appends zero to the answer before starting the positive-number generation. If `low > 0`, zero must not appear.

**Generate exactly the legal children**

After removing value `v`, the code takes its last digit with `x = v % 10`.

When `x > 0`, appending `x - 1` creates `v * 10 + x - 1`. The new final digit differs from the old final digit by exactly one.

When `x < 9`, appending `x + 1` creates the other legal child.

At digit zero, only one is legal; at digit nine, only eight is legal. Every generated child remains a stepping number because all earlier adjacent pairs were already valid and the newly added pair is explicitly valid.

Conversely, remove the final digit from any multi-digit positive stepping number. The remaining prefix is a positive stepping number, and the removed digit must be one of exactly these generated children. Therefore, every positive stepping number is eventually generated once.

**Why the queue is numerically sorted**

The seeds are increasing. Within one parent, the smaller legal child is enqueued before the larger child.

More importantly, every child of a smaller same-length parent is smaller than every child of the next larger parent. If `u < v`, then the largest child of `u` is at most `10u + 9`, while the smallest child of `v` is at least `10v`. Since `v >= u + 1`, `10v >= 10u + 10`.

Breadth-first processing also completes all shorter decimal lengths before longer ones, and every shorter positive integer is smaller than every longer positive integer. The queue therefore yields stepping numbers in increasing numeric order.

This ordering justifies `if v > high: break`. Once one dequeued value exceeds `high`, every remaining queued value is at least as large, so none can belong to the range.

**Filter the inclusive range while generating**

Every dequeued `v <= high` is appended only when `v >= low`. These comparisons include both endpoints.

Values below `low` are not returned, but they are still expanded because their children may grow into the requested interval. Values above `high` are neither returned nor expanded after the first such value ends the ordered traversal.

For range zero through 21, zero is inserted separately. Seeds one through nine are returned, then the two-digit generation yields 10, 12, and 21 before the next value exceeds the bound. The answer is already sorted and needs no final sort.

**Why the result is exact**

The generation rules preserve stepping validity and can reconstruct every positive stepping number from its prefix, establishing soundness and completeness. The range checks retain exactly the values between the inclusive bounds. Queue ordering gives increasing output order and makes the early termination safe.

No number is generated twice because every positive integer has one unique decimal prefix obtained by removing its final digit.

## Complexity detail

Let $S$ be the number of stepping numbers from zero through `high`, inclusive.

Each relevant generated number is dequeued once and creates at most two children. The first frontier beyond `high` can contain additional enqueued children, but their number is proportional to the preceding stepping-number frontier. Total generation work is $O(S)$.

The answer stores up to $O(S)$ values, and the queue can hold a breadth-first frontier of stepping numbers, also bounded by $O(S)$. Total space is $O(S)$ including output; auxiliary queue space is at most $O(S)$.

Python integers avoid overflow when children just beyond the upper bound are formed. The constraint keeps useful values within roughly 32-bit range.

## Alternatives and edge cases

- **Depth-first generation plus sorting:** DFS can generate the same tree, but its natural order is not globally numeric and would require a final sort.
- **Scan every integer:** Testing all values from `low` through `high` wastes work when stepping numbers are sparse.
- **Digit dynamic programming:** It can count stepping numbers efficiently over much larger string bounds, but listing every answer still requires output-proportional work.
- **`low = 0`:** Zero is inserted once; it is never used as a leading-digit seed.
- **`high < 9`:** Ordered seeds cause an early break at the first value above the bound.
- **Last digit zero:** Only digit one may be appended, preventing a negative digit.
- **Last digit nine:** Only digit eight may be appended, preventing digit ten.
- **Inclusive endpoints:** Both `v >= low` and the pre-break `v <= high` logic include qualifying boundary values.
- **Sorted output:** BFS numeric ordering removes the need for a separate sort.
- **Unique generation:** Each number has exactly one parent formed by deleting its last decimal digit.
