## General

**When a one already exists.** The gcd of `1` and any positive integer is `1`. Each non-one position can therefore be converted exactly once by spreading an existing `1` through adjacent pairs. If there are $c$ ones initially, the answer is $n-c$: every non-one needs an operation, and that lower bound is attainable.

**When a one must be created.** Repeated adjacent-gcd replacements within a contiguous segment can reduce one position to the gcd of that entire segment. Consequently, a `1` can be created exactly when some subarray has gcd $1$. For each left endpoint, extend the right endpoint while updating a running gcd; record the shortest length $L$ that reaches $1$. If none does, the gcd of the entire array exceeds $1$, every obtainable value remains divisible by that common divisor, and the task is impossible.

A qualifying segment of length $L$ needs $L-1$ operations to combine its values into one `1`. Afterward, that `1` needs another $n-1$ operations to propagate through all other positions because no ones existed initially. Using the shortest qualifying segment minimizes the first phase, giving $(L-1)+(n-1)$. Conversely, creating the first `1` from any segment of length $L$ requires at least $L-1$ adjacent combinations, and converting the other $n-1$ positions requires at least one operation each, so this construction meets the lower bound.

## Complexity detail

Let $n$ be the length of `nums`. Counting existing ones takes $O(n)$ time. When none exist, there are $O(n^2)$ candidate endpoints, and each extension updates its gcd in constant time, for $O(n^2)$ total time. The algorithm retains only counters and gcd values, so its auxiliary space is $O(1)$.

The benchmark uses no qualifying subarray, forcing every endpoint pair to be examined. A slower but correct implementation that recomputes each subarray gcd from its entire slice completes the legal tiers and grows as $O(n^3)$.

## Alternatives and edge cases

- **Recompute every subarray gcd:** Testing each slice independently is correct but repeats prefix work and takes $O(n^3)$ time.
- **Distinct suffix-gcd states:** Coalescing equal gcds of subarrays ending at each position can reduce work for larger constraints, but the quadratic scan is simpler and fully bounded here by $n \le 50$.
- If the array already contains multiple ones, only the non-one elements require operations.
- If the gcd of the whole array is greater than `1`, no subarray can have gcd `1`, so the answer is `-1`.
- A shortest qualifying segment of length two takes one operation to create the first `1`.
- Values may be as large as $10^6$, but gcd updates do not depend linearly on their magnitude.
