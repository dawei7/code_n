## General

**Store frequencies by value, not the sorted array itself**

At insertion `i`, the cost needs only two counts among the `i` earlier values:

- how many are strictly smaller than `x`;
- how many are strictly greater than `x`.

Maintaining an actual sorted Python list would make insertion linear because later elements must shift. A Binary Indexed Tree, also called a Fenwick tree, stores how many times each value has appeared and answers prefix counts in logarithmic time.

The largest instruction value `m` defines tree indices 1 through `m`. Input values are already positive, so no coordinate shift or compression is needed.

**Fenwick prefix queries**

`tree.query(x)` returns the count of inserted values less than or equal to `x`. It repeatedly adds `c[x]` and removes the least significant set bit with `x -= x & -x`. Each stored tree cell summarizes a power-of-two suffix of a prefix, and these jumps partition the requested prefix without overlap.

Therefore `tree.query(x - 1)` counts values strictly below `x`. Excluding index `x` is essential because equal values do not count as smaller.

After `i` instructions have been processed, there are exactly `i` values in the conceptual sorted container. `tree.query(x)` counts those less than or equal to `x`, so

`i - tree.query(x)`

counts values strictly greater than `x`. Subtracting `query(x-1)` instead would incorrectly include equal values among the greater side.

The insertion cost is the minimum of these two strict counts.

**Fenwick point updates**

After calculating the cost, `tree.update(x, 1)` records the new occurrence. It adds one at index `x` and repeatedly moves to `x + (x & -x)`. Those are precisely the Fenwick cells whose summarized ranges contain `x`.

Cost must be calculated before this update. Otherwise, the new value would be included among existing elements. Although equality is excluded from both strict counts here, maintaining the invariant “tree contains exactly the first `i` instructions” makes the formulas and proof reliable.

**A trace**

For `[1,5,6,2]`:

- Before 1, both counts are zero.
- Before 5, one value is below it and none is above, so cost is zero.
- Before 6, two are below and none above.
- Before 2, `query(1)=1` counts value 1. `query(2)=1`, so `3-1=2` earlier values are greater. Cost is `min(1,2)=1`.

The accumulated result is one.

**Why the tree represents the conceptual container**

Initially every frequency is zero, matching the empty container. Each iteration queries the frequency multiset for the first `i` instructions and then adds exactly the current value. Inductively, before the next iteration, the tree stores precisely the values that would be present in `nums`, including duplicates.

Prefix sums therefore give exact strict-smaller and strict-greater counts. Adding their minimum for each instruction matches the cost definition, so the accumulated `ans` is the required total.

The algorithm never needs to decide the physical position at which an equal value is inserted. Every possible position among equal values has the same number of strictly smaller and strictly greater elements. A frequency data structure therefore contains all information relevant to cost even though it does not materialize the sorted sequence itself.

## Complexity detail

Let $n$ be the instruction count and $M$ the maximum instruction value. Constructing the tree array uses $O(M)$ time and space. Each instruction performs two prefix queries and one update, each $O(\log M)$, for total $O(n\log M)$ processing time.

The full time bound including zero initialization is $O(M+n\log M)$. Because the constraints give $M\le10^5$ and the manifest focuses on operations, it records $O(n\log M)$.

The Fenwick array has $M+1$ entries, so auxiliary space is $O(M)$. Only scalar state is used beyond it.

The modulo is applied once to the final sum. Python integers can hold the unreduced total; reducing on each iteration would also be mathematically valid.

## Alternatives and edge cases

- **Segment tree:** It supports the same frequency range sums and point updates in $O(\log M)$ with a larger constant and storage footprint.
- **Coordinate compression:** Sort distinct instruction values and map them to dense ranks. This changes space to $O(n)$ and supports much larger numeric values.
- **Balanced order-statistics tree:** Store values with subtree sizes to query ranks. Python has no suitable built-in structure, making Fenwick simpler here.
- **Sorted list with binary search:** Rank queries are fast, but insertion shifts elements and makes worst-case time $O(n^2)$.
- **Equal prior values:** They are included in `query(x)` but not `query(x-1)`, so they contribute to neither strict side.
- **Smallest value:** `query(0)` returns zero because the query loop does not execute.
- **Largest value:** The greater count becomes zero when every prior value is at most it.
- **Duplicate instructions:** Each update adds another frequency occurrence, preserving multiplicity.
- **Positive-value constraint:** Fenwick index zero cannot be updated because its low bit is zero; inputs starting at one avoid that infinite-loop issue.
- **Single instruction:** Both counts are zero and total cost is zero.
