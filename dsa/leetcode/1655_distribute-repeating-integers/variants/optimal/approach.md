## General
**Compress values into capacities.** Only the number of copies of each distinct value matters. Count `nums` and sort the frequencies. At most $m$ different values can be used by a solution with $m$ customers; if a solution uses a smaller frequency while a discarded larger frequency is unused, moving that entire customer group to the larger frequency remains valid. Therefore only the $m$ largest frequencies need to be retained.

**Precompute every customer-subset demand.** Represent served customers by an $m$-bit mask. For each mask, compute the sum of its requested quantities by removing its lowest set bit and extending a previously computed sum. A subset can share one integer value precisely when its total demand does not exceed that value's frequency.

**Assign one frequency at a time.** Start with only mask 0 reachable. For a frequency capacity and each previously reachable mask, enumerate every submask of the unserved customers. When that submask's precomputed demand fits the capacity, mark the union reachable for the next frequency. Keep the old mask as well, because an inventory value may remain unused.

Each transition assigns a whole customer to exactly one value through its submask membership, and the demand check prevents overusing that value. Conversely, any valid distribution partitions the customers into subsets assigned to distinct frequencies; processing those frequencies reproduces that sequence of reachable masks. Thus the full mask is reachable exactly when all customers can be satisfied.

## Complexity detail
Counting the inventory takes $O(n)$ time. Across all served masks, enumerating submasks of their complements has the standard $O(3^m)$ total bound per retained frequency, so the dynamic program takes $O(f3^m)$ time. Subset sums and reachable masks use $O(2^m)$ space, while retained capacities use $O(f)$ space.

## Alternatives and edge cases
- **Customer-by-customer backtracking:** Try each remaining frequency for the next largest demand and restore it afterward. Sorting and symmetry pruning can work well for $m\le10$, but the worst case explores exponentially many repeated assignments without the subset-state reuse.
- **Enumerate every customer-to-value mapping:** Trying all $f^m$ assignments and checking capacities is correct but repeats equivalent partial states and scales much worse than subset DP.
- **Greedy largest-to-largest:** Assigning each largest request to the largest current capacity can block two smaller requests that would have shared that capacity, so the local choice is not generally sound.
- Several customers may share one value if their total demand fits its frequency.
- One customer may never split a request across different values.
- Unused inventory is allowed, so capacities need not be exhausted.
- If the sum of all demands exceeds $n$, distribution is immediately impossible, although the DP also rejects it.
- A single request succeeds exactly when some frequency is at least that request.
- Equal frequencies create interchangeable choices; mask reachability avoids depending on which equal value is selected.
