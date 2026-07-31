## General

The score is unchanged when every element of `perm` is rotated by the same number of positions, because the cyclic edges stay identical. Every cycle has exactly one rotation beginning with `0`, and that rotation is lexicographically smaller than the others. It is therefore both safe and necessary for tie-breaking to fix `perm[0] = 0`.

**Describe a partially built cycle**

Let `best(mask, last)` be the minimum additional score after visiting exactly the values selected by `mask`, with `last` at the end of the current path. Value `0` is always selected. If every value has been used, the only remaining contribution closes the cycle:

$$
\lvert \texttt{last}-\texttt{nums[0]}\rvert.
$$

Otherwise, choosing an unused value `next` contributes

$$
\lvert \texttt{last}-\texttt{nums[next]}\rvert
+\texttt{best(mask with next, next)}.
$$

Taking the minimum over all unused next values considers every possible continuation. Induction on the number of unused values proves that each memoized state holds its true minimum completion cost.

**Recover the lexicographically smallest optimum**

Start from `mask = 1` and `last = 0`. At every step, inspect unused next values in increasing order and select the first one whose transition equals the memoized optimum for the current state. That choice preserves the minimum total score. Because the earliest position where two optimal results differ is assigned the smallest feasible value, repeating this rule constructs the lexicographically smallest optimal permutation.

## Complexity detail

There are at most $n2^n$ pairs of a visited mask and final value. Each state tests up to $n$ unused next values, so the running time is $O(n^2 2^n)$. Reconstruction performs only $O(n^2)$ additional transition checks and does not change the bound.

The memoized costs occupy $O(n2^n)$ space. The returned permutation, recursion depth, and reconstruction state use $O(n)$ additional space.

## Alternatives and edge cases

- **Enumerate all permutations:** Fixing `0` still leaves $(n-1)!$ orders to score. This is correct but factorial and forms the principal slower benchmark comparison.
- **Bottom-up bitmask DP:** Iterating masks explicitly has the same $O(n^2 2^n)$ time and $O(n2^n)$ space, but careful processing order and separate reconstruction data make it more cumbersome.
- **Store full paths in every state:** Tuple comparison can handle lexicographic ties directly, but copying paths inflates memory and transition costs unnecessarily.
- The edge cost is `abs(last - nums[next])`, not `abs(nums[last] - next)`; reversing those roles changes the ordered permutation returned after tie-breaking.
- The wrap contribution uses `nums[0]` because the fixed first permutation value is `0`.
- Lexicographic comparison applies to the returned permutation, not to the sequence of values obtained by indexing `nums`.
- At $n=2$, fixing the first element determines the only possible returned order.
