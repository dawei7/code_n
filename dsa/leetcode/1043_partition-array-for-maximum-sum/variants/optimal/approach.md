## General
**Define optimal prefix states:** Let `dp[end]` be the largest transformed sum for the first `end` array elements, with `dp[0] = 0`. This state contains all information needed before choosing the final subarray of that prefix.

**Enumerate the final partition length:** For each `end` from `1` through `N`, try every final length from `1` through `min(K, end)`. The elements before that final block contribute the already optimal value `dp[end - length]`. The block itself contributes its length multiplied by the maximum among its original elements.

**Maintain the block maximum incrementally:** As the candidate final block grows leftward one element at a time, update `current_max = max(current_max, arr[end - length])`. This avoids rescanning the block for each length. The candidate is then `dp[end - length] + current_max * length`, and the largest candidate becomes `dp[end]`.

Every valid partition of the first `end` elements has one final contiguous block whose length is among the tested choices. Removing it leaves a prefix optimally represented by the corresponding earlier state; replacing a worse prefix partition by `dp[end - length]` cannot reduce the total. Conversely, every tested candidate appends a legal block to a valid prefix partition. Induction over `end` therefore establishes that `dp[N]` is the requested maximum.

## Complexity detail
There are $N$ prefix states, and each tests at most $K$ final-block lengths while updating the maximum in constant time. The total time is $O(NK)$. The dynamic-programming array contains $N+1$ values, so space is $O(N)$.

## Alternatives and edge cases
- **Top-down memoization:** Cache the best result from each starting index and try up to $K$ next-block lengths. It has the same $O(NK)$ time and $O(N)$ stored states, plus recursion depth.
- **Recompute each block maximum:** Calling `max(arr[end - length:end])` for every candidate remains correct but adds up to another factor of $K$.
- **Enumerate all partitions:** Trying every placement of partition boundaries grows exponentially.
- **Unit maximum length:** When $K=1$, no values can be grouped and the answer is the original array sum.
- **Whole-array block:** When $K=N$, using one block yields $N$ times the overall maximum, though another partition may tie it.
- **Zero values:** A block maximum and its contribution may be zero; initializing prefix scores and running maxima to zero remains valid.
- **Contiguity:** Elements may only share a replacement maximum when they belong to the same contiguous subarray; their original order cannot be rearranged.
- **Large values:** Products and accumulated sums should use integer arithmetic capable of holding the guaranteed 32-bit result.
