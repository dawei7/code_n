## General

Process indices from left to right. An index `i` introduces a new category exactly when it does not share a category with any earlier index. Compare `i` with `0, 1, ..., i - 1` through `haveSameCategory`. If any comparison returns true, its category has already appeared and the scan moves to the next index. If every comparison is false, increment the category count.

This does not require knowing or storing category labels. By the time index `i` is considered, every category occurring in the prefix `0...i-1` has already contributed exactly once to the count. A successful comparison proves that `i` belongs to one of those existing categories. If all comparisons fail, then `i` is unequal to every prefix element and therefore cannot belong to any previously counted category, so adding one is necessary. Induction over the indices shows that the final count is exactly the number of categories.

**Why every pair can be necessary**

Consider an execution in which every oracle answer is false. Unless the algorithm asks about a particular pair $(a,b)$, two hidden assignments remain consistent with all observed answers: one where every element is in its own category and another where only $a$ and $b$ share a category. Their required outputs differ by one. A correct algorithm must therefore query every one of the $\binom{n}{2}$ pairs in this worst case.

## Complexity detail

Index `i` triggers at most $i$ oracle calls, so the total is

$$
\sum_{i=0}^{n-1} i = \frac{n(n-1)}{2} = O(n^2).
$$

The all-distinct adversary proves an $\Omega(n^2)$ query lower bound, making the algorithm asymptotically optimal at $\Theta(n^2)$. Apart from the loop indices and category counter, it stores no data that grows with $n$, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Store one representative per discovered category:** Compare each new index only with representatives. This can reduce calls when categories are large, but still needs $O(n^2)$ calls when all categories are distinct and uses $O(n)$ storage.
- **Union-find over all pairs:** Query every pair and union equal ones. It is correct but adds $O(n)$ memory and data-structure overhead without reducing the necessary worst-case queries.
- **Read displayed category labels:** The arrays shown in examples and app-local fixtures are visualizations; direct label access is unavailable in the native interactive contract.
- **Single element:** No oracle call is necessary, and the result is one.
- **All elements equal:** Every index after zero matches immediately, so only $n-1$ calls are made.
- **All elements distinct:** Every comparison is false, attaining the $n(n-1)/2$ worst-case query count.
- **Interleaved categories:** The method relies only on equality answers and does not assume category members are adjacent or sorted.
