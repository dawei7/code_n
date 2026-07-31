## General

**Separate possible small and large roles**

Every operation consumes one value that plays the smaller role and one that plays the larger role. At most $\lfloor n/2 \rfloor$ pairs can exist. After sorting, an optimal solution may choose its smaller-role values from the smallest half: replacing any chosen small value with an unused smaller one cannot invalidate its pair. The remaining values, beginning at index `n // 2`, provide enough candidates for the larger role.

**Use the smallest sufficient partner**

Maintain one pointer at the smallest unmatched value in the lower half and another at the beginning of the upper portion. If twice the small value is at most the current large value, pair them and advance both roles. Choosing that large value is safe because every later candidate is at least as large; saving the current one cannot help a future, no-smaller small value more than it helps the current value.

If the current large value is too small, it cannot pair with the current small value or with any later small value. Discard it from large-role consideration by advancing only the large pointer.

This exchange reasoning shows that each successful greedy match can appear in some maximum matching, while each rejected large candidate is unusable. When either pointer exhausts its permitted range, no further pair can be added. Twice the number of matches is therefore the maximum number of marked indices.

## Complexity detail

Sorting dominates the linear two-pointer scan, giving $O(n \log n)$ time. The manifest records $O(n)$ space to cover the worst-case auxiliary storage of the language's sorting implementation; the pointer scan itself uses $O(1)$ additional space.

## Alternatives and edge cases

- **Binary search on the pair count:** For a proposed $k$, compare the $k$ smallest values with the $k$ largest values. This yields a correct $O(n \log n)$ method after sorting, but the direct two-pointer scan avoids the extra search factor over the feasibility check.
- **Exhaustive unmarked-pair search:** Repeatedly find the smallest feasible pair. With a careful greedy choice it is correct, but scanning pairs can take quadratic time and list deletion can add further cost.
- **Maximum bipartite matching:** Model small-to-large compatibility as edges and compute a maximum matching. The monotone sorted inequality makes a general graph algorithm unnecessary and much slower.
- **Odd length:** At least one index must remain unmarked; the result is always even.
- **Exact equality:** A pair is valid when `2 * small == large`, not only when the inequality is strict.
- **Large values:** Evaluate the doubled value in a type wide enough to avoid overflow at $10^9$.
