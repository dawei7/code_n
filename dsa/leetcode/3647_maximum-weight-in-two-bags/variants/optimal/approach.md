## General

**Recognize a two-capacity 0/1 knapsack**

Every item has three possible outcomes:

1. Leave it unpacked.
2. Put it in bag one.
3. Put it in bag two.

The item may not be split or used twice, which makes this a 0/1 choice. Unlike ordinary one-bag knapsack, feasibility depends on two separate capacities. A single scalar such as total remaining capacity is not enough: using four units in bag one and zero in bag two is different from using zero in bag one and four in bag two, even though both use four total units.

The reward of packing an item is equal to its weight. Therefore, the objective is to make the combined used capacity of the two bags as large as possible without exceeding either individual limit.

Trying all three choices for every item would create up to `3^n` assignments. With as many as 100 items, exhaustive search is impossible. The capacities are at most 300, however, so dynamic programming over the two capacity dimensions is practical.

**Define what one table cell means**

After some prefix of the items has been processed, let

`f[j][k]`

be the maximum total packed weight obtainable from those processed items when bag one has capacity at most `j` and bag two has capacity at most `k`.

The state represents capacity limits, not exact used weights. A value of zero is valid for every pair because choosing no processed item fits within any capacities. This is why the source can initialize the whole table to zero without a separate unreachable marker.

This detail also corrects the wording in the manifest summary. The exact source does not maintain a Boolean table of “exactly reachable bag weights.” It maintains the best total value under each pair of capacity bounds. Both formulations can solve the task, but the recurrence and zero initialization here follow the bounded-capacity interpretation.

**Derive the three choices for one item**

Suppose the current item has weight `x`, and we want to update state `f[j][k]`.

If the item is skipped, the best value already stored in `f[j][k]` remains available. No explicit assignment is needed for this choice because the table is updated in place and its old value is retained.

If the item goes into bag one, it consumes `x` units of the first capacity. This is possible only when `x <= j`. Before adding it, the remaining processed items must fit within capacities `j - x` and `k`, whose best total is `f[j - x][k]`. The candidate becomes

`f[j - x][k] + x`.

If the item goes into bag two, it consumes `x` units of the second capacity. This is possible only when `x <= k`, and the corresponding candidate is

`f[j][k - x] + x`.

The update takes the maximum among the retained skip value and whichever placement candidates are feasible. Although the code executes the two `if` statements one after another, they are competing alternatives for the same item. They must not allow the item to enter both bags.

**Why both capacity loops run backward**

In a separate-layer implementation, every transition would read from a table for the previous item and write to a new table for the current item. The source saves that extra layer by updating one table in place. Backward iteration makes the source cells behave as though they still belonged to the previous layer.

The outer loop visits `j` from `w1` down to zero. A bag-one transition reads `f[j - x][k]`, whose first index is smaller than `j`. Because smaller `j` values have not yet been processed for the current item, that source cell cannot already include `x`.

For one fixed `j`, the inner loop visits `k` from `w2` down to zero. A bag-two transition reads `f[j][k - x]`, whose second index is smaller. That cell has also not yet been processed for the current item.

Thus both placement candidates add `x` to a state formed using only earlier items. The first `if` may update the destination `f[j][k]`, but the second `if` reads a different, still-old source cell `f[j][k - x]` and merely competes for the same destination. It does not add `x` to the bag-one candidate already written there.

If either loop ran forward, a smaller-capacity state could be updated with `x` and then reused to update a larger-capacity state during the same item iteration. That would behave like having multiple copies of the item and violate “at most one bag.”

**Why the recurrence finds the best legal packing**

Assume the table is correct for all items before the current weight `x`. Consider an optimal packing for capacity pair `(j, k)` after `x` becomes available.

Exactly one of three cases applies:

- The packing omits `x`. Its total is no larger than the old `f[j][k]`.
- It places `x` in bag one. Removing `x` leaves a legal packing of earlier items within `(j - x, k)`, so its remaining total is no larger than old `f[j - x][k]`.
- It places `x` in bag two. Removing `x` leaves a legal earlier-item packing within `(j, k - x)`.

The recurrence considers the best value from every possible case, so it cannot be smaller than the optimum. Each candidate it constructs is also legal: it extends a legal earlier-item packing by placing `x` in at most one bag with enough capacity. It therefore cannot exceed the optimum either.

