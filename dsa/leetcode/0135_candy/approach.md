## General

**Translate the rule into two independent directions**

Each child needs at least one candy. In addition:

- if `ratings[i] > ratings[i - 1]`, child `i` must receive more than the left neighbor;
- if `ratings[i] > ratings[i + 1]`, child `i` must receive more than the right neighbor.

Equal ratings impose no ordering requirement. Two equally rated neighbors may receive equal or different counts; minimizing the total normally lets both remain as low as their other constraints permit.

Trying to satisfy both directions in one left-to-right pass is difficult because a future decreasing run can force earlier children upward. The solution separates the two directions into `left` and `right` arrays, computes the minimum requirement from each side, and combines them.

**What the left array guarantees**

Every entry begins at one, satisfying the universal minimum.

The forward loop starts at index one. When the current rating is greater than the previous rating, it sets:

`left[i] = left[i - 1] + 1`

Otherwise, `left[i]` remains one.

After this pass, `left[i]` is the smallest candy count that satisfies all comparisons with left neighbors within the prefix ending at `i`.

For an increasing run such as ratings `[1, 3, 5, 8]`, the required counts become `[1, 2, 3, 4]`. Each step must exceed the previous one by at least one, and using exactly one more is minimal. When the rating stops increasing, the current child has no obligation to exceed the left neighbor, so restarting at one is the cheapest possible choice under the left-only rules.

**What the right array guarantees**

The backward pass is the mirror image. It starts at index `n - 2` and moves left. When `ratings[i] > ratings[i + 1]`, it sets:

`right[i] = right[i + 1] + 1`

Otherwise, the entry stays one.

Thus `right[i]` is the smallest number satisfying every comparison with right neighbors in the suffix beginning at `i`.

For a decreasing rating run `[8, 5, 3, 1]`, the right requirements become `[4, 3, 2, 1]`. The high-rated child at the left end must stand above the whole descending chain.

**Why take the maximum at each child**

A final candy count at index `i` must satisfy both directional lower bounds. It cannot be smaller than `left[i]`, or some increasing relationship from the left would fail. It cannot be smaller than `right[i]`, or some decreasing relationship toward the right would fail. Therefore, every valid assignment must give at least:

$$
\max(\texttt{left[i]},\texttt{right[i]}).
$$

Giving exactly that maximum is sufficient. Consider the relationship between `i - 1` and `i`.

If `ratings[i] > ratings[i - 1]`, the forward pass made `left[i] = left[i - 1] + 1`. On this rising edge, `right[i]` is one unless another right-side descent requires still more. Taking the maximum cannot make child `i` too small. It also cannot raise child `i - 1` in a way that invalidates the edge, because any large right requirement at `i - 1` comes from a descent beginning there, which is incompatible with `ratings[i - 1] < ratings[i]` on its right edge. The directional construction preserves the strict comparison.

Symmetrically, when `ratings[i - 1] > ratings[i]`, the right array enforces a one-candy increase for `i - 1` over `i`.

At a mountain peak, both directions may demand more than one. For ratings `[1, 2, 3, 2, 1]`, the left requirement at the peak is three and the right requirement is also three. For an uneven mountain, one side can demand more. The peak needs the larger demand, not their sum, because one candy count can satisfy both inequalities simultaneously.

Because every valid solution is bounded below element by element by these maxima, and the maxima themselves form a valid solution, their sum is the global minimum.

**Trace the examples**

For `[1, 0, 2]`, the left array is `[1, 1, 2]`; the right array is `[2, 1, 1]`. Their elementwise maxima are `[2, 1, 2]`, summing to five.

For `[1, 2, 2]`, the left array is `[1, 2, 1]`; the right array remains `[1, 1, 1]`. The maximum is `[1, 2, 1]`. The final equal-rating edge requires no strict candy comparison, so the third child may receive one.

The generator expression combines corresponding entries with `zip(left, right)` and sums them without building a third array.

## Complexity detail

Let $n$ be the number of children.

The forward pass visits $n-1$ indices, the backward pass visits $n-1$, and the final sum consumes $n$ pairs. Every operation is constant time, giving $O(n)$ total time.

The two arrays each hold $n$ integers, so auxiliary space is $O(n)$. The generator used by `sum` produces one maximum at a time and does not allocate another length-$n$ list.

There is a constant-space slope method with the same time bound, but this selected implementation intentionally uses linear memory for simpler directional reasoning. Its bounds exactly match the manifest.

## Alternatives and edge cases

- **One candy array and two passes:** Build left requirements in one array, then scan right-to-left and raise an entry with `max(current, right-neighbor + 1)` when needed. It uses $O(n)$ space with one array.
- **Slope counting:** Track lengths of increasing and decreasing rating runs and add triangular-number contributions. It achieves $O(1)$ auxiliary space but peak and plateau accounting is easier to get wrong.
- **Repeated relaxation:** Start everyone at one and repeatedly repair violated neighbor constraints until stable. It is intuitive but can require $O(n^2)$ time.
- **Priority queue by rating:** Process children from lower to higher ratings so lower-rated neighbor counts are known first. It works but adds $O(n\log n)$ sorting or heap cost.
- **One child:** Both arrays are `[1]`, so the result is one.
- **All ratings equal:** No strict comparison fires; everyone receives one and the result is $n$.
- **Strictly increasing ratings:** The minimum distribution is `1, 2, ..., n`.
- **Strictly decreasing ratings:** The right pass creates `n, ..., 2, 1`.
- **Valleys:** A local low point may remain at one even when both neighbors require larger counts.
- **Uneven peaks:** Taking the maximum, rather than adding directional counts, prevents double-counting the peak.
- **Runtime dependency:** The selected source uses `List` in its annotation without importing it. A standalone module needs `from typing import List`.
