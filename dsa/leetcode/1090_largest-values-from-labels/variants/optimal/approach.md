## General

**Take valuable items first, subject to two capacities**

Each item consumes one slot from a global allowance of at most `numWanted` items and one slot from its label’s allowance of at most `useLimit`. All values are nonnegative. This structure suggests a greedy order: examine items from greatest value to smallest and accept an item whenever both allowances still have room.

The expression `zip(values, labels)` pairs each value with the label at the same index. `sorted(..., reverse=True)` then orders those tuples descending. Python compares tuples lexicographically, so value is the primary key and label breaks a tie. Only the primary value order matters for optimality; when two values are equal, selecting either one first cannot change the sum, although their labels can influence which equal-valued representative is chosen.

**Track label usage and total usage separately**

`cnt` is a `Counter` whose missing labels automatically have count zero. Before accepting pair `v, l`, the condition `cnt[l] < useLimit` checks the label-specific capacity. If it passes, the algorithm increments that label’s count, increments the total selected count `num`, and adds `v` to `ans`.

The global item limit is enforced by stopping as soon as `num == numWanted`. Before that moment `num` is smaller than the limit, and after that moment no further item may legally be selected. If label restrictions prevent filling all requested slots, the loop simply reaches the end and returns the sum of the smaller feasible set. The contract says “at most,” so filling fewer slots is legal.

**Why accepting the current feasible maximum is safe**

Consider the items in descending value order. When the algorithm accepts the current item, it is the greatest-valued unprocessed item. Suppose some optimal solution did not contain it.

If that solution has an unused global slot and unused capacity for this label, adding the item cannot hurt because values are nonnegative; it would improve or preserve the sum. Otherwise, to include the current item one can remove a selected item that uses the blocking capacity. If the global slot is the only issue, remove any later selected item. If the label limit is the issue, remove a selected item with the same label. Every such replaceable item appears no earlier in the descending order and therefore has value no greater than the current item. The exchange preserves feasibility and does not decrease the total.

Repeatedly applying this exchange transforms some optimal solution so that it agrees with every greedy acceptance. Therefore, accepting a feasible item never prevents the existence of an optimal completion.

Now consider a rejected item. It is rejected only because its label already contributed `useLimit` earlier items. Those earlier same-label items have values at least as large because of the sorted order. Any feasible solution can use at most that many items of the label, so replacing one of them with the rejected item cannot improve the sum. Skipping it is safe.

Together, these two arguments establish that the final greedy set has maximum possible value.

**Why nonnegative values matter**

The greedy method accepts a feasible zero-valued item when a slot remains. This does not decrease the sum, and the problem permits using fewer than `numWanted`, so accepting zero is harmless even if it is unnecessary. If negative values were allowed, automatically filling slots could reduce the total and the algorithm would need to stop once values became negative. The official constraint `values[i] >= 0` is what makes the current behavior correct.

## Complexity detail

Let $n$ be the number of items. Building and sorting the list of value-label tuples costs $O(n\log n)$ time. The subsequent loop visits each tuple at most once. `Counter` lookup and update take expected $O(1)$ time, so the scan costs $O(n)$ and does not change the dominant bound.

The sorted tuple list contains $n$ pairs and therefore uses $O(n)$ space. The counter has one entry per label encountered or selected, at most $n$, so it also fits within $O(n)$. Other variables use constant space. The overall auxiliary-space bound is $O(n)$.

An early break after selecting `numWanted` items can shorten the scan in favorable inputs, but sorting has already processed all items. It does not improve the worst-case asymptotic time.

## Alternatives and edge cases

- **Group by label first:** Keep the greatest `useLimit` values from each label, merge those candidates, and take the global greatest `numWanted`. This is also correct because lower values beyond a label’s cap can never be selected, but it requires more grouping machinery.
- **Per-label heaps:** Maintain a min-heap capped at `useLimit` for each label, then choose the global best candidates. This can save candidate space when label groups are huge, though the final selection still requires ordering or another heap.
- **Bucket by value:** Values are bounded by twenty thousand, so value-frequency buckets can replace comparison sorting and approach $O(n+V)$ time for value range $V$. Label-capacity bookkeeping becomes less direct, and ordinary sorting is simpler.
- **Dynamic programming:** A state over selected count and every label’s usage would be far larger than necessary. The exchange property makes greedy selection sufficient.
- **`numWanted` larger than feasible capacity:** The algorithm returns after scanning all items with fewer than `numWanted` selections, which is valid because the limit is an upper bound.
- **`useLimit` at least every label frequency:** The label constraint never binds, so the algorithm simply sums the globally greatest permitted number of values.
- **All items share one label:** At most `useLimit` items are accepted, even when `numWanted` is larger. They are the greatest values of that label due to the order.
- **Equal values with different labels:** Tuple sorting may inspect labels to break the tie, but either equal-valued choice contributes the same amount. Later feasibility checks still enforce every label cap.
- **Duplicate items:** Each array position is a separate selectable item. Equal value-label pairs may both be chosen while capacity permits.
- **Zero values:** Selecting a zero cannot reduce the sum. It may fill a remaining slot, but the maximum sum remains unchanged.
- **`numWanted == 1`:** The first feasible item is simply the largest-value item, and every label initially has capacity.
- **`useLimit == 1`:** Only the greatest encountered item for each label can be accepted; all later items with that label are skipped.
- **Parallel-array alignment:** `zip` deliberately pairs equal indices. Sorting values separately from labels would destroy item identity and produce invalid combinations.