Starting from the empty-prefix table of zeros and applying this argument for every item establishes that `f[w1][w2]` is the maximum total weight packable into the two full-capacity bags.

**Trace the first example**

For `weights = [1, 4, 3, 2]`, `w1 = 5`, and `w2 = 4`, the table gradually records useful capacity combinations. One optimal chain of choices places weight three and weight two in bag one, filling it to five, and places weight four in bag two, filling it to four. Weight one is skipped.

The final total is nine, equal to `w1 + w2`. Since no legal packing can exceed the sum of both capacities, reaching nine also supplies an immediate upper-bound check that this result is optimal.

For `weights = [5, 7]` with capacities two and three, each item fails both `x <= j` and `x <= k` for the full-capacity state and every smaller state. The initialized skip value zero survives all iterations, so the method correctly returns zero.

**Why a one-dimensional total-capacity table is insufficient**

Suppose a one-dimensional method only checked whether the packed total stayed below `w1 + w2`. It could accept a selection whose total is small enough overall but cannot be divided between the bags without overflowing one of them. The two indices retain exactly the distribution information needed to decide where a new item may go.

The table does not need an item dimension because backward traversal supplies the previous-item behavior in place. This reduces the straightforward three-dimensional `O(n * w1 * w2)` storage to `O(w1 * w2)`.

## Complexity detail

Let `n` be the number of weights. For each item, the source visits all `(w1 + 1)(w2 + 1)` capacity pairs. Every state performs at most two comparisons and two constant-time candidate updates. The total time is

`O(n * w1 * w2)`.

Including the plus-one zero-capacity rows does not change the asymptotic bound. At the maximum constraints, the table has roughly 90,000 cells and the algorithm performs roughly nine million state visits, which is appropriate for the given limits.

The table contains `(w1 + 1)(w2 + 1)` integers, so auxiliary space is `O(w1 * w2)`. Loop variables and the local two-argument `max` function use constant additional space.

A full item-indexed table would require `O(n * w1 * w2)` space. The descending loops are what make that dimension unnecessary while preserving 0/1 behavior.

## Alternatives and edge cases

- **Three-dimensional dynamic programming:** Store a separate `f[i][j][k]` layer for each item prefix. It makes the “previous item” dependency visually explicit but increases space to `O(n * w1 * w2)` without improving time.
- **Two alternating tables:** Read from a previous 2D table and write into a fresh current table for every item. This avoids reasoning about loop direction but still uses twice the 2D storage and performs copying or reinitialization.
- **Boolean exact-reachability states:** Track whether exact used weights `(a, b)` are reachable, transition each item into either bag, and maximize `a + b` afterward. This is valid, but it is not the state meaning implemented by the source.
- **One-dimensional knapsack over `w1 + w2`:** It loses the division between bags and can accept totals that cannot respect the two individual capacities.
- **Enumerate assignments:** Trying skip, bag one, or bag two for every item costs exponential time and cannot handle 100 items.
- **Forward capacity iteration:** It can reuse the current item through a state updated earlier in the same iteration, turning the 0/1 problem into an unbounded one. Both capacity dimensions must descend for this in-place recurrence.
- **Item fits both bags:** The two transitions compete through the maximum. The item is not added twice because each reads an old state that excludes it.
- **Item fits only one bag:** Only the corresponding `if` condition contributes a placement candidate; skipping remains possible.
- **Item fits neither bag:** Every state retains its prior value, so the item is ignored without special handling.
- **Empty packing:** Returning zero is valid when no item fits. The all-zero initialization represents this option for every capacity pair.
- **Unused capacity:** A state means “at most” each capacity, so an optimal result need not fill either bag exactly.
- **Repeated weights:** Items are separate 0/1 objects even when their numeric weights match. Each outer-loop iteration permits one more copy corresponding to one input position.
- **Positive weights:** Packing a feasible item always adds a positive reward, but it can still be optimal to skip it because using its capacity may prevent a better combination of other items.
- **Symmetric capacities:** Swapping `w1` and `w2` does not change the mathematical answer, though it transposes the conceptual table.
- **Shadowing Python’s built-in `max`:** The source assigns a local two-argument lambda named `max`. It behaves correctly for these updates, but using the built-in directly would be clearer and would preserve access to its other calling forms.
- **Missing type import:** The stored source refers to `List` without importing it. Standalone Python needs `from typing import List` unless the judge environment provides the name.
