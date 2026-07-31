## General

**Reduce an index to its squarefree kernel**

Write a positive index as $i = q a^2$, where $q$ is squarefree. Two indices $i = q a^2$ and $j = r b^2$ have a perfect-square product exactly when $q = r$: matching kernels give $ij = (qab)^2$, while different squarefree kernels leave at least one prime with odd exponent. Pairwise compatibility is therefore an equivalence relation, and every complete subset lies within one kernel class.

All values in `nums` are positive. Once a kernel class is chosen, omitting one of its compatible indices can only decrease the sum, so the best subset for that class contains every index of the form $q s^2$ that does not exceed $n$.

**Enumerate square-multiple sequences**

For each `base` from $1$ through $n$, sum `nums[base * square * square - 1]` for consecutive positive values of `square` while the 1-indexed position remains within the array. When `base` is squarefree, this sequence is exactly one full kernel class, so every candidate optimum is examined.

A non-squarefree base has the form $q t^2$ and enumerates only the subsequence $q(ts)^2$ of kernel $q$'s full class. Such duplicates are harmless: because all values are positive, a partial class cannot have a greater sum than the full class that is also evaluated. Taking the maximum sequence sum therefore returns exactly the maximum complete-subset sum.

## Complexity detail

Let $n$ be the length of `nums`. The inner loop visits one pair $(b,s)$ for every $bs^2 \le n$. Reordering the count by $s$ gives

$$
\sum_{s=1}^{\lfloor\sqrt n\rfloor}
\left\lfloor\frac{n}{s^2}\right\rfloor
\le
n\sum_{s=1}^{\infty}\frac{1}{s^2}
= O(n).
$$

Together with the $n$ outer-loop iterations, the algorithm takes $O(n)$ time. It stores only counters and running sums, so auxiliary space is $O(1)$.

The benchmark uses the array length $n$ as `size` and fills every value with `1`. The square-multiple method performs linear total work. A correct pairwise implementation scans every possible partner for each anchor index, completes all tiers, and exhibits $O(n^2)$ scaling.

## Alternatives and edge cases

- **Group explicit squarefree kernels:** Factor every index, multiply the primes with odd exponents, and accumulate values in a map keyed by that product. This directly represents the equivalence classes but requires factorization logic and additional storage.
- **Smallest-prime-factor sieve:** Precompute factor information and derive every squarefree kernel efficiently. It can achieve linear or near-linear preprocessing but uses $O(n)$ auxiliary arrays.
- **Pairwise compatibility scan:** For every anchor, test every other index with an integer square root and sum compatible values. It is straightforward but takes $O(n^2)$ time.
- **1-indexed positions:** The mathematical index $i$ corresponds to `nums[i - 1]`; using the language's 0-based position in the product changes the problem.
- **Singleton subsets:** Any single index is complete, so the answer is always at least the largest individual value.
- **Positive values:** Including every member of a compatible class is valid only because `nums[i]` is positive; no beneficial member needs to be discarded.
- **Large sums:** Up to $10^4$ values of size $10^9$ may contribute, so the result can exceed 32-bit integer range.
