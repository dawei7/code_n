## General

**Describe the best mountain for a fixed peak**

Suppose index `i` is chosen as the peak and is kept at its maximum allowed height. Moving left from `i`, each tower should be as tall as possible without exceeding either its own limit or its neighbor to the right. The right side follows the symmetric rule. These greedy choices maximize each side independently, but scanning both sides again for every possible peak would take $O(n^2)$ time.

**Summarize constrained prefixes with a monotonic stack**

Let `left[i]` be the largest sum on indices `0` through `i` when `i` is the rightmost peak and its chosen height is `maxHeights[i]`. Maintain indices in non-decreasing order of their limits. Before processing `i`, pop every index whose limit is greater than `maxHeights[i]`. The remaining top, if any, is the nearest index `previous` to the left with `maxHeights[previous] \le \texttt{maxHeights[i]}`.

All positions after `previous` through `i` can contribute exactly `maxHeights[i]` each: their limits are larger, while the non-decreasing prefix cannot rise above its final height. The best portion through `previous` was already computed, giving

$$
\texttt{left[i]} = \texttt{left[previous]} + (i - \texttt{previous})\,\texttt{maxHeights[i]}.
$$

When no such previous index exists, the current limit caps the whole prefix, so `left[i] = (i + 1) * maxHeights[i]`.

**Mirror the argument and combine the sides**

Scan from right to left to compute `right[i]`, the largest suffix sum when `i` is its leftmost peak. For each possible peak, `left[i] + right[i]` includes the peak twice, so its complete mountain sum is

$$
\texttt{left[i]} + \texttt{right[i]} - \texttt{maxHeights[i]}.
$$

The maximum of these values is attainable because both directional constructions meet at the same peak. Conversely, every beautiful configuration has some peak `i`, and neither side can exceed the corresponding greedy directional sum. Therefore the maximum combined value is optimal. Keeping equal limits on the stack also handles flat peaks without special cases.

## Complexity detail

Let $n$ be the length of `maxHeights`. Each index is pushed once and popped at most once during each directional scan, so the total time is $O(n)$. The prefix and suffix sum arrays and the stack use $O(n)$ space.

The benchmark uses $n$ as `size` and supplies legal flat arrays from length 32 through 512. The monotonic-stack solution scales linearly. A correct implementation that explicitly constructs both sides for every peak completes every tier but exhibits $O(n^2)$ scaling.

## Alternatives and edge cases

- **Enumerate every peak:** Greedily scan left and right for each peak. This directly follows the definition and is correct, but $10^5$ towers make its $O(n^2)$ running time infeasible.
- **Repeated range minima:** Querying minima separately for every peak and boundary avoids some scanning only with more elaborate structures; it does not improve on the direct linear stack formulation.
- **Endpoint peak:** A non-decreasing or non-increasing array is already a valid mountain whose peak lies at an endpoint.
- **Flat peak:** Equal neighboring heights are allowed, and multiple indices may describe the same optimum peak plateau.
- **Deep valley:** A small limit constrains all taller positions between it and a chosen peak, even when those positions are individually large.
- **Positive lower bound:** Every final height must be at least $1$; the positive input limits ensure the greedy construction respects that condition.
- **Large total:** The answer can be as large as $10^{14}$, so fixed-width languages need a 64-bit integer type.
- **Single tower:** Its maximum allowed height is the unique optimal sum.
