## General
**Maintain the aggregate instead of rebuilding it:** Compute the initial sum of even values once. A query changes only one array position, so every other contribution remains unchanged.

**Remove the old contribution before updating:** Let `index` be the queried position. If `nums[index]` is even, subtract it from the running sum. Perform `nums[index] += value`. If the updated value is even, add it to the running sum. Append the resulting aggregate to the answer.

Before each query, the running value equals the sum of all current even entries. Removing the old indexed value when necessary leaves exactly the contribution of all unchanged positions. Adding the new indexed value when necessary restores the complete even sum for the updated array. This maintains the invariant after every query and produces each required answer in order.

## Complexity detail
The initial aggregate scans $N$ values. Each of the $Q$ queries then performs constant work, giving $O(N+Q)$ time. The returned list uses $O(Q)$ space; excluding output, the running sum and in-place array updates use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Rescan after every query:** Summing all even values from scratch is correct but costs $O(NQ)$ time.
- **Fenwick tree:** A tree of even contributions supports point updates and total queries in $O(\log N)$ time, but a single maintained total already supports this exact whole-array query in $O(1)$.
- **Even-to-odd transition:** Remove the old even contribution and add nothing after the update.
- **Odd-to-even transition:** The old value contributes nothing, while the new even value is added.
- **Negative even values:** They contribute their signed value to the sum, just like positive even values.
