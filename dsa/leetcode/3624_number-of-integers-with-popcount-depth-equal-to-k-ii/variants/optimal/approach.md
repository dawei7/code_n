## General

**Reduce values to one of six classes.** Computing an element's popcount-depth takes only a few popcounts: after the first operation, a legal value is at most 50, and the sequence rapidly reaches 1. Store each index's current depth so an update knows which class loses that position and which class gains it.

**Represent every class by a Fenwick tree.** Create one binary indexed tree for each queryable depth 0 through 5. Tree `k` stores a 1 at an index exactly when the current array value there has depth `k`; all other positions contribute 0. Populate the leaves from the initial depths and build each Fenwick tree in linear time by forwarding every node's count to its parent.

A range query for depth `k` becomes the difference between two prefix sums in tree `k`, so it counts precisely the qualifying indices in `[l, r]`. For an update, compute the replacement's depth. If it differs from the stored old depth, subtract 1 from the old tree, add 1 to the new tree, and record the new class. Fenwick point changes and prefix sums preserve every tree's class-count invariant after each operation, so queries observe all preceding updates in order.

## Complexity detail

Let $n$ be the array length and $q$ the query count. Depth classification and linear Fenwick construction take $O(n)$ time. Each range query performs two $O(\log n)$ prefix sums, and each depth-changing update performs two $O(\log n)$ point changes; depth calculation is bounded by a constant number of popcounts for values at most $10^{15}$. Total time is $O(n+q\log n)$. Six trees and the depth array use $O(n)$ space.

The benchmark sets $n=q=S$, mixes full-range counts with depth-changing updates, and uses all depth classes. The accepted method takes $O(S\log S)$ time, while a correct implementation that scans the requested subarray for every count query takes $O(S^2)$.

## Alternatives and edge cases

- **Scan every requested range:** It is simple and correct but can take $O(nq)$ time when many queries cover most of the array.
- **Segment tree of six-count vectors:** It supports the same asymptotic bounds and is a valid alternative, but Fenwick trees make point updates and one-class sums more compact.
- **Depth zero:** Only the value 1 belongs to this class.
- **Depth five:** No legal stored value reaches this depth, but its empty tree naturally answers every such query with zero.
- **Inclusive endpoints:** Use the prefix through `r + 1` minus the prefix before `l`.
- **Same-depth replacement:** The numeric value may change without changing its class; no tree update is needed.
- **Repeated updates:** The stored depth, rather than the original `nums` value, supplies the correct class to remove each time.
- **Only update queries:** The returned answer list is empty.
