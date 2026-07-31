## General

**Separate subarray ownership from product maximization**

Every non-empty subarray deterministically selects one index: the leftmost index whose prime score is maximal inside that subarray. If index `i` owns $c_i$ subarrays, then the operation can multiply by `nums[i]` up to $c_i$ times. Once these capacities are known, the remaining problem is simply to take the largest available numeric factors until `k` operations have been used.

**Compute distinct-prime scores with a sieve**

Allocate a score table through $V$, the largest array value. Whenever an unmarked integer `p` is reached, it is prime; increment the score of every multiple of `p`. Each distinct prime contributes exactly once to each divisible value, regardless of exponent. Reading the table at each array value gives its prime score.

**Assign every subarray with asymmetric boundaries**

For index `i`, let `left[i]` be the nearest index to its left whose prime score is greater than or equal to `score[i]`. Let `right[i]` be the nearest index to its right whose score is strictly greater. A non-increasing monotonic stack computes both boundaries in one pass: a larger incoming score pops smaller scores and becomes their strict right boundary, while the remaining top becomes the current index's greater-or-equal left boundary.

The asymmetry encodes the smallest-index tie rule. An equal score on the left blocks `i`, because that earlier index would win; an equal score on the right does not block `i`, because `i` wins that tie. Consequently, `i` is selected exactly for subarrays whose left endpoint lies in `[left[i] + 1, i]` and right endpoint lies in `[i, right[i] - 1]`. Its capacity is therefore

$$
c_i = (i-\texttt{left[i]})(\texttt{right[i]}-i).
$$

These ownership rectangles are disjoint and cover all subarrays: every subarray has exactly one maximum-score, leftmost winner, and its endpoints fall inside that winner's boundaries.

**Spend capacities on the largest values**

Sort indices by `nums[i]` in descending order. For each index, use its value `min(k, c_i)` times, multiply with modular exponentiation, and decrease `k`. Exchanging any chosen smaller factor for an available larger one cannot reduce the product, so this greedy order is optimal. All values are positive, so using every permitted operation is never worse than stopping early.

## Complexity detail

Let $n$ be the array length and $V$ its maximum value. The prime-score sieve costs $O(V\log\log V)$ time. The monotonic-stack pass is $O(n)$, sorting indices is $O(n\log n)$, and modular exponentiation across at most $n$ capacities costs $O(n\log k)$ in the loose worst case but is dominated under the problem bounds by the stated sorting and bounded exponent work. The required bound is $O(V\log\log V+n\log n)$ time. Score tables, boundaries, the stack, and the sorted indices use $O(V+n)$ space.

## Alternatives and edge cases

- **Enumerate every subarray:** Extending each left endpoint while tracking its current winner is correct but takes $O(n^2)$ time and materializes or sorts up to $O(n^2)$ factors.
- **Factor each value independently:** Trial division avoids a sieve but may cost $O(n\sqrt V)$ time; caching helps repeated values but does not match the sieve's full-domain bound.
- **Symmetric strict boundaries:** Using strict comparisons on both sides double-counts equal-score ties; using non-strict comparisons on both sides leaves gaps. The left `>=` and right `>` rules are deliberate.
- The value `1` has prime score zero because it has no prime factors.
- Repeated prime factors count once: `12 = 2^2 * 3` has prime score two.
- Equal prime scores are resolved by index, not by the larger numeric value.
- Equal numeric values may be used many times when they own different subarrays or one index owns many subarrays.
- `k` can be much larger than $n$, so capacities and exponent counts require integer arithmetic beyond a single operation per element.
- Reduce after every modular multiplication and use fast modular exponentiation for large capacities.
